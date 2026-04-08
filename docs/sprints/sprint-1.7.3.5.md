# Sprint 1.7.3.5: ORP v0.2 Implementation & Validation

**Sprint Duration:** 2-3 days
**Status:** In Progress
**Prerequisites:** Sprint 1.7.3.4 complete (empirical validation report)

---

## Sprint Goal

Implement ORP v0.2 core infrastructure based on empirical validation findings: design, JSON schema, and validator support.

**Deliverables**:
1. ✅ ORP v0.2 design document
2. ✅ ORP v0.2 JSON Schema (flexible, extensible)
3. ✅ Validator v0.2 support (auto-detection, extensions, post-hoc)
4. ✅ ImageNet example upgraded and validates successfully

**Note**: Example validation completion and specification writing moved to sprints 1.7.3.6 and 1.7.3.7.

---

## Context

### Empirical Validation Results (Sprint 1.7.3.4)

**Total errors found**: 311 across 4 documents
- ImageNet: 85 errors
- LAION-5B: 88 errors
- Common Crawl: 71 errors
- GitHub Copilot: 67 errors

**Error Categories**:
- additionalProperties violations: 113 (36%)
- Missing required fields: 142 (46%) - unknowable in post-hoc
- Type mismatches: 45 (14%) - rigid structures
- Enum violations: 11 (4%) - missing values

**Key Finding**: Documents naturally evolved **richer structures** than v0.1 schema anticipated.

---

## Phases

### Phase 1: Design ORP v0.2 ✅ COMPLETED

**Deliverable**: `docs/specs/ORP_V0.2_DESIGN.md`

**Design Principles**:
1. **Strict core + flexible extensions**: Required fields enforced, additionalProperties: true everywhere
2. **Post-hoc reconstruction support**: post_hoc flag, analyst role, accountability_gap field
3. **Array OR object flexibility**: Accept both simple and rich formats
4. **Extension registry**: Domain-specific fields (orp-ai-training-v1, orp-safety-v1, orp-license-v1)

**P0 Critical Fixes**:
1. additionalProperties: false → true (eliminates 113 errors, 36%)
2. Post-hoc support (eliminates ~50 errors, 16%)
3. Array OR object flexibility (eliminates 45 errors, 14%)
4. Missing enums: analyst, constitutive, research roles
5. New core fields: confidence, affected_count, accountability_gap

---

### Phase 2: Implement JSON Schema v0.2 ✅ COMPLETED

**Deliverable**: `orp_validator/schemas/orp-v0.2.schema.json` (714 lines)

**Schema Changes**:
- ✅ additionalProperties: true throughout (32 instances changed)
- ✅ Post-hoc fields: post_hoc flag, analyst/reconstructor roles
- ✅ Extension registry: extensions array with validation pattern
- ✅ Flexible structures: exclusion_criteria, cleaning_decisions accept objects
- ✅ New enums: analyst, constitutive, research, granular confidence (7 levels)
- ✅ Optional descriptions: affected_population.description not required
- ✅ Null support: document_id can be null, alternatives_considered can be null

**Extension Schemas Created**:
1. `orp-ai-training-v1.schema.json` (164 lines) - harm_tier, safety_filtering
2. `orp-safety-v1.schema.json` (67 lines) - CSAM detection, vulnerable populations
3. `orp-license-v1.schema.json` (80 lines) - GPL compliance, license distribution

---

### Phase 3: Update Validator ✅ COMPLETED

**Deliverable**: Updated `orp_validator/validator.py` and CLI

**Changes**:
- ✅ Auto-detects document version from `orp_version` field
- ✅ Supports both v0.1 and v0.2 validation
- ✅ Extension registry tracking (`_load_extensions` method)
- ✅ ORP-PostHoc compliance level recognition
- ✅ CLI `--orp-version` parameter for explicit version selection
- ✅ Enhanced warnings for post-hoc reconstruction and extensions
- ✅ Version bumped to 0.4.0 in `__init__.py`

**Test Results**:
- ✅ v0.1 documents validate correctly (danish_property_tax_reform.yaml)
- ✅ v0.2 documents validate correctly (test_orp_v0.2.yaml)
- ✅ ORP-PostHoc compliance level displays correctly (magenta color)

---

### Phase 4: Upgrade ImageNet Example ✅ COMPLETED

**Goal**: Validate that v0.2 schema works with at least one complete example

#### 4.1: ImageNet ✅ COMPLETED

**Changes**:
- Updated header: orp_version → "0.2", added post_hoc: true, extensions
- Fixed domain: ai-training-data → ai-training
- Added author affiliation
- Updated last_modified

**Result**: ✅ Validates successfully (ORP-PostHoc compliance)

