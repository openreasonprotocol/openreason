# DRAFT — Proposal to AdCP: an ORP-based provenance object for signals

**Status:** DRAFT for Asbjørn's review — **not yet filed.** When approved, file as an issue/RFC on `github.com/adcontextprotocol/adcp` (the maintainers are soliciting this per the open provenance RFC #4441). Everything below is the proposed issue body.

---

## Title
RFC: a signed provenance object for **signals** (audience segments / data), reusing the #4441 envelope

## Summary
AdCP RFC #4441 adds signed provenance claims for **creatives** (C2PA references, IPTC source types). There is no equivalent for **signals** — a buying agent that activates an audience segment or dataset has no machine-verifiable statement of where that data came from, on what legal basis, or what it may be used for. This proposes adopting the **OpenReason Protocol (ORP) passport** (the ORP-Ads profile) as that provenance object, using the **same signing envelope #4441 already defines**, so it adds data provenance without new crypto or a new dialect.

## Motivation
- Creative provenance answers "is this ad what it claims to be." Signal provenance answers "is this *data* legitimate, and what may I do with it" — the question a buyer's counsel and a regulator (EU AI Act, state privacy laws) actually ask.
- Today that lives in private contracts and clean-room T&Cs, unverifiable by the agent on the other side of the trade. AdCP already standardises the *media* side of an agent-to-agent trade; the data side is the gap.
- ORP Layer 1 already asks the questions no commercial data standard does — `cleaning_decisions`, `synthetic_elements`, `known_limitations` — plus (v0.3) `legal_basis`, `consent_scope`, `sensitive_categories`, `optout_signals_honoured`. It is a natural fit as the signals provenance object.

## Proposal
1. **Same envelope as #4441.** The ORP passport is signed as a detached JWS over an RFC 8785-canonicalised object, Ed25519, key purpose-constrained (`adcp_use: provenance-claim` / ORP `use: orp-attestation` are the same object), short-lived keys, discovered via JWKS at a well-known URL or `did:web`/`did:key`. A relay/rail that already verifies #4441 creative provenance verifies a signals passport with the same code (see ORP v0.3 RFC §2.5).
2. **Binding to the signals vocabulary.** `get_signals` returns the passport summary (source, reach, freshness, legal basis, sensitive categories, tier); `activate_signal` requires an `allow` from a policy evaluator over the passport's ODRL `usage_policy` for the requested `{purpose, assignee, geo, media, time}`. Unknown purpose/scope → deny.
3. **Profile, not core.** Ship as the **ORP-Ads** profile (a JSON Schema), with a published field-mapping table to the **IAB Tech Lab Data Transparency Standard** so buyers recognise the fields. Purposes restricted to advertising + `measurement`/`analytics`.
4. **Usage records.** An activation produces a signed usage record (ORP Layer 4). A rail's signed clearing receipt carrying the data hash + policy hash **is** a usage record by construction — so the audit trail is a by-product of clearing, not extra work.

## What it adds beyond #4441
Data provenance (cleaning/synthetic/exclusions), legal basis + consent scope + sensitive categories + opt-out signals honoured, a machine-enforceable usage policy (ODRL profile with a fixed purpose taxonomy), lineage with constraint inheritance for derived segments (lookalikes, overlaps), and a usage-record ledger — none of which the creative-provenance object covers.

## Non-goals / scope
- Does not change AdCP creative provenance (#4441); purely additive, signals-only.
- Does not require ORP, OpenReason, or any specific rail to exist for the AdCP spec to adopt it; ORP is an open MIT spec with a validator + conformance suite.
- No dependency on any one vendor. (Disclosure: I maintain ORP; **yumipop** is offered as a reference implementation that enforces the passport at activation and emits usage-record receipts — but the proposal stands independently.)

## Reference implementation
yumipop (AdCP-native exchange on Cloudflare) enforces the ORP-Ads passport at `/v1/execute`: it refuses to activate a segment outside its policy, fails closed, and every activation lands in a signed receipt that is also an ORP Layer 4 usage record. It already emits `adcp_use: request-signing` JWKS, so it's a short step from #4441. Happy to contribute the ORP-Ads ↔ IAB DTS mapping table and a conformance fixture set.

## Questions for maintainers
- Is a provenance object for signals in scope for the signals spec, or better as a separate profile referenced by it?
- Preference on where the usage policy lives — inline on the signal, or a separately-hashed/versioned object (ORP proposes the latter)?
- Appetite for adopting the ORP purpose taxonomy vs defining an AdCP-native one? (ORP's is a superset that already includes `model_training`…`inference` for the dataset case.)

## Links
- ORP v0.3 RFC (machine-attested data products): `docs/specs/ORP_V0.3_RFC.md` (this repo)
- AdCP #4441 (signed provenance claims), #2324 (RFC 9421 relay signature model)
- IAB Tech Lab Data Transparency Standard

---

### Filing checklist (for Asbjørn, before this goes out)
- [ ] Confirm you want to disclose the yumipop reference-impl relationship up front (recommended — it's the honest framing and the maintainers value working code).
- [ ] Decide: open as a discussion/issue first (lighter, gauges appetite) or a full RFC/PR. Recommend a discussion/issue that links the ORP RFC.
- [ ] Trim the "reference implementation" section if you'd rather keep yumipop out of the initial ask and lead purely with the spec.
- [ ] File under your ORP/PublicReason identity (`asbjorn@publicreasonproject.org`), not a yumipop identity, so it reads as a neutral spec contribution.
