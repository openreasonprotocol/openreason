# Security policy

OpenReason's value rests on verification being trustworthy. If you find a way to make the validator accept a document it should reject, verify a signature it should not, or evaluate a usage policy more permissively than the specification says, we want to hear from you first.

## Supported versions

| Package | Supported |
|---|---|
| `orp-validator` 0.5.x (ORP v0.3) | Yes |
| `orp-validator` < 0.5 | No, please upgrade |
| `@openreason/sdk`, `@openreason/mcp` | Latest commit on `main` |
| Hosted API `api.publicreasonproject.org` | Current deployment |

## Reporting a vulnerability

- Email **security@publicreasonproject.org**. Please do not open a public issue for anything that could let a document pass verification incorrectly.
- Include: the affected component and version, a minimal reproducing document or request, and what you expected versus what happened.
- We acknowledge reports within 3 working days and aim to publish a fix and advisory within 30 days for confirmed issues. We will credit you unless you ask otherwise.

## What counts

In scope: signature or hash verification bypass, canonicalisation ambiguities that let two documents share a hash, key-resolution weaknesses (for example accepting a key for the wrong purpose or after expiry), usage-policy or lineage evaluation that is more permissive than the spec, and injection or denial-of-service in the hosted API.

Out of scope: findings that require a compromised signing key, reports against the marketing site, and the fact that `self_declared` documents are, by design, not verified.

## Design notes for researchers

- Verification is offline and fail-closed. Unknown `kid`, wrong key `use`, expired keys and unresolved lineage ancestors are hard errors.
- The signing input is the RFC 8785 (JCS) canonical form of the document minus its own `attestation` block, hashed with SHA-256.
- `verified` and `full` trust tiers require a signature from an accredited verifier who is not the document owner.
