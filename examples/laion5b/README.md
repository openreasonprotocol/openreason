# LAION-5B Training Data - ORP Documentation

**Document:** `laion5b_training_data.yaml`
**Status:** Draft (Post-hoc Reconstruction)
**Created:** 2026-04-07
**Sprint:** 1.7.3.1 (7 days)

---

## Overview

This ORP-Full document reconstructs the constitutive decisions behind LAION-5B (5.85 billion image-text pairs, March 2022), the largest open-source image-text dataset used to train Stable Diffusion and other generative AI models.

**Key Finding:** LAION-5B demonstrates CONSTITUTIVE OPACITY → IRREVERSIBLE HARM pattern. Seven major decisions (Sep 2021 - Mar 2022) were made without transparent documentation, resulting in:
- **1,008 confirmed CSAM victims** re-victimized for 21 months (March 2022 - December 2023)
- **Medical privacy violations** (HIPAA-protected imagery, unknown scale)
- **Non-consensual intimate imagery** (NCII victims, unknown scale)
- **Billions depicted without consent** (privacy, dignity violations)
- **80% of global population under-represented** (Western/English bias baked into generative AI)

**ORP's Value:** If LAION had conducted Layer 3 empathy mapping BEFORE publication, minority stress test would have identified CSAM victims as vulnerable population requiring absolute protection, triggering hash matching ($50-100K, 2-3 months delay) preventing Tier 1 federal crime distribution.

---

## Document Structure

### Header
- **Author:** Asbjørn Ras (analyst role - post-hoc reconstruction)
- **Domain:** ai-training-images (not in current schema, needs expansion)
- **Summary:** 12-month CSAM distribution, medical/NCII violations, consent failure, Western bias

### Layer 1: Data Provenance (375 lines)
**Critical Undocumented Exclusions:**
1. **NO CSAM filtering** - Despite $50-100K PhotoDNA hash matching available, LAION released without child protection measures
2. **NO medical privacy filtering** - HIPAA-protected imagery scraped from healthcare websites
3. **NO consent mechanism** - "Publicly accessible URL" assumed = "consented to AI training" (contested assumption)

**Key Decisions:**
- Common Crawl sole source (Dec 2020 - Mar 2021, 4 snapshots)
- CLIP filtering threshold 0.28 (50B+ candidates → 5.85B pairs)
- Minimal NSFW classifier (adult pornography only, not CSAM/NCII/medical)
- Federated distribution (URLs only, prevents post-hoc remediation)

### Layer 2: Consequence Simulation (410 lines)
**4 Scenarios Modeled:**
- **S1 (Actual):** No safety filtering → 3,226 CSAM URLs, medical/NCII violations, 80% bias
- **S2 (Hash Matching):** $50-100K, 2-3 months → prevents 2,236 CSAM URLs (Tier 1 harm eliminated)
- **S3 (Comprehensive Safety):** $1-1.5M, 12-18 months → Tier 1-3 harms eliminated (CSAM, HIPAA, NCII)
- **S4 (Consent-Based):** $500K-2M, 12-24 months → 95% dataset reduction (250M pairs), zero consent violations

**Sensitivity Analysis:**
- **CRITICAL VARIABLE:** CSAM_filtering_methodology - changing from "none" to "hash_only" prevents federal crime at 5-10% of budget
- **RADICAL VARIABLE:** Consent_mechanism - opt-in reduces scale 95%+, UNTESTED if smaller dataset trains viable models

### Layer 3: Empathy Mapping (510 lines)
**10 Stakeholder Groups:**
1. LAION Team (100% representation, benefits > harms)
2. AI Researchers (high representation, 2,000+ papers enabled)
3. Commercial Companies (high representation, $1B+ valuations)
4. Generative AI Users (no representation, 10M+ users)
5. **CSAM Victims** (0% representation, Tier 1 harm - CRITICAL ABSENT NODE)
6. **Medical Patients** (0% representation, Tier 2-3 harm - HIPAA violations)
7. **NCII Victims** (0% representation, Tier 3 harm - privacy, dignity)
8. Copyright Holders (0% representation, Tier 4 harm - $1.8T lawsuit)
9. Web Users Generally (0% representation, billions depicted)
10. Non-Western Communities (0% representation, 80% global population)

