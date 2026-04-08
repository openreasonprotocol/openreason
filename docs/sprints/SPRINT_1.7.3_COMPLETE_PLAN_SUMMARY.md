# Sprint 1.7.3 Complete Plan: Summary

**Created:** 2026-04-07
**Status:** ImageNet complete, 4 sub-sprints planned
**Total Duration:** ~5 weeks (26 days)
**Strategic Goal:** Empirically validate ORP v0.2 before public comment

---

## Quick Reference

### Sprint Files Created:

1. ✅ **sprint-1.7.3.md** - ImageNet example (COMPLETED)
2. ✅ **sprint-1.7.3-COMPLETED.md** - ImageNet retrospective
3. ⏳ **sprint-1.7.3.1.md** - LAION-5B example (7 days)
4. ⏳ **sprint-1.7.3.2.md** - Common Crawl example (7 days)
5. ⏳ **sprint-1.7.3.3.md** - GitHub Copilot example (7 days)
6. ⏳ **sprint-1.7.3.4.md** - Schema Revision & Consolidation (4 days)
7. ✅ **sprint-1.7.3-EXPANSION-PLAN.md** - Master plan document
8. ✅ **THIS FILE** - Quick reference summary

---

## The Four AI Datasets

### 1. ImageNet ILSVRC-2012 (✅ COMPLETE)
**File:** `examples/imagenet_training_data.yaml` (1,513 lines)
**Completed:** 2026-04-07

**What it demonstrates:**
- Constitutive decisions (2009) → decade of AI bias
- Absent nodes: 49K AMT workers, millions depicted, billions affected
- Harm type: **Bias** (demographic), **Dignity** (offensive labels)

**Key findings:**
- 80%+ Western images → 10-20pp accuracy drop on non-Western test sets
- 54% person categories (1,593 labels) offensive, removed 2019
- Post-hoc remediation cannot undo millions of models trained 2012-2019

**Schema discoveries:** 85 validation errors

---

### 2. LAION-5B (⏳ PLANNED - Sprint 1.7.3.1)
**File:** `examples/laion5b_training_data.yaml` (estimated 1,500+ lines)
**Duration:** 7 days (2026-04-08 to 2026-04-15)

**What it demonstrates:**
- Worst-case safety issues (CSAM, medical privacy, revenge porn)
- Absent nodes: CSAM victims (children), medical patients, NCII victims
- Harm type: **Safety** (illegal content), **Legal** (HIPAA, privacy)

**Expected findings:**
- 3,226+ CSAM images (Stanford Internet Observatory)
- Medical imagery (HIPAA violations)
- Non-consensual intimate images
- Federated structure (URLs not images)

**Expected schema discoveries:** 30-50 new issues
- Harm severity taxonomy (criminal > legal > ethical > economic)
- Vulnerable populations flag (children cannot consent)
- Safety compliance fields (CSAM filtering, HIPAA)

---

### 3. Common Crawl (⏳ PLANNED - Sprint 1.7.3.2)
**File:** `examples/common_crawl_training_data.yaml` (estimated 1,500+ lines)
**Duration:** 7 days (2026-04-15 to 2026-04-22)

**What it demonstrates:**
- Living dataset (monthly releases since 2008)
- Extreme scale (250B+ pages, 3PB compressed)
- Absent nodes: 6,900+ linguistic communities
- Harm type: **Existential** (language extinction), **Cultural** (erasure)

**Expected findings:**
- 90%+ English content (despite 7,000+ languages globally)
- Low-resource languages virtually absent
- Feeds all major LLMs (GPT, Claude, LLaMA, PaLM, Gemini)
- Linguistic extinction accelerating

**Expected schema discoveries:** 40-60 new issues
- Living dataset methodology (temporal evolution)
- Scale-appropriate provenance (statistical sampling)
- Linguistic diversity metrics
- Existential harm category

---

