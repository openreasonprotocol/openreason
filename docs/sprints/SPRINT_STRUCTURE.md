# Sprint 1.7.3 Structure: AI Training Dataset Examples & ORP v0.2

**Epic**: Sprint 1.7.0 - Foundation for Expansion
**Status**: In Progress (Phase 4)
**Duration**: ~3 weeks (2026-04-07 to 2026-04-27)

---

## Overview

Sprint 1.7.3 began as "ImageNet example (ORP-Full)" but expanded to a comprehensive ORP v0.2 development effort after empirical validation revealed 311 schema errors across 4 AI training dataset examples.

**Strategic Decision**: Rather than rush to public comment with unvalidated schema, we expanded Sprint 1.7.3 to include empirical validation + schema revision, producing ORP v0.2 grounded in real-world usage.

---

## Sprint Structure

### Planning Documents

| Document | Purpose | Status |
|----------|---------|--------|
| **sprint-1.7.3.md** | Original ImageNet plan | ✅ Completed |
| **sprint-1.7.3-COMPLETED.md** | ImageNet completion report | ✅ Completed (2026-04-07) |
| **sprint-1.7.3-EXPANSION-PLAN.md** | Strategic expansion overview | ✅ Reference document |

### Example Creation Sprints

| Sprint | Example | Status | Lines | Errors Found |
|--------|---------|--------|-------|--------------|
| **sprint-1.7.3.0** | (ImageNet in main sprint) | ✅ Completed | 1,513 | 85 |
| **sprint-1.7.3.1.md** | LAION-5B | ✅ Completed | 2,162 | 88 |
| **sprint-1.7.3.2.md** | Common Crawl | ✅ Completed | 2,232 | 71 |
| **sprint-1.7.3.3.md** | GitHub Copilot | ✅ Completed | 2,421 | 67 |

**Total**: 4 comprehensive AI training dataset examples, 8,328 lines, 311 validation errors discovered.

### Validation & Implementation Sprint

| Sprint | Purpose | Status |
|--------|---------|--------|
| **sprint-1.7.3.4.md** | Empirical validation | ✅ Completed (archived) |
| **sprint-1.7.3.4-validation-report.md** | 311 errors categorized | ✅ Reference document |
| **sprint-1.7.3.5.md** | ORP v0.2 implementation (consolidated) | 🔄 In Progress |

### Sprint 1.7.3.5 Phases (Consolidated)

**Phase 1**: Design ORP v0.2 ✅ COMPLETED
- Deliverable: `docs/specs/ORP_V0.2_DESIGN.md`
- Outcome: "Strict core + flexible extensions" design philosophy

**Phase 2**: Implement JSON Schema v0.2 ✅ COMPLETED
- Deliverable: `orp_validator/schemas/orp-v0.2.schema.json` (714 lines)
- Extensions: orp-ai-training-v1, orp-safety-v1, orp-license-v1

**Phase 3**: Update Validator ✅ COMPLETED
- Deliverable: Updated `orp_validator/validator.py`, CLI
- Features: Auto-detection, extension support, ORP-PostHoc compliance

**Phase 4**: Upgrade Examples & Schema Flexibility 🔄 IN PROGRESS
- 4.1: ImageNet ✅ Validates successfully
- 4.2: LAION-5B, Common Crawl, GitHub Copilot 🔄 Schema flexibility needed

**Phase 5**: Write Specification & Migration Guide 📝 NOT STARTED
- 5.1: ORP v0.2 Specification (15+ pages)
- 5.2: Migration Guide (v0.1 → v0.2)
- 5.3: Update README

---

## Key Deliverables

### Completed ✅

1. **4 AI Training Dataset Examples**:
   - examples/imagenet_training_data.yaml (v0.2, validates)
   - examples/laion5b_training_data.yaml (v0.2 header)
   - examples/common_crawl_training_data.yaml (v0.2 header)
   - examples/github_copilot_training_data.yaml (v0.2 header)

2. **ORP v0.2 Infrastructure**:
   - JSON Schema v0.2 (714 lines + 3 extension schemas)
   - Validator v0.2 (version 0.4.0)
   - Design documentation (ORP_V0.2_DESIGN.md)
   - Empirical validation report (311 errors analyzed)

### In Progress 🔄