**Minority Stress Test: FAILED**
- Vulnerable populations (children, abuse victims, Global South) bore Tier 1-5 harms
- Privileged groups (Western AI community) captured 90%+ benefits
- Distributional injustice: least advantaged harmed for others' benefit (violates Rawlsian justice)

**Net Welfare Assessment: NEGATIVE**
- Utilitarian analysis inadequate (Tier 1 harms not tradeable against research benefits)
- Deontological failure (CSAM victims treated as MEANS to AI research ENDS, violates Kantian dignity)
- Harm prioritization: TIER 1 (CSAM) absolute priority, no cost justifies federal crime distribution

### Layer 4: Accountability Ledger (530 lines)
**7 Constitutive Decisions Documented:**

1. **D1: CLIP Filtering** (Sep 2021) - Christoph Schuhmann, LAION team
   - Decision: Use CLIP similarity > 0.28 as primary criterion
   - Consequences: 5.85B high-relevance pairs, but CLIP blind to age/consent/medical context

2. **D2: NO CSAM Filtering** (Sep 2021 - Mar 2022) - LAION team (individuals unknown)
   - **CRITICAL ACCOUNTABILITY FAILURE:** Most consequential decision, completely undocumented
   - Rationale: UNKNOWN (cost? legal? technical? ignorance?)
   - Consequences: 1,008 CSAM victims, 21 months federal crime distribution, irreversible harm
   - **ORP's Value:** Layer 4 would REQUIRE this decision logged BEFORE publication

3. **D3: Minimal NSFW Filtering** (Sep 2021 - Mar 2022) - LAION team
   - Decision: Remove hardcore pornography only, preserve artistic/medical nudity
   - Consequences: CSAM missed (classifier can't detect age), NCII missed (can't detect consent)