### 4. GitHub Copilot (⏳ PLANNED - Sprint 1.7.3.3)
**File:** `examples/github_copilot_training_data.yaml` (estimated 1,500+ lines)
**Duration:** 7 days (2026-04-22 to 2026-04-29)

**What it demonstrates:**
- Code modality (not images/text)
- Legal dimension (license compliance, GPL copyleft)
- Absent nodes: GPL authors, open source maintainers, future contributors
- Harm type: **Legal** (copyright), **Economic** (exploitation), **Ecosystem** (sustainability)

**Expected findings:**
- GPL code in training data (copyleft violated?)
- No attribution mechanism (MIT/Apache require credit)
- No compensation (labor extraction)
- Open source sustainability crisis

**Expected schema discoveries:** 20-40 new issues
- License compliance fields (distribution, review, attribution)
- Legal risk assessment (IP, contractual obligations)
- Ecosystem harm (future-oriented, collective)
- Economic fairness (compensation, revenue sharing)

---

## Schema Consolidation (Sprint 1.7.3.4)

**Duration:** 4 days (2026-04-29 to 2026-05-03)

**Goal:** Consolidate 175-235 schema issues → ORP v0.2

**Major deliverables:**
1. **ORP_SPEC.md v0.2** - Comprehensive schema revision
2. **orp-v0.2.schema.json** - Updated JSON Schema
3. **All 5 examples validated** - Clean validation (<5 errors each)
4. **Validator updated** - CLI supports v0.2
5. **API updated** - Production supports v0.2
6. **Migration guide** - v0.1 → v0.2 conversion
7. **Schema evolution retrospective** - Research methodology documented

**Key schema changes:**

**Header:**
- Expanded domain enum (ai-training-images, ai-training-text, ai-training-code)
- New author roles (analyst, attester for post-hoc reconstruction)

**Layer 1 (Data Provenance):**
- Dataset types (static, living, federated, synthetic)
- License compliance (distribution, review, attribution)
- Safety compliance (CSAM filtering, HIPAA, illegal content)
- Linguistic diversity (language counts, distribution, low-resource)
- Temporal metadata (for living datasets)

**Layer 2 (Consequence Simulation):**
- Variable structure refinement (actual_value + default_value)
- Assumptions: both confidence + sensitivity
- Scenarios: allow list outcomes

**Layer 3 (Empathy Mapping):**
- **Harm severity taxonomy** (existential > safety > legal > ethical > economic)
- Vulnerable populations (children, medical patients, crime victims)
- Distributional welfare notes (who benefits, who is harmed)
- Minority stress test (explicit section)

**Layer 4 (Accountability Ledger):**
- Expanded decision types (taxonomy, safety, legal_compliance, ethical_remediation)
- Add consequences/source fields
- Legal review flag, ethical review flag

**Layer 5 (Fork Registry):**
- Potential forks section (add back - ImageNet uses this)
- Flexible known fork structure (less rigid)
- Version vs fork distinction

---

## Timeline

### Sprint Sequence:

```
Week 1: ImageNet (✅ DONE)
  └─ 2026-04-07: Completed in 1 day

Week 2: LAION-5B (⏳ NEXT)
  └─ 2026-04-08 to 2026-04-15 (7 days)

Week 3: Common Crawl
  └─ 2026-04-15 to 2026-04-22 (7 days)

Week 4: GitHub Copilot
  └─ 2026-04-22 to 2026-04-29 (7 days)

Week 5: Schema Consolidation
  └─ 2026-04-29 to 2026-05-03 (4 days)

Public Comment Period
  └─ Starts ~2026-05-05 (60 days)
```

**Total:** ~5 weeks from ImageNet complete to v0.2 published

---

## Expected Schema Issues Summary

| Example | Errors | Cumulative Total |
|---------|--------|------------------|
| ImageNet | 85 | 85 |
| LAION-5B | 30-50 | 115-135 |
| Common Crawl | 40-60 | 155-195 |
| GitHub Copilot | 20-40 | 175-235 |
| **After v0.2 revision** | **<25** | **Target: >90% resolved** |

