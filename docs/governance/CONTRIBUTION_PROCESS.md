# OpenReason Contribution Process

**Version:** 1.0
**Status:** Operational
**Last Updated:** 2026-04-07
**Governance Phase:** Phase 0 (Founder Stewardship)

---

## Purpose

This document defines the operational process for contributing to OpenReason — how to propose changes, what information is required, who reviews contributions, how decisions are made, and how long each step takes.

OpenReason is designed to be forkable and contestable. If you disagree with a decision made here, you can fork the protocol and demonstrate your alternative approach. This contribution process exists to make participation easier, not to gate-keep.

---

## Overview: Five Contribution Types

| Type | What | Process | Timeline | Decision Maker (Phase 0) |
|------|------|---------|----------|------------------------|
| **1. Protocol Specification Changes** | Changes to ORP_SPEC.md layers, compliance levels, schema | Issue → Discussion → Working Draft → Decision | 30+ days | Founder (documented in DECISION_LOG) |
| **2. Philosophical Changes** | Changes to REE_PHILOSOPHY.md principles or foundations | Issue → Discussion → Working Draft → Decision | 30+ days | Founder (documented in DECISION_LOG) |
| **3. Governance Changes** | Changes to GOVERNANCE.md or governance processes | Issue → Discussion → Working Draft → Decision | 60+ days | Founder (documented in DECISION_LOG) |
| **4. Documentation Improvements** | Clarifications, examples, guides, corrections | Issue or Direct MR | 7-14 days | Founder or Working Group (when formed) |
| **5. New Worked Examples** | ORP documents demonstrating protocol application | Issue → Submission → Review → Acceptance | 14-30 days | See EXAMPLE_REVIEW.md |

---

## General Principles

### 1. Discussion Before Code
For substantial changes (Types 1-3), **open an issue before writing**. Discuss the problem and proposed solution before investing effort in a full proposal. This prevents wasted work on changes that won't be accepted.

### 2. Fork-First Philosophy
If you disagree with the protocol's direction or a decision, **fork it**. Create an alternative version with your assumptions documented. The best argument wins through demonstration, not through voting. See Layer 5 (Fork Registry) for how to document protocol forks.

### 3. Transparency and Traceability
All decisions are documented in the [DECISION_LOG.md](./DECISION_LOG.md) with:
- What was decided
- Who decided it
- Why it was decided
- What alternatives were considered

This is Layer 4 (Accountability Ledger) applied to governance itself.

### 4. No Silent Rejections
If a contribution is rejected, you receive a clear explanation with documented reasoning in the DECISION_LOG. You may disagree with the decision, but you will not be left wondering why.

---

## Type 1: Protocol Specification Changes

**Examples:**
- Adding a new required field to Layer 1
- Changing a compliance level definition
- Modifying the JSON schema
- Adding a new layer (L6+)

### Process

**Step 1: Open an Issue**
- **Where:** GitLab issue tracker, label: `type::protocol-change`
- **Required information:**
  - **Problem statement:** What current limitation does this address?
  - **Proposed change:** Specific modification to ORP_SPEC.md
  - **Rationale:** Why this change improves the protocol
  - **Alternatives considered:** What other approaches did you consider?
  - **Breaking change assessment:** Does this invalidate existing ORP documents?
  - **Use cases:** What does this enable that's currently impossible?

**Step 2: Community Discussion (30+ days)**
- Issue remains open for community comment
- Founder and any Working Group members engage with questions/concerns
- Proposal may be revised based on feedback

**Step 3: Working Draft**
- If proposal has support, contributor (or founder) drafts specific changes
- Draft posted as comment on issue or as merge request
- Draft includes: spec changes + schema updates + migration guide (if breaking)

**Step 4: Decision**
- **Phase 0:** Founder makes decision, documented in DECISION_LOG
- **Post-Phase 0:** Core Specification Working Group recommendation → Stewardship Council ratification
- Decision timeline: Within 14 days of working draft completion
- Outcome: Accept (with version number), Defer (needs more work), or Reject (with reasoning)