4. **D4: Federated Distribution** (Sep 2021) - LAION team
   - Decision: URLs only, no image hosting ($20-100M cost savings)
   - Consequences: ZERO remediation capability (can't retrieve cached images or fix trained models)

5. **D5: No Consent Mechanism** (Sep 2021 - Mar 2022) - LAION team
   - Decision: Assume "publicly accessible" = "consented to AI training"
   - Consequences: 1-2 billion depicted without notification, CSAM/NCII victims unaware

6. **D6: Zero Human Review** (Sep 2021 - Mar 2022) - LAION team
   - Decision: 100% automated pipeline, no sampling (0% vs 0.01-0.1% industry standard)
   - Consequences: CSAM/medical/NCII undetected, no feedback loop for classifiers

7. **D7: Common Crawl Sole Source** (Sep 2021) - LAION team
   - Decision: No targeted non-Western crawling, no linguistic diversity targets
   - Consequences: 40% English, 80% Western, linguistic extinction accelerated

### Layer 5: Fork Registry (337 lines)
**4 Known Forks:**
1. **Re-LAION-5B** (Aug 2024) - 2,236 CSAM URLs removed, but can't fix cached images or trained models
2. **LAION-400M** (Sep 2021) - Predecessor proof-of-concept (400M pairs)
3. **LAION-2B-en** (May 2022) - Stable Diffusion training data (English subset, CSAM inherited)
4. **LAION-Aesthetics** (Apr 2022) - Quality-filtered subset (aesthetic score > 6.0)

**4 Potential Forks:**
1. **LAION-5B-Safe** (Hypothetical) - Comprehensive safety ($1-1.5M, 12-18 months, Tier 1-3 harms eliminated)
2. **LAION-Consent** (Hypothetical) - Opt-in only ($500K-2M, 12-24 months, 250M pairs, zero consent violations)
3. **LAION-Global** (Hypothetical) - Linguistic diversity ($1-5M, 6-12 months, 50% non-Western)
4. **LAION-Living** (Hypothetical) - Hosted hybrid ($5-20M, quarterly updates, remediation capability)

**Fork Encouragement:** If you disagree with LAION's decisions or this document's analysis, FORK IT. Create LAION-Safe, LAION-Consent, or propose better alternatives. ORP's purpose: make decisions transparent so alternatives can be demonstrated, not just debated.

---

## Methodology

### Sources
- **Primary:** Schuhmann et al. (2021, 2022) LAION papers
- **Safety:** Thiel (2023) Stanford Internet Observatory CSAM report
- **Remediation:** LAION blog posts (Dec 2023 takedown, Aug 2024 Re-LAION-5B)
- **Legal:** Getty Images v. Stability AI, Andersen v. Stability AI (2023)
- **Criticism:** Birhane et al. (2021) ImageNet bias, Bender et al. (2021) Stochastic Parrots

### Limitations
1. **Post-hoc reconstruction** - LAION did not document internal deliberations, rationales inferred from public sources
2. **Unknown rationales** - Decision D2 (no CSAM filtering) completely undocumented, marked "UNKNOWN" in accountability ledger
3. **Harm quantification incomplete** - Medical patients and NCII victims UNKNOWN count (no systematic audit)
4. **Link rot** - 50% URLs dead by 2024, cannot fully audit dataset post-hoc

### Attestation
**Analyst:** Asbjørn Ras, Public Reason Project
**Date:** 2026-04-07
**Statement:** This document represents external analysis for demonstrating ORP's value, not official LAION documentation. Gaps marked "UNKNOWN" indicate undocumented decisions where internal deliberations not public.

---

## Validation Status

**Validation Date:** 2026-04-07
**Validator:** ORP v0.1 JSON Schema
**Result:** ❌ **88 validation errors** (expected - schema gaps discovered through applied research)

**Error Categories:**
- Domain taxonomy (1): Needs `ai-training-images` not just `ai-training`
- Author roles (2-3): Needs `analyst` role, `affiliation` field
- Layer 1 structure (4-33): Exclusion criteria, cleaning decisions, limitations mismatches
- Layer 2 structure (34-47): Missing `model` field, wrong types for variables/outcomes
- Layer 3 structure (48-58): Stakeholder map, minority stress test structure
- Layer 4 structure (59): List vs object for accountability ledger
- Layer 5 structure (60-88): Fork registry structure completely different

**Note:** These errors are **VALUABLE** - they reveal what ORP v0.2 schema should support. Sprint 1.7.3.4 (Schema Consolidation) will analyze 175-235 errors across 4 AI examples to design empirically-validated schema.

---

## Key Insights

### 1. Constitutive Opacity Enables Irreversible Harm
LAION made 7 major decisions (Sep 2021 - Mar 2022) without transparent documentation. Result: 1,008 CSAM victims, 21 months federal crime distribution. Post-hoc remediation (Re-LAION-5B Aug 2024) cannot undo cached images, trained Stable Diffusion weights, or propagated Western bias.

### 2. Tier 1 Harms Not Tradeable in Cost-Benefit Analysis
Classical utilitarianism (2,000 papers + $1B value > 1,008 CSAM victims) is morally inadequate. Children's safety is absolute constraint, not utility factor. 18 U.S.C. § 2252 has no "scientific research" exception - strict liability crime regardless of benefits.

### 3. Federated Architecture Prevents Remediation
Distributing URLs (not images) saved $20-100M but permanently prevented CSAM remediation. When Stanford discovered 3,226 CSAM URLs (Dec 2023), LAION could remove URLs but not retrieve cached images or fix trained models. Architectural choice prioritized cost over safety capability.

### 4. Absent Nodes Bear Disproportionate Harms
Stakeholder groups with 0% governance representation bore Tier 1-5 harms:
- CSAM victims: 0% voice, Tier 1 harm (federal crime)
- Medical patients: 0% voice, Tier 2 harm (HIPAA)
- NCII victims: 0% voice, Tier 3 harm (dignity)
- Non-Western communities: <5% voice, Tier 5 harm (bias)

Meanwhile, Western AI community (20% global population) held 100% governance power, captured 90%+ benefits.

### 5. Missed Opportunities at Negligible Cost
- **Hash matching:** $50-100K (1-2% of budget) prevents Tier 1 harm
- **Comprehensive safety:** $1-1.5M (10-30% of budget) eliminates Tier 1-3 harms
- **Linguistic diversity:** $1-5M (0.1-0.5% of Stability AI's $1B valuation) benefits 80% global population

LAION chose none of these, for UNKNOWN reasons (not documented).

### 6. ORP Would Have Changed Outcomes
If LAION conducted ORP analysis BEFORE publication (March 2022):
- **Layer 2 scenarios** would model hash matching ($50-100K vs $0 for Tier 1 harm prevention)
- **Layer 3 empathy mapping** would identify CSAM victims as vulnerable population requiring absolute protection
- **Layer 4 accountability ledger** would REQUIRE Decision D2 (no CSAM filtering) be logged and justified
- **Layer 5 fork registry** would invite alternatives ("If you think hash matching worth 2-3 month delay, fork and show us")

Result: Constitutive transparency → proactive safety → 1,008 children protected from re-victimization.

---

## Files

```
examples/laion5b/
├── README.md                      # This file
├── research_notes.md              # 823 lines, comprehensive background research
└── ../laion5b_training_data.yaml  # 2,162 lines, ORP-Full document
```

**Related Examples:**
- `examples/imagenet_training_data.yaml` - ImageNet ILSVRC-2012 (85 validation errors, similar pattern)
- `examples/danish_property_tax_reform.yaml` - Policy domain (ORP-Full baseline)

**Sprint Documentation:**
- `docs/sprints/sprint-1.7.3.1.md` - Detailed 7-day plan for LAION-5B
- `docs/sprints/sprint-1.7.3-EXPANSION-PLAN.md` - Master plan for 4 AI examples + consolidation
- `docs/sprints/SPRINT_1.7.3_COMPLETE_PLAN_SUMMARY.md` - Quick reference

---

## Next Steps

**For Sprint 1.7.3.1 (LAION-5B):** ✅ COMPLETE
- ✅ Research (823 lines research_notes.md)
- ✅ Layer 1 - Data Provenance (375 lines)
- ✅ Layer 2 - Consequence Simulation (410 lines)
- ✅ Layer 3 - Empathy Mapping (510 lines)
- ✅ Layer 4 - Accountability Ledger (530 lines)
- ✅ Layer 5 - Fork Registry (337 lines)
- ✅ Validation (88 errors documented)
- ✅ Documentation (this README)

**For Sprint 1.7.3.2 (Common Crawl):** ⏳ NEXT (7 days, 2026-04-08 to 2026-04-15)
- Focus: Living datasets, linguistic extinction, petabyte scale
- Expected discoveries: Temporal evolution, existential harm, scale-appropriate provenance
- Expected errors: 40-60 new schema issues

**For Sprint 1.7.3.3 (GitHub Copilot):** ⏳ (7 days, 2026-04-22 to 2026-04-29)
- Focus: Code modality, license compliance, ecosystem harm
- Expected discoveries: Legal dimensions, economic fairness
- Expected errors: 20-40 new schema issues

**For Sprint 1.7.3.4 (Schema Consolidation):** ⏳ (4 days, 2026-04-29 to 2026-05-03)
- Analyze 175-235 errors across 4 examples
- Design ORP v0.2 with flexible schema (`additionalProperties: true`)
- Update validator, API, all examples
- Result: <5 errors per document, empirically-validated schema

---

**Document Owner:** Asbjørn Ras
**Last Updated:** 2026-04-07
**License:** CC-BY 4.0 (documentation), content may reference copyrighted sources under fair use