---

## Pattern Across All Examples

### Common Thread: Constitutive Opacity → Decades of Harm

**Timeline pattern:**
1. **Constitutive decision** (2007-2021): Taxonomy choice, crawl method, license handling
2. **Absent nodes excluded** (design time): AMT workers, linguistic communities, GPL authors
3. **Deployment** (2009-2021): Models trained, systems deployed
4. **Harms discovered** (2017-2023): 7-12 years later, critics surface issues
5. **Post-hoc remediation** (2019-2023): Remove offensive labels, CSAM URLs, etc.
6. **Irreversible consequences**: Deployed models can't be retrained, extinct languages gone forever

**What ORP would have changed:**
- Layer 3 identifies absent nodes **at design time** (not 7 years later)
- Layer 2 models consequences **before deployment** (not after)
- Layer 4 logs alternatives considered (enables critique without guessing intent)
- Layer 5 enables constructive forks (critics propose alternatives, not just criticize)

---

## Harm Taxonomy Discovered

### Evolution Through Examples:

**ImageNet:**
- Dignity harm (offensive labels)
- Bias harm (demographic disparities)

**LAION-5B adds:**
- Safety harm (CSAM - illegal)
- Legal harm (HIPAA violations)

**Common Crawl adds:**
- Existential harm (language extinction - irreversible)
- Cultural harm (erasure of communities)

**GitHub Copilot adds:**
- Ecosystem harm (sustainability crisis)
- Economic harm (labor extraction)

**Final ORP v0.2 taxonomy:**
```
Tier 1: Existential (language death, cultural genocide)
Tier 2: Safety (CSAM, violence, abuse)
Tier 3: Legal (HIPAA, copyright, GPL)
Tier 4: Ethical (dignity, privacy, consent)
Tier 5: Economic (wage theft, exploitation)
```

**This could not have been designed theoretically—emerged from applied research.**

---

## Academic Paper Impact

### Section 5 (ORP Operationalization) - Before:
- "ORP demonstrated in two domains (policy, AI)"
- Single AI example (ImageNet)
- Weakness: "Is this generalizable?"

### Section 5 (ORP Operationalization) - After:
- "ORP validated across 5 domains: policy + 4 AI sub-domains"
- **Pattern demonstrated:** Constitutive opacity → decades of harm (across 4 datasets, 2009-2024)
- **Schema evolution documented:** v0.1 (theoretical) → v0.2 (empirically validated)
- **Harm taxonomy discovered:** Existential > Safety > Legal > Ethical > Economic
- **Research methodology rigorous:** Theory → Test → Revise → Validate

**Reviewer response:**
- Before: "Interesting but limited evidence"
- After: "Comprehensive empirical validation, systematic pattern, rigorous methodology"

---

## Key Insights