**Step 5: Implementation (if accepted)**
- Changes merged to spec document
- Schema updated
- Validator updated (if needed)
- Documentation updated
- CHANGELOG.md entry added
- Decision logged in DECISION_LOG.md

### Timeline
- Minimum: 30 days (discussion) + 14 days (decision) = 44 days
- Typical: 60-90 days for substantial changes

### Template: Protocol Change Proposal

```markdown
## Problem Statement
[What limitation or gap does this address?]

## Proposed Change
[Specific modification to ORP_SPEC.md - be precise]

## Rationale
[Why this change improves the protocol]

## Alternatives Considered
1. **Option A:** [description] — Rejected because [reason]
2. **Option B:** [description] — Selected because [reason]

## Breaking Change Assessment
- [ ] Breaking (invalidates existing documents): [explain impact]
- [ ] Non-breaking (backwards compatible)

## Use Cases
[What this enables that's currently impossible or difficult]

## Related Documents
- Link to related issues/discussions
- Link to fork demonstrating alternative (if applicable)
```

---

## Type 2: Philosophical Changes

**Examples:**
- Modifying one of the five REE principles
- Adding a sixth principle
- Changing the philosophical grounding
- Altering the REE → ORP mapping

### Process

**Same as Type 1**, with additional requirements:

**Extra Required Information:**
- **Philosophical justification:** How does this align with REE's core purpose (epistemic accountability)?
- **Operational implications:** How does this change affect ORP's layer structure?
- **Academic context:** How does this relate to existing ethics literature?

**Extra Review Step:**
- Philosophical changes require engagement with the academic paper arguments
- Changes that contradict the paper's foundation require substantial justification

### Timeline
- Minimum: 30 days (discussion) + 14 days (decision) = 44 days
- Typical: 60-90 days (philosophical changes require deep consideration)

**Note:** Philosophical changes are expected to be rare. REE is the stable foundation; ORP is where evolution happens.

---

## Type 3: Governance Changes

**Examples:**
- Modifying decision-making processes
- Changing Working Group structure
- Altering Council composition rules
- Updating contribution processes (this document!)

### Process

**Step 1: Open an Issue**
- **Where:** GitLab issue tracker, label: `type::governance`
- **Required information:**
  - **Problem statement:** What governance problem does this address?
  - **Proposed change:** Specific modification to governance documents
  - **Rationale:** Why this improves governance
  - **Power dynamics analysis:** How does this affect who has influence?
  - **Failure modes:** What could go wrong with this change?

**Step 2: Community Discussion (60+ days)**
- **Longer period** because governance affects everyone
- Must include discussion of how this change affects community participation
- Founder actively solicits critical feedback

**Step 3: Working Draft**
- Draft posted as merge request with tracked changes to governance docs
- Includes: updated governance doc + DECISION_LOG entry + transition plan

**Step 4: Decision**
- **Phase 0:** Founder makes decision, but with explicit invitation to fork if community disagrees
- **Post-Phase 0:** Stewardship Council two-thirds vote required
- Decision timeline: Within 14 days of working draft completion

**Step 5: Implementation (if accepted)**
- Governance documents updated
- Transition plan executed (if needed)
- Announcement published
- Decision logged in DECISION_LOG.md

### Timeline
- Minimum: 60 days (discussion) + 14 days (decision) = 74 days
- Typical: 90-120 days for substantial governance changes

**Important:** Governance changes during Phase 0 are provisional. The Stewardship Council may revise any governance decision once formed.

---

## Type 4: Documentation Improvements

**Examples:**
- Fixing typos or broken links
- Clarifying ambiguous language
- Adding examples or tutorials
- Improving README, guides, or API docs

### Process

**Option A: Direct Merge Request (for minor changes)**
- **When to use:** Typos, broken links, minor clarifications
- **Process:**
  1. Open merge request with clear description of change
  2. Founder or Working Group member reviews within 7 days
  3. Merge if approved, feedback if revisions needed
- **Timeline:** 1-7 days

**Option B: Issue First (for substantial changes)**
- **When to use:** New documentation sections, restructuring, major rewrites
- **Process:**
  1. Open issue describing proposed documentation improvement
  2. Discuss approach (5-7 days)
  3. Create merge request with changes
  4. Review and merge (7 days)
