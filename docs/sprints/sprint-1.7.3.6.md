# Sprint 1.7.3.6: Complete ORP v0.2 Schema Flexibility

**Sprint Goal**: Finalize ORP v0.2 schema flexibility to validate all 4 AI training dataset examples

**Status**: Not Started
**Duration**: 2-4 hours
**Dependencies**: Sprint 1.7.3.5 (ORP v0.2 implementation)

---

## Context

Sprint 1.7.3.5 successfully implemented ORP v0.2 core infrastructure:
- ✅ Validator supports v0.2 with auto-detection
- ✅ JSON Schema v0.2 with additionalProperties: true throughout
- ✅ ImageNet example upgraded and validates successfully
- ⏸️  3 remaining examples (LAION-5B, Common Crawl, GitHub Copilot) have 40+ validation errors

**Key Finding**: Documents naturally evolved **richer structures** than schema anticipated:
- `benefits`/`harms`: Objects with severity/description, not just strings
- `vulnerable_populations`: Objects with population_type/harm_description
- `affected_population`: Can have size/geographic_scope without description
- `sensitivity_analysis`: Object structure, not array

**Philosophy**: v0.2 embraces "strict core + flexible everything else" - but current schema still has type constraints that are too rigid.

---

## Scope

### In Scope
1. **Schema Flexibility Improvements**:
   - L3 stakeholder benefits/harms: Accept string OR object
   - L3 vulnerable_populations_identified: Accept string OR object
   - L2 affected_population: Make description optional
   - L2 sensitivity_analysis: Accept object OR array
   - L1 access.public: Accept string OR boolean

2. **Validation**:
   - Upgrade LAION-5B, Common Crawl, GitHub Copilot to v0.2
   - Validate all 4 examples pass v0.2 validation
   - Document any remaining edge cases

3. **Documentation**:
   - Update ORP_V0.2_DESIGN.md with final flexibility decisions
   - Document schema flexibility patterns for future extensions

### Out of Scope
- Writing ORP v0.2 specification (Sprint 1.7.3.7)
- Migration guide (Sprint 1.7.3.7)
- Updating existing v0.1 examples beyond the 4 AI training datasets
- Breaking changes to required fields

---

## Tasks

### Task 1: Schema Flexibility Round 2 (1-2 hours)

**Objective**: Make schema accept both simple (string) and rich (object) formats for all descriptive fields

**Changes Needed**:

```json
// L3 stakeholder_groups
"benefits": {
  "oneOf": [
    {"type": "array", "items": {"type": "string"}},
    {"type": "array", "items": {"type": "object", "additionalProperties": true}}
  ]
},
"harms": {
  "oneOf": [
    {"type": "array", "items": {"type": "string"}},
    {"type": "array", "items": {"type": "object", "additionalProperties": true}}
  ]
}

// L3 minority_stress_test
"vulnerable_populations_identified": {
  "oneOf": [
    {"type": "array", "items": {"type": "string"}},
    {"type": "array", "items": {"type": "object", "additionalProperties": true}}
  ]
}

// L2 affected_population
"affected_population": {
  "type": "object",
  "properties": {
    "description": {"type": "string"},  // Remove from required
    "size": {"type": "number"},
    "affected_count": {"type": "number"}
  }
}

// L2 sensitivity_analysis
"sensitivity_analysis": {
  "oneOf": [
    {"type": "array"},
    {"type": "object", "additionalProperties": true}
  ]
}

// L1 access.public
"public": {
  "oneOf": [
    {"type": "boolean"},
    {"type": "string"}  // Accept "yes"/"no"/"partial"
  ]
}
```

**Validation**:
- Test schema changes don't break ImageNet validation
- Incrementally add flexibility, validate after each change

---

### Task 2: Upgrade Remaining Examples (30-60 minutes)

**Objective**: Update LAION-5B, Common Crawl, GitHub Copilot headers to v0.2

**Changes per document**:
1. `orp_version: "0.1"` → `"0.2"`
2. Add `post_hoc: true` flag
3. Add `extensions: [orp-ai-training-v1]`
4. Fix domain: `ai-training-data` → `ai-training`
5. Update `last_modified` to current date
6. Ensure authors have `role: analyst` and `affiliation`

**Validation after upgrade**:
```bash
source /tmp/orp_validation_env/bin/activate
pip install -e . --quiet

python3 -m orp_validator.cli examples/laion5b_training_data.yaml
python3 -m orp_validator.cli examples/common_crawl_training_data.yaml
python3 -m orp_validator.cli examples/github_copilot_training_data.yaml
```

**Success Criteria**: All 3 documents validate with 0 errors

---

### Task 3: Final Validation Suite (15 minutes)

**Objective**: Confirm all 4 examples pass v0.2 validation

**Test Matrix**:

| Document | v0.2 Valid? | Compliance Level | Warnings |
|----------|-------------|------------------|----------|
| ImageNet | ✅ | ORP-PostHoc | Extensions declared, accountability_gap |
| LAION-5B | ⏳ | ORP-PostHoc | TBD |
| Common Crawl | ⏳ | ORP-PostHoc | TBD |
| GitHub Copilot | ⏳ | ORP-PostHoc | TBD |

**Validation Commands**:
```bash
for doc in examples/*training_data.yaml; do
  echo "=== Validating $(basename $doc) ==="
  python3 -m orp_validator.cli "$doc" | grep -E "(Valid|Compliance|Warnings)"
done
```

**Success Criteria**:
- All 4 documents show `✓ Valid`
- All show `Compliance Level: ORP-PostHoc`
- Warnings are informational only (extensions, accountability_gap)

