# OpenReason Protocol — v0.3 Specification

**Status:** Draft (as-built). Consolidates the changes proposed in `ORP_V0.3_RFC.md` into one normative
reference for v0.3 as implemented in `orp-validator` ≥ 0.5.0. Where this document and the RFC disagree,
this document (the as-built spec) wins; where it is silent, v0.2 (`ORP_V0.2_SPEC.md`) still applies.

**License:** Apache-2.0. **`orp_version`:** `"0.3"`.

---

## 0. What v0.3 adds, in one paragraph

v0.2 is a document standard for transparent, human-attested, human-read policy reasoning. v0.3 keeps all
of that and makes an ORP document additionally usable as a **machine-verifiable data product**: it can be
cryptographically **attested** (verified offline by a party that never met the publisher), split into
**profiles** so the core stays domain-neutral, graded by **trust tier**, carry an enforceable **usage
policy**, track **derivation lineage** with constraint inheritance, and record **usage**. None of this is
required of a plain policy document — v0.2-shaped documents remain valid under the ORP-Policy profile.

The eight RFC changes map to the sections below: C1 attestation (§2), C8 identifiers/access/freshness/reach
and C2 legal provenance (§3), C3 usage policy (§4), C4 lineage (§5), C5 usage records (§6), C6 profiles (§7),
C7 trust tiers (§8).

---

## 1. Document shape

A v0.3 document is a v0.2 document with `orp_version: "0.3"`, an optional `profile`, and these optional
additions: a top-level `attestation` block (§2); extended Layer-1 dataset fields (§3); a Layer-6
`usage_policy` (§4); Layer-5 `lineage` alongside or in place of `l5_fork_registry` (§5); and `usage_records`
in Layer-4 (§6). The required header is unchanged from v0.2, plus **L1 is required** in every profile.

---

## 2. Attestation (C1)

A top-level `attestation` block makes the document verifiable without trusting the publisher. It is
deliberately the **same crypto posture as an AdCP #4441 signed provenance claim** so a rail that already
verifies AdCP provenance verifies an ORP attestation with no new machinery.

```yaml
attestation:
  hash: "sha256:<hex>"          # sha256 over the RFC 8785 canonical form of the document MINUS this block
  version: 3                    # monotonically increasing per document/dataset id
  previous_hash: "sha256:..."   # hash of the prior version; null for version 1
  tier: attested                # see §8
  signatures:
    - kid: "did:web:example.org#key-1"   # resolvable to an Ed25519 public key (did:web / did:key / JWKS)
      alg: Ed25519
      use: orp-attestation      # key-purpose constraint; a key MUST NOT be accepted for another purpose
      sig: "<base64url>"        # detached Ed25519 signature over the canonical bytes
      role: data_steward        # who this key speaks for
      signed_at: "2026-09-24T12:00:00Z"
      key_expires: "2026-10-24T12:00:00Z"   # short-lived; a verifier MUST reject a past-expiry key (± skew)
```

**Verification (all failures are errors, not warnings):** recompute the hash over the canonical content
(document minus `attestation`); `version` is a positive integer and `previous_hash` is null iff `version == 1`;
each signature has `use == orp-attestation`, `alg == Ed25519`, an unexpired `key_expires`, a key resolvable
from `kid`, and a signature that verifies over the canonical bytes. Canonicalisation is RFC 8785 (JCS).
Verification MUST work offline given the key. Reference: `orp_validator.attestation.verify_attestation`.

Key discovery is the verifier's responsibility; the core does not fetch. `did:key` is accepted so agents
without a domain can attest. Keys SHOULD be short-lived and rotated rather than carried on a revocation list.

---

## 3. Layer 1 extensions — legal provenance (C2) + identifier/access/freshness/reach (C8)

All optional in ORP-Core (profiles make the relevant subset required). Added to each L1 dataset entry:

- `legal_basis`: `consent | contract | legitimate_interest | public_task | public_source | licence | other`
  (+ `legal_basis_detail`, `consent_scope`, `sensitive_categories` (empty list is a valid answer),
  `rights_holders`, `optout_signals_honoured` {`robots_txt`, `tdm_reservation`, `ai_txt`}, `data_subject_contact`).
- `access`: `{ visibility: public|restricted|private, endpoints: [{kind: sample|schema|full|activation, url, auth}], sample_hash }`.
- `freshness`: `{ collected_to, refreshed_at, decay_days }`.
- `reach`: `{ estimate, unit: people|devices|records|tokens, confidence: high|medium|low, as_of }`.

`dataset_id` SHOULD be a resolvable URI in the data-product profiles (ORP-Ads/ORP-AI).

---

## 4. Usage policy — Layer 6 (C3)

A profile of W3C ODRL 2.2 restricted to a fixed vocabulary, saying what may be done with the data product
in a form a rail can enforce automatically.

```yaml
usage_policy:
  policy_id: "https://..."
  permissions:
    - permission_id: "p1"
      purpose: advertising_targeting      # taxonomy below
      assignee: any                        # 'any' or a list of principal ids / DIDs
      scope: { geo: [DK], media: [ctv], time: { from, to } }
      derivation: internal                 # none | internal | licensed
      duties: [report_usage, delete_on_expiry]   # attribution | report_usage | delete_on_expiry | pay
  prohibitions: [ { purpose: model_training }, { purpose: resale } ]
  expiry: "2027-10-24T00:00:00Z"
  revocable: true
  governing_law: "DK"
```