- **Timeline:** 14 days typical

### What Doesn't Require Process
- Fixing obvious errors (typos, broken links) — just submit MR
- Adding yourself to contributors list after accepted contribution
- Updating dates or version numbers in metadata

### Decision Maker
- **Phase 0:** Founder reviews and merges
- **Post-Phase 0:** Community Working Group or any Working Group member with merge rights

---

## Type 5: New Worked Examples

**Examples:**
- ORP-Full document for a policy decision
- ORP-Standard document for a dataset
- ORP-Basic document for a research paper
- Domain-specific examples (AI, healthcare, climate)

### Process

See [EXAMPLE_REVIEW.md](./EXAMPLE_REVIEW.md) for detailed review criteria.

**Quick Overview:**

**Step 1: Open an Issue**
- **Where:** GitLab issue tracker, label: `type::example`
- **Required information:**
  - **Domain:** What domain does this example cover?
  - **Compliance level:** ORP-Basic, Standard, or Full?
  - **What it demonstrates:** What aspect of ORP does this showcase?
  - **Status:** Draft, ready for review, or published elsewhere?

**Step 2: Submit Example**
- Attach YAML file or link to repository
- Ensure `orp validate` passes
- Include brief README explaining context

**Step 3: Review**
- **Automated:** Does it validate? (orp validate)
- **Manual:** Does it meet quality criteria? (see EXAMPLE_REVIEW.md)
- **Substantive:** Are all layers meaningful (not placeholder text)?

**Step 4: Acceptance**
- **Official Examples:** Merged to `examples/` directory, high quality standard
- **Community Examples:** Linked from docs, validated but not vetted
- **External Registry:** Listed with URL, no quality guarantee

### Timeline
- Review: 14-21 days
- Feedback loop: Variable (depends on revisions needed)
- Acceptance: Once quality criteria met

---

## Contribution Workflow Diagram

```
┌─────────────────────────────────────────────────┐
│ Contributor identifies problem/improvement      │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  Open Issue    │ (for Types 1-3, 5)
         │  or Direct MR  │ (for Type 4 minor)
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │   Discussion   │ (30-60 days for major changes)
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │ Working Draft  │ (contributor or founder)
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │    Decision    │ (documented in DECISION_LOG)
         └────────┬───────┘
                  │
          ┌───────┴───────┐
          │               │
          ▼               ▼
    ┌─────────┐     ┌──────────┐
    │ Accept  │     │  Reject  │
    │         │     │  /Defer  │
    └────┬────┘     └────┬─────┘
         │               │
         ▼               ▼
   ┌──────────┐   ┌────────────────┐
   │ Merge &  │   │ Document       │
   │ Publish  │   │ Reasoning      │
   └──────────┘   └────────────────┘
```

---

## Worked Example: Proposing a New Layer 1 Field

**Scenario:** You want to add an optional field `data_quality_assessment` to Layer 1.

**Step 1: Open Issue**

```markdown
Title: [Protocol Change] Add optional data_quality_assessment field to Layer 1

## Problem Statement
Currently, Layer 1 documents data provenance but doesn't capture quality assessments performed on the dataset. Users must document quality checks in free-text descriptions, making it hard to query or compare quality practices across documents.

## Proposed Change
Add optional field to Layer 1:
```yaml
l1_data_provenance:
  - dataset_id: example
    ...
    data_quality_assessment:  # OPTIONAL
      performed: true/false
      methods: ["validation", "cross-checking", "expert review"]
      documented_in: "URL or citation"
      limitations: "Known quality issues"
```

## Rationale
This enables:
1. Explicit documentation of quality checks (transparency)
2. Comparison of quality practices across datasets
3. Queryability (SPARQL: "find datasets with expert review")

## Alternatives Considered
1. **Status quo (free-text):** Rejected — not queryable, inconsistent
2. **Mandatory field:** Rejected — too strict, many datasets lack formal quality assessment
3. **New layer (L1.5):** Rejected — quality is part of provenance, not separate concern

## Breaking Change Assessment
- [ ] Non-breaking: Optional field, existing documents remain valid

## Use Cases
- Scientific datasets with peer review
- AI training datasets with annotation quality checks
- Policy datasets with audit trails
```