**Outcome**: Proof-of-concept validated - v0.2 schema works for real documents

---

## Success Criteria

### Must Have ✅ ALL COMPLETED
- [x] ORP v0.2 design document complete
- [x] JSON Schema v0.2 implemented (714 lines)
- [x] 3 extension schemas created
- [x] Validator supports v0.2 with auto-detection
- [x] ImageNet validates successfully

### Nice to Have
- [ ] Automated test suite for schema flexibility
- [ ] Automated migration script
- [ ] Video walkthrough of migration
- [ ] Performance benchmark (v0.2 vs v0.1 validation speed)

---

## Sprint Status

**Status**: ✅ COMPLETED (2026-04-08)

**Completed**:
- Phase 1: ORP v0.2 design ✅
- Phase 2: JSON Schema v0.2 implementation ✅
- Phase 3: Validator v0.2 support ✅
- Phase 4: ImageNet upgrade & validation ✅

**Next Sprints**:
- Sprint 1.7.3.6: Complete schema flexibility + validate all 4 examples
- Sprint 1.7.3.7: Write ORP v0.2 specification and migration guide

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

### Risk 3: Specification Completeness
**Risk**: Specification may miss important details or edge cases
**Mitigation**:
- Use validated examples as reference
- Include comprehensive changelog
- Provide examples for every flexibility pattern
- Public comment period will catch gaps

---

## Files Modified/Created

**Schema Files**:
- ✅ `orp_validator/schemas/orp-v0.2.schema.json` (714 lines)
- ✅ `orp_validator/schemas/extensions/orp-ai-training-v1.schema.json` (164 lines)
- ✅ `orp_validator/schemas/extensions/orp-safety-v1.schema.json` (67 lines)
- ✅ `orp_validator/schemas/extensions/orp-license-v1.schema.json` (80 lines)

**Validator Files**:
- ✅ `orp_validator/validator.py` (updated for v0.2)
- ✅ `orp_validator/cli.py` (added --orp-version parameter)
- ✅ `orp_validator/__init__.py` (version 0.4.0, export ORPValidator)

**Documentation Files**:
- ✅ `docs/specs/ORP_V0.2_DESIGN.md` (comprehensive design document)
- ✅ `docs/sprints/sprint-1.7.3.4.md` (empirical validation sprint)
- ✅ `docs/sprints/sprint-1.7.3.4-validation-report.md` (311 errors categorized)
- 📝 `docs/specs/ORP_V0.2_SPEC.md` (TODO)
- 📝 `docs/specs/MIGRATION_V0.1_TO_V0.2.md` (TODO)

**Example Files**:
- ✅ `examples/imagenet_training_data.yaml` (upgraded to v0.2, validates)
- 🔄 `examples/laion5b_training_data.yaml` (header updated, needs validation)
- 🔄 `examples/common_crawl_training_data.yaml` (header updated, needs validation)
- 🔄 `examples/github_copilot_training_data.yaml` (header updated, needs validation)

---

## Next Steps

### Sprint 1.7.3.6: Complete Schema Flexibility (2-3 hours)
1. Apply schema flexibility for benefits/harms/vulnerable_populations (objects)
2. Upgrade and validate LAION-5B, Common Crawl, GitHub Copilot
3. Confirm all 4 examples validate successfully

### Sprint 1.7.3.7: Write Specification & Migration Guide (4-6 hours)
1. Write ORP v0.2 specification (15+ pages)
2. Write migration guide (v0.1 → v0.2)
3. Update README with v0.2 release notes
4. Optional: Automated migration script

### Future Sprints
- Sprint 1.7.3.8: Release ORP v0.2 to PyPI
- Sprint 1.7.3.9: Update REST API for v0.2
- Sprint 1.7.4: Begin public comment period

---

## Retrospective Notes

### What Went Well
- ✅ Empirical validation approach revealed real issues (not guessed)
- ✅ Validator auto-detection works seamlessly
- ✅ Extension system is clean and extensible
- ✅ ImageNet validates perfectly after schema updates

### What Didn't Go Well
- ⚠️ Initial schema still too rigid (benefits/harms objects not anticipated)
- ⚠️ Took multiple iterations to get flexibility right
- ⚠️ sed commands for batch header updates didn't work reliably

### Lessons Learned
1. **Empirical validation is essential**: Can't design schemas in a vacuum
2. **Flexibility is hard to predict**: Documents evolve richer structures naturally
3. **Test after every change**: Incremental validation prevents breakage
4. **additionalProperties: true is powerful**: Enables progressive enhancement

### Action Items for Next Sprints
- Consider automated schema generation from validated examples
- Build test suite for schema flexibility patterns
- Document "recommended but not required" fields more clearly
- Create schema evolution policy (when to add required fields)
