# RFC: OpenReason Protocol v0.3, machine-attested data products

**Status:** Draft for discussion
**Date:** 2026-09-24
**Applies to:** OpenReason Protocol v0.2 (released 2026-04-08)
**Audience:** Claude Code in the Public Reason Project repo, and contributors. This RFC proposes changes to the specification, the validator, the JSON-LD context and the compliance levels.
**Companion:** `yumipop-data-layer-brief.md` in the Yumipop repo. Yumipop is the first implementer of the profiles defined here; this RFC does not depend on it.

---

## 0. Motivation

ORP v0.2 is a document standard for transparent, reproducible policy reasoning. Its five layers (Data Provenance, Consequence Simulation, Empathy Mapping, Accountability Ledger, Fork Registry) are written by people, attested by name, validated as YAML, and read by people.

A second use has appeared that the current spec almost serves: describing a **data product** (an audience segment, a dataset, a corpus) so that a machine on the other side of a trade can decide whether to accept it, under what terms, and prove afterwards what it did with it. Layer 1 already asks the right questions about a dataset, and asks several that no commercial data standard asks (`cleaning_decisions`, `synthetic_elements`, `known_limitations`). Layer 4 is a ledger. Layer 5 is lineage. The compliance levels are a trust tier waiting to be priced.

What is missing is everything a machine needs and a person does not: cryptographic attestation, a usage policy it can enforce, a lineage model for derived datasets rather than forked documents, a transactional ledger entry, and a profile mechanism so the core stays domain-neutral while advertising and AI-training profiles can be strict.

This RFC proposes those changes. The intent is that ORP becomes the passport format for any data product traded on agent-to-agent rails, that the first rail to enforce an ORP passport rather than merely read it is Yumipop, and that the two reinforce each other without either depending on the other's adoption.

Design principles kept from v0.2: explicit over implicit; limitations stated, not hidden; every decision has an author; forks are invited. Added: every claim verifiable without trusting the author; every use recorded.

---

## 1. Summary of changes

| # | Change | Layer | Breaking? |
|---|---|---|---|
| C1 | Cryptographic attestation: content hash, version chain, signature, key discovery | all | No (additive) |
| C2 | Legal provenance fields | L1 | No (new required fields in profiles only) |
| C3 | Usage policy as a new section (`usage_policy`), ODRL profile | L1 or new L6 | No |
| C4 | Layer 5 becomes a derivation graph with constraint inheritance | L5 | Yes for L5 semantics; v0.2 forks map to one derivation kind |
| C5 | Layer 4 gains a signed `usage_record` entry type | L4 | No |
| C6 | Profiles: ORP-Core, ORP-Ads, ORP-AI | spec structure | No |
| C7 | Compliance levels become trust tiers with verification methods; JSON Schema conformance suite | validation | Renames; v0.2 levels map 1:1 |
| C8 | Identifier and access changes: resolvable `dataset_id`, endpoint descriptors, freshness, reach with confidence | L1 | No |

Sections 2 to 9 give each change in detail. Section 10 lists implementation tasks for the repo.

---

## 2. C1: Cryptographic attestation

### 2.1 Problem

`attested_by` is a name, a role, a date and a statement. A reader must trust the publisher of the document. An agent that has never met the publisher cannot.

### 2.2 Proposal

Add a top-level `attestation` block to every ORP document and, in profiles, to every dataset entry:

```yaml
attestation:
  hash: "sha256:..."            # over canonical serialisation of the attested content (see 2.3)
  version: 3                    # monotonically increasing per dataset_id
  previous_hash: "sha256:..."   # hash of version 2; null for version 1
  signatures:
    - kid: "did:web:example.org#key-1"   # or a JWKS-resolvable key id
      alg: "Ed25519"
      sig: "base64url..."
      role: "data_steward"      # who this key speaks for
      signed_at: "2026-09-24T12:00:00Z"
  tier: "attested"              # see C7
```

`attested_by` is retained as the human-readable statement and MUST correspond to at least one signature's `role` when `tier` is `attested` or above.

### 2.3 Canonicalisation