3. **Example Validation**:
   - ImageNet: ✅ Valid
   - LAION-5B: Schema flexibility needed (benefits/harms objects)
   - Common Crawl: Schema flexibility needed
   - GitHub Copilot: Schema flexibility needed

### Not Started 📝

4. **Formal Documentation**:
   - ORP v0.2 Specification (comprehensive)
   - Migration Guide (v0.1 → v0.2)
   - README updates

---

## Files Overview

### Active Sprint Documents (docs/sprints/)
```
sprint-1.7.3.md                          # Original ImageNet plan
sprint-1.7.3-COMPLETED.md                # ImageNet completion
sprint-1.7.3-EXPANSION-PLAN.md           # Strategic overview
sprint-1.7.3.1.md                        # LAION-5B sprint
sprint-1.7.3.2.md                        # Common Crawl sprint
sprint-1.7.3.3.md                        # GitHub Copilot sprint
sprint-1.7.3.4-validation-report.md      # 311 errors analyzed
sprint-1.7.3.5.md                        # ORP v0.2 implementation (consolidated)
archive/                                 # Superseded/completed sprints
  ├── sprint-1.7.3.4-original-SUPERSEDED.md
  ├── sprint-1.7.3.4-COMPLETED.md
  ├── sprint-1.7.3.5-original.md
  ├── sprint-1.7.3.6-superseded.md
  └── sprint-1.7.3.7-superseded.md
```

### Key Outputs
```
docs/specs/
  └── ORP_V0.2_DESIGN.md                # v0.2 design philosophy

orp_validator/schemas/
  ├── orp-v0.2.schema.json              # Main schema (714 lines)
  └── extensions/
      ├── orp-ai-training-v1.schema.json
      ├── orp-safety-v1.schema.json
      └── orp-license-v1.schema.json

examples/
  ├── imagenet_training_data.yaml       # v0.2, validates ✅
  ├── laion5b_training_data.yaml        # v0.2 header
  ├── common_crawl_training_data.yaml   # v0.2 header
  └── github_copilot_training_data.yaml # v0.2 header
```

---

## Progress Summary

**Completed**:
- ✅ 4 comprehensive AI training dataset examples (8,328 lines)
- ✅ Empirical validation (311 errors discovered and categorized)
- ✅ ORP v0.2 design and implementation
- ✅ Validator v0.2 with auto-detection and extension support
- ✅ 1/4 examples validates successfully (ImageNet)

**Current Work** (Phase 4.2):
- 🔄 Additional schema flexibility (benefits/harms/vulnerable_populations)
- 🔄 Validate remaining 3 examples

**Next** (Phase 5):
- 📝 Write ORP v0.2 specification (15+ pages)
- 📝 Write migration guide (v0.1 → v0.2)
- 📝 Update README

**Estimated Time Remaining**: 6-10 hours
- Schema flexibility & validation: 2-3 hours
- Specification writing: 3-4 hours
- Migration guide: 1-2 hours
- README updates: 30 minutes

---

## Lessons Learned

### What Went Well
1. **Empirical validation approach**: Discovered real issues vs theoretical guesses
2. **Sprint consolidation**: Unified v0.2 implementation reduces fragmentation
3. **Flexible schema philosophy**: "Strict core + flexible extensions" validated by real documents
4. **Validator auto-detection**: Seamless v0.1/v0.2 support

### What Didn't Go Well
1. **Initial over-granular sprint planning**: Created redundant sprints (1.7.3.6, 1.7.3.7)
2. **Schema flexibility underestimated**: Multiple iterations needed
3. **Batch updates fragile**: sed commands for header updates didn't work reliably

### Action Items
1. **Future sprint planning**: Consolidate related work into single sprint with phases
2. **Empirical validation first**: Always validate examples before designing schemas
3. **Incremental testing**: Test after every schema change to catch breakage early
4. **Document flexibility patterns**: Create reusable patterns for future extensions

---

## Next Sprints

**Sprint 1.7.4**: Public Comment Period Preparation
- Finalize ORP v0.2 specification
- Create public-facing examples
- Set up feedback infrastructure

**Sprint 1.7.5**: PyPI Release & REST API Update
- Release orp-validator v0.4.0 to PyPI
- Update REST API (api.publicreasonproject.org) for v0.2
- Backward compatibility testing

---

*Last updated: 2026-04-08*
*Next review: After Sprint 1.7.3.5 completion*
