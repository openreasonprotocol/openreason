# Sprint 1.7.3.1: LAION-5B Training Data Example (ORP-Full)

**Version:** `sprint-1.7.3.1`
**Parent Sprint:** `sprint-1.7.3` (Foundation for Expansion - Worked Examples)
**Status:** Not Started
**Start Date:** 2026-04-08 (after ImageNet completion)
**Target End Date:** 2026-04-15 (7 days)

**Code Target Version:** `v0.6.1`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Create a rigorous ORP-Full document for the LAION-5B dataset (5 billion image-text pairs, 2022), demonstrating that ORP applies to contemporary large-scale web-scraped multimodal datasets and surfacing critical safety issues (CSAM, medical imagery, non-consensual intimate images) that existing dataset documentation standards do not adequately address.

---

## Strategic Importance

This is **critical stress-test** for ORP:
- **Most controversial dataset**: CSAM, medical privacy violations, revenge porn
- **Most recent** (2022): Proves ORP relevant for current AI, not just historical
- **Largest scale** (5 billion pairs): Tests ORP at extreme scale
- **Directly feeds Stable Diffusion**: Billions of generated images daily
- **Worst-case absent nodes**: Children (CSAM victims), medical patients, intimate image victims
- **Tests ORP's safety dimension**: ImageNet = dignity/bias, LAION = safety/legality

---

## Why LAION-5B Is Different from ImageNet

### Scale
- ImageNet: 1.2M images (curated)
- LAION-5B: 5 billion image-text pairs (uncurated)

### Methodology
- ImageNet: Targeted collection (WordNet categories) + AMT annotation
- LAION: Broad web scraping (Common Crawl) + CLIP filtering (automated)

### Absent Nodes
- ImageNet: AMT workers (labor), depicted individuals (privacy)
- LAION: **Children** (CSAM victims - cannot consent), **medical patients** (HIPAA), **intimate image victims** (revenge porn)

### Harm Severity
- ImageNet: Dignity harm (offensive labels), bias (demographic)
- LAION: **Safety harm** (CSAM distribution), **legal violations** (medical privacy), **criminal content** (revenge porn)

### ORP Challenge
Can Layer 3 (Empathy Mapping) distinguish between:
- Dignity harm (offensive label) vs
- Safety harm (child exploitation) vs
- Legal harm (HIPAA violation)

**Expected discovery**: ORP needs **harm severity taxonomy**

---

## Scope

### In Scope
- **ORP-Full** (all 5 layers) for LAION-5B dataset
- Focus on **dataset constitution** (how LAION-5B was built, 2022)
- Use existing research (Stanford Internet Observatory, LAION team disclosures, researchers)
- Real data: Documented CSAM findings, medical imagery, known issues
- Demonstrates ORP's application to **safety-critical absent nodes**

### Dataset Choice: LAION-5B
**Full name:** Large-scale Artificial Intelligence Open Network - 5 Billion
**Released:** March 2022 (LAION-5B), prior versions LAION-400M (2021)
**Purpose:** Open-source alternative to proprietary datasets (Google JFT-300M, etc.)
**Impact:** Training data for Stable Diffusion, DALL-E clones, multimodal models

**Why LAION-5B:**
- Most influential open training dataset for generative AI (2022-present)
- Well-documented safety issues (Stanford report, LAION responses)
- Demonstrates **constitutive decisions → safety failures** causation
- Tests ORP on worst-case scenario (illegal content in training data)
- Public, citeable, highly controversial

**Scope limitation:**
- LAION-5B (5 billion pairs), not LAION-400M or later versions
- March 2022 release, before CSAM takedowns (September 2023)
- Focus on dataset decisions, not models trained on it (Stable Diffusion = model governance)

