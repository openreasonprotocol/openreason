# OpenReason Governance Decision Log

**Purpose:** Transparent, traceable record of all significant governance decisions
**Format:** ORP Layer 4 (Accountability Ledger) applied to governance itself
**Status:** Operational
**Started:** 2026-04-07

---

## About This Log

This document is OpenReason's **accountability ledger for governance decisions**. Every significant decision about the protocol, governance processes, examples, or project direction is recorded here with:

- **What** was decided
- **Who** made the decision
- **When** it was made
- **Why** it was made
- **What alternatives** were considered

This is Layer 4 of ORP applied to the protocol's own governance — transparent accountability for how the protocol itself is governed.

---

## Decision Entry Template

```markdown
## Decision ID: GOV-YYYY-NNN

**Date:** YYYY-MM-DD
**Type:** Process | Specification | Governance | Example | Other
**Proposer:** [Name or "Initiative by founder/council"]
**Decision Maker:** [Name/Body] (Phase 0: Asbjørn | Post-Phase 0: Working Group/Council)
**Status:** Proposed | Accepted | Rejected | Superseded | Under Review

### Context
[Why this decision was needed. What problem does it address?]

### Alternatives Considered
1. **Option A:** [description]
   - Pros: [...]
   - Cons: [...]
   - **Decision:** Rejected because [reason]

2. **Option B:** [description]
   - Pros: [...]
   - Cons: [...]
   - **Decision:** **Accepted** because [reason]

3. **Option C:** [description]
   - Pros: [...]
   - Cons: [...]
   - **Decision:** Rejected because [reason]

### Decision
[Clear statement of what was decided]

### Rationale
[Detailed explanation of why this decision was made]

### Implementation
[How this decision will be enacted. What changes, by when, by whom?]

### Impact Assessment
[Who/what does this affect? Any risks or concerns?]

### Related Decisions
[Links to related decision IDs: GOV-YYYY-NNN]

### Community Input
[Summary of community discussion, if applicable]

### Dissent
[Any documented objections or alternative views]

---
```

---

## Active Decisions

---

## Decision ID: GOV-2026-001

**Date:** 2026-04-07
**Type:** Process
**Proposer:** Initiative by founder (Sprint 1.7.1)
**Decision Maker:** Asbjørn (founder, Phase 0)
**Status:** Accepted

### Context

OpenReason's GOVERNANCE.md describes high-level governance structure (Council, Working Groups, decision-making processes) but lacks operational procedures for:
- How to submit contributions
- When protocol versions change
- How examples are reviewed
- How decisions are documented

Without operational procedures, governance remains aspirational rather than functional. This blocks:
- Community participation (unclear how to contribute)
- Public comment period (no process for incorporating feedback)
- Example submissions (no review criteria)
- Transparent decision-making (no accountability ledger)

This decision addresses the gap between governance principles and operational reality.

### Alternatives Considered