**Purpose taxonomy (normative):** `advertising_targeting, suppression, measurement, analytics,
model_training, fine_tuning, evaluation, retrieval, inference, resale, research`. Profiles may restrict,
not extend.

**Evaluation (normative, RFC §5.5).** Given a context `{purpose, assignee?, geo?, media?, time?,
derivation_requested?}` an evaluator MUST return **deny** if any prohibition matches, **deny** if no
permission matches, otherwise **allow** with the matching permission id. **Unknown purpose or unknown
scope key ⇒ deny** (fail closed). Derivation is ordered `none < internal < licensed` (a grant permits
itself and anything below). Reference: `orp_validator.usage.evaluate_policy`.

---

## 5. Lineage — Layer 5 as a derivation graph (C4)

```yaml
lineage:
  forks: [ ... ]                 # v0.2 semantics, unchanged: alternative reasoning
  derivations:                   # new: this product was produced from these ancestors
    - parent_id: "https://..."
      parent_hash: "sha256:..."
      transformation: subset | overlap | lookalike | aggregation | enrichment | training | other
      inherits: full | relaxed
      relaxation_basis: "<ancestor permission_id>"   # REQUIRED if inherits == relaxed
  this_document: { forking_permitted: true, derivation_permitted: none|internal|licensed }
```

**Inheritance (normative, RFC §6.3).** A derivative's effective policy is the **intersection** of its own
`usage_policy` and every ancestor's — an activation is allowed only if every policy in the ancestry allows
it. Exception: an ancestor that granted `derivation: licensed` via the permission named in a `relaxed`
edge's `relaxation_basis` is enforced via its `derivative_policy` instead. The walk descends **every**
`derivations` edge (a DAG), to the root or to the nearest ancestor whose attestation tier is `verified`+
(which vouches for everything above it), whichever comes first; it fails closed on an unresolved ancestor.
Reference: `orp_validator.lineage.resolve_effective_decision`.

---

## 6. Usage records — Layer 4 (C5)

An append-only record of *use*, added alongside the v0.2 decision ledger:

```yaml
accountability_ledger:
  usage_records:
    - { record_id, timestamp, dataset_id, dataset_hash, policy_hash, counterparty, purpose,
        context: { geo, media, execution_id, volume }, fee: { amount, currency },
        signatures: [ { kid, alg, sig, role: rail|licensee|licensor } ] }
```

**Receipt equivalence (normative, RFC §7.2):** a rail's signed clearing receipt that carries the dataset
and policy hashes **is** a usage record by construction. The ledger MAY live at the rail rather than in the
document (`usage_ledger: { url, query }` pointer). Reference: `orp_validator.usage.usage_record_from_receipt`
and `verify_usage_record`.

---

## 7. Profiles (C6)

The spec is a **core plus profiles**. The validator takes `--profile` (or reads the document's `profile`
field; default **ORP-Core**).

| Profile | Adds to ORP-Core |
|---|---|
| **ORP-Core** | Header + L1 + optional attestation/L2/L3/L4/L5/L6. Domain-neutral. |
| **ORP-Policy** | L2 (Consequence Simulation) and L3 (Empathy Mapping) required. The v0.2 shape, renamed. |
| **ORP-Ads** | Segment vocabulary: every L1 dataset carries `reach` + `freshness`. |
| **ORP-AI** | Corpus vocabulary: every L1 dataset carries `rights_holders` + `optout_signals_honoured`. |

Each profile is a JSON Schema that extends the core schema. (ODRL/AdCP-signals bindings for ORP-Ads and the
regulatory-summary export for ORP-AI are later refinements.)

---

## 8. Trust tiers (C7)

Compliance levels are renamed to trust tiers. A claimed tier never exceeds what the signatures prove.

| Tier | Requires | Verified how |
|---|---|---|
| `self_declared` | Core fields present; self/platform signature or none | Schema validation |
| `attested` | A valid owner-key signature | Signature verification |
| `verified` | A valid signature with `role: verifier` whose `kid` is on the accredited-verifier list, and who is **not** the dataset's own owner | Verifier signature vs the accredited list |
| `full` | `verified` plus an L3 impact statement where the profile requires it | As above + L3 |
| `posthoc` | L1/L4 reconstructed, `post_hoc: true` | Schema validation |

Accredited verifiers are maintained in `orp_validator/schemas/accredited_verifiers.json` (empty by default →
nothing reaches `verified`, fail safe); a caller may override. A rail MAY refuse purposes below a tier; the
spec does not price tiers. Reference: `ORPValidator.validate(..., resolve_key=, accredited_verifiers=)`.

---

## 9. Conformance (§9.2)

An implementation claims conformance by passing the bundled suite: per-profile positive/negative schema
fixtures, usage-policy evaluation fixtures (§4), and lineage inheritance fixtures (§5). Run `orp conform`
(exit 0/1) or `orp_validator.conformance.run()`. CI runs it on every change.

---

## 10. Backward compatibility

v0.1/v0.2 documents validate unchanged under their own `orp_version`. A v0.2 document becomes a valid
ORP-Policy v0.3 document by bumping `orp_version` to `"0.3"` (see `MIGRATION_V0.2_TO_V0.3.md`). Everything
v0.3 adds is additive and optional in ORP-Core.