**Step 2: Discussion (30 days)**
- Community comments on whether this belongs in L1 or elsewhere
- Discussion of whether "methods" should be controlled vocabulary
- Founder asks clarifying questions

**Step 3: Working Draft**
- Contributor drafts specific schema changes
- Updates ORP_SPEC.md with field definition
- Updates JSON schema with new optional field
- Adds example in Danish property tax document

**Step 4: Decision (Founder, Phase 0)**
- Founder reviews, decides to accept for v0.2
- Decision logged in DECISION_LOG.md as GOV-2026-003

**Step 5: Implementation**
- Merged to main branch
- Tagged as part of v0.2-draft
- CHANGELOG updated
- Announcement posted

---

## Common Questions

### Q: What if my proposal is rejected?
**A:** You receive documented reasoning in DECISION_LOG. You have two options:
1. Revise and resubmit based on feedback
2. Fork the protocol and demonstrate your approach works better

Rejection is not the end — it's an invitation to show your alternative is better.

### Q: Can I contribute anonymously?
**A:** Yes for minor documentation fixes. For substantial contributions (protocol changes, examples), attribution is required for Layer 4 accountability. You can use a pseudonym consistently, but decisions need to be traceable to some identity.

### Q: What if I disagree with the founder's decision during Phase 0?
**A:** You have several options:
1. Request reconsideration with new evidence/arguments
2. Wait for Stewardship Council formation and re-propose
3. Fork the protocol and build a community around your alternative
4. Document your disagreement publicly (we won't silence criticism)

Phase 0 is explicitly temporary. All decisions can be revisited post-handover.

### Q: How do I know if something should be a protocol change vs a fork?
**A:** Ask: "Does this change benefit everyone using ORP, or just my specific use case?"
- **Benefits everyone:** Propose a protocol change
- **Specific to your use case:** Create a fork or extension (e.g., ORP-Healthcare)

### Q: Can I propose changes to multiple documents at once?
**A:** Yes, if they're logically connected. For example, a new REE principle + corresponding ORP layer would be one combined proposal. But separate concerns (e.g., governance change + protocol change) should be separate issues.

---

## Code of Conduct

While a formal Code of Conduct will be established by the Stewardship Council, these principles apply now:

1. **Critique ideas, not people** — "This approach has limitation X" not "You don't understand Y"
2. **Assume good faith** — Contributors are trying to improve the protocol, even if you disagree
3. **Show your work** — Arguments backed by evidence and reasoning, not authority
4. **Accept disagreement** — Not every proposal will be accepted; that's okay
5. **Fork when you need to** — If you can't convince others, demonstrate your alternative

Violations of these principles (personal attacks, bad faith arguments, harassment) will result in contribution privilege suspension with documented reasoning.

---

## Phase Transition

When Phase 0 ends and the Stewardship Council forms:

- **This document will be reviewed** by the Council and likely amended
- **Decision authority** transfers from founder to Council + Working Groups
- **Timelines may change** based on Council decisions
- **Process may be refined** based on early experience

This document is v1.0 but explicitly provisional. The community will improve it.

---

## Related Documents

- [GOVERNANCE.md](./GOVERNANCE.md) — High-level governance model
- [VERSIONING_POLICY.md](./VERSIONING_POLICY.md) — When versions change
- [EXAMPLE_REVIEW.md](./EXAMPLE_REVIEW.md) — How examples are reviewed
- [DECISION_LOG.md](./DECISION_LOG.md) — Record of all governance decisions
- [CONTRIBUTING.md](../CONTRIBUTING.md) — Technical contribution guidelines (code, testing)

---

## Document History

- **v1.0** (2026-04-07): Initial operational version (Sprint 1.7.1)
- Created by: Asbjørn (founder, Phase 0)
- Status: Operational during Phase 0, subject to Council review post-handover

---

*This contribution process is itself subject to contribution. If you think it can be improved, follow Type 3 (Governance Changes) to propose amendments.*

*Fork-first. Show us better.*