---

### Task 4: Update Design Documentation (30 minutes)

**Objective**: Document final v0.2 schema flexibility decisions

**File**: `docs/specs/ORP_V0.2_DESIGN.md`

**Sections to Add**:

```markdown
## Schema Flexibility Patterns

### Principle: Progressive Enhancement
v0.2 accepts both **simple** (string/array of strings) and **rich** (object/array of objects) formats for descriptive fields. This enables:

1. **Backward compatibility**: v0.1 simple formats still validate
2. **Progressive enhancement**: Authors can add structure as needed
3. **Real-world evolution**: Documents naturally develop richer structures over time

### Pattern: String OR Object Arrays

Applied to:
- L1: exclusion_criteria, cleaning_decisions, known_limitations
- L3: benefits, harms, vulnerable_populations_identified

**Simple format** (v0.1 style):
```yaml
benefits:
  - "Enabled deep learning revolution"
  - "Improved object recognition accuracy"
```

**Rich format** (v0.2 enhancement):
```yaml
benefits:
  - benefit: "Enabled deep learning revolution"
    magnitude: "Transformative"
    affected_population: "Global AI research community"
    evidence: "ImageNet Challenge results 2012-2017"
```

**Schema accepts both** via oneOf:
```json
"benefits": {
  "oneOf": [
    {"type": "array", "items": {"type": "string"}},
    {"type": "array", "items": {"type": "object", "additionalProperties": true}}
  ]
}
```

### Pattern: Optional Descriptions

Required fields should only be **structural identifiers**, not descriptive prose.

**Bad** (v0.1):
```json
"affected_population": {
  "required": ["description"]  // Forces prose even if size known
}
```

**Good** (v0.2):
```json
"affected_population": {
  "properties": {
    "description": {"type": "string"},
    "size": {"type": "number"}
  }
  // No required fields - any combination valid
}
```

### Pattern: Type Flexibility for Legacy Data

When fields naturally accept multiple types, support all reasonable interpretations:

```json
"public": {
  "oneOf": [
    {"type": "boolean"},  // true/false
    {"type": "string"}    // "yes"/"no"/"partial"/"conditional"
  ]
}
```

This handles:
- Clean v0.1 data: `public: true`
- Nuanced v0.2 data: `public: "partial (requires registration)"`
- Post-hoc reconstruction: `public: "unknown"`
```

---

## Success Criteria

### Must Have
- [x] All 4 AI training dataset examples validate successfully with v0.2 schema
- [x] ImageNet remains valid after schema changes
- [x] No required fields removed (only made more flexible)
- [x] ORP_V0.2_DESIGN.md documents flexibility patterns

### Nice to Have
- [ ] Automated test suite for schema flexibility (Phase 5.5.1)
- [ ] JSON Schema validation of schema itself (meta-validation)
- [ ] Performance benchmark (v0.2 validation speed vs v0.1)

---

## Risks and Mitigations

### Risk 1: Schema Too Permissive
**Risk**: Accepting both string and object everywhere may allow invalid structures
**Mitigation**:
- Keep required fields strict (orp_version, document_id, title, etc.)
- Document recommended structures in specification
- Future: Extension schemas can add stricter validation

### Risk 2: Breaking ImageNet Validation
**Risk**: Schema changes to fix 3 documents may break ImageNet
**Mitigation**:
- Test ImageNet after every schema change
- Use git to track schema versions
- Rollback immediately if ImageNet breaks

### Risk 3: Complexity Creep
**Risk**: Too many oneOf alternatives makes schema hard to understand
**Mitigation**:
- Document "why" for each flexibility decision
- Provide examples of both simple and rich formats
- Consider consolidating patterns in future (v0.3)

---

## Dependencies

**Requires**:
- Sprint 1.7.3.5 complete (v0.2 validator and core schema implemented)
- Python virtual environment at /tmp/orp_validation_env
- 4 AI training dataset examples in examples/ directory

**Blocks**:
- Sprint 1.7.3.7 (ORP v0.2 specification writing)
- Sprint 1.7.3.8 (Migration guide v0.1→v0.2)

---

## Deliverables

1. **Updated Schema**: `orp_validator/schemas/orp-v0.2.schema.json`
   - All flexibility patterns implemented
   - Validates all 4 examples

2. **Upgraded Examples**:
   - `examples/laion5b_training_data.yaml` (v0.2 header)
   - `examples/common_crawl_training_data.yaml` (v0.2 header)
   - `examples/github_copilot_training_data.yaml` (v0.2 header)

3. **Updated Documentation**:
   - `docs/specs/ORP_V0.2_DESIGN.md` (flexibility patterns section)
   - This sprint document updated with actual results

4. **Validation Report**: Summary of final validation status for all 4 documents

---

## Notes

**Philosophy Reminder**:
> "The protocol should evolve to match how documents are actually written, not force documents into rigid structures. v0.2's flexibility is a feature, not a bug."

**From Empirical Validation** (Sprint 1.7.3.4):
- Authors naturally add structure (objects) when detail needed
- Simple formats (strings) sufficient for straightforward cases
- Post-hoc reconstruction needs "unknown"/"null" flexibility
- Real-world documents are messier than theoretical schemas predict

**Key Lesson**:
Empirical validation (running actual validator on real documents) reveals patterns invisible to theoretical design. Always validate early, iterate often.

---

## Retrospective (Post-Sprint)

*To be filled after sprint completion*

### What Went Well
-

### What Didn't Go Well
-

### Lessons Learned
-

### Action Items for Next Sprint
-
