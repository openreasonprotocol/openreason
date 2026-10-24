// @openreason/sdk — validate and cryptographically verify OpenReason Protocol documents.
// Works in Node and the browser. Attestation verification is a faithful port of the
// Python reference (orp-validator), so signatures interoperate across both SDKs.

export * from "./validate.js";
export { checkDocument, type CheckResult } from "./check.js";
export {
  verifyAttestation,
  contentHash,
  attestedContent,
  publicKeyFromDidKey,
  b64uDecode,
  ATTESTATION_USE,
  SUPPORTED_ALG,
  DEFAULT_SKEW_SECONDS,
} from "./attestation.js";
export type { ResolveKey, KeyMaterial, AttestationResult, SignatureVerdict } from "./attestation.js";
export { canonicalize, canonicalString } from "./canonicalize.js";
