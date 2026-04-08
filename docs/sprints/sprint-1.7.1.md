# Sprint 1.7.1: Operational Governance

**Version:** `sprint-1.7.1`
**Parent Epic:** `sprint-1.7.0` (Foundation for Expansion)
**Status:** Not Started
**Start Date:** 2026-04-04
**Target End Date:** 2026-04-07 (3 days)

**Code Target Version:** `v0.6.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Make ORP's governance model operational by creating concrete processes for community contribution, version management, example review, and decision-making — transforming aspirational governance documents into usable workflows that enable community participation before the public comment period.

---

## Scope

### In Scope
- Four governance process documents with templates/examples
- Decision log system (ORP-style accountability for governance)
- Contribution workflow (issue → proposal → review → merge)
- Versioning policy (when 0.1 → 0.2 → 1.0)
- Example review process (how community examples get accepted)
- Update to main GOVERNANCE.md integrating all processes

### Explicitly Out of Scope
- Technical contribution guidelines (code style, testing) - use existing CONTRIBUTING.md
- Community Code of Conduct (add in 1.8.0 if needed)
- Formal steering committee (defer until community exists)
- Trademark/legal governance (not needed yet)

---

## Tasks

### Task 1: Create CONTRIBUTION_PROCESS.md
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Critical

**Description:**
Document the end-to-end process for proposing changes to the ORP specification, governance model, or core documentation.

**Acceptance Criteria:**
- [ ] Document covers 5 contribution types:
  1. Protocol specification changes (ORP_SPEC.md)
  2. Philosophical changes (REE_PHILOSOPHY.md)
  3. Governance changes (GOVERNANCE.md, etc.)
  4. Documentation improvements
  5. New worked examples
- [ ] For each type, document:
  - When to use GitLab issue vs direct MR
  - What information is required
  - Who reviews (initially: Asbjørn, future: community process)
  - How decisions are made and recorded
  - Timeline expectations
- [ ] Include worked example: "Proposing a new required field in Layer 1"
- [ ] Include template: Issue template for protocol change proposal
- [ ] Link to DECISION_LOG.md for transparency
- [ ] Addresses fork-first philosophy (when to fork vs propose change)

**Output:** `docs/governance/CONTRIBUTION_PROCESS.md`

---

### Task 2: Create VERSIONING_POLICY.md
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Critical

**Description:**
Define clear versioning policy for ORP protocol versions (currently 0.1, moving toward 1.0).

**Acceptance Criteria:**
- [ ] Semantic versioning adapted for protocols:
  - **Major (1.0 → 2.0):** Breaking changes to layer structure or compliance levels
  - **Minor (0.1 → 0.2):** New required fields, backwards-compatible additions
  - **Patch (0.1.0 → 0.1.1):** Clarifications, examples, non-normative changes
- [ ] Define what constitutes a "breaking change" for ORP:
  - Changes that invalidate existing ORP documents
  - Changes to layer definitions or core concepts
  - Removal of fields or compliance levels
- [ ] Process for proposing version changes:
  - Who can propose (anyone via issue)
  - How proposals are reviewed (public comment for minor+, decision log for patch)
  - Ratification process (initially: Asbjørn, future: governance body)
- [ ] Backwards compatibility policy:
  - Validators must support N-1 version
  - Migration guide required for breaking changes
  - Deprecation timeline (min 6 months notice)
- [ ] Document v0.1 → v0.2 → v1.0 roadmap:
  - v0.2: Incorporating public comment feedback (Sprint 1.8)
  - v1.0: First ratified stable version (after 60-day comment + revisions)
- [ ] Include decision: When does v0.1 become "frozen"? (Answer: When v0.2 draft opens)

**Output:** `docs/governance/VERSIONING_POLICY.md`

---

### Task 3: Create EXAMPLE_REVIEW.md
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Define process for reviewing and accepting community-contributed ORP examples, ensuring quality without gatekeeping.

**Acceptance Criteria:**
- [ ] Three tiers of example status:
  1. **Official Examples** (in main repo, high quality, peer-reviewed)
  2. **Community Examples** (linked from docs, validated but not vetted)
  3. **External Examples** (listed in registry, no quality guarantee)
- [ ] Review criteria for Official Examples:
  - Validates against ORP schema (orp validate passes)
  - Compliance level clearly stated and met
  - All layers have substantive content (not placeholder)
  - Layer 1 cites verifiable sources
  - Layer 4 includes real attribution (not "TBD")
  - Demonstrates something new (domain, use case, or depth)
- [ ] Submission process:
  - GitLab issue with example attached
  - Initial review: Does it validate? (automated)
  - Substantive review: Quality check (manual)
  - Feedback loop: Revision process
  - Acceptance: Merge to examples/ directory
  - Publication: Added to docs site examples page
- [ ] Include example submission template
- [ ] Community examples: Lower bar, must validate but content not reviewed
- [ ] External registry: JSON file listing third-party examples (URL + description)

**Output:** `docs/governance/EXAMPLE_REVIEW.md`

---

### Task 4: Create DECISION_LOG.md System
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Create ORP-style accountability ledger for governance decisions (meta-compliance with Layer 4).

**Acceptance Criteria:**
- [ ] Decision log structure:
  ```markdown
  ## Decision ID: GOV-2026-001
  **Date:** 2026-04-04
  **Type:** Process | Specification | Governance
  **Proposer:** [Name]
  **Decision Maker:** [Name/Body]
  **Status:** Proposed | Accepted | Rejected | Superseded

  ### Context
  [Why this decision was needed]

  ### Alternatives Considered
  1. Option A: [description] - Rejected because [reason]
  2. Option B: [description] - Accepted because [reason]

  ### Decision
  [What was decided]

  ### Rationale
  [Why this decision was made]

  ### Implementation
  [How to enact this decision]

  ### Related Decisions
  [Links to GOV-XXXX-XXX]
  ```
- [ ] Create initial decision: GOV-2026-001 (Adopting operational governance processes)
- [ ] Create template for new decisions
- [ ] Document when decisions required vs when they're optional
- [ ] Link from all other governance docs
- [ ] Note: This IS Layer 4 applied to ORP's own governance

**Output:** `docs/governance/DECISION_LOG.md` with template and first decision

---

### Task 5: Test Governance Process with Fake Contribution
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Validate that governance processes work by simulating a community contribution end-to-end.

**Acceptance Criteria:**
- [ ] Create fake GitLab issue: "Add `data_quality_assessment` optional field to Layer 1"
- [ ] Follow CONTRIBUTION_PROCESS.md steps
- [ ] Record decision in DECISION_LOG.md (GOV-2026-002)
- [ ] Document outcome: Accept or reject with rationale
- [ ] Identify any friction points in process
- [ ] Revise process docs if needed
- [ ] Close issue with clear outcome

**Output:** One completed decision log entry demonstrating process

---

### Task 6: Update Main GOVERNANCE.md
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Update high-level GOVERNANCE.md to integrate all new operational processes.

**Acceptance Criteria:**
- [ ] Add section: "Operational Processes" with links to 4 new docs
- [ ] Update "How Decisions Are Made" with pointer to DECISION_LOG
- [ ] Update "Current Governance Status" (Phase 0 → Phase 1 transition)
- [ ] Add "Governance Roadmap":
  - Now: Founder-led with transparent processes
  - v0.2: Community input via public comment
  - v1.0: Potential governance body (TBD based on community size)
- [ ] Clarify fork-first philosophy in governance context
- [ ] Ensure consistency with new process docs

**Output:** Updated `docs/governance/GOVERNANCE.md`

---

## Success Criteria

### Completion Criteria
- [ ] All 6 tasks completed
- [ ] Four new governance documents published
- [ ] Decision log initialized with 2+ entries
- [ ] At least one simulated contribution tested
- [ ] All docs cross-linked and consistent

### Quality Criteria
- [ ] Each process doc includes worked example or template
- [ ] A new contributor could follow processes without asking questions
- [ ] Processes are transparent and documented (REE compliance)
- [ ] Decision-making is traceable (Layer 4 compliance)
- [ ] Fork-first philosophy clearly represented

### Impact Criteria (1-2 months)
- First external contribution successfully merged using these processes
- Public comment period participants reference governance docs
- Decision log has 5+ entries showing real usage
- Zero "how do I contribute?" issues (docs answer the question)

---

## Dependencies

**Depends on:**
- None (first sub-sprint in epic)

**Enables:**
- Sprint 1.7.5 (paper can reference operational governance)
- Sprint 1.8.0 (public comment needs these processes)
- All future community contribution

---

## Risks and Mitigations

### Risk 1: Processes too bureaucratic
**Mitigation:** Test with fake contribution (Task 5), optimize for simplicity

### Risk 2: Processes remain theoretical
**Mitigation:** Each doc requires worked example, test before publishing

### Risk 3: Over-engineering for non-existent community
**Mitigation:** Document processes that scale (work for 1 contributor or 100)

---

## Documentation Updates

- [ ] Update `CLAUDE.md` repository structure with governance/ files
- [ ] Update docs site with new governance section
- [ ] Link governance docs from main README.md
- [ ] Add governance to docs site navigation

---

## Retrospective Notes

(To be completed at sprint end)

### What Went Well
- [TBD]

### What Didn't Go Well
- [TBD]

### Lessons Learned
- [TBD]

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-04
**Target Completion:** 2026-04-07
**Estimated Effort:** 17 hours over 3 days
