# Sprint 1.7.3.4: Schema Revision & Consolidation

**Version:** `sprint-1.7.3.4`
**Parent Sprint:** `sprint-1.7.3` (Foundation for Expansion - Worked Examples)
**Status:** Not Started
**Start Date:** 2026-04-29 (after all 4 AI examples complete)
**Target End Date:** 2026-05-03 (4 days)

**Code Target Version:** `v0.7.0` (ORP Schema v0.2)
**Protocol Version Supported:** `0.2`

---

## Sprint Goal

Consolidate schema discoveries from 5 worked examples (Danish Tax, ImageNet, LAION-5B, Common Crawl, GitHub Copilot), revise ORP specification to v0.2, and prepare for 60-day public comment period with empirically-validated schema.

---

## Strategic Importance

This is **critical quality assurance** before Phase 0 completion:
- **175-235 schema issues discovered** across 4 AI examples
- **ORP v0.1 spec inadequate** for real-world application
- **Must revise before public comment** (don't ask community to comment on broken schema)
- **Empirical validation complete** (5 domains tested: policy + 4 AI)
- **Ready for v0.2** (stable enough for public scrutiny)

---

## Discovered Schema Issues Summary

### From ImageNet (Sprint 1.7.3):
**85 validation errors**

**Categories:**
1. **Header issues** (3): domain enum too restrictive, author role enum, access fields
2. **Layer 2 structure** (42): variable fields (actual_value vs default_value), scenario outcomes structure, assumptions confidence vs sensitivity
3. **Layer 3 structure** (5): stakeholder_groups vs stakeholder_map, missing unresolved_impacts, confidence enum
4. **Layer 4 structure** (12): decision_type enum too restrictive, additional fields (consequences, source)
5. **Layer 5 structure** (23): fork structure rigid (missing fields), potential_forks not in schema

### From LAION-5B (Sprint 1.7.3.1):
**30-50 estimated new issues**

**Key discoveries:**
1. **Harm severity taxonomy** (L3): Need tiers (criminal > legal > ethical > economic)
2. **Vulnerable populations flag** (L3): Children, medical patients, crime victims
3. **Legal compliance fields** (L1): CSAM detection, HIPAA compliance, copyright
4. **Federated dataset structure** (L1): URLs vs hosted images (affects L1, L5)
5. **Safety vs ethics distinction** (L3): CSAM (safety, illegal) vs privacy (ethical)

### From Common Crawl (Sprint 1.7.3.2):
**40-60 estimated new issues**

**Key discoveries:**
1. **Living dataset methodology** (L1): Temporal evolution, version history
2. **Scale-appropriate provenance** (L1): Statistical sampling vs enumeration (petabytes)
3. **Linguistic diversity metrics** (L1): Quantify 7,000+ languages representation
4. **Existential harm category** (L3): Language extinction, cultural erasure (irreversible)
5. **Ecosystem-level consequences** (L2): Not just individual bias, but cultural elimination
6. **Version vs fork distinction** (L5): Monthly releases (versions) vs methodology changes (forks)

### From GitHub Copilot (Sprint 1.7.3.3):
**20-40 estimated new issues**

**Key discoveries:**
1. **License compliance fields** (L1): License distribution, compliance review, attribution mechanism
2. **Legal risk assessment** (L4): IP risk, legal opinions, contractual obligations
3. **Ecosystem harm taxonomy** (L3): Future-oriented (deterring contributors), collective (sustainability)
4. **Economic fairness fields** (L3): Compensation, revenue sharing, labor extraction
5. **Code-specific provenance** (L1): License metadata, attribution tracking

---

## Consolidated Schema Revisions Needed

### 1. Header Revisions

**Current v0.1:**
```yaml
domain: [policy, ai-training, governance, other]
authors:
  - role: [author, contributor, reviewer]
```

**Proposed v0.2:**
```yaml
domain: [policy, ai-training-images, ai-training-text, ai-training-code, ai-deployment, governance, research, other]
authors:
  - role: [author, contributor, reviewer, analyst, attester]
```

**Rationale:** ImageNet/LAION/CC/Copilot revealed need for finer-grained AI domains, new role types (analyst for post-hoc reconstruction).

---

### 2. Layer 1 (Data Provenance) Revisions

**Add: Dataset Type**
```yaml
dataset_type: [static, living, federated, synthetic, hybrid]
```
- Static: ImageNet (frozen 2012)
- Living: Common Crawl (monthly updates)
- Federated: LAION-5B (URLs not images)

**Add: License Compliance (for code/content datasets)**
```yaml
license_compliance:
  licenses_present: [MIT, GPL-2.0, Apache-2.0, none, proprietary]
  license_distribution: {MIT: 40%, GPL: 20%, Apache: 15%, none: 20%, other: 5%}
  compliance_review: yes/no
  attribution_mechanism: [none, partial, full]
  copyleft_handling: [included, excluded, unknown]
```

**Add: Safety Compliance (for image/content datasets)**
```yaml
safety_compliance:
  csam_filtering: [none, automated, PhotoDNA, CSAI_Match, human_review]
  medical_privacy: [none, HIPAA_reviewed, filtered]
  illegal_content: [included_unfiltered, automated_removal, legal_review]
```

**Add: Linguistic Diversity (for text datasets)**
```yaml
linguistic_diversity:
  languages_represented: [estimated count or list]
  dominant_language: en (ISO 639-1 code)
  language_distribution: {en: 90%, es: 3%, zh: 2%, other: 5%}
  low_resource_languages: [list of <1M speaker languages included]
```

**Add: Temporal Metadata (for living datasets)**
```yaml
temporal_metadata:
  first_release: YYYY-MM-DD
  latest_release: YYYY-MM-DD
  update_frequency: [daily, weekly, monthly, annually, irregular]
  version_history_url: https://...
```

**Revise: Access**
```yaml
access:
  public: true/false
  url: https://...
  license: string
  registration_required: true/false  # Add back (ImageNet needs this)
  registration_reason: string  # Add back
  federated: true/false  # LAION-5B (URLs vs hosted)
  download_size: string  # "3 petabytes compressed"
```

---

### 3. Layer 2 (Consequence Simulation) Revisions

**Revise: Variables Structure**
```yaml
variables:
  independent:
    - variable: string
      description: string
      range: string  # Keep as string (allows "[low, medium, high]" or "0-100")
      default_value: string  # Rename from actual_value
      actual_value: string  # Keep for retrospective analysis
  dependent:
    - variable: string
      description: string
      unit: string
      default_value: string  # For prospective
      observed_value: string  # For retrospective (ImageNet, LAION, CC, Copilot)
```

**Revise: Model Assumptions**
```yaml
model:
  assumptions:
    - assumption: string
      confidence: [very_high, high, medium, low, very_low]  # Keep (more intuitive than sensitivity)
      sensitivity: [critical, high, medium, low]  # Add back (how much outcome changes if assumption wrong)
      basis: string
  limitations: [string]  # Add back (ImageNet needs this)
```

**Revise: Scenarios**
```yaml
scenarios:
  - scenario_id: string
    name: string
    description: string
    variable_values: {var1: value1, var2: value2}  # Rename from parameter_values
    outcomes:
      - outcome: string  # Allow list (ImageNet uses this)
        magnitude: string
        confidence: [very_high, high, medium, low]
        evidence: string
    uncertainties: [string]  # Add back (ImageNet uses this)
```

---

### 4. Layer 3 (Empathy Mapping) Revisions

**Major restructure needed:**

**Add: Stakeholder Groups (current schema uses stakeholder_map, ImageNet uses stakeholder_groups)**
```yaml
stakeholder_groups:
  - stakeholder: string
    description: string
    estimated_population: string
    relationship_to_proposal: string
    representation_level: [full, high, moderate, low, none]  # New: quantify absent node
    impacts_by_scenario:
      - scenario_id: string
        financial_impact: string
        quality_of_life_impact: string
        direction: [strong_benefits, benefits, mixed, net_harm, severe_harm]
    vulnerability_flags: [string]  # LAION: children, medical patients
    harm_severity: [none, economic, ethical, legal, safety, existential]  # NEW: LAION/CC/Copilot discovery
```

**Add: Harm Severity Taxonomy**
```yaml
harm_severity_taxonomy:
  existential:  # Common Crawl: language extinction
    description: Irreversible elimination of entire communities/cultures
    examples: [language death, cultural genocide]
  safety:  # LAION-5B: CSAM
    description: Physical/psychological harm, illegal content
    examples: [CSAM, violence, abuse imagery]
  legal:  # LAION-5B: HIPAA, Copilot: GPL
    description: Violation of laws, regulations, contracts
    examples: [HIPAA violations, copyright infringement, license violations]
  ethical:  # ImageNet: dignity, privacy
    description: Dignity harm, privacy violations, consent issues
    examples: [offensive labels, privacy violations, lack of consent]
  economic:  # Copilot: labor extraction
    description: Financial harm, labor exploitation, unfair compensation
    examples: [unpaid labor, revenue extraction, wage theft]
```

**Add: Minority Stress Test** (ImageNet has this, schema missing)
```yaml
minority_stress_test:
  description: string
  groups_tested:
    - group: string
      scenario_tested: string
      outcome: string
      mitigation: string
```

**Revise: Net Welfare Assessment**
```yaml
net_welfare_assessment:
  methodology: string
  conclusion: string
  confidence: [very_high, high, medium, low, very_low]  # Expand enum
  confidence_basis: string
  distributional_notes: string  # NEW: who benefits, who is harmed
```

---

### 5. Layer 4 (Accountability Ledger) Revisions

**Revise: Decision Types**
```yaml
decision_type: [
  data_source,  # Rename from "data"
  methodology,
  assumption,
  exclusion,
  framing,
  scope,  # New: ILSVRC 1000 categories
  taxonomy,  # New: WordNet choice
  safety,  # New: CSAM filtering decision
  legal_compliance,  # New: GPL filtering decision
  access_policy,  # New: open vs gated
  ethical_remediation,  # New: post-hoc fixes
  other
]
```

**Add: Consequences and Source** (ImageNet uses these, schema rejects)
```yaml
entries:
  - entry_id: string
    timestamp: string
    decision_type: enum
    description: string
    decided_by: [array of {name, role}]
    basis: string
    alternatives_considered: string
    dissenting_views: string (optional)
    consequences: string  # ADD BACK (ImageNet needs this)
    source: string  # ADD BACK (citations for reconstructed ledgers)
    legal_review: [yes, no, unknown]  # NEW: Copilot needs this
    ethical_review: [yes, no, unknown]  # NEW: LAION needs this
```

---

### 6. Layer 5 (Fork Registry) Revisions

**Add: Potential Forks** (ImageNet uses this, schema rejects)
```yaml
potential_forks:
  - potential_fork_idea: string
    description: string
    enabled_by_orp: string  # How ORP makes this fork proposal legible
```

**Revise: Known Forks** (too rigid currently)
```yaml
known_forks:
  - fork_id: string  # Optional (may not have formal ID)
    document_id: string  # Optional (may not have ORP doc yet)
    name: string
    fork_type: [methodology, safety, quality, ethical, legal, subset, extension, revision]  # Expand types
    created_by: string  # More flexible (was array, now string)
    created_date: string  # More flexible format
    created: string  # Keep for backward compat
    rationale: string
    key_differences: string
    outcomes: string  # Add back (ImageNet uses this)
    relationship: string  # Add back (sibling, derivative, revision)
    citation: string  # Add back (academic citation)
    orp_documentation: string (optional)  # Link to ORP doc if exists
    fork_reason: string  # Keep for backward compat
    author: string  # Keep for backward compat
    url: string  # Keep for backward compat
```

---

## Tasks

### Task 1: Comprehensive Schema Analysis
**Owner:** Asbjørn
**Estimate:** 8 hours
**Priority:** Critical

**Description:**
Consolidate all schema issues from 4 AI examples + Danish example.

**Acceptance Criteria:**
- [ ] Read all validation reports:
  - ImageNet: 85 errors documented
  - LAION-5B: Schema discoveries doc
  - Common Crawl: Schema discoveries doc
  - Copilot: Schema discoveries doc
- [ ] Categorize issues:
  - Missing fields (fields examples use that schema rejects)
  - Restrictive enums (domain, decision_type, etc.)
  - Structural mismatches (stakeholder_groups vs stakeholder_map)
  - New concepts (harm severity, living datasets, federated structure)
- [ ] Prioritize: Critical (blocks real use) vs Nice-to-have (refinement)
- [ ] Create: `docs/sprints/sprint-1.7.3.4-schema-analysis.md`

**Output:** Comprehensive schema issue analysis with priorities

---

### Task 2: Draft ORP Specification v0.2
**Owner:** Asbjørn
**Estimate:** 12 hours
**Priority:** Critical

**Description:**
Revise ORP_SPEC.md to v0.2 incorporating all schema discoveries.

**Acceptance Criteria:**
- [ ] Update: `docs/specs/ORP_SPEC.md`
- [ ] Version: Change to v0.2
- [ ] Add: Changelog section (v0.1 → v0.2 changes)
- [ ] Revisions:
  - Header: Expanded domain enum, new author roles
  - L1: Dataset type, license compliance, safety compliance, linguistic diversity, temporal metadata
  - L2: Variable structure refinement, assumptions both confidence+sensitivity, scenarios allow list outcomes
  - L3: Harm severity taxonomy, minority stress test, distributional welfare notes
  - L4: Expanded decision types, add consequences/source fields, legal/ethical review flags
  - L5: Potential forks, flexible known fork structure
- [ ] Add: Examples for each new field (code snippets showing usage)
- [ ] Add: Migration guide (v0.1 → v0.2 conversion notes)

**Output:** ORP_SPEC.md v0.2 (comprehensive revision)

---

### Task 3: Update JSON Schema (orp-v0.2.schema.json)
**Owner:** Asbjørn
**Estimate:** 10 hours
**Priority:** Critical

**Description:**
Update JSON Schema definition to match v0.2 spec.

**Acceptance Criteria:**
- [ ] Create: `orp_validator/schemas/orp-v0.2.schema.json`
- [ ] Update: All field definitions per Task 2 revisions
- [ ] Update: Required vs optional fields (some v0.1 required fields should be optional for flexibility)
- [ ] Add: Conditional requirements (if dataset_type=living, then temporal_metadata required)
- [ ] Add: Better descriptions for each field (help validator users)
- [ ] Test: Validate against all 5 examples (should reduce errors dramatically)

**Output:** orp-v0.2.schema.json

---

### Task 4: Validate All Examples Against v0.2
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** High

**Description:**
Update all 5 examples to v0.2 compliance, validate clean.

**Acceptance Criteria:**
- [ ] Update: `examples/danish_property_tax_reform.yaml` (should already be close)
- [ ] Update: `examples/imagenet_training_data.yaml` (fix 85 errors)
- [ ] Update: `examples/laion5b_training_data.yaml` (once created)
- [ ] Update: `examples/common_crawl_training_data.yaml` (once created)
- [ ] Update: `examples/github_copilot_training_data.yaml` (once created)
- [ ] Run: `orp validate` on each
- [ ] Target: 0 errors (or <5 minor issues per example)
- [ ] Document: Remaining issues (if any) for v0.3

**Output:** All 5 examples validated against v0.2 schema

---

### Task 5: Update Validator Code
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** High

**Description:**
Update orp_validator.py to handle v0.2 schema features.

**Acceptance Criteria:**
- [ ] Update: `orp_validator/validator.py`
- [ ] Add: v0.2 schema support (detect orp_version field, use appropriate schema)
- [ ] Add: Better error messages for new fields (harm_severity, dataset_type, etc.)
- [ ] Update: CLI help text (explain new fields)
- [ ] Update: Templates (basic/standard/full) to include new fields
- [ ] Test: Run validator on all 5 examples, verify error messages helpful

**Output:** Updated validator supporting v0.2

---

### Task 6: Update API (api.publicreasonproject.org)
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** High

**Description:**
Update REST API to support v0.2 schema.

**Acceptance Criteria:**
- [ ] Update: `api/main.py` - add v0.2 schema
- [ ] Update: Validation endpoint - detect orp_version, use correct schema
- [ ] Update: OpenAPI docs - document v0.2 fields
- [ ] Update: Tests - add v0.2 validation tests
- [ ] Deploy: Push to production (api.publicreasonproject.org)
- [ ] Test: POST all 5 examples to API, verify validation

**Output:** API supporting v0.2 schema in production

---

### Task 7: Update Documentation
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** High

**Description:**
Update all docs to reference v0.2, explain changes.

**Acceptance Criteria:**
- [ ] Update: `README.md` - mention v0.2, link to changelog
- [ ] Update: `CLAUDE.md` - ORP v0.2, schema discoveries
- [ ] Update: `CHANGELOG.md` - add v0.2 entry with all changes
- [ ] Create: `docs/specs/ORP_V0.1_TO_V0.2_MIGRATION.md`
- [ ] Update: Example READMEs - note v0.2 compliance
- [ ] Update: `docs/CONTRIBUTING.md` - reference v0.2 schema

**Output:** Documentation ecosystem updated for v0.2

---

### Task 8: Write Schema Evolution Retrospective
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Medium

**Description:**
Document what we learned from schema evolution process.

**Acceptance Criteria:**
- [ ] Create: `docs/specs/SCHEMA_EVOLUTION_RETROSPECTIVE.md`
- [ ] Sections:
  - Why schema needed revision (v0.1 inadequate for real examples)
  - What we discovered (harm severity, living datasets, license compliance, etc.)
  - How applied research reveals theory gaps
  - Lessons for v0.3+ (expect further evolution)
  - When to stabilize schema (Phase 0 → Phase 1 transition)
- [ ] Academic value: Demonstrates research rigor (theory → test → revise)

**Output:** Schema evolution retrospective

---

### Task 9: Prepare for Public Comment
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Final prep before 60-day public comment period.

**Acceptance Criteria:**
- [ ] Verify: All 5 examples validate against v0.2
- [ ] Verify: API supports v0.2 in production
- [ ] Verify: Docs updated and consistent
- [ ] Create: `docs/PUBLIC_COMMENT_ANNOUNCEMENT.md`
- [ ] Prepare: Comment submission process (GitHub issues, email, web form?)
- [ ] Prepare: Review committee (who evaluates comments?)
- [ ] Set: Comment period dates (start + 60 days)

**Output:** Ready to launch public comment period

---

## Success Criteria

### Completion Criteria
- [ ] All 9 tasks completed
- [ ] ORP_SPEC.md v0.2 published
- [ ] orp-v0.2.schema.json created
- [ ] All 5 examples validate clean (or <5 errors each)
- [ ] Validator updated to v0.2
- [ ] API updated to v0.2 (production)
- [ ] Documentation updated

### Quality Criteria
- [ ] Schema addresses all critical issues (175-235 errors → <25 total)
- [ ] Backward compatible where possible (v0.1 docs still parseable)
- [ ] Migration path clear (v0.1 → v0.2 guide)
- [ ] Examples demonstrate new features (harm severity, living datasets, etc.)

### Impact Criteria
- [ ] Ready for public comment (stable enough for external scrutiny)
- [ ] Empirically validated (5 domains tested)
- [ ] Academic credibility (rigorous theory-revision process)

---

## Schema Version Summary

### ORP v0.1 (Sprint 1.6.0)
- **Status:** Draft (untested on real examples)
- **Tested on:** 0 examples when published
- **Known issues:** 175-235 discovered through applied research

### ORP v0.2 (This Sprint)
- **Status:** Empirically validated
- **Tested on:** 5 examples (policy + 4 AI domains)
- **Remaining issues:** <25 expected (minor refinements)
- **Ready for:** Public comment period (60 days)

### ORP v1.0 (Future - Post-Public Comment)
- **Status:** Not yet started
- **Input:** v0.2 + public comment feedback
- **Timeline:** After 60-day comment period + revision sprint
- **Goal:** Production-ready, stable for Phase 1 tooling

---

## Retrospective Structure

This sprint will produce retrospective document covering:

### What Went Well ✅
- Applied research methodology (theory → test → revise)
- 5 examples revealed comprehensive schema gaps
- Each example revealed unique issues (not redundant)
- Pattern clear: v0.1 inadequate for real-world complexity

### What Didn't Go Well ⚠️
- v0.1 published prematurely (should have tested on 1-2 examples first)
- 175-235 errors is large technical debt (but necessary for learning)
- Some examples blocked on schema issues (had to write "wrong" to continue)

### Lessons Learned 💡
1. **Test spec before publishing**: Should have validated Danish + ImageNet before calling v0.1 "done"
2. **Applied research reveals theory gaps**: Can't reason about schema without real examples
3. **Each domain reveals new dimensions**: Images (bias), safety (CSAM), text (language), code (legal)
4. **Harm severity matters**: Not all absent nodes equal (CSAM victim ≠ privacy violation ≠ linguistic exclusion)
5. **Living datasets need temporal handling**: Common Crawl revealed version/fork ambiguity

### Recommendations for v0.3+ 📋
- Continue applied research (test on new domains before stabilizing)
- Expect 2-3 more revisions (v0.3, v0.4) before v1.0
- Stabilize for Phase 1 (tooling can't be built on moving target)
- Consider "ORP-Core" (minimal stable fields) + "ORP-Extensions" (domain-specific fields)

---

## Timeline Impact

**Phase 0 Original Plan:**
- Spec drafted → 1 example → public comment

**Phase 0 Revised (Actual):**
- Spec v0.1 drafted → 5 examples → **schema revision** → v0.2 → public comment

**Added time:** ~4 weeks (4 examples + schema revision)

**Value:** Much stronger empirical foundation, fewer issues during public comment, higher academic credibility

---

## Dependencies

**Depends on:**
- Sprint 1.7.3 (ImageNet complete)
- Sprint 1.7.3.1 (LAION-5B complete)
- Sprint 1.7.3.2 (Common Crawl complete)
- Sprint 1.7.3.3 (GitHub Copilot complete)

**Enables:**
- 60-day public comment period (Phase 0 milestone)
- Academic paper submission (Section 5 now has v0.2 validated on 5 domains)
- Phase 1 planning (tooling can target stable v0.2)

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-29
**Target Completion:** 2026-05-03
**Estimated Effort:** 56 hours over 4 days (intensive consolidation)
