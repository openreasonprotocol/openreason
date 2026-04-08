# OpenReason Versioning Policy

**Version:** 1.0
**Status:** Operational
**Last Updated:** 2026-04-07
**Governance Phase:** Phase 0 (Founder Stewardship)

---

## Purpose

This document defines how OpenReason Protocol versions are numbered, when versions change, what constitutes a breaking change, and how version transitions are managed. It ensures that:

1. **Users know what to expect** — version numbers signal the impact of changes
2. **Backwards compatibility is protected** — existing documents don't break unexpectedly
3. **Innovation isn't blocked** — the protocol can evolve while maintaining stability
4. **Transitions are managed** — migrations have clear timelines and support

---

## Semantic Versioning for Protocols

OpenReason adapts [Semantic Versioning 2.0](https://semver.org/) for protocol specifications:

```
MAJOR.MINOR.PATCH
  │     │     │
  │     │     └─── Clarifications, typos, non-normative changes
  │     └─────────  Backwards-compatible additions
  └───────────────  Breaking changes
```

### Version Format: `MAJOR.MINOR.PATCH`

**Examples:**
- `0.1.0` — Initial draft (current version)
- `0.2.0` — After public comment period (minor additions)
- `1.0.0` — First ratified stable version
- `1.1.0` — Adds optional fields (backwards-compatible)
- `2.0.0` — Restructures layers (breaking change)

---

## What Each Version Level Means

### MAJOR Version (X.0.0)

**When to increment:**
- Changes to layer structure (adding/removing/reordering layers)
- Changes to compliance levels (redefining Basic/Standard/Full)
- Removal of required fields
- Changes that invalidate existing ORP documents

**Examples of MAJOR changes:**
- Adding a Layer 6 that all documents must include
- Removing Layer 5 (Fork Registry)
- Making Layer 1 funding disclosure mandatory (currently optional in some cases)
- Changing YAML schema in incompatible ways

**Process required:**
- Minimum 60-day public comment period
- Stewardship Council ratification (two-thirds vote)
- Migration guide published
- Deprecation timeline announced (minimum 6 months)
- Validators must support N-1 version during transition

**Impact:**
- Existing documents are valid under old version but not new version
- Tools must update to support new version
- Users must migrate documents (migration guide provided)

### MINOR Version (x.Y.0)

**When to increment:**
- Adding new optional fields
- Adding new examples or templates
- Extending schema with backwards-compatible additions
- Adding guidance to specification without changing requirements

**Examples of MINOR changes:**
- Adding optional `data_quality_assessment` field to Layer 1
- Adding new stakeholder categories to Layer 3
- Adding ORP-Extended compliance level (between Standard and Full)
- Expanding acceptable data types for a field

**Process required:**
- Minimum 30-day public comment period
- Working Group approval + Stewardship Council ratification (Phase 0: founder decision)
- CHANGELOG entry with rationale
- Decision logged in DECISION_LOG.md

**Impact:**
- Existing documents remain valid
- New features available but not required
- Tools can update immediately (no migration needed)
- Validators accept both old and new syntax

### PATCH Version (x.x.Z)

**When to increment:**
- Fixing typos or grammatical errors
- Clarifying ambiguous language
- Adding examples to illustrate existing requirements
- Correcting documentation errors
- Updating broken links or references

**Examples of PATCH changes:**
- Fixing typo: "afftected" → "affected"
- Clarifying: "Authors should include..." → "Authors must include... (required)"
- Adding example showing how to format dates
- Updating reference to moved documentation

**Process required:**
- Working Group approval (Phase 0: founder decision)
- No public comment period required
- CHANGELOG entry (can batch multiple patches)
- Decision logged (can be batched)

**Impact:**
- No functional changes
- Existing documents remain valid with no modifications
- Validators unchanged (no schema update)
- Documentation updates only

---

## What Constitutes a Breaking Change?

A change is **breaking** if it causes previously valid ORP documents to become invalid under the new version.

### Breaking Change Examples ✗

1. **Making optional fields required**
   - Before: `funding_source` optional
   - After: `funding_source` required
   - Impact: Documents without this field become invalid

2. **Removing fields**
   - Before: `l1_data_provenance` includes `temporary_field`
   - After: `temporary_field` removed
   - Impact: Documents with this field may fail validation

3. **Changing field types**
   - Before: `created: "2026-01-01"` (string)
   - After: `created: 2026-01-01` (date object)
   - Impact: Existing date strings invalid

4. **Restructuring layers**
   - Before: Layer 1 = Data Provenance
   - After: Layer 1 = Metadata, Layer 2 = Data Provenance
   - Impact: All layer numbering shifts

5. **Changing compliance level definitions**
   - Before: ORP-Basic requires L1 only
   - After: ORP-Basic requires L1 + L2
   - Impact: Documents claiming ORP-Basic now insufficient

### Non-Breaking Change Examples ✓

1. **Adding optional fields**
   - Adding `data_quality_assessment` as optional
   - Impact: Existing documents valid, new feature available

2. **Relaxing requirements**
   - Before: `authors` requires affiliation
   - After: `authors` affiliation optional
   - Impact: More documents become valid

3. **Clarifying ambiguity**
   - Before: "Stakeholders should be identified"
   - After: "Stakeholders should be identified where feasible; unknown stakeholders may be marked as TBD"
   - Impact: Interpretation clearer, no validation change

4. **Adding examples or templates**
   - Adding worked example for healthcare domain
   - Impact: None on existing documents

5. **Expanding enumerations**
   - Before: `fork_type: ["critique", "extension"]`
   - After: `fork_type: ["critique", "extension", "translation"]`
   - Impact: Existing documents valid, new option available

---

## Version Lifecycle

### Draft Versions (0.x.y)

**Status:** Pre-1.0 versions are explicitly unstable
- Breaking changes allowed without major version bump (0.1 → 0.2 can break)
- No long-term support guarantees
- Rapid iteration encouraged
- Community feedback actively solicited

**Current phase:** We are in 0.1.x (initial draft)

**Path to 1.0:**
```
0.1.0 → 0.2.0 → ... → 0.9.0 → 1.0.0-rc1 → 1.0.0
  │       │              │         │          │
  │       │              │         │          └─ First stable release
  │       │              │         └─ Release candidate (final testing)
  │       │              └─ Mature draft (feature-complete)
  │       └─ Post public-comment revisions
  └─ Initial draft (current)
```

### Stable Versions (1.x.y+)

**Status:** Post-1.0 versions have stability guarantees
- MAJOR changes require extensive justification
- MINOR changes common (new optional features)
- PATCH changes frequent (clarifications, fixes)
- Long-term support for N-1 major version

### Deprecated Versions

**When a version is deprecated:**
- Announcement published (minimum 6 months before end-of-life)
- Migration guide provided
- Validators continue supporting deprecated version during transition
- Docs marked with deprecation notice
- Community support on transition

**Example deprecation timeline:**
```
Day 0:   Version 2.0.0 released, 1.x.y enters deprecation
Month 1: Migration guide published
Month 3: Validator warnings for 1.x.y documents ("upgrade recommended")
Month 6: 1.x.y validation support ends (documents must upgrade)
```

---

## Roadmap: v0.1 → v0.2 → v1.0

### Current Version: 0.1.0
**Status:** Initial draft
**Released:** January 2026
**Stability:** Unstable (pre-1.0)
**Features:**
- Five-layer structure (L1-L5)
- Three compliance levels (Basic, Standard, Full)
- YAML format with JSON Schema validation
- One worked example (Danish property tax)

### Next Version: 0.2.0 (Target: June 2026)
**Trigger:** Completion of 60-day public comment period
**Expected changes:**
- Community feedback incorporated (new fields, clarifications)
- Second worked example (ImageNet AI training data)
- Governance processes operational
- Possibly: New optional fields based on use cases
- Status: Still draft (unstable)

**Decision point:** Is 0.2.0 feature-complete enough for 1.0?
- If yes → 1.0.0-rc1 (release candidate)
- If no → 0.3.0, 0.4.0, ... (more iteration)

### Target Version: 1.0.0 (Target: Q4 2026)
**Trigger:** Protocol is feature-complete and community-tested
**Requirements before 1.0:**
- [ ] Minimum 3 worked examples across 2+ domains
- [ ] 60-day public comment period completed with feedback incorporated
- [ ] Stewardship Council formed (governance transition complete)
- [ ] At least 2 independent implementations (validators)
- [ ] Academic paper published or in review
- [ ] No major known issues or pending breaking changes

**1.0.0 = Commitment to stability:**
- Breaking changes require MAJOR version bump (2.0.0)
- Backwards compatibility guaranteed within 1.x.y
- Long-term support begins

---

## Version Decision Process

### Who Decides Version Numbers?

**Phase 0 (Current):**
- Founder proposes version number based on change type
- Decision documented in DECISION_LOG.md
- Community can contest through fork or formal objection

**Post-Phase 0:**
- Core Specification Working Group recommends version number
- Stewardship Council ratifies (for MAJOR/MINOR)
- Working Group decides PATCH versions independently

### Version Number Disputes

**If there's disagreement about whether a change is MAJOR vs MINOR:**

1. **Err on the side of caution** — if unsure, use MAJOR
2. **Test with existing documents** — does validation break?
3. **Community vote** (Post-Phase 0) — Working Group + Council decide
4. **Fork if necessary** — create alternative versioning approach

**Example dispute:**
- Proposed: Make Layer 1 funding disclosure required (currently optional)
- Claim: This is MINOR (just making existing optional field required)
- Reality: This is MAJOR (breaks documents without funding field)
- Resolution: Council votes, or community forks with different policy

---

## Backwards Compatibility Policy

### Validators Must Support N-1 Major Version

**Requirement:** ORP validators must support the current major version AND the previous major version simultaneously.

**Example:**
- When v2.0.0 is released, validators must support both 2.x.y AND 1.x.y
- When v3.0.0 is released, validators must support both 3.x.y AND 2.x.y (1.x.y support can be dropped)

**Implementation:**
```bash
orp validate document.yaml --version 1.0.0  # Validates against 1.0 schema
orp validate document.yaml                   # Validates against latest (2.0)
```

**Rationale:** Gives users time to migrate without breaking existing workflows

### Version Declaration in Documents

**Required field in all ORP documents:**
```yaml
orp_version: "0.1"
```

This tells validators which schema version to use. Without it, validator uses latest version.

**Version declaration rules:**
- **MAJOR.MINOR** format (patch version not specified in documents)
- Validators apply latest PATCH within declared MINOR version
- Example: `orp_version: "1.0"` uses v1.0.4 if that's the latest patch

---

## Migration Guidance Requirements

### For Every MAJOR Version Change

The release of a new MAJOR version MUST include:

1. **Migration Guide Document**
   - What changed (breaking changes listed)
   - How to update documents (step-by-step)
   - Before/after examples
   - Common pitfalls

2. **Automated Migration Tool (if feasible)**
   - CLI command: `orp migrate document.yaml --from 1.0 --to 2.0`
   - Best-effort conversion (manual review still required)
   - Clear warnings about what couldn't be automated

3. **Transition Timeline**
   - Announcement date
   - Deprecation date (old version still supported)
   - End-of-life date (old version validation ends)
   - Minimum 6 months between announcement and EOL

4. **Community Support**
   - Forum/chat for migration questions
   - Office hours or live migration help (if community large enough)
   - Documentation of common migration patterns

---

## Version Freeze Periods

### Before 1.0 Ratification

**60-day freeze before 1.0.0 release:**
- No new features added
- Only bug fixes and clarifications (PATCH-level changes)
- Release candidate phase: 1.0.0-rc1, 1.0.0-rc2, etc.
- Community testing and final feedback

**Rationale:** 1.0.0 is a commitment to stability. Must be thoroughly tested.

### After 1.0

**No formal freeze periods** — continuous evolution allowed
- MINOR versions can be released anytime (backwards-compatible)
- MAJOR versions require justification + long comment period
- PATCH versions can be batched or released individually

---

## Emergency Fixes

### Security or Critical Bugs

**If a critical issue is discovered:**
- Can bypass normal comment period for PATCH fixes
- Must be documented in DECISION_LOG with emergency justification
- Community notified immediately
- Longer discussion period applied retroactively if community objects

**Example:**
- Discovered: Validator has bug allowing invalid documents to pass
- Action: Release 0.1.1 immediately with fix
- Process: Announce fix, document reasoning, open issue for feedback
- If controversial: Community can contest, revert if necessary

---

## Version Metadata

### How Versions Are Tagged

**Git tags:**
```bash
git tag -a v0.1.0 -m "Initial draft release"
git tag -a v0.2.0 -m "Post public comment revision"
git tag -a v1.0.0 -m "First stable release"
```

**Release artifacts:**
- ORP_SPEC.md (versioned)
- REE_PHILOSOPHY.md (versioned separately)
- JSON Schema (versioned, file: orp-schema-v0.1.json)
- Validators (versioned with protocol)

**Version documentation:**
- CHANGELOG.md (comprehensive record of all changes)
- Release notes (user-facing summary)
- Migration guides (for MAJOR versions)

---

## Questions and Edge Cases

### Q: Can MINOR versions be skipped?
**A:** Yes. 0.1 → 0.3 is valid if 0.2 was never released. Version numbers are not promises.

### Q: Can we downgrade a version number?
**A:** No. Once a version is tagged and released, it's permanent. If a release is wrong, release a corrected PATCH version.

### Q: What if a MAJOR change is urgent?
**A:** Still requires 60-day comment period. If truly urgent, explain why in proposal and shorten to 30 days minimum with explicit justification.

### Q: Can multiple MAJOR versions be supported simultaneously?
**A:** Validators must support N-1. Supporting older versions (N-2, N-3) is optional but encouraged.

### Q: How do side protocols (ORP-AI, ORP-Econ) version?
**A:** Independently. ORP-AI v1.0 can depend on ORP v1.x but versions separately. Must declare compatibility: "ORP-AI v2.0 requires ORP >= v1.0"

### Q: What if community disagrees with version number choice?
**A:** Fork and use different versioning approach. If fork gains adoption, may become new canonical version (decided by usage, not authority).

---

## When v0.1 Becomes "Frozen"

**Current status:** v0.1.0 is active and can be patched
**Freeze trigger:** When v0.2.0-draft is opened
**After freeze:** v0.1.x can only receive PATCH updates (typos, clarifications)

**Why freeze?**
- Prevents divergent evolution (two active branches)
- Forces decisions forward into next version
- Clear migration path for users

**Post-freeze process:**
```
0.1.0 (current) ──┬─> 0.1.1, 0.1.2, ... (patches only)
                  │
                  └─> 0.2.0-draft → 0.2.0 (new features)
```

---

## Document History

- **v1.0** (2026-04-07): Initial operational version (Sprint 1.7.1)
- Created by: Asbjørn (founder, Phase 0)
- Status: Operational during Phase 0, subject to Council review post-handover

---

## Related Documents

- [GOVERNANCE.md](./GOVERNANCE.md) — High-level governance model
- [CONTRIBUTION_PROCESS.md](./CONTRIBUTION_PROCESS.md) — How to propose changes
- [DECISION_LOG.md](./DECISION_LOG.md) — Record of version decisions
- [CHANGELOG.md](../../CHANGELOG.md) — Comprehensive version history

---

*This versioning policy is itself versioned. If you propose improvements, follow the Governance Changes process (CONTRIBUTION_PROCESS.md Type 3).*
