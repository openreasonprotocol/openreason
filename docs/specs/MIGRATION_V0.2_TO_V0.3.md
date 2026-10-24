# Migration Guide: ORP v0.2 → v0.3

**Audience:** anyone with ORP v0.2 documents or tooling. **Spec:** `ORP_V0.3_SPEC.md`.
**Tooling:** `orp-validator` ≥ 0.5.0 (`pip install orp-validator`; add `[attestation]` for signatures).

---

## Overview

v0.3 is **additive and backward-compatible**. Everything it introduces — attestation, profiles, trust
tiers, usage policy, lineage, usage records, extra Layer-1 fields — is **optional in ORP-Core**. A v0.2
document becomes a valid v0.3 **ORP-Policy** document by changing one field. You adopt the machine-facing
features only if you are trading the document as a data product.

There is one semantic rename to be aware of: **compliance levels → trust tiers** (§8 of the spec). The old
`compliance_level` field still validates; v0.3 additionally reports a `trust_tier`.

---

## Quick Start: minimal migration (keep it a policy document)

### Step 1 — bump the version

```yaml
orp_version: "0.3"     # was "0.2"
```

### Step 2 — (recommended) declare the profile

A v0.2 document with L1+L2+L3 is an **ORP-Policy** document:

```yaml
profile: ORP-Policy
```

If you omit `profile`, it validates as **ORP-Core** (which does not require L2/L3). Declare `ORP-Policy`
to keep the v0.2 guarantee that consequence simulation and empathy mapping are present.

### Step 3 — update `last_modified` and validate

```bash
orp validate my-document.yaml --profile ORP-Policy
```

That is the whole minimal migration. Nothing else is required.

---

## What changed that you might notice

| v0.2 | v0.3 | Action |
|---|---|---|
| `compliance_level: ORP-Standard` etc. | still valid; `trust_tier` now also reported | none required |
| `l5_fork_registry` | still valid; `lineage` is the new home for forks **and** derivations | optional: move forks under `lineage.forks` |
| Layers numbered L1–L5 | L6 `usage_policy` added | optional |
| `attested_by` (human statement) | unchanged; add a signed `attestation` block to go beyond `self_declared` | optional |

No v0.2 field was removed or made stricter. If a v0.2 document validated, its v0.3-bumped form validates.

---

## Optional: become a verifiable data product

Do these only if the document describes a dataset/segment/corpus you want a machine to accept and prove use of.

### Add an attestation (reach `attested`)

Sign the RFC 8785 canonical form of the document **minus** the `attestation` block with an Ed25519 key, then:

```yaml
attestation:
  hash: "sha256:<recomputed>"
  version: 1
  previous_hash: null
  tier: attested
  signatures:
    - { kid: "did:web:you.example#k1", alg: Ed25519, use: orp-attestation,
        sig: "<base64url>", role: data_steward, key_expires: "2026-12-01T00:00:00Z" }
```

Without a key resolver a verifier caps you at `self_declared`; a valid owner signature reaches `attested`.
`verified`/`full` additionally require an **accredited** `verifier`-role signature (see spec §8).

### Add a usage policy (Layer 6)

```yaml
usage_policy:
  policy_id: "https://you.example/policy/1"
  permissions: [ { permission_id: p1, purpose: advertising_targeting, scope: { geo: [DK] }, derivation: internal } ]
  prohibitions: [ { purpose: model_training }, { purpose: resale } ]
  expiry: "2027-01-01T00:00:00Z"
```

A rail evaluates this with `orp_validator.usage.evaluate_policy` (deny-on-prohibition / deny-if-no-match /
unknown-purpose-or-scope fails closed).

### Pick a data-product profile

- **ORP-Ads** — add `reach` + `freshness` to each L1 dataset.
- **ORP-AI** — add `rights_holders` + `optout_signals_honoured` to each L1 dataset.

### Record derivations (lineage)

If this product was derived from another, add a `lineage.derivations` edge; a rail will enforce the
intersection of your policy and every ancestor's (spec §5).

---

## Example

Before (v0.2 policy document):

```yaml
orp_version: "0.2"
compliance_level: ORP-Standard
# ... L1 + L2 + L3 ...
```

After (minimal v0.3 — unchanged body):

```yaml
orp_version: "0.3"
profile: ORP-Policy
# ... L1 + L2 + L3 unchanged ...
```

A worked data-product example is in `examples/data_product_ctv_segment.v0.3.yaml` (ORP-Ads).

---

## Tooling notes

- `orp validate <doc> --profile <ORP-Core|ORP-Policy|ORP-Ads|ORP-AI>` — validate + report profile and tier.
- `orp conform` — run the v0.3 conformance suite.
- Attestation verification needs the optional extra: `pip install "orp-validator[attestation]"`.
- Python: `validate(doc, profile=..., resolve_key=..., accredited_verifiers=...)` returns `profile` and
  `trust_tier` on the result for v0.3 documents (v0.1/v0.2 output is unchanged).
