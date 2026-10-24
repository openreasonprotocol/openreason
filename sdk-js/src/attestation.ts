// ORP v0.3 attestation verification — JS port of orp_validator/attestation.py.
// Same crypto posture as an AdCP #4441 signed-provenance claim: RFC 8785 canonicalisation,
// Ed25519, purpose-constrained short-lived keys, did:key / JWK discovery. Offline & universal
// (Node + browser): SHA-256 via WebCrypto, Ed25519 via @noble/ed25519.

import { verifyAsync } from "@noble/ed25519";
import { canonicalize } from "./canonicalize.js";

export const ATTESTATION_USE = "orp-attestation";
export const SUPPORTED_ALG = "Ed25519";
export const DEFAULT_SKEW_SECONDS = 300;
const SIGNED_TIERS = new Set(["attested", "verified", "full"]);

export type Doc = Record<string, unknown>;
/** Resolve a key id (kid) to key material: 32 raw bytes, a base64url string, a did:key, or a JWK. */
export type ResolveKey = (kid: string) => KeyMaterial | Promise<KeyMaterial>;
export type KeyMaterial = Uint8Array | string | { kty?: string; crv?: string; x?: string };

export interface SignatureVerdict {
  kid: string;
  valid: boolean;
  role: string | null;
  errors: string[];
}
export interface AttestationResult {
  valid: boolean;
  tier: string | null;
  computed_hash: string | null;
  errors: string[];
  signatures: SignatureVerdict[];
}

// ── base64url ────────────────────────────────────────────────────────────────
export function b64uDecode(s: string): Uint8Array {
  const pad = s.length % 4 === 0 ? "" : "=".repeat(4 - (s.length % 4));
  const b64 = (s + pad).replace(/-/g, "+").replace(/_/g, "/");
  if (typeof atob === "function") {
    const bin = atob(b64);
    const out = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }
  return new Uint8Array(Buffer.from(b64, "base64"));
}

// ── base58btc (Bitcoin alphabet), for did:key ────────────────────────────────
const B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
function b58decode(s: string): Uint8Array {
  let num = 0n;
  for (const ch of s) {
    const idx = B58.indexOf(ch);
    if (idx < 0) throw new Error(`invalid base58 character: ${ch}`);
    num = num * 58n + BigInt(idx);
  }
  const bytes: number[] = [];
  while (num > 0n) {
    bytes.unshift(Number(num & 0xffn));
    num >>= 8n;
  }
  // restore leading zero bytes (each '1' prefix == one 0x00)
  for (const ch of s) {
    if (ch === "1") bytes.unshift(0);
    else break;
  }
  return new Uint8Array(bytes);
}

/** Decode a `did:key:z6Mk...` Ed25519 DID into 32 raw public-key bytes (offline). */
export function publicKeyFromDidKey(did: string): Uint8Array {
  if (!did.startsWith("did:key:z")) throw new Error("not a base58btc did:key");
  const decoded = b58decode(did.slice("did:key:z".length));
  if (decoded[0] !== 0xed || decoded[1] !== 0x01) {
    throw new Error("did:key multicodec is not ed25519-pub (0xed01)");
  }
  const raw = decoded.slice(2);
  if (raw.length !== 32) throw new Error(`ed25519 public key must be 32 bytes, got ${raw.length}`);
  return raw;
}

function toRawPublicKey(material: KeyMaterial): Uint8Array {
  if (material instanceof Uint8Array) return material;
  if (typeof material === "string") {
    return material.startsWith("did:key:") ? publicKeyFromDidKey(material) : b64uDecode(material);
  }
  if (material && typeof material === "object" && material.x) return b64uDecode(material.x);
  throw new Error("unsupported key material");
}

/** The content that is hashed/signed: the document WITHOUT its own `attestation` block. */
export function attestedContent(document: Doc): Doc {
  const { attestation: _omit, ...rest } = document;
  return rest;
}

async function sha256Hex(bytes: Uint8Array): Promise<string> {
  const subtle =
    (typeof globalThis !== "undefined" && (globalThis.crypto as Crypto | undefined)?.subtle) ||
    ((await import("node:crypto")).webcrypto.subtle as SubtleCrypto);
  const digest = await subtle.digest("SHA-256", bytes as unknown as BufferSource);
  return Array.from(new Uint8Array(digest))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
}

/** sha256 over the canonical bytes, in the spec's `sha256:<hex>` form. */
export async function contentHash(content: unknown): Promise<string> {
  return "sha256:" + (await sha256Hex(canonicalize(content)));
}

function parseIso(ts: string): number {
  return Date.parse(ts.endsWith("Z") || /[+-]\d\d:?\d\d$/.test(ts) ? ts : ts + "Z");
}

