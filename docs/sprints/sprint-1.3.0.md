# Sprint 1.3.0: Danish Property Tax Reference Implementation

**Version:** `sprint-1.3.0`
**Status:** Planned
**Start Date:** TBD
**Target End Date:** TBD
**Actual End Date:** (if completed)

**Code Target Version:** `v0.2.1`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Create the first ORP-Full compliant real-world policy document as pure, validated YAML to prove the protocol works for complex proposals and provide a reference implementation for users.

---

## Scope

### In Scope
- Convert existing Danish Property Tax Reform markdown to pure YAML
- Ensure document validates as ORP-Full with `orp validate`
- Complete all 5 layers with real content (not placeholders)
- Add helpful comments as reference for other users
- Document any schema gaps or usability issues discovered
- Update `examples/README.md` with explanation

### Explicitly Out of Scope
- Creating additional examples (just Danish tax for now)
- Modifying the ORP schema itself (document issues, fix in later sprint)
- Building visualization tools for the example
- Translating to other languages

---

## Tasks

### Task 1: Extract YAML from Markdown
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
The current `danish_property_tax_reform.md` has YAML scattered across multiple code blocks in markdown. Extract and consolidate into a single YAML file.

**Acceptance Criteria:**
- [ ] All YAML blocks from markdown are consolidated
- [ ] File saved as `examples/danish_property_tax_reform.yaml`
- [ ] No information loss from original
- [ ] File loads without YAML syntax errors

**Dependencies:**
- Existing markdown file at `examples/danish_property_tax_reform.md`

---

### Task 2: Complete Header Fields
**Owner:** TBD
**Estimate:** 30 minutes
**Status:** Not Started

**Description:**
Ensure all required header fields are present and accurate.

**Acceptance Criteria:**
- [ ] `orp_version: "0.1"`
- [ ] `document_id` is meaningful and unique
- [ ] `title` accurately describes proposal
- [ ] `domain: "policy"`
- [ ] `authors` array with at least one author (can use placeholder with note)
- [ ] `created` and `last_modified` dates
- [ ] `status` is appropriate (likely "open-for-comment")
- [ ] `compliance_level: "ORP-Full"`
- [ ] `summary` is clear and concise (2-3 sentences)

**Dependencies:**
- Task 1 complete

---

### Task 3: Complete L1 - Data Provenance
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Document all data sources used in the analysis with full provenance.

**Acceptance Criteria:**
- [ ] At least one dataset fully documented
- [ ] Each dataset has:
  - Unique `dataset_id`
  - Clear `name` and `description`
  - `source` (government/academic/industry/other)
  - `collection_method` explained
  - `date_range` specified
  - `geographic_scope` defined
  - `inclusion_criteria` documented
  - `exclusion_criteria` listed (or empty array)
  - `cleaning_decisions` documented (or empty array)
  - `synthetic_elements` addressed
  - `known_limitations` listed
  - `access` information (public/restricted)
  - `attested_by` with at least one attestation
- [ ] Add inline comments explaining choices
- [ ] Validates against schema

**Dependencies:**
- Task 2 complete

---

### Task 4: Complete L2 - Consequence Simulation
**Owner:** TBD
**Estimate:** 3 hours
**Status:** Not Started

**Description:**
Document the economic modeling, variables, assumptions, and scenarios.

**Acceptance Criteria:**
- [ ] `affected_population` clearly defined
- [ ] `variables` section includes:
  - At least one `independent` variable
  - At least one `dependent` variable (outcome)
  - All variables have clear descriptions
- [ ] `model` section documents:
  - Model type/approach
  - Key assumptions with basis and sensitivity
- [ ] `scenarios` array with at least:
  - Baseline scenario
  - Reform scenario
  - Each scenario has variable values and outcomes
- [ ] `primary_scenario` specified
- [ ] Add comments explaining economic reasoning
- [ ] Validates against schema

**Dependencies:**
- Task 3 complete

---

### Task 5: Complete L3 - Empathy Mapping
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Map stakeholders and differential impacts, including minority stress testing.

**Acceptance Criteria:**
- [ ] `stakeholder_map` includes major groups:
  - Homeowners
  - Renters (if applicable)
  - Different income brackets
  - Regional differences
  - Each stakeholder has impacts by scenario
- [ ] `minority_stress_test` documents:
  - Which minorities were considered
  - Test scenarios
  - Outcomes
  - Mitigations
- [ ] `unresolved_impacts` honestly listed
- [ ] `net_welfare_assessment` with:
  - Methodology explained
  - Clear conclusion
  - Confidence level and basis
- [ ] Add comments on difficult tradeoffs
- [ ] Validates against schema

**Dependencies:**
- Task 4 complete

---

### Task 6: Complete L4 - Accountability Ledger
**Owner:** TBD
**Estimate:** 1.5 hours
**Status:** Not Started

