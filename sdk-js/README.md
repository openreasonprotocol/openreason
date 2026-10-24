# @openreason/sdk

Validate and cryptographically verify [OpenReason Protocol](https://openreasonprotocol.org) (ORP) documents in Node and the browser.

Attestation verification is a faithful port of the Python reference (`orp-validator`): the same RFC 8785 canonical form, the same SHA-256 content hash, the same Ed25519 check. A signature made on one side verifies on the other.

```bash
npm install @openreason/sdk
```

```ts
import { validateDocument, checkDocument, verifyAttestation } from "@openreason/sdk";

const result = validateDocument(doc);      // schema validity (ORP v0.1, v0.2)
const check  = checkDocument(doc);         // compliance level, layers present

// Offline: recompute the hash, check the Ed25519 signature. did:key kids self-resolve.
const verdict = await verifyAttestation(doc, (kid) => kid);
console.log(verdict.valid, verdict.tier, verdict.computed_hash);
```

Key resolution is the caller's job: the SDK makes no network calls and fails closed on unknown keys.

Docs: https://openreasonprotocol.org/tools/javascript-sdk · Source: https://github.com/openreasonprotocol/openreason/tree/main/sdk-js · Apache-2.0