### Explicitly Out of Scope
- Stable Diffusion model (that's model governance, not data governance)
- Generated images from models (downstream use, not dataset constitution)
- LAION-Aesthetics, LAION-COCO subsets (derivatives, could be L5 forks later)
- New primary research (use existing published findings)
- Verification of CSAM claims (trust Stanford Internet Observatory research)

---

## Key Research Questions

### For Layer 1 (Data Provenance):
1. Who funded LAION-5B? (Open-source, but who provided compute/resources?)
2. What was collection methodology? (Common Crawl → CLIP filtering)
3. What exclusion criteria were applied? (NSFW filtering, but how effective?)
4. What was **not** filtered? (CSAM, medical imagery, revenge porn - why?)
5. Who attested to data quality? (LAION team, but what validation process?)

### For Layer 2 (Consequence Simulation):
1. If CSAM filtering had been priority in 2022, what would it cost? (Compute, delay)
2. What are downstream consequences of CSAM in training data? (Model memorization, legal liability)
3. Counterfactual: LAION-5B with PhotoDNA/CSAI filtering pre-publication?

### For Layer 3 (Empathy Mapping):
1. **Children depicted in CSAM**: How do we document as absent nodes? (Cannot consent, legal protection)
2. **Medical patients**: Scraped medical imagery (HIPAA violations) - who are they?
3. **Intimate image victims**: Revenge porn scraped - how many affected?
4. **Harm severity**: How do we distinguish CSAM (criminal) from privacy (ethical)?

### For Layer 4 (Accountability Ledger):
1. Who decided not to pre-filter CSAM? (LAION team, 2021-2022)
2. What alternatives were considered? (PhotoDNA, CSAI Match, manual review)
3. Why rejected? (Cost, compute, "let community filter later")
4. Who decided alt-text quality threshold? (CLIP similarity score)

### For Layer 5 (Fork Registry):
1. Post-CSAM-discovery actions (September 2023): Is this a "fork" or "cleaning"?
2. LAION-COCO, LAION-Aesthetics: Filtered subsets as forks?
3. Potential fork: LAION-Safe (pre-filtered for CSAM, medical, NCII)?

---

## Tasks

### Task 1: Research LAION-5B Constitution History
**Owner:** Asbjørn
**Estimate:** 8 hours (more complex than ImageNet due to safety issues)
**Priority:** Critical

**Description:**
Gather primary and secondary sources documenting how LAION-5B was constituted, with focus on safety decisions.

**Acceptance Criteria:**
- [ ] Read/review key sources:
  - Schuhmann et al. (2022): "LAION-5B: An open large-scale dataset" (original paper)
  - Stanford Internet Observatory (2023): "CSAM in LAION-5B" report
  - LAION team responses (blog posts, GitHub issues re: CSAM)
  - Thiel et al. (2023): Research on LAION-5B content issues
  - News coverage (Washington Post, TechCrunch re: Stable Diffusion/LAION)
- [ ] Document key facts:
  - Funding sources (if any - LAION is non-profit)
  - Dataset scope decisions (why 5 billion? Why Common Crawl source?)
  - Collection methodology (Common Crawl → image URLs → CLIP filtering)
  - CLIP threshold decisions (similarity score for image-text pairs)
  - Exclusion criteria (NSFW filtering methodology)
  - What was NOT filtered (CSAM, medical, NCII - why not?)
  - Known limitations (documented by creators)
  - CSAM discovery timeline (when found, how many, what response)
  - Medical imagery findings (who documented, scale)
  - Legal responses (takedown requests, liability)
- [ ] Create research notes: `examples/laion5b/research_notes.md`

**Output:** Research notes with citations for all claims (especially safety-critical claims)

**Key sources to locate:**
- Schuhmann, C., Beaumont, R., Vencu, R., et al. (2022). LAION-5B: An open large-scale dataset for training next generation image-text models. NeurIPS 2022.
- Stanford Internet Observatory (2023). CSAM in LAION dataset report.
- LAION GitHub issues #1 and related discussions
- Washington Post coverage (2023) on Stable Diffusion training data

---

### Task 2: Draft Layer 1 - Data Provenance
**Owner:** Asbjørn
**Estimate:** 8 hours
**Priority:** Critical

**Description:**
Document the constitutive conditions of LAION-5B's creation, with emphasis on safety exclusions.

**Acceptance Criteria:**

**L1.1: Dataset Overview**
- [ ] Dataset ID: `laion-5b-2022` or similar
- [ ] Name: LAION-5B (Large-scale Artificial Intelligence Open Network)
- [ ] Description: 5 billion image-text pairs scraped from web via Common Crawl
- [ ] Version: March 2022 release (pre-CSAM-takedown September 2023)
- [ ] Access: Open (URLs provided, not images themselves - federated structure)

**L1.2: Provenance Details**
- [ ] **Source:** Common Crawl web scraping (2014-2022 archives)
- [ ] **Funding:** Non-profit LAION, compute donations (Stability AI, others)
- [ ] **Collection methodology:**
  - Common Crawl HTML → extract image URLs + alt text
  - CLIP filtering (OpenAI CLIP model) → similarity score threshold
  - Only image URLs stored (not images - federated dataset)
  - No human annotation (fully automated)
- [ ] **Collection period:** 2021-2022 (processing Common Crawl archives)
- [ ] **Geographic scope:** Global web scraping (but Western-biased, like ImageNet)
- [ ] **Creators:** Christoph Schuhmann, Ross Wightman, Richard Vencu, et al. (LAION team)

**L1.3: Inclusion/Exclusion Criteria** (the critical section)
- [ ] **Documented inclusions:**
  - Image URL accessible via Common Crawl
  - Alt text exists for image
  - CLIP similarity score above threshold (image matches text)
  - English, non-English subsets (multi-lingual)
- [ ] **Documented exclusions:**
  - NSFW content filtered using automated classifier
  - Broken links excluded
  - Images without alt text excluded
  - CLIP score below threshold excluded
- [ ] **CRITICAL UNDOCUMENTED/INADEQUATE EXCLUSIONS:**
  - **CSAM (Child Sexual Abuse Material):** NOT filtered pre-publication
    - Stanford report: 3,226+ known CSAM images in LAION-5B (verified against NCMEC hash database)
    - Likely thousands more undetected (hash database incomplete)
    - Reason not filtered: "Too expensive, too slow, trusted NSFW filter"
  - **Medical imagery:** NOT filtered for HIPAA compliance
    - Private medical photos scraped (patients' faces visible)
    - X-rays, CT scans, surgical photos from hospital leaks
    - No mechanism to identify medical vs non-medical images
  - **Non-consensual intimate images (NCII):** NOT filtered
    - "Revenge porn" scraped from web
    - Intimate images shared without consent
    - No victim notification or removal mechanism (until September 2023)
  - **Copyrighted images:** NOT filtered
    - Getty Images watermarks visible in dataset
    - Artist portfolios scraped wholesale
    - No copyright clearance (unlike ImageNet which attempted filtering)

**L1.4: Cleaning Decisions**
- [ ] NSFW filtering (automated classifier) - threshold chosen
- [ ] CLIP similarity threshold (precision vs recall trade-off)
- [ ] Deduplication (URL-based, not image-based)
- [ ] Post-publication CSAM removal (September 2023, after Stanford report)

**L1.5: Known Limitations** (cite creator acknowledgments + critics)
- [ ] **No CSAM filtering** (acknowledged only after discovery)
- [ ] **NSFW filter inadequate** (pornography passed through, CSAM not caught)
- [ ] **No human review** (fully automated → safety risks)
- [ ] **URL-only storage** (can't remove images, only URLs - images cached elsewhere)
- [ ] **Western bias** (like ImageNet - Common Crawl English-heavy)
- [ ] **Alt text quality variable** (scraped from web, often inaccurate/absent)

**L1.6: Synthetic Elements**
- [ ] Present: false (real images scraped from web, though may include AI-generated images if on web)

**L1.7: Access**
- [ ] Public: true (URLs freely available)
- [ ] License: Creative Commons (various - scraped images have original licenses)
- [ ] Structure: **Federated** (LAION provides URLs, users download images)
  - Implication: LAION can remove URLs but not cached images

**L1.8: Attestation**
- [ ] Attested by: [Your name] (analyst, not creator)
- [ ] Date: 2026-04-XX
- [ ] Statement: "Provenance reconstructed from published sources [citations]. Safety claims (CSAM, medical imagery) based on Stanford Internet Observatory and other third-party research. LAION team's responses documented."

**Output:** Layer 1 section in `examples/laion5b_training_data.yaml`

---

### Task 3: Draft Layer 2 - Consequence Simulation
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Model how LAION-5B's constitutive decisions (no CSAM filtering, no medical filtering) affect downstream model safety.

**Acceptance Criteria:**

**L2.1: Affected Population**
- [ ] **Primary:** AI researchers/companies training generative models (Stable Diffusion, etc.)
- [ ] **Secondary:** Billions of users of generative AI tools
- [ ] **Tertiary - CRITICAL ABSENT NODES:**
  - **Children depicted in CSAM** (cannot consent, crime victims)
  - **Medical patients** (HIPAA violations, private health data)
  - **Intimate image victims** (revenge porn, non-consensual distribution)

**L2.2: Variables**
- [ ] **Independent variables:**
  - CSAM filtering (yes/no, thoroughness level)
  - Medical privacy filtering (yes/no)
  - NCII filtering (yes/no)
  - Human review (yes/no, percentage sampled)
  - Federated vs hosted (URL-only vs image storage)
- [ ] **Dependent variables:**
  - CSAM in training data (count, estimated)
  - Model memorization of CSAM (likelihood)
  - Legal liability (CSAM distribution, HIPAA)
  - Victim harm (re-victimization through AI generation)

**L2.3: Scenarios**

**Scenario A: Current Constitution (as built - March 2022)**
- [ ] No CSAM filtering → 3,226+ known CSAM images
- [ ] No medical filtering → thousands of medical privacy violations
- [ ] No NCII filtering → unknown quantity of revenge porn
- [ ] Federated structure → can remove URLs but not cached images
- [ ] Outcome: Legal liability, victim harm, model memorization risks

**Scenario B: Alternative - Pre-Publication CSAM Filtering**
- [ ] If: PhotoDNA/CSAI Match database used before release
- [ ] If: Human review of flagged content (estimated 0.1% of dataset)
- [ ] Expected outcome: 99%+ CSAM removed, legal liability avoided
- [ ] Cost: ~2-3 months delay, compute cost (estimated $50-100K)
- [ ] Uncertainty: Some CSAM may evade detection (hash databases incomplete)

**Scenario C: Alternative - Human Review Sample**
- [ ] If: 0.1% random sample (5 million pairs) reviewed by humans
- [ ] If: Extrapolate findings, filter similar content algorithmically
- [ ] Expected outcome: Major safety issues identified pre-publication
- [ ] Cost: ~100 reviewers × 2 months = ~$400K
- [ ] Benefit: Catch issues NSFW filter missed (CSAM, medical, NCII)

**Scenario D: Alternative - Hosted (Not Federated)**
- [ ] If: LAION hosted images, not just URLs
- [ ] Then: Could remove images after publication
- [ ] But: Storage cost prohibitive (~100+ petabytes)
- [ ] And: Creates single point of liability/failure

**L2.4: Uncertainties**
- [ ] Exact CSAM count (Stanford found 3,226 via hash matching, likely more exist)
- [ ] Model memorization rate (how often do models reproduce training CSAM?)
- [ ] Legal precedent (is LAION liable? Users of Stable Diffusion?)
- [ ] Victim identification (most CSAM victims unknown, cannot notify)

**Output:** Layer 2 section demonstrating consequence modeling for safety-critical decisions

---

### Task 4: Draft Layer 3 - Empathy Mapping
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Identify affected stakeholders, with emphasis on **worst-case absent nodes** (child CSAM victims, medical patients, intimate image victims).

**Acceptance Criteria:**

**L3.1: Stakeholder Groups**

**Group 1: Dataset Creators** (LAION team)
- [ ] Interest: Open-source AI, democratize access (vs proprietary datasets)
- [ ] Impact: Positive (enabled Stable Diffusion, open ecosystem) + Negative (legal liability post-CSAM discovery)
- [ ] Representation: Full (they made all decisions)

**Group 2: AI Researchers/Companies** (Stable Diffusion, etc.)
- [ ] Interest: Training data for generative models
- [ ] Impact: Positive (open dataset enabled innovation) + Negative (legal/reputational risk if trained on CSAM)
- [ ] Representation: High (active community, feedback loops)

**Group 3: Generative AI Users** (billions)
- [ ] Interest: Create images via AI tools
- [ ] Impact: Positive (creative tools) + Negative (may unknowingly use models trained on CSAM)
- [ ] Representation: None (downstream users, no voice in dataset governance)

**Group 4: CHILDREN DEPICTED IN CSAM** (CRITICAL ABSENT NODE)
- [ ] Interest: **Protection from exploitation, removal of CSAM**
- [ ] Impact: **SEVERE HARM** - re-victimization through dataset distribution
- [ ] Representation: **NONE** - cannot consent (minors), crime victims
- [ ] Absent node: **MOST CRITICAL** - child safety trumps all other concerns
- [ ] Legal status: CSAM possession/distribution is **federal crime** (18 U.S.C. § 2252)

**Group 5: Medical Patients** (HIPAA-protected imagery)
- [ ] Interest: Medical privacy, HIPAA compliance
- [ ] Impact: Negative - private medical photos exposed without consent
- [ ] Representation: None (no consent process, no notification)
- [ ] Absent node: Medical imagery scraped from hospital breaches, patient portals

**Group 6: Intimate Image Victims** (revenge porn, NCII)
- [ ] Interest: Privacy, consent, removal of non-consensual images
- [ ] Impact: Negative - intimate images distributed without consent
- [ ] Representation: None (no consent, no removal mechanism until 2023)
- [ ] Absent node: "Revenge porn" victims had no voice in dataset governance

**Group 7: Artists/Photographers** (copyright holders)
- [ ] Interest: Copyright protection, attribution, compensation
- [ ] Impact: Negative - portfolios scraped, models trained on copyrighted work
- [ ] Representation: None (no consent, no licensing)
- [ ] Absent node: Getty Images lawsuit (February 2023) - artists had no voice

**Group 8: Web Users Generally** (depicted in scraped images)
- [ ] Interest: Privacy, consent for AI training use
- [ ] Impact: Variable - many unaware their photos are in LAION-5B
- [ ] Representation: None (no consent process, no opt-out until 2023)

**L3.2: Minority Stakeholder Analysis - HARM SEVERITY TIERS**

**CRITICAL FINDING**: Not all absent nodes equal - **harm severity matters**

**Tier 1 - Criminal/Safety Harm:**
- [ ] **CSAM victims (children)**: Federal crime, re-victimization, cannot consent
- [ ] **Requires immediate removal**, legal reporting (NCMEC), criminal investigation

**Tier 2 - Legal Harm:**
- [ ] **Medical patients**: HIPAA violations, civil liability, privacy law
- [ ] **Requires removal**, legal compliance, potential damages

**Tier 3 - Ethical Harm:**
- [ ] **NCII victims**: Privacy violations, dignity harm, consent issues
- [ ] **Requires removal**, victim support, platform policies

**Tier 4 - Economic Harm:**
- [ ] **Copyright holders**: Financial damages, attribution, licensing
- [ ] **Requires licensing**, compensation negotiation, attribution

**ORP DISCOVERY**: Current schema treats all absent nodes equally → **inadequate for safety-critical issues**

**Proposed**: Layer 3 needs **"harm_severity" field** with tiers (criminal > legal > ethical > economic)

**L3.3: Net Welfare Assessment**
- [ ] LAION-5B enabled open-source generative AI (massive positive)
- [ ] BUT: **Child safety harm cannot be offset by innovation benefits**
- [ ] Legal principle: Children's rights absolute, not subject to utilitarian trade-offs
- [ ] Conclusion: LAION-5B constitutive decisions (no CSAM filtering) **ethically and legally unacceptable** regardless of innovation value

**Output:** Layer 3 section with 8 stakeholder groups, **harm severity taxonomy**, net welfare assessment

---

### Task 5: Draft Layer 4 - Accountability Ledger
**Owner:** Asbjørn
**Estimate:** 5 hours
**Priority:** High

**Description:**
Document major constitutive decisions made during LAION-5B creation, **with focus on safety decisions**.

**Acceptance Criteria:**

**Decision 1: Use Common Crawl as Source**
- [ ] Decision: Scrape Common Crawl (8 years of archives, 2014-2022)
- [ ] Decision maker: LAION team (Schuhmann, Beaumont, et al.)
- [ ] Date: ~2021
- [ ] Rationale: Largest available web corpus, open-source, well-documented
- [ ] Alternative considered: Curated sources (Flickr, Instagram) - rejected (smaller scale, API restrictions)
- [ ] Consequence: Inherited Common Crawl's content (including illegal material)

**Decision 2: Automated CLIP Filtering (No Human Review)**
- [ ] Decision: Use CLIP similarity score, no human annotation
- [ ] Decision maker: LAION team
- [ ] Date: 2021-2022
- [ ] Rationale: Scalability (5 billion pairs infeasible to manually review), cost-effectiveness
- [ ] Alternative considered: Human review sample (rejected: too expensive)
- [ ] Consequence: Safety issues not caught (CSAM, medical, NCII passed NSFW filter)

**Decision 3: NSFW Filtering Methodology**
- [ ] Decision: Use automated NSFW classifier (threshold chosen)
- [ ] Decision maker: LAION team
- [ ] Date: 2021-2022
- [ ] Rationale: Remove pornography, sexual content
- [ ] Parameters: [specific NSFW classifier and threshold from paper]
- [ ] **CRITICAL GAP**: NSFW filter designed for adult content, NOT CSAM detection
- [ ] Consequence: CSAM not filtered (visually similar to adult content but legally distinct)

**Decision 4: NO CSAM Pre-Filtering**
- [ ] Decision: Do not use PhotoDNA/CSAI Match database before publication
- [ ] Decision maker: LAION team
- [ ] Date: 2021-2022
- [ ] Rationale: [UNKNOWN - not documented in paper, no public statement]
- [ ] Possible reasons (speculative): Compute cost, database access, "trusted NSFW filter"
- [ ] Alternative considered: [UNKNOWN - no evidence alternatives were considered]
- [ ] **Consequence: 3,226+ known CSAM images in dataset (Stanford report)**
- [ ] **Legal consequence**: Potential CSAM distribution charges (federal crime)
- [ ] **Victim consequence**: Re-victimization of child abuse survivors

**Decision 5: Federated Structure (URLs Only)**
- [ ] Decision: Store image URLs, not images themselves
- [ ] Decision maker: LAION team
- [ ] Date: ~2021
- [ ] Rationale: Storage cost (5B images = ~100PB), legal liability (hosting vs linking)
- [ ] Alternative: Host images directly (rejected: cost prohibitive, liability)
- [ ] Consequence: Can remove URLs but not cached images (users download before removal)

**Decision 6: Open Release (No Registration)**
- [ ] Decision: Freely available, no restrictions
- [ ] Decision maker: LAION team
- [ ] Date: March 2022
- [ ] Rationale: Maximize open-source impact, democratize AI
- [ ] Alternative: Gated access (registration, review) - rejected (anti-open-source)
- [ ] Consequence: Cannot track who downloaded, cannot notify of CSAM removal

**Decision 7: Post-Discovery CSAM Removal** (September 2023)
- [ ] Decision: Remove CSAM URLs after Stanford report
- [ ] Decision maker: LAION team (responding to Stanford findings)
- [ ] Date: September 2023 (18 months after release)
- [ ] Rationale: Legal liability, ethical imperative
- [ ] But: URLs removed, images cached by thousands of users
- [ ] Cannot retrieve distributed data

**Output:** Layer 4 section with 7 major decisions, **Decision 4 flagged as critical safety failure**

---

### Task 6: Draft Layer 5 - Fork Registry
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Medium

**Description:**
Document LAION-5B variants and potential safety-focused forks.

**Acceptance Criteria:**

**Fork 1: LAION-Aesthetics** (Schuhmann et al., 2022)
- [ ] Fork type: Quality-filtered subset
- [ ] Rationale: Higher aesthetic quality (CLIP+aesthetic predictor)
- [ ] Changes: ~600M pairs (subset of 5B), higher aesthetic scores
- [ ] Status: Published, used for Stable Diffusion training
- [ ] Relationship: Filtered subset (same source, quality criteria)
- [ ] **Safety note**: Still contains CSAM (no additional safety filtering)

**Fork 2: LAION-COCO** (LAION team)
- [ ] Fork type: COCO-compatible subset
- [ ] Rationale: Compatibility with COCO benchmarks
- [ ] Changes: 600M pairs annotated with COCO categories
- [ ] Relationship: Filtered subset with additional annotations
- [ ] **Safety note**: Unknown if safer than parent dataset

**Fork 3: LAION-5B Post-CSAM-Removal** (September 2023)
- [ ] Fork type: **Safety remediation**
- [ ] Rationale: Remove known CSAM URLs after Stanford report
- [ ] Changes: ~3,226+ URLs removed (0.00006% of dataset)
- [ ] Status: Current version available for download
- [ ] Relationship: **Revision fork** (addressing L1 critical gap)
- [ ] **Limitation**: URLs removed but images cached by users (can't retrieve)

**Potential Forks (not yet created):**

**Potential Fork: LAION-Safe**
- [ ] Proposed: Pre-filtered for CSAM, medical imagery, NCII
- [ ] Methodology: PhotoDNA + CSAI Match + medical image classifier + human review sample
- [ ] Expected outcome: 99%+ harmful content removed, legal compliance
- [ ] Cost: ~$500K (compute + human review), 3-6 months
- [ ] Benefit: Safe for training, legal liability minimized, ethical foundation

**Potential Fork: LAION-Consented**
- [ ] Proposed: Only images with explicit creator consent for AI training
- [ ] Methodology: Partner with stock photo sites, artist cooperatives, Creative Commons explicit-AI-training licenses
- [ ] Expected outcome: ~100M pairs (vs 5B), but fully consented
- [ ] Trade-off: Dramatic scale reduction vs ethical compliance

**Potential Fork: LAION-Curated**
- [ ] Proposed: Human-reviewed sample (1% = 50M pairs) → train classifier → filter full dataset
- [ ] Methodology: Diverse review team flags issues → algorithmic filtering
- [ ] Expected outcome: Safety issues caught, scalable process
- [ ] Cost: ~$1M (100 reviewers × 6 months), feasible for large organizations

**Output:** Layer 5 section with 3 existing forks + 3 potential safety-focused forks

---

### Task 7: Validate and Refine
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Ensure LAION-5B example meets quality standards and documents schema discoveries.

**Acceptance Criteria:**
- [ ] Run: `orp validate examples/laion5b_training_data.yaml` (expect errors - document them)
- [ ] Document new schema issues discovered (beyond ImageNet's 85)
- [ ] **Expected discoveries**:
  - Harm severity taxonomy needed (L3)
  - Legal compliance fields needed (L1, L4)
  - Vulnerable populations flagging (L3)
  - Federated dataset structure (L1 - URLs vs hosted)
- [ ] All citations verified (papers exist, quotes accurate)
- [ ] Tone check: Descriptive not prescriptive, focus on constitutive decisions not blaming
- [ ] Sensitivity check: CSAM discussed appropriately (clinical, not sensationalized)
- [ ] Legal disclaimer: Document acknowledges CSAM as crime, cites legal framework
- [ ] Cross-reference: Claims align with academic paper arguments

**Output:** Validated document + schema discovery report

---

### Task 8: Write Accompanying Documentation
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Medium

**Description:**
Create README explaining LAION-5B example and methodology.

**Acceptance Criteria:**
- [ ] Create: `examples/laion5b/README.md`
- [ ] Explains:
  - Why LAION-5B chosen (most controversial, tests ORP on safety)
  - What this demonstrates (constitutive decisions → safety failures)
  - Methodology: Reconstructed from Stanford report + LAION papers
  - **Harm severity taxonomy**: Why CSAM ≠ privacy violation
  - Limitations: Post-hoc analysis, cannot verify all claims
  - Legal context: CSAM as federal crime, HIPAA, copyright
- [ ] Sensitivity statement: Respectful treatment of victim stakeholders
- [ ] Links to Stanford report, LAION papers, legal framework
- [ ] Comparison: How this differs from ImageNet (safety vs bias)

**Output:** `examples/laion5b/README.md`

---

### Task 9: Schema Discovery Documentation
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** High

**Description:**
Document what LAION-5B revealed about ORP schema limitations.

**Acceptance Criteria:**
- [ ] Create: `docs/sprints/sprint-1.7.3.1-schema-discoveries.md`
- [ ] Document new issues found:
  - **Harm severity taxonomy** (criminal > legal > ethical > economic)
  - **Vulnerable populations flag** (children, medical patients, crime victims)
  - **Legal compliance fields** (CSAM, HIPAA, copyright)
  - **Federated dataset structure** (URLs vs hosted - affects L1, L5)
  - **Automated vs human review** (L1 methodology distinction)
- [ ] Compare to ImageNet discoveries (85 errors)
- [ ] Estimate: LAION adds 30-50 new schema issues
- [ ] Recommendations for ORP v0.2

**Output:** Schema discovery report

---

## Success Criteria

### Completion Criteria
- [ ] All 9 tasks completed
- [ ] `examples/laion5b_training_data.yaml` created (ORP-Full)
- [ ] All claims cited to published sources (especially safety claims)
- [ ] Harm severity taxonomy documented
- [ ] Schema discoveries documented

### Quality Criteria
- [ ] As detailed as ImageNet example
- [ ] Demonstrates all 5 ORP layers meaningfully
- [ ] **Shows worst-case absent nodes** (CSAM victims, medical patients)
- [ ] **Harm severity distinction** clear (criminal vs ethical)
- [ ] Tone: Clinical, descriptive, appropriate sensitivity
- [ ] Citations verifiable (Stanford report, LAION papers, legal statutes)

### Impact Criteria
- [ ] Demonstrates ORP handles safety-critical issues
- [ ] Reveals ORP schema gaps (harm severity, vulnerable populations)
- [ ] Strengthens academic paper (contemporary relevance, safety dimension)
- [ ] Tests ORP at extreme scale (5 billion pairs)

---

## Dependencies

**Depends on:**
- Sprint 1.7.3 (ImageNet complete - provides template)
- Stanford Internet Observatory report (foundational research)
- LAION team public statements (constitutive decisions)

**Enables:**
- Sprint 1.7.3.2 (Common Crawl - tests living dataset)
- Sprint 1.7.3.3 (GitHub Copilot - tests code modality)
- Sprint 1.7.3.4 (Schema revision - consolidates discoveries)

---

## Risks and Mitigations

### Risk 1: Sensitivity to CSAM Topic
**Mitigation:** Clinical language, cite legal framework, focus on constitutive decisions not sensationalism. Consult legal/ethical guidelines for discussing CSAM in research context.

### Risk 2: LAION Team Perception
**Mitigation:** Emphasize system-level analysis, not individual blame. Acknowledge 2022 standards, open-source mission. Frame as "what ORP would reveal prospectively."

### Risk 3: Incomplete Public Information
**Mitigation:** Document uncertainties. LAION's internal deliberations not public - acknowledge reconstruction limitations. Use Stanford report as authoritative source for CSAM findings.

### Risk 4: Legal Liability Questions
**Mitigation:** Include legal disclaimer. Cite 18 U.S.C. § 2252 (CSAM law), HIPAA, copyright law. Clarify ORP document is analysis, not legal judgment.

---

## Retrospective Notes

(To be completed at sprint end)

### What Went Well
- [TBD]

### What Didn't Go Well
- [TBD]

### Schema Discoveries
- [TBD - document new ORP limitations discovered]

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-08
**Target Completion:** 2026-04-15
**Estimated Effort:** 45 hours over 7 days
