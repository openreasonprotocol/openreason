# Sprint 1.7.3.5: Schema Consolidation & ORP v0.2 Design

**Sprint Duration:** 4-6 days (estimated)
**Start Date:** After completing Sprint 1.7.3.4 (Empirical Validation)
**Target Completion:** ~2026-04-14
**Sprint Goal:** Consolidate actual validation errors from 4 AI examples → design ORP v0.2 with flexible, extensible schema
**Status:** PLANNED (dependencies: sprint 1.7.3.4 validation report must complete first)

---

## Context

### Problem Statement
ORP v0.1 schema was designed theoretically before real-world application. Creating 4 comprehensive AI training dataset examples revealed significant validation errors, demonstrating the schema is too rigid for diverse domains.

**Completed Examples (as of 2026-04-08):**
- ✅ ImageNet ILSVRC-2012: 1,513 lines
- ✅ LAION-5B: 2,162 lines
- ✅ Common Crawl: 2,232 lines
- ✅ GitHub Copilot: 2,421 lines

**Actual Error Counts (from Sprint 1.7.3.4 validation):**
- ImageNet: 85 errors (anticipated 85 - ✓ exact)
- LAION-5B: 88 errors (anticipated 88 - ✓ exact)
- Common Crawl: 71 errors (anticipated 71 - ✓ exact)
- GitHub Copilot: 67 errors (anticipated 30-50 - slightly higher)
- **TOTAL: 311 errors** (anticipated 274-294)

### Strategic Insight
These errors are **VALUABLE** - they reveal what the schema SHOULD support, not what we guessed it should support. Applied research beats theoretical design.

### User's Vision (2026-04-07)
> "Our protocol should be able to capture [domain-specific fields] 'if' setup to capture them, not per default. Our protocol should somehow become a dynamic entity that can be molded into this."

**Translation:** Schema should be:
- **Strict on core** (minimum fields for compliance)
- **Flexible on extensions** (domain-specific fields allowed)
- **Extensible over time** (new domains can add validated extensions)

---

## Sprint Goal

Design and implement **ORP v0.2** - a flexible, extensible schema that:
1. **Maintains rigor** (core required fields for compliance)
2. **Enables domain-specific extensions** (safety fields, harm tiers, license compliance, etc.)
3. **Supports post-hoc reconstruction** (analyst role, affiliation, accountability gaps)
4. **Accommodates real-world complexity** (list vs object flexibility, living datasets, federated structures)
5. **Validates cleanly** (all 5 examples <5 errors each after v0.2 upgrade)

**Success Criteria:**
- [ ] ORP v0.2 specification published
- [ ] JSON Schema v0.2 implemented  
- [ ] All 5 examples validate with <5 errors each
- [ ] Validator updated to support v0.2
- [ ] API updated to support v0.2
- [ ] Migration guide published (v0.1 → v0.2)
- [ ] Schema evolution retrospective documented

---

**See full sprint plan in /Users/asbjornras/open-reason/docs/sprints/sprint-1.7.3.4-original.md for original detailed schema field changes.**

**This version focuses on phased execution:**

## Phase 1: Error Consolidation (Day 1)
- Aggregate all errors from 4 examples
- Categorize by type (50-60% flexibility issues)
- Prioritize P0-P3 (15-20 blocker fields)
- Document patterns

## Phase 2: Schema Design (Day 2)  
- Design principles: strict core + flexible extensions
- Header changes: domain taxonomy, roles, post_hoc flag
- Layer changes: additionalProperties true, list/object flexibility
- Extension registry pattern

## Phase 3: Implementation (Days 3-4)
- Update JSON Schema with base + extensions
- Update validator logic (extension loading, warnings)
- Update CLI (migrate, extensions commands)
- Update API (version parameter, migration endpoint)

## Phase 4: Example Updates (Day 5)
- Upgrade all 5 examples to v0.2
- Target <5 errors each (from 175-235)
- Test migration workflow

## Phase 5: Documentation (Day 6)
- ORP v0.2 specification
- Migration guide  
- Schema evolution retrospective

---

## Key Design Decisions

### 1. Strict Core + Flexible Extensions
```json
{
  "required": ["excluded", "reason", "potential_impact"],
  "additionalProperties": true  // Allow domain-specific fields
}
```

### 2. Extension Registry Pattern
```yaml
orp_version: "0.2"
extensions:
  - orp-ai-training-v1    # Adds harm_tier, safety fields
  - orp-safety-v1         # Adds vulnerable_populations
```

### 3. List vs Object Flexibility  
Accept both formats where natural:
```yaml
# Both valid:
variables: [{id, name}, {id, name}]  # List
variables: {VAR1: {name}, VAR2: {name}}  # Object
```

### 4. Post-Hoc Support
```yaml
post_hoc: true
authors:
  - role: analyst  # NEW role for reconstruction
    affiliation: "Public Reason Project"  # NEW field
```

---

## Timeline

**Day 1:** Error analysis (8h)  
**Day 2:** Schema design (8h)  
**Day 3:** JSON Schema + validator (8h)  
**Day 4:** API + tests (8h)  
**Day 5:** Example upgrades (8h)  
**Day 6:** Documentation (8h)  

**Total:** 6 days (48 hours)  
**Contingency:** +1 day if needed

---

## Success Metrics

**Quantitative:**
- All 5 examples <5 errors (from 175-235)
- 90%+ of P0+P1 errors resolved  
- Validator coverage >80%

**Qualitative:**
- Schema feels natural (not fighting structure)
- Extensions enable innovation
- Post-hoc reconstruction supported
- Fork-first philosophy enabled

---

## Deliverables

**Code:**
- orp-v0.2.schema.json + extensions
- Updated validator + CLI
- Updated API

**Examples:**
- All 5 upgraded to v0.2

**Docs:**
- ORP_SPEC.md v0.2
- Migration guide
- Schema evolution retrospective

---

**Sprint Owner:** Asbjørn Ras  
**Created:** 2026-04-07  
**Status:** IN PROGRESS
**Start:** 2026-04-08 (Sprint 1.7.3.4 validation complete)

---

## Phase 1: Error Consolidation ✅ COMPLETE

**Completed in Sprint 1.7.3.4** (see validation report)

**Key Findings:**
- 311 total errors across 4 documents
- Error distribution: 36% additionalProperties, 46% missing fields, 14% type mismatches, 4% enum
- All 4 documents show similar patterns → systematic schema gaps, not document bugs
- P0 fixes (14 changes) will eliminate ~80% of errors (250/311)

**P0 Critical Fixes (all 4 documents affected):**
1. additionalProperties: false → true (113 errors eliminated)
2. Post-hoc reconstruction support (50+ errors eliminated)
3. Array OR object flexibility (45 errors eliminated)
4. Missing enums: analyst role, constitutive decision_type, ai-training domain
5. Missing core fields: confidence, affected_count, comparison_to_actual, consequences, accountability_gap, notes, affiliation

**P1 High Priority (3-4 documents):**
6. temporal_metadata, critical_undocumented_exclusions (Layer 1)
7. sensitivity_analysis, uncertainties (Layer 2)
8. stakeholder_groups, vulnerable_population_flags (Layer 3)

**P2 Domain-Specific (extensions):**
- harm_tier, data_removed, license_compliance, vulnerability_rate

**See:** `docs/sprints/sprint-1.7.3.4-validation-report.md` for full analysis

---

## Phase 2: Schema Design (IN PROGRESS)

**Goal:** Design ORP v0.2 schema structure based on empirical validation findings

**Design Principles:**