async function verifyOne(
  s: Record<string, unknown>,
  signingInput: Uint8Array,
  resolveKey: ResolveKey,
  nowMs: number,
  skewSeconds: number,
): Promise<SignatureVerdict> {
  const kid = String(s.kid ?? "");
  const v: SignatureVerdict = { kid, valid: true, role: (s.role as string) ?? null, errors: [] };

  if (s.use !== ATTESTATION_USE) {
    v.valid = false;
    v.errors.push(`wrong_key_use: ${JSON.stringify(s.use)} != ${JSON.stringify(ATTESTATION_USE)}`);
  }
  if (s.alg !== SUPPORTED_ALG) {
    v.valid = false;
    v.errors.push(`unsupported_alg: ${JSON.stringify(s.alg)}`);
  }
  const exp = s.key_expires as string | undefined;
  if (exp) {
    const expMs = parseIso(exp);
    if (Number.isNaN(expMs)) {
      v.valid = false;
      v.errors.push(`bad_key_expires: ${JSON.stringify(exp)}`);
    } else if (expMs < nowMs - skewSeconds * 1000) {
      v.valid = false;
      v.errors.push(`key_expired: ${exp}`);
    }
  }

  let pub: Uint8Array;
  try {
    pub = toRawPublicKey(await resolveKey(kid));
  } catch (e) {
    v.valid = false;
    v.errors.push(`key_resolution_failed: ${(e as Error).message}`);
    return v;
  }
  try {
    const ok = await verifyAsync(b64uDecode(String(s.sig ?? "")), signingInput, pub);
    if (!ok) {
      v.valid = false;
      v.errors.push("bad_signature");
    }
  } catch (e) {
    v.valid = false;
    v.errors.push(`signature_error: ${(e as Error).message}`);
  }
  return v;
}

/** Verify a v0.3 `attestation` block against the document it attests (RFC §2). */
export async function verifyAttestation(
  document: Doc,
  resolveKey: ResolveKey,
  opts: { now?: Date; skewSeconds?: number } = {},
): Promise<AttestationResult> {
  const nowMs = (opts.now ?? new Date()).getTime();
  const skew = opts.skewSeconds ?? DEFAULT_SKEW_SECONDS;
  const att = document.attestation as Record<string, unknown> | undefined;
  if (!att || typeof att !== "object") {
    return { valid: false, tier: null, computed_hash: null, errors: ["no_attestation_block"], signatures: [] };
  }

  const result: AttestationResult = {
    valid: true,
    tier: (att.tier as string) ?? null,
    computed_hash: null,
    errors: [],
    signatures: [],
  };

  // 1. hash recomputes over canonical bytes of the document minus `attestation`
  const content = attestedContent(document);
  const computed = await contentHash(content);
  result.computed_hash = computed;
  if (att.hash !== computed) {
    result.valid = false;
    result.errors.push(`hash_mismatch: claimed ${JSON.stringify(att.hash)} != computed ${JSON.stringify(computed)}`);
  }

  // 2. version chain (shape only)
  const version = att.version;
  if (typeof version !== "number" || !Number.isInteger(version) || version < 1) {
    result.valid = false;
    result.errors.push("version_must_be_positive_integer");
  } else {
    const prev = att.previous_hash;
    if (version === 1 && prev !== null && prev !== undefined && prev !== "") {
      result.errors.push("version_1_should_have_null_previous_hash");
    }
    if (version > 1 && !prev) {
      result.valid = false;
      result.errors.push("version_gt_1_requires_previous_hash");
    }
  }

  // 3. signatures (signing input = canonical bytes of the attested content)
  const signingInput = canonicalize(content);
  const sigs = (att.signatures as Record<string, unknown>[]) ?? [];
  let anyValid = false;
  for (const s of sigs) {
    const verdict = await verifyOne(s, signingInput, resolveKey, nowMs, skew);
    result.signatures.push(verdict);
    anyValid = anyValid || verdict.valid;
  }

  // 4. a signed tier needs at least one good signature; attested_by role correspondence
  const tier = att.tier as string | undefined;
  if (tier && SIGNED_TIERS.has(tier)) {
    if (!anyValid) {
      result.valid = false;
      result.errors.push(`tier_${tier}_requires_a_valid_signature`);
    }
    const attestedBy = document.attested_by as Record<string, unknown> | undefined;
    const roles = new Set(result.signatures.filter((x) => x.valid && x.role).map((x) => x.role));
    if (attestedBy && typeof attestedBy === "object" && attestedBy.role && !roles.has(attestedBy.role as string)) {
      result.errors.push("attested_by_role_has_no_matching_valid_signature");
    }
  }

  return result;
}
