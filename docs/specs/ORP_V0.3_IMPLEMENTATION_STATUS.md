# ORP v0.3 — implementation status & sequence

*Tracks delivery of `ORP_V0.3_RFC.md` (machine-attested data products). "Fully ready for the policy and for use
by Railu" = R1 + R6/R7 + ORP-Policy + the `policy.dk.v1` pack, with R2–R5/R8 close behind. Started 2026-10-24.*

## Why this order

Two consumers pull on v0.3:
- **Railu / Yumipop (the rail)** needs, first, to *verify* an ORP passport offline with the crypto it already runs
  (AdCP #4441-shaped Ed25519/JWKS). That is **R1** — the keystone — and it's done. Then it needs the **profiles +
  trust tiers (R6/R7)** to decide *which* passports to accept, and **usage_policy + usage_records (R3/R5)** to enforce
  and prove use. A Railu clearing receipt that carries the dataset+policy hashes *is* an ORP usage record by
  construction (RFC §7.2) — that's the tightest integration point.
- **The policy flagship** (Danish legislation) needs the **ORP-Policy** profile (the renamed v0.2 shape) + a
  domain pack (`policy.dk.v1`) + the attestation core so each record is provenance-signed by its source, not by us.

So: R1 (done) → R6/R7 profiles+tiers → R3/R5 (the enforce/prove pair Railu needs) → R2/R4/R8 → the Danish pack.

## Status

| RFC task | What | Status |
|---|---|---|
| **R1** | Attestation: JCS canonicalisation, hash, Ed25519 detached-sig verify, key-purpose constraint, short-lived-key expiry, `did:key`/JWK resolution; optional `[attestation]` extra; 15 tests | **DONE** 2026-10-24 — `orp_validator/attestation.py`, `schemas/attestation.schema.json`, `tests/test_attestation.py` |
| — | **License → Apache-2.0** (owner call) | **DONE** 2026-10-24 |
| **R6** | Split spec into ORP-Core + ORP-Policy/Ads/AI profiles; `--profile` on CLI | **DONE** 2026-10-24 — `schemas/orp-v0.3-{core,policy,ads,ai}.schema.json` (core reuses v0.2 layer defs by `$ref`; profiles `allOf`-extend core), validator profile loader w/ in-memory RefResolver, `orp validate --profile`, 13 tests |
| **R7** | Compliance levels → trust tiers (`self_declared`/`attested`/`verified`/`full`/`posthoc`) with verification methods | **DONE** 2026-10-24 — `TrustTier` enum + `_determine_tier` (ladder keyed off verified attestation signatures; `verifier`-role → verified, +L3 → full; no-resolver caps at self_declared); surfaced in CLI + `to_dict`. Accredited-verifier key *list* mechanism still TODO (currently any valid `verifier`-role sig). |
| **R3** | Layer 6 `usage_policy` (ODRL profile) + purpose taxonomy + **pure reference evaluator** + fixtures | **DONE** 2026-10-24 — `usage.py::evaluate_policy` (deny-on-prohibition / deny-if-no-permission / unknown-purpose+scope fail closed; assignee, geo/media/time scope, derivation ordering, duties, expiry), `schemas/usage-policy.schema.json` wired into Core as Layer 6, 11 conformance fixtures (`tests/fixtures/usage_policy_cases.json`) |
| **R5** | Layer 4 `usage_records` + receipt equivalence (Railu clearing receipt = usage record) + external-ledger pointer | **DONE** 2026-10-24 — `usage.py::usage_record_from_receipt` (the Railu receipt→record mapping), `is_wellformed_usage_record`, `verify_usage_record` (signatures via R1), `schemas/usage-record.schema.json`. External-ledger pointer field allowed via additionalProperties; formal `usage_ledger` pointer schema still TODO |
| **R4** | Layer 5 → `lineage` (forks + derivations) + constraint-inheritance walk | **DONE** 2026-10-24 — `lineage.py` (`build_chain` + `evaluate_effective` + `resolve_effective_decision`): intersection across the ancestry, trust short-circuit at the first `verified`+ ancestor, licensed-relaxation via `derivative_policy`, cycle/depth guards, unresolved-ancestor fails closed. `schemas/orp-v0.3-lineage.schema.json` wired into Core (relaxed edge requires `relaxation_basis` via if/then). 7 tests. *Single-parent chain; multi-parent DAG intersection is a documented follow-up.* |
| **R2** | Layer 1 legal-provenance fields + resolvable `dataset_id`, `access`, `freshness`, `reach` | **DONE** 2026-10-24 — `schemas/orp-v0.3-l1-ext.schema.json` (C2 legal_basis/consent_scope/sensitive_categories/rights_holders/optout_signals_honoured/data_subject_contact + C8 access/freshness/reach), `allOf`-merged onto each Core L1 dataset (additive; v0.2 datasets still valid). 6 tests. *Profile-level `dataset_id`-must-be-URI tightening deferred.* |
| **R8** | Conformance suite per profile; CI runs it; online validator reports tier + profile | **DONE** 2026-10-24 — `conformance.py` runner + `orp conform` CLI + bundled fixtures (`schemas/conformance/{schema,policy,lineage}_cases.json`, 26 cases across all three suites), `tests/test_conformance.py`, GitLab CI `conformance:v0.3` job. Python reference validator reports profile + tier. *Still TODO: the deployed TS CF worker reporting tier+profile (deploy surface, owner-gated); accredited-verifier key list; usage_ledger pointer; multi-parent lineage DAG.* |
| **R9** | Docs "Data products" section; sharpen the AI example under ORP-AI | TODO |
| **R10** | v0.2→v0.3 migration guide; `orp_version: "0.3"` | TODO |

## R1 notes (what's locked, what's pinned)

- **Signing input** = RFC 8785 canonical bytes of the document minus its own `attestation` block. `sig` is the
  base64url Ed25519 signature with `kid`/`alg`/`use`/`role` as sibling fields (the construction the v0.3 schema
  encodes). The exact JOSE/detached-JWS envelope is **pinned to AdCP #4441** and isolated in
  `attestation._signing_input` — reconciling to AdCP's confirmed construction is a one-line change, not a rewrite.
  *Action when AdCP #4441's envelope is read first-hand: confirm or adjust `_signing_input` + re-run the suite.*
- **Portability:** key *resolution* is the caller's job (`resolve_key(kid)`), mirroring the rail convention that
  signing is the caller's job. Core stays dependency-light; crypto is an optional extra and degrades gracefully.
- **Known limitation (documented):** JCS number serialisation is exact for integers/bool/null/strings and typical
  decimals; exotic float exponents are best-effort via `repr` (not hit by ORP content, which is integers + enums);
  NaN/Infinity rejected.

## Railu alignment (cross-repo)

The companion is `praevis-exchange:docs/rails/ORP-KEEL-ALIGNMENT.md` (model B). The attestation core here is the
"attestation-core ↔ Keel-envelope" mapping named there: one Ed25519/JWKS verifier for both a Keel receipt and an ORP
passport. The RFC's `yumipop-data-layer-brief.md` companion should be located/rebuilt on the Railu side when R3/R5 land.