### 1. Applied Research Beats Theoretical Design
- Can't design perfect schema without real examples
- Each domain reveals unique requirements
- 85 errors from ImageNet alone (would have been 0 if we'd guessed right)

### 2. Each Example Reveals Unique Dimension
- ImageNet: Bias, absent workers, post-hoc remediation failure
- LAION: Safety harms (illegal content), vulnerable populations
- Common Crawl: Existential harms (language death), living datasets
- Copilot: Legal dimension (licenses), ecosystem sustainability

Not redundant—each adds new discovery.

### 3. Pattern Requires N≥4
- 1 example = anecdote
- 2 examples = coincidence
- 3-4 examples = pattern
- **4 AI examples = robust pattern:** Constitutive decisions → years → irreversible harms

### 4. Quality Assurance Saves Time
- Fix schema now (4 weeks) vs during public comment (unknown delay, restart)
- One major revision (v0.1 → v0.2) vs many small fixes (v0.1.1, v0.1.2, ...)
- Public comment on stable schema = productive (vs reactive fire-fighting)

### 5. Depth > Breadth for Schema Validation
- Could have done 10 ORP-Basic examples (shallow)
- Chose 5 ORP-Full examples (deep)
- **Deep reveals schema gaps**, shallow doesn't stress-test

---

## Success Criteria

### By End of Sprint 1.7.3.4:

**Completion:**
- [ ] All 4 AI examples completed (LAION, Common Crawl, Copilot)
- [ ] ORP v0.2 specification published
- [ ] All 5 examples validate clean (<5 errors each)
- [ ] API/validator support v0.2 in production
- [ ] Migration guide available (v0.1 → v0.2)

**Quality:**
- [ ] 175-235 schema issues addressed (>90% resolved)
- [ ] Harm taxonomy comprehensive (all 5 types covered)
- [ ] Schema stable for public comment (expect <10 community issues)
- [ ] Each example demonstrates unique ORP value

**Impact:**
- [ ] Academic paper Section 5 strengthened (5-domain validation)
- [ ] Pattern demonstrated (systematic, not anecdotal)
- [ ] Research methodology documented (rigorous theory-revision process)
- [ ] Phase 1 can target stable schema (v0.2 good enough for tooling)

---

## Next Action

**START:** Sprint 1.7.3.1 (LAION-5B)
**Date:** 2026-04-08
**Duration:** 7 days
**First task:** Research LAION-5B constitution (Stanford report, LAION papers, safety issues)

**Key focus:** Worst-case safety scenario (CSAM, medical privacy, revenge porn)

---

## Files Inventory

### Sprint Plans:
- `docs/sprints/sprint-1.7.3.md` - ImageNet original plan
- `docs/sprints/sprint-1.7.3-COMPLETED.md` - ImageNet retrospective
- `docs/sprints/sprint-1.7.3.1.md` - LAION-5B plan
- `docs/sprints/sprint-1.7.3.2.md` - Common Crawl plan
- `docs/sprints/sprint-1.7.3.3.md` - GitHub Copilot plan
- `docs/sprints/sprint-1.7.3.4.md` - Schema Consolidation plan
- `docs/sprints/sprint-1.7.3-EXPANSION-PLAN.md` - Master plan (detailed)
- `docs/sprints/SPRINT_1.7.3_COMPLETE_PLAN_SUMMARY.md` - This file (quick reference)

### Examples (Current):
- `examples/danish_property_tax_reform.yaml` - Policy domain (ORP-Full)
- `examples/imagenet_training_data.yaml` - AI domain (ORP-Full) ✅
- `examples/imagenet/README.md` - Methodology
- `examples/imagenet/research_notes.md` - 744 lines of citations

### Examples (To Create):
- `examples/laion5b_training_data.yaml` - Sprint 1.7.3.1
- `examples/laion5b/README.md` - Sprint 1.7.3.1
- `examples/laion5b/research_notes.md` - Sprint 1.7.3.1
- `examples/common_crawl_training_data.yaml` - Sprint 1.7.3.2
- `examples/common_crawl/README.md` - Sprint 1.7.3.2
- `examples/common_crawl/research_notes.md` - Sprint 1.7.3.2
- `examples/github_copilot_training_data.yaml` - Sprint 1.7.3.3
- `examples/github_copilot/README.md` - Sprint 1.7.3.3
- `examples/github_copilot/research_notes.md` - Sprint 1.7.3.3

### Schema (To Create):
- `docs/specs/ORP_SPEC.md` v0.2 - Sprint 1.7.3.4
- `orp_validator/schemas/orp-v0.2.schema.json` - Sprint 1.7.3.4
- `docs/specs/ORP_V0.1_TO_V0.2_MIGRATION.md` - Sprint 1.7.3.4
- `docs/specs/SCHEMA_EVOLUTION_RETROSPECTIVE.md` - Sprint 1.7.3.4

---

**This is your roadmap. Ready to begin Sprint 1.7.3.1 (LAION-5B)?**