Use JSON Canonicalization Scheme (RFC 8785) over the JSON-LD form of the attested content, excluding the `attestation` block itself. The validator MUST recompute the hash and MUST verify every signature against a key resolved from `kid` (DID document, or a `/.well-known/jwks.json` on the `kid`'s host). Verification MUST work offline given the key.

### 2.4 Effect on the validator

New checks: hash recomputes; every signature verifies; `previous_hash` resolves to a known prior version or is null; `version` increments. Failures are errors, not warnings.

---

## 3. C8: Identifiers, access, freshness, reach

Grouped here because they are all Layer 1 field changes.

- `dataset_id` MUST be a resolvable URI (`https://` or `did:`), not a local string. Dereferencing it SHOULD return the current attested document.
- `access` becomes an object: `{ visibility: public | restricted | private, endpoints: [{ kind: sample | schema | full | activation, url, auth }], sample_hash }`. A machine can then fetch a sample and a schema before deciding.
- `freshness: { collected_to: date, refreshed_at: date, decay_days: int }` for datasets whose value decays (audience segments especially).
- `reach: { estimate: int, unit: "people" | "devices" | "records" | "tokens", confidence: high | medium | low, as_of: date }`, reusing the Layer 3 confidence vocabulary rather than inventing one.

---

## 4. C2: Legal provenance fields (Layer 1)

### 4.1 Problem

Layer 1 says how data was collected and cleaned but not on what legal footing, which is the first question a buyer's counsel asks and the first thing a regulator asks about a training set.

### 4.2 Proposal

Add to Layer 1:

```yaml
legal_basis: consent | contract | legitimate_interest | public_task | public_source | licence | other
legal_basis_detail: "..."                  # required if other
consent_scope:                             # required if legal_basis == consent
  purposes: [ ... ]                        # from the purpose taxonomy, §5.3
  collected_via: "..."
  withdrawal_mechanism: "..."
sensitive_categories: [ ... ]              # empty list is a valid, meaningful answer
rights_holders:                            # for content datasets
  - { name, role: author | publisher | licensor, licence: "SPDX id or URL" }
optout_signals_honoured:                   # for scraped or crawled sources
  robots_txt: true | false | not_applicable
  tdm_reservation: true | false | not_applicable   # EU DSM Directive art. 4 machine-readable reservation
  ai_txt: true | false | not_applicable
  other: [ ... ]
data_subject_contact: "..."                # where rights requests go
```

`sensitive_categories` MUST be present (possibly empty) in every profile. A non-empty value raises the minimum tier for certain purposes (C7).

---

## 5. C3: Usage policy

### 5.1 Problem

ORP describes what a dataset is. A trade needs to say what may be done with it, in a form a rail can enforce automatically and a lawyer can read.

### 5.2 Proposal

A new section, `usage_policy`, defined as a profile of W3C ODRL 2.2 restricted to a fixed vocabulary. It can live inside Layer 1 or be numbered Layer 6; this RFC proposes Layer 6 so that Layer 1 stays descriptive and the policy is separately versioned and hashed.

```yaml
usage_policy:
  policy_id: "https://..."
  hash: "sha256:..."
  permissions:
    - purpose: advertising_targeting
      assignee: any | [principal ids]
      scope:
        geo: [ "DK", "SE" ]
        media: [ "ctv", "web" ]
        time: { from, to }
      derivation: none | internal | licensed
      duties: [ attribution | report_usage | delete_on_expiry | pay ]
  prohibitions:
    - purpose: model_training
    - purpose: resale
  expiry: "2026-12-31T23:59:59Z"
  revocable: true
  governing_law: "DK"
```

### 5.3 Purpose taxonomy (normative)

`advertising_targeting`, `suppression`, `measurement`, `analytics`, `model_training`, `fine_tuning`, `evaluation`, `retrieval`, `inference`, `resale`, `research`. Profiles may restrict but not extend this list; extension goes through the spec.

### 5.4 Derivation values

- `none`: no derivative datasets or models may be produced.
- `internal`: derivatives may be produced for the assignee's own use and inherit this policy in full (C4).
- `licensed`: derivatives may be produced under a stated `derivative_policy` that may relax specified constraints; ownership of the derivative is stated (`assignee` | `licensor` | `shared`).

For `model_training` and `fine_tuning`, a derivative is the model. The policy MUST say whether the model may be distributed and under what duties. This is the clause that matters most for AI datasets, and the one that cannot be undone after the fact.

### 5.5 Evaluation semantics

An implementer evaluating a policy against a context `{purpose, assignee, geo, media, time, derivation_requested}` MUST return `deny` if any prohibition matches, `deny` if no permission matches, and `allow` with the matching permission id otherwise. Unknown purpose or unknown scope keys MUST evaluate to `deny`. The spec SHOULD ship a reference evaluator and a fixture suite.

---

## 6. C4: Layer 5 as a derivation graph

### 6.1 Problem

The Fork Registry tracks forks of a *document*: alternative reasoning about the same question. Data products are derived from other data products (an overlap, a lookalike, a filtered subset, a model trained on a corpus), and each derivative must carry its ancestors' constraints. These are different relationships.

### 6.2 Proposal

Layer 5 becomes `lineage` with two relationship kinds:

```yaml
lineage:
  forks:                       # v0.2 semantics, unchanged: alternative reasoning
    - { fork_id, title, authors, created, key_differences, url }
  derivations:                 # new: this dataset was produced from these
    - parent_id: "https://..."
      parent_hash: "sha256:..."
      parent_policy_hash: "sha256:..."
      transformation: subset | overlap | lookalike | aggregation | enrichment | training | other
      transformation_detail: "..."
      inherits: full | relaxed
      relaxation_basis: "parent policy permission id"   # required if relaxed
  this_document:
    forking_permitted: true
    derivation_permitted: none | internal | licensed   # mirrors usage_policy
```

### 6.3 Inheritance rule (normative)

A derivative's effective policy is the intersection of its own `usage_policy` and every ancestor's, unless an ancestor's policy grants `derivation: licensed` with a `derivative_policy` that explicitly relaxes a named constraint. An implementer enforcing a policy MUST walk `derivations` to the root, or to the nearest ancestor whose attestation tier is `verified` or above, whichever comes first.

`responses_to_forks` from v0.2 is kept under `forks`.

---

## 7. C5: Layer 4 usage records

### 7.1 Problem

The Accountability Ledger records methodological decisions by named people. A traded dataset also needs a record of *use*: who activated it, for what, under which policy, when. Today that record exists only in the counterparties' private logs.

### 7.2 Proposal

Add an entry type to Layer 4:

```yaml
accountability_ledger:
  decisions:                   # v0.2 entries, unchanged
    - { timestamp, decision, decision_maker, role, basis, affected_sections }
  usage_records:               # new
    - record_id: "..."
      timestamp: "..."
      dataset_id: "..."
      dataset_hash: "sha256:..."
      policy_hash: "sha256:..."
      counterparty: "principal id or DID"
      purpose: "..."             # from §5.3
      context: { geo, media, execution_id, volume }
      fee: { amount, currency }  # optional
      signatures: [ { kid, alg, sig, role: "rail" | "licensee" | "licensor" } ]
```

Usage records are append-only. A record signed by a neutral rail and referencing the dataset and policy hashes is a **receipt**; a rail's signed clearing receipt that carries these fields is a valid usage record by construction. The ledger MAY be held by the rail rather than inside the document, in which case the document's Layer 4 carries a pointer (`usage_ledger: { url, query }`).

---

## 8. C6: Profiles

### 8.1 Problem

Policy reasoning needs Layers 2 and 3. A segment trade does not. A training corpus with people in it needs Layer 3 again. One set of requirements cannot serve all three.

### 8.2 Proposal

Split the spec into a core and profiles:

- **ORP-Core**: Layer 1 (with C2, C8), attestation (C1), Layer 4 (with C5), Layer 5 (C4), Layer 6 usage policy (C3). Layers 2 and 3 optional.
- **ORP-Policy**: the v0.2 shape. Core plus Layers 2 and 3 required at Standard and above. This is the existing use, renamed.
- **ORP-Ads**: Core with a segment vocabulary: `reach` in people or devices, `freshness` required, purpose restricted to advertising purposes plus `measurement` and `analytics`, field mapping to the IAB Tech Lab Data Transparency Standard published as a table, and an AdCP signals binding (`get_signals` returns the passport summary; `activate_signal` requires an `allow` from the policy evaluator).
- **ORP-AI**: Core with a corpus vocabulary: `reach` in records or tokens, `rights_holders` and `optout_signals_honoured` required, purposes `model_training` through `inference`, Layer 3 (impact on data subjects) required at the `full` tier when `sensitive_categories` is non-empty or the corpus contains personal data, and an export format for regulatory training-data summaries.

Each profile is a JSON Schema that extends the core schema. The validator takes `--profile`.

---

## 9. C7: Trust tiers and conformance

### 9.1 Proposal

Rename the compliance levels to trust tiers, keep the mapping, add verification methods and one new tier:

| v0.3 tier | v0.2 level | Requires | Verified how |
|---|---|---|---|
| `self_declared` | ORP-Basic | Core fields present, platform or self signature | Schema validation |
| `attested` | ORP-Standard | Owner-key signature, named steward, Layers 2 and 3 in ORP-Policy | Signature verification |
| `verified` | (new) | Independent party has checked the passport against the data and signed | Verifier signature with `role: verifier` from an accredited key list |
| `full` | ORP-Full | `verified` plus Layer 3 impact statement where the profile requires it | As above plus L3 validation |
| `posthoc` | ORP-PostHoc | L1 and L4 reconstructed, marked as such | Schema validation, `reconstructed: true` |

Rails and marketplaces MAY refuse purposes below a tier; the spec does not price tiers.

### 9.2 Conformance suite

Publish the schemas as JSON Schema (draft 2020-12) alongside the YAML validator, and a conformance suite of positive and negative fixtures per profile, including policy evaluation fixtures (§5.5) and inheritance fixtures (§6.3). An implementation claims conformance to a profile by passing its suite.

---

## 10. Implementation tasks for the ORP repo

- **R1** Add `attestation` to the spec and validator; implement JCS canonicalisation, hash recomputation, signature verification with JWKS and `did:web` resolution. Tests: tampered document fails; unknown key fails; offline verification with a supplied key passes.
- **R2** Add the C2 legal provenance fields and the C8 identifier, access, freshness, reach changes to Layer 1; update the JSON-LD context.
- **R3** Add Layer 6 `usage_policy` with the ODRL profile, the purpose taxonomy, and a reference evaluator (pure function) plus fixtures.
- **R4** Rewrite Layer 5 as `lineage` with `forks` and `derivations`; implement the inheritance walk in the reference evaluator.
- **R5** Add `usage_records` to Layer 4; define the receipt equivalence; support an external ledger pointer.
- **R6** Split the spec into ORP-Core, ORP-Policy, ORP-Ads, ORP-AI; publish JSON Schemas; add `--profile` to the CLI and the REST validator; add the IAB Data Transparency Standard field mapping table and the AdCP signals binding to ORP-Ads.
- **R7** Rename compliance levels to trust tiers with the mapping table; add `verified`; add the accredited verifier key list mechanism.
- **R8** Conformance suite per profile; CI runs it; the online validator reports tier and profile.
- **R9** Docs: a "Data products" section; rewrite the AI training datasets example (ImageNet, LAION-5B, Common Crawl, Copilot) under ORP-AI with `optout_signals_honoured` and `rights_holders` filled in as far as public information allows, which also makes the example sharper than it is today.
- **R10** Migration guide v0.2 to v0.3; `orp_version: "0.3"`.

---

## 11. What this does not change

The philosophy page stands. Layers 2 and 3 are untouched in substance. `attested_by` stays as the human statement. Forks are still invited; derivations are now also tracked. Nothing in this RFC requires a rail, a marketplace, or Yumipop to exist for an ORP document to be valid; it only makes such documents usable by them.

## 12. Open questions

- Should `usage_policy` be Layer 6 or nested in Layer 1? Proposed: Layer 6, for independent versioning and hashing.
- `did:web` and JWKS are proposed for key discovery. Should `did:key` be allowed for agents without a domain? Proposed: yes.
- Who accredits verifiers for the `verified` tier at first? Proposed: a list maintained in the repo, with the rule that a verifier cannot verify its own datasets.
- Is the purpose taxonomy complete enough? Missing candidates: `identity_resolution`, `fraud_prevention`, `journalism`.
