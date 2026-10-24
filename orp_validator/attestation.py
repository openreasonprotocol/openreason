"""Cryptographic attestation for ORP v0.3 (RFC: docs/specs/ORP_V0.3_RFC.md, change C1).

This is the keystone that lets an agent that has *never met the publisher* verify an ORP document
offline: recompute the content hash, verify a detached Ed25519 signature against a key it resolves
itself, and enforce a key-purpose constraint and a short-lived-key expiry. It is deliberately the
same crypto posture as an AdCP #4441 signed-provenance claim (RFC 8785 canonicalisation, Ed25519,
purpose-constrained short-lived keys, JWKS / did:key discovery) so that a rail which already verifies
AdCP provenance — e.g. Railu/Yumipop — verifies an ORP attestation with no new machinery.

Design rules (match the repo's conventions):
  * Pure + offline. No network. Key *resolution* is the caller's job (pass a `resolve_key`
    callable), exactly as signing is the caller's job on the rail side. This keeps the module
    portable and the core dependency-light.
  * Crypto is an OPTIONAL dependency (`pip install orp-validator[attestation]`). Canonicalisation
    and hashing work with the standard library alone; signature verification degrades gracefully to
    a clear `crypto_unavailable` error rather than a crash when `cryptography` is absent.
  * Failures are errors, not warnings (RFC §2.4): a tampered document, an unknown/expired/wrong-use
    key, or a bad signature all make the attestation invalid.

Known limitation (documented, not hidden — see CLAUDE.md): the RFC 8785 number serialisation here is
exact for integers, booleans, null, strings and typical finite decimals; the full ECMAScript
shortest-round-trip float formatting for exotic exponents is best-effort via Python's `repr`. ORP
attested content is JSON/YAML with integers and enums, so this is not hit in practice; NaN/Infinity
are rejected outright. The exact JOSE-envelope detail is pinned to AdCP #4441 (see `verify_attestation`).
"""

from __future__ import annotations

import base64
import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Callable

ATTESTATION_USE = "orp-attestation"  # the key-purpose constraint value (mirrors AdCP `adcp_use: provenance-claim`)
SUPPORTED_ALG = "Ed25519"
DEFAULT_SKEW_SECONDS = 300  # reasonable clock skew for key_expires (RFC §2.4)

# Optional crypto. The module imports and hashes fine without it; only signature verification needs it.
try:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

    CRYPTO_AVAILABLE = True
except Exception:  # pragma: no cover - exercised only in crypto-less environments
    CRYPTO_AVAILABLE = False
    Ed25519PublicKey = None  # type: ignore
    InvalidSignature = Exception  # type: ignore


# --------------------------------------------------------------------------------------
# RFC 8785 JSON Canonicalization Scheme (JCS)
# --------------------------------------------------------------------------------------


def _canon_string(s: str) -> str:
    """Serialise a JSON string per RFC 8785 §3.2.2.2: escape only what MUST be escaped."""
    out = ['"']
    for ch in s:
        code = ord(ch)
        if ch == '"':
            out.append('\\"')
        elif ch == "\\":
            out.append("\\\\")
        elif ch == "\b":
            out.append("\\b")
        elif ch == "\t":
            out.append("\\t")
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\f":
            out.append("\\f")
        elif ch == "\r":
            out.append("\\r")
        elif code < 0x20:
            out.append(f"\\u{code:04x}")
        else:
            # Everything else (including non-ASCII) is emitted literally as UTF-8. Forward slash is NOT escaped.
            out.append(ch)
    out.append('"')
    return "".join(out)


def _canon_number(n: Any) -> str:
    """Serialise a number per RFC 8785 §3.2.2.3 (ECMAScript Number::toString).

    Exact for integers; best-effort shortest-round-trip for finite floats via `repr`. Rejects
    NaN/Infinity (not valid JSON). Integer-valued floats collapse to the integer form.
    """
    if isinstance(n, bool):  # bool is a subclass of int — guard explicitly
        raise TypeError("bool is not a JSON number")
    if isinstance(n, int):
        return str(n)
    # float
    if n != n or n in (float("inf"), float("-inf")):
        raise ValueError("NaN and Infinity are not permitted in canonical JSON")
    if n == int(n) and abs(n) < 1e21:
        return str(int(n))
    return repr(n)


def canonicalize(obj: Any) -> bytes:
    """Return the RFC 8785 canonical UTF-8 bytes of a JSON-compatible Python value.

    Object keys are sorted by Unicode code point (equivalent to the spec's UTF-16 ordering for the
    BMP, which covers every key ORP uses). No insignificant whitespace.
    """
    return _canon(obj).encode("utf-8")