**Description:**
Log key decisions made during analysis with attribution.

**Acceptance Criteria:**
- [ ] `entries` array with at least 3 decision entries:
  - Data selection decisions
  - Methodological choices
  - Framing decisions
- [ ] Each entry has:
  - Unique `entry_id`
  - ISO 8601 `timestamp`
  - `decision_type` (data/methodology/assumption/exclusion/framing/other)
  - Clear `description`
  - `decided_by` array
  - `basis` explaining reasoning
  - `alternatives_considered` documented
  - `dissenting_views` if any (or null)
- [ ] `review_history` array (can be empty for now)
- [ ] Add comments showing accountability principle
- [ ] Validates against schema

**Dependencies:**
- Task 5 complete

---

### Task 7: Complete L5 - Fork Registry
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Document fork metadata and prepare for future forks/responses.

**Acceptance Criteria:**
- [ ] `this_document` section with:
  - `document_id` (matches header)
  - `forked_from: null` (this is original)
  - `fork_reason` explaining it's the original proposal
  - `key_differences: "N/A - original document"`
- [ ] `known_forks: []` (empty array - none yet)
- [ ] `responses: []` (empty array - none yet)
- [ ] Add comments explaining how forks would work
- [ ] Validates against schema

**Dependencies:**
- Task 6 complete

---

### Task 8: Validation and Quality Check
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Ensure document validates perfectly and reads well.

**Acceptance Criteria:**
- [ ] `orp validate examples/danish_property_tax_reform.yaml` passes with ORP-Full
- [ ] No validation errors
- [ ] No validation warnings (or warnings are intentional and documented)
- [ ] Comments are helpful for someone learning ORP
- [ ] YAML is well-formatted and readable
- [ ] Check all field values are meaningful (not placeholder text)

**Dependencies:**
- Tasks 2-7 complete

---

### Task 9: Documentation
**Owner:** TBD
**Estimate:** 30 minutes
**Status:** Not Started

**Description:**
Document the example for users.

**Acceptance Criteria:**
- [ ] Create or update `examples/README.md` explaining:
  - What the Danish Property Tax Reform example is
  - Why it's useful as reference
  - How to validate it
  - What layers it demonstrates
- [ ] Add example to main README.md
- [ ] Reference it from docs/ROADMAP.md (Phase 1.4 complete)

**Dependencies:**
- Task 8 complete

---

## Success Criteria

This sprint is complete when:

1. `examples/danish_property_tax_reform.yaml` exists and is valid YAML
2. `orp validate examples/danish_property_tax_reform.yaml` reports ORP-Full compliance with no errors
3. All 5 layers (L1-L5) contain substantive, real content (not placeholders)
4. Document is well-commented as a reference for other users
5. Documentation explains what the example demonstrates
6. Any schema issues discovered are documented for future sprints

---

## Dependencies

**Requires from previous work:**
- Sprint 1.1.0: JSON Schema for validation
- Sprint 1.2.0: `orp validate` command

**Blocks future work:**
- Sprint 1.6.0: Website wants to showcase this example
- (But can proceed in parallel with 1.4, 1.5)

---

## Risks and Unknowns

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Original markdown content insufficient for ORP-Full | Medium | High | May need to add synthetic data/assumptions with clear notes |
| Schema doesn't support some economic modeling needs | Low | Medium | Document issues, fix schema in future sprint if needed |
| Takes longer than estimated | Low | Low | Parallel-safe sprint, won't block critical path |

---

## Decisions Made

### Decision 1: Use Danish Property Tax as first reference
**When:** Phase 0 planning
**Who:** Project founders
**Reasoning:**
- Already partially documented
- Complex enough to stress-test protocol
- Policy domain (core use case)
- Economic modeling demonstrates L2
**Alternatives Considered:**
- AI training data example (deferred - needs ORP-AI extension)
- Simple example (wouldn't test protocol adequately)

### Decision 2: Keep as YAML, not JSON
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- More human-readable
- Supports comments (valuable for reference implementation)
- YAML is superset of JSON (can convert later if needed)
**Alternatives Considered:**
- JSON (less readable, no comments)
- Keep as markdown (doesn't validate properly)

---

## Retrospective

*(Added after sprint completes)*

### What Worked Well
- TBD

### What Didn't Work
- TBD

### What We Learned
- TBD

### What Assumptions Were Wrong
- TBD

### Changes for Next Sprint
- TBD

---

## Notes

- This sprint deliberately does NOT modify the schema or validator
- If we find schema gaps, document them for a future sprint
- Goal is to prove the protocol works AS IS for real complexity
- This is a learning sprint - expect to discover rough edges
- The example should be "good enough to learn from" not "perfect"

---

**Reference:**
- Original markdown: `examples/danish_property_tax_reform.md`
- ROADMAP: Phase 1.4 - Reference Implementation
- See PHASE1_PLAN.md for sprint sequencing rationale
