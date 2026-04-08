# Sprint Archive

This directory contains superseded, completed, or redundant sprint documents that have been archived for historical reference.

---

## Archived Files

### sprint-1.7.3.4-original-SUPERSEDED.md
**Original Purpose**: Schema consolidation plan
**Status**: Superseded by actual sprint execution
**Reason**: Sprint 1.7.3.4 evolved during execution to focus on empirical validation first
**Replaced By**: sprint-1.7.3.4-COMPLETED.md (actual empirical validation) + sprint-1.7.3.5.md (consolidated implementation)

### sprint-1.7.3.4-COMPLETED.md
**Purpose**: Empirical validation of 4 AI training dataset examples
**Status**: Completed 2026-04-08
**Result**: 311 validation errors discovered and categorized
**Key Output**: sprint-1.7.3.4-validation-report.md

### sprint-1.7.3.5-original.md
**Purpose**: Schema consolidation & ORP v0.2 design (original plan)
**Status**: Superseded by expanded consolidated version
**Reason**: Sprint expanded to include full implementation + specification writing
**Replaced By**: sprint-1.7.3.5.md (consolidated version with all phases)

### sprint-1.7.3.6-superseded.md
**Purpose**: Complete ORP v0.2 schema flexibility
**Status**: Superseded - merged into sprint-1.7.3.5.md
**Reason**: Overlapping scope with sprint-1.7.3.5 Phase 4.2
**Replaced By**: sprint-1.7.3.5.md Phase 4.2

### sprint-1.7.3.7-superseded.md
**Purpose**: ORP v0.2 specification and migration guide
**Status**: Superseded - merged into sprint-1.7.3.5.md
**Reason**: Specification writing is part of unified v0.2 implementation sprint
**Replaced By**: sprint-1.7.3.5.md Phase 5

---

## Current Active Sprints

See `docs/sprints/` for active sprint documents:

- **sprint-1.7.3.5.md**: ORP v0.2 Implementation & Validation (consolidated, all phases)
  - Phase 1-3: ✅ Completed (design, schema, validator)
  - Phase 4: 🔄 In Progress (example upgrades + schema flexibility)
  - Phase 5: 📝 Not Started (specification + migration guide)

---

## How to Use This Archive

**For historical research**:
- Check sprint evolution and decision rationale
- Compare original plans vs actual execution
- Understand why certain approaches were abandoned

**For future sprints**:
- Learn from sprint planning mistakes (over-granular splitting)
- See how empirical validation changed scope mid-sprint
- Reference consolidation patterns for similar work

**Do NOT use for**:
- Current sprint planning (use active sprints in parent directory)
- Implementation reference (schemas/code have evolved)
- Documentation (see docs/specs/ for current specs)

---

## Archive Policy

Sprint documents are archived when:
1. **Completed**: Sprint finished, documented in retrospective
2. **Superseded**: Replaced by evolved/consolidated version
3. **Redundant**: Overlapping with other sprints, merged to reduce fragmentation

Archived documents are **read-only** - do not edit. Create new sprint documents for new work.

---

*Last updated: 2026-04-08*