def _canon(obj: Any) -> str:
    if obj is None:
        return "null"
    if obj is True:
        return "true"
    if obj is False:
        return "false"
    if isinstance(obj, str):
        return _canon_string(obj)
    if isinstance(obj, (int, float)):
        return _canon_number(obj)
    if isinstance(obj, (list, tuple)):
        return "[" + ",".join(_canon(v) for v in obj) + "]"
    if isinstance(obj, dict):
        items = sorted(obj.items(), key=lambda kv: kv[0])
        return "{" + ",".join(_canon_string(str(k)) + ":" + _canon(v) for k, v in items) + "}"
    raise TypeError(f"not JSON-serialisable for canonicalisation: {type(obj).__name__}")


def content_hash(content: Any) -> str:
    """sha256 over the canonical bytes, in the spec's `sha256:<hex>` form."""
    return "sha256:" + hashlib.sha256(canonicalize(content)).hexdigest()


def attested_content(document: dict[str, Any]) -> dict[str, Any]:
    """The content that is hashed/signed: the document WITHOUT its own `attestation` block (RFC §2.3)."""
    return {k: v for k, v in document.items() if k != "attestation"}


# --------------------------------------------------------------------------------------
# Keys
# --------------------------------------------------------------------------------------

_B58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def _b58decode(s: str) -> bytes:
    num = 0
    for ch in s:
        idx = _B58_ALPHABET.find(ch)
        if idx == -1:
            raise ValueError(f"invalid base58 character: {ch!r}")
        num = num * 58 + idx
    full = num.to_bytes((num.bit_length() + 7) // 8, "big") if num else b""
    pad = len(s) - len(s.lstrip("1"))  # leading '1's are leading zero bytes
    return b"\x00" * pad + full


def public_key_from_did_key(did: str) -> bytes:
    """Decode a `did:key:z6Mk...` Ed25519 DID into 32 raw public-key bytes (pure, offline).

    did:key = 'did:key:' + multibase('z' = base58btc)( multicodec(0xed 0x01) || raw32 ).
    """
    if not did.startswith("did:key:z"):
        raise ValueError("not a base58btc did:key")
    decoded = _b58decode(did[len("did:key:z") :])
    if len(decoded) < 2 or decoded[0] != 0xED or decoded[1] != 0x01:
        raise ValueError("did:key multicodec is not ed25519-pub (0xed01)")
    raw = decoded[2:]
    if len(raw) != 32:
        raise ValueError(f"ed25519 public key must be 32 bytes, got {len(raw)}")
    return raw


def load_ed25519_public_key(material: Any) -> Ed25519PublicKey:
    """Build an Ed25519 public key object from raw 32 bytes, a base64url string, a did:key, or a JWK dict."""
    if not CRYPTO_AVAILABLE:
        raise RuntimeError("crypto_unavailable: install orp-validator[attestation]")
    if isinstance(material, Ed25519PublicKey):
        return material
    if isinstance(material, dict):  # JWK: {"kty":"OKP","crv":"Ed25519","x":"<b64url>"}
        material = b64u_decode(material["x"])
    elif isinstance(material, str):
        material = (
            public_key_from_did_key(material)
            if material.startswith("did:key:")
            else b64u_decode(material)
        )
    if not isinstance(material, (bytes, bytearray)) or len(material) != 32:
        raise ValueError("expected 32 raw Ed25519 public-key bytes")
    return Ed25519PublicKey.from_public_bytes(bytes(material))


def b64u_decode(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def b64u_encode(b: bytes) -> str:
    return base64.urlsafe_b64encode(b).decode("ascii").rstrip("=")


# --------------------------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------------------------


@dataclass
class SignatureVerdict:
    kid: str
    valid: bool
    role: str | None = None
    errors: list[str] = field(default_factory=list)


@dataclass
class AttestationResult:
    valid: bool
    tier: str | None = None
    computed_hash: str | None = None
    errors: list[str] = field(default_factory=list)
    signatures: list[SignatureVerdict] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "tier": self.tier,
            "computed_hash": self.computed_hash,
            "errors": self.errors,
            "signatures": [
                {"kid": s.kid, "valid": s.valid, "role": s.role, "errors": s.errors}
                for s in self.signatures
            ],
        }


ResolveKey = Callable[
    [str], Any
]  # kid -> key material (raw32 / b64url / did:key / JWK / Ed25519PublicKey)

_SIGNED_TIERS = {"attested", "verified", "full"}


def _parse_iso(ts: str) -> datetime:
    dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def verify_attestation(
    document: dict[str, Any],
    resolve_key: ResolveKey,
    now: datetime | None = None,
    skew_seconds: int = DEFAULT_SKEW_SECONDS,
) -> AttestationResult:
    """Verify a v0.3 `attestation` block against the document it attests (RFC §2, change C1).

    Checks, all of which are hard failures:
      1. hash recomputes over the canonical bytes of the document minus `attestation`;
      2. version is a positive integer; previous_hash is null iff version == 1 (shape only, offline);
      3. every signature: `use == orp-attestation`, `alg == Ed25519`, key not expired (with skew),
         key resolves via `resolve_key(kid)`, and the detached signature verifies over the canonical bytes;
      4. for a signed tier, at least one signature verifies.

    The signing input is the RFC 8785 canonical bytes of the attested content; `sig` is the base64url
    Ed25519 signature, with `kid`/`alg`/`use`/`role` as sibling fields (the construction the v0.3 schema
    encodes). The exact JOSE/detached-JWS envelope is pinned to AdCP #4441 — the ONE spot to reconcile
    when AdCP's construction is confirmed; `_signing_input` isolates it so that reconciliation is a
    one-line change, not a rewrite.
    """
    now = now or datetime.now(timezone.utc)
    att = document.get("attestation")
    if not isinstance(att, dict):
        return AttestationResult(valid=False, errors=["no_attestation_block"])

    result = AttestationResult(valid=True, tier=att.get("tier"))

    # 1. hash
    content = attested_content(document)
    computed = content_hash(content)
    result.computed_hash = computed
    claimed = att.get("hash")
    if claimed != computed:
        result.valid = False
        result.errors.append(f"hash_mismatch: claimed {claimed!r} != computed {computed!r}")

    # 2. version chain (shape only — resolving a prior version needs a store the caller owns)
    version = att.get("version")
    if not isinstance(version, int) or isinstance(version, bool) or version < 1:
        result.valid = False
        result.errors.append("version_must_be_positive_integer")
    else:
        prev = att.get("previous_hash")
        if version == 1 and prev not in (
            None,
            "",
        ):
            result.errors.append("version_1_should_have_null_previous_hash")
        if version > 1 and not prev:
            result.valid = False
            result.errors.append("version_gt_1_requires_previous_hash")

    # 3. signatures
    signing_input = _signing_input(content)
    sigs = att.get("signatures") or []
    any_valid = False
    for s in sigs:
        v = _verify_one_signature(s, signing_input, resolve_key, now, skew_seconds)
        result.signatures.append(v)
        any_valid = any_valid or v.valid

    # 4. a signed tier needs at least one good signature; attested_by role correspondence (RFC §2.2)
    tier = att.get("tier")
    if tier in _SIGNED_TIERS:
        if not any_valid:
            result.valid = False
            result.errors.append(f"tier_{tier}_requires_a_valid_signature")
        attested_by = document.get("attested_by")
        roles = {s.role for s in result.signatures if s.valid and s.role}
        if (
            isinstance(attested_by, dict)
            and attested_by.get("role")
            and attested_by["role"] not in roles
        ):
            result.errors.append("attested_by_role_has_no_matching_valid_signature")

    return result


def _signing_input(content: dict[str, Any]) -> bytes:
    """The bytes a signature is computed over. Isolated so the AdCP #4441 envelope detail lives in one place."""
    return canonicalize(content)


def _verify_one_signature(
    s: dict[str, Any],
    signing_input: bytes,
    resolve_key: ResolveKey,
    now: datetime,
    skew_seconds: int,
) -> SignatureVerdict:
    kid = str(s.get("kid", ""))
    verdict = SignatureVerdict(kid=kid, valid=True, role=s.get("role"))

    if s.get("use") != ATTESTATION_USE:
        verdict.valid = False
        verdict.errors.append(f"wrong_key_use: {s.get('use')!r} != {ATTESTATION_USE!r}")
    if s.get("alg") != SUPPORTED_ALG:
        verdict.valid = False
        verdict.errors.append(f"unsupported_alg: {s.get('alg')!r}")

    exp = s.get("key_expires")
    if exp:
        try:
            # Lenient by skew: a key counts as expired only once it is past its expiry by more than the skew.
            if _parse_iso(exp) < now - timedelta(seconds=skew_seconds):
                verdict.valid = False
                verdict.errors.append(f"key_expired: {exp}")
        except Exception:
            verdict.valid = False
            verdict.errors.append(f"bad_key_expires: {exp!r}")

    if not CRYPTO_AVAILABLE:
        verdict.valid = False
        verdict.errors.append("crypto_unavailable")
        return verdict

    try:
        pub = load_ed25519_public_key(resolve_key(kid))
    except Exception as e:
        verdict.valid = False
        verdict.errors.append(f"key_resolution_failed: {e}")
        return verdict

    try:
        pub.verify(b64u_decode(str(s.get("sig", ""))), signing_input)
    except InvalidSignature:
        verdict.valid = False
        verdict.errors.append("bad_signature")
    except Exception as e:
        verdict.valid = False
        verdict.errors.append(f"signature_error: {e}")

    return verdict