1. **Option A: Wait for Stewardship Council**
   - Pros: Council can design processes democratically
   - Cons: Phase 0 continues indefinitely without community participation
   - Cons: Public comment period blocked (can't launch without processes)
   - **Decision:** Rejected — Phase 0 needs operational procedures now

2. **Option B: Minimal processes (contribution only)**
   - Pros: Lower effort, get started quickly
   - Cons: Leaves gaps (versioning unclear, examples unreviewed)
   - Cons: Piecemeal approach creates inconsistency
   - **Decision:** Rejected — comprehensive approach better

3. **Option C: Comprehensive operational governance package**
   - Pros: Complete operational procedures covering all contribution types
   - Pros: Enables public comment period and community engagement
   - Pros: Transparent accountability from day one
   - Cons: More upfront work (but necessary work)
   - **Decision:** **Accepted** — establishes complete operational foundation

### Decision

**Adopt four operational governance documents:**

1. **CONTRIBUTION_PROCESS.md**
   - Defines 5 contribution types (protocol, philosophy, governance, docs, examples)
   - Specifies process for each (issue → discussion → decision → merge)
   - Includes templates and worked examples

2. **VERSIONING_POLICY.md**
   - Defines semantic versioning for protocols (MAJOR.MINOR.PATCH)
   - Specifies what constitutes breaking changes
   - Establishes version transition procedures
   - Maps path from v0.1 → v0.2 → v1.0

3. **EXAMPLE_REVIEW.md**
   - Establishes three-tier example system (Official, Community, External)
   - Defines review criteria for each tier
   - Specifies submission and review process
   - Balances quality standards with inclusivity

4. **DECISION_LOG.md**
   - This document
   - ORP Layer 4 applied to governance
   - Transparent record of all significant decisions
   - Template for future decision entries

**Status:** All four documents created and published in `docs/governance/`

**Effective date:** 2026-04-07

### Rationale

**Why now:**
- Public comment period (Sprint 1.8.0) requires operational processes
- Community contributions need clear pathways
- Academic paper (Sprint 1.7.5) can reference operational governance
- Transparency principle demands documented decision-making

**Why comprehensive (not minimal):**
- Governance gaps create confusion and friction
- Complete procedures enable full community participation
- Transparency requires documentation of all decision types
- Easier to iterate on complete system than patch gaps later

**Why Phase 0 (not wait for Council):**
- Council formation requires community, community requires processes
- Phase 0 is explicitly temporary — Council will review and revise
- Better to have provisional procedures than no procedures
- Document explicitly states: "Subject to Council review post-handover"

**Transparency about founder authority:**
- Phase 0 = founder decision-making authority (documented in GOVERNANCE.md)
- All decisions logged transparently in this ledger
- Community can contest through: feedback, formal objection, or fork
- Council will inherit and likely revise these processes

### Implementation

**Created documents:**
- [x] `docs/governance/CONTRIBUTION_PROCESS.md` (v1.0)
- [x] `docs/governance/VERSIONING_POLICY.md` (v1.0)
- [x] `docs/governance/EXAMPLE_REVIEW.md` (v1.0)
- [x] `docs/governance/DECISION_LOG.md` (this document, v1.0)

**Next steps:**
1. Test processes with simulated contribution (GOV-2026-002)
2. Update main GOVERNANCE.md to reference operational docs
3. Publish on docs site under "Governance" section
4. Announce operational governance in project communications
5. Link from README and CONTRIBUTING files
6. Use in Sprint 1.8.0 (public comment period)

**Timeline:**
- Decision: 2026-04-07
- Implementation: Immediate (documents published)
- Announcement: Within Sprint 1.7.1 (by 2026-04-10)

### Impact Assessment

**Affected parties:**
- **Contributors** (future): Clear pathways for participation ✅
- **Users**: Transparent decision-making increases trust ✅
- **Founder**: Explicit accountability for Phase 0 decisions ✅
- **Council** (future): Inherits operational processes to review/revise ✅

**Risks:**
- Processes may be suboptimal (first iteration) — **Mitigation:** Explicit provisional status, Council review
- Complexity may discourage contribution — **Mitigation:** Three-tier example system, clear templates
- Founder bias in design — **Mitigation:** Transparent documentation, community can critique/fork

**Benefits:**
- Unblocks public comment period (Sprint 1.8.0)
- Enables community contribution immediately
- Demonstrates transparency principle in practice
- Provides foundation for Council governance

### Related Decisions

- None yet (this is the first decision)
- Future decisions will reference this as foundational

### Community Input

**Pre-decision:**
- No community input (Phase 0, no community yet)
- Decision made proactively by founder to enable community formation

**Post-decision:**
- Open for feedback via GitLab issues (type::governance)
- Community invited to critique, propose amendments, or fork
- All feedback will be considered for revisions

### Dissent

**Current:** None (decision made before community exists)

**Invitation for dissent:**
If you disagree with these processes:
1. Open issue with specific critiques and alternative proposals
2. Propose amendments via governance change process (CONTRIBUTION_PROCESS Type 3)
3. Fork OpenReason with different governance approach

Dissent is welcome and will be documented here if raised.

---

## Decision ID: GOV-2026-002

**Date:** 2026-04-07
**Type:** Process Test
**Proposer:** Testing initiative (Sprint 1.7.1, Task 5)
**Decision Maker:** Asbjørn (founder, Phase 0)
**Status:** Accepted (with modifications)

### Context

To validate that the contribution process (GOV-2026-001) actually works, Sprint 1.7.1 includes testing with a simulated contribution. This decision evaluates the test proposal: "Add optional `data_quality_assessment` field to Layer 1".

This tests:
- Contribution template usability
- Decision-making workflow
- DECISION_LOG documentation process
- Process timing and friction points

**Simulated proposal:** A contributor proposes adding an optional field to Layer 1 that documents quality assessments performed on datasets (validation, cross-checking, expert review). Currently, quality checks are documented in free-text descriptions, making them hard to query across documents.

### Alternatives Considered

1. **Option A: Accept as proposed**
   - Pros: Addresses real need (queryable quality documentation)
   - Pros: Optional field (non-breaking, backwards compatible)
   - Pros: Well-scoped (specific structure, clear use cases)
   - Cons: Adds complexity to schema
   - Cons: Not yet validated by real-world use
   - **Decision:** Accepted with modification (defer to v0.2, not immediate merge)

2. **Option B: Reject (keep status quo)**
   - Pros: Maintains simplicity
   - Pros: Avoids premature optimization
   - Cons: Real need goes unaddressed
   - Cons: Quality documentation remains inconsistent
   - **Decision:** Rejected — need is legitimate

3. **Option C: Defer to v1.0 (wait for more evidence)**
   - Pros: Gathers more use cases before committing
   - Pros: Allows community input during public comment
   - Cons: Delays useful feature unnecessarily
   - **Decision:** Rejected — can add to v0.2 during public comment

### Decision

**Accept the proposal for inclusion in v0.2** (not immediate merge to v0.1)

**Rationale for deferral:**
- Feature is valuable but not urgent
- v0.2 will incorporate public comment feedback — good time to add
- Allows community to weigh in during public comment period
- Tests "deferred acceptance" workflow

**Modified proposal:**
```yaml
l1_data_provenance:
  - dataset_id: example
    ...
    data_quality_assessment:  # OPTIONAL, added in v0.2
      performed: true  # boolean
      methods:  # array of strings
        - "automated_validation"
        - "manual_cross_checking"
        - "expert_review"
        - "statistical_testing"
        - "other"
      documented_in: "URL or citation to quality report"  # string, optional
      limitations: "Known quality issues or gaps"  # string, optional
      assessment_date: "YYYY-MM-DD"  # date, optional
```

**Implementation plan:**
1. Create issue: "Add data_quality_assessment field (approved for v0.2)"
2. Draft JSON schema changes
3. Include in v0.2 public comment announcement
4. Solicit feedback during public comment
5. Merge to v0.2 if no major objections

### Rationale

**Why this decision was made:**

1. **Real need identified:** Quality documentation is currently ad-hoc
2. **Non-breaking change:** Optional field preserves backwards compatibility
3. **Queryable:** Structured format enables SPARQL queries ("find datasets with expert review")
4. **Validates process:** Tests contribution workflow successfully
5. **Community timing:** Public comment period is appropriate venue

**Why deferred to v0.2 (not immediate):**
- v0.1 is stable enough for now (no urgent need to patch)
- v0.2 is the natural home for accumulated improvements
- Community should weigh in (public comment period)
- Tests "deferred acceptance" pathway (not every proposal merges immediately)

**Friction points discovered:**
- ✅ Template was clear and usable
- ✅ Decision criteria were sufficient
- ⚠️  Timeline expectations: Need to clarify "accept for v0.2" vs "accept immediately"
- ⚠️  Version targeting: Should proposals specify target version?

**Process improvements identified:**
1. Add "Target Version" field to proposal template
2. Clarify in CONTRIBUTION_PROCESS: acceptance can be conditional on version
3. Create "v0.2 scope" tracking issue for approved-but-deferred changes

### Implementation

**Immediate actions:**
- [x] Log decision (this entry)
- [x] Validate process worked (it did, with minor improvements needed)
- [ ] Create GitLab issue: "Add data_quality_assessment field (approved for v0.2)"
- [ ] Update CONTRIBUTION_PROCESS template with "Target Version" field
- [ ] Create v0.2 scope tracking issue

**Future actions (Sprint 1.8.0):**
- Include in v0.2 public comment announcement
- Draft JSON schema changes
- Solicit community feedback
- Merge if approved after public comment

**Timeline:**
- Decision: 2026-04-07
- Issue creation: Sprint 1.7.1 (by 2026-04-10)
- Implementation: Sprint 1.8.0 (v0.2 preparation)
- Merge: After public comment period (target: June 2026)

### Impact Assessment

**Affected parties:**
- **Future contributors** — clearer process ✅
- **Dataset documenters** — new optional feature (v0.2+) ✅
- **Tool developers** — schema update required (v0.2+) ⚠️
- **Existing documents** — unaffected (optional field) ✅

**Risks:**
- Field may go unused if not promoted — **Mitigation:** Document in examples, templates
- Controlled vocabulary ("methods") may be incomplete — **Mitigation:** Allow "other" option
- Adds schema complexity — **Mitigation:** Optional, defer to v0.2 for feedback

**Benefits:**
- Queryable quality documentation
- More structured transparency
- Validates contribution process successfully
- Tests deferred acceptance workflow

### Related Decisions

- **GOV-2026-001** — Established the process being tested here
- **Future GOV-2026-00X** — v0.2 scope ratification (will reference this)

### Community Input

**Pre-decision:**
- None (simulated test, no community yet)

**Post-decision:**
- Will be included in public comment period announcement
- Community can provide feedback on field design
- May be revised based on feedback

### Dissent

**Current:** None (test decision)

**Process observation:**
This simulated test validates the contribution process works. Real contributions will likely surface issues not captured here. Process should be treated as "working draft" and refined based on actual use.

---

---

## Future Decisions

*(Decisions will be added here as they are made)*

**Expected upcoming decisions:**
- **GOV-2026-003** — Accept/defer ImageNet example for Official tier (Sprint 1.7.3)
- **GOV-2026-004** — Approve v0.2 scope and timeline (Sprint 1.8.0)
- **GOV-2026-005** — Ratify comparison document publication (Sprint 1.7.2)
- **GOV-2026-006** — Approve JSON-LD schema addition (Sprint 1.7.4)
- **GOV-2026-007** — Academic paper submission approval (Sprint 1.7.5)

---

## Superseded Decisions

*(Decisions that have been overridden by later decisions will be moved here)*

When a decision is superseded:
- Original entry remains in log (never deleted)
- Status changed to "Superseded"
- Link added to superseding decision
- Rationale for change documented

**Format:**
```markdown
## Decision ID: GOV-YYYY-NNN

**Status:** Superseded by GOV-YYYY-NNN on YYYY-MM-DD

[Original decision text preserved]

**Why superseded:**
[Explanation of why this decision was overridden]
```

---

## Decision Log Statistics

**Total decisions:** 2 (1 accepted, 1 proposed)
**Phase 0 decisions:** 2
**Post-Council decisions:** 0

**Decisions by type:**
- Process: 2
- Specification: 0
- Governance: 0
- Example: 0
- Other: 0

**Last updated:** 2026-04-07

---

## Using This Log

### For Contributors

**Before proposing a change:**
1. Search this log to see if similar decision was already made
2. Reference related decision IDs in your proposal
3. Show how your proposal differs or why circumstances changed

**After your proposal:**
- Your proposal will be logged here (even if rejected)
- Decision reasoning will be transparent
- You can reference this entry in future proposals or forks

### For Decision Makers

**When making a decision:**
1. Copy the Decision Entry Template above
2. Assign next sequential GOV-YYYY-NNN ID
3. Fill all sections thoroughly
4. Document alternatives considered (not just chosen option)
5. Include dissenting views if any
6. Commit decision to this log before implementing

**Never:**
- Delete or retroactively edit decisions (preserve history)
- Make significant decisions without logging
- Log only accepted decisions (rejections must be documented too)

### For Researchers/Critics

**This log enables:**
- Analysis of project decision patterns
- Accountability auditing (who decided what, when, why)
- Critique of decision-making processes
- Evidence for forks (document disagreements, show alternative)

**You can:**
- Cite specific decisions (use GOV-YYYY-NNN IDs)
- Analyze decision quality (were alternatives considered?)
- Track decision makers (does power concentrate?)
- Identify decision patterns (biases, blind spots)

---

## Governance Log Integrity

### Preservation Principle

**Never delete or retroactively edit decision entries.**

Decisions, once made and logged, are permanent historical records. They can be:
- Superseded by new decisions
- Marked as reversed
- Criticized in retrospect

But they cannot be erased. This is Layer 4 accountability applied to governance itself.

### Amendment Process

If a decision entry has an error (typo, broken link, factual mistake):
1. Add correction as addendum to original entry
2. Note: "Correction added YYYY-MM-DD: [description]"
3. Original text preserved with strikethrough if needed

**Example:**
```markdown
**Decision Maker:** ~~Council~~ Founder (Phase 0)
*Correction added 2026-04-10: Initial entry incorrectly stated Council; Phase 0 decisions are founder-made.*
```

### Audit Trail

**All changes to this file are tracked via Git:**
```bash
git log docs/governance/DECISION_LOG.md
```

Anyone can verify:
- When decisions were added
- Whether entries were edited
- Who made commits

This is additional transparency layer beyond document content.

---

## Document History

- **v1.0** (2026-04-07): Decision log initiated (Sprint 1.7.1)
  - First decision: GOV-2026-001 (Operational governance adoption)
  - Created by: Asbjørn (founder, Phase 0)
  - Template established for future decisions

---

## Related Documents

- [GOVERNANCE.md](./GOVERNANCE.md) — High-level governance model
- [CONTRIBUTION_PROCESS.md](./CONTRIBUTION_PROCESS.md) — How decisions are proposed
- [VERSIONING_POLICY.md](./VERSIONING_POLICY.md) — Version change decisions
- [EXAMPLE_REVIEW.md](./EXAMPLE_REVIEW.md) — Example acceptance decisions
- [ORP_SPEC.md](../specs/ORP_SPEC.md) — Protocol specification (subject to decisions here)

---

*This decision log is itself an ORP document. It applies Layer 4 (Accountability Ledger) to OpenReason's own governance.*

*Every significant decision is here. Nothing is hidden. If you can't find a decision, either it wasn't made, or it should have been documented and wasn't — in which case, open an issue.*

*Fork-first. Challenge decisions. Demand accountability.*
