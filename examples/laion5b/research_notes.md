# LAION-5B Training Data - Research Notes

**Purpose:** Background research for ORP-Full document on LAION-5B dataset constitution
**Date:** 2026-04-08
**Researcher:** Asbjørn Ras

---

## Primary Sources

### 1. Schuhmann et al. (2022) - Original LAION-5B Paper

**Citation:** Schuhmann, C., Beaumont, R., Vencu, R., Gordon, C., Wightman, R., Cherti, M., Coombes, T., Katta, A., Mullis, C., Wortsman, M., Schramowski, P., Kundurthy, S., Crowson, K., Schmidt, L., Kaczmarczyk, R., & Jitsev, J. (2022). LAION-5B: An open large-scale dataset for training next generation image-text models. *Proceedings of the 36th Conference on Neural Information Processing Systems (NeurIPS 2022)*. arXiv:2210.08402

**arXiv:** https://arxiv.org/abs/2210.08402
**Published:** October 16, 2022

**Key Information:**
- **Dataset scale:** 5.85 billion CLIP-filtered image-text pairs
- **Language distribution:**
  - 2.32 billion English language pairs
  - 2.26 billion multilingual examples
  - 1.27 billion non-language-specific examples
- **Source:** Common Crawl web archive
- **Collection period:** Data scraped from Common Crawl archives (2014-2022)
- **Creators:** LAION (Large-scale Artificial Intelligence Open Network) - German non-profit
- **Purpose:** Open-source alternative to proprietary datasets (Google JFT-300M, etc.)

### 2. Stanford Internet Observatory (2023) - CSAM Discovery

**Citation:** Thiel, D. (2023). Identifying and Eliminating CSAM in Generative ML Training Data and Models. *Stanford Internet Observatory*. Stanford Digital Repository. https://purl.stanford.edu/kh752sm9123

**Report Release:** December 20, 2023

**Key Findings:**
- **CSAM discovered:** 3,226 suspected instances of child sexual abuse material (CSAM)
- **Externally validated:** 1,008 images confirmed as CSAM by third-party validation
- **Validation methods:**
  - National Center for Missing and Exploited Children (NCMEC) guidance
  - Canadian Centre for Child Protection (C3P) validation
  - Microsoft PhotoDNA tool matching
- **Impact:** LAION took dataset offline December 19, 2023 (immediately after report)

**Report Recommendations:**
- Datasets with CSAM should be restricted to "research settings only"
- Only "more curated and well-sourced datasets" should be used for publicly distributed models
- Downstream models (Stable Diffusion, etc.) could generate new realistic child abuse content

### 3. LAION Response & Re-LAION-5B (2024)

**Source:** LAION.ai blog post - "Releasing Re-LAION-5B: transparent iteration on LAION-5B with additional safety fixes"
**Date:** August 30, 2024

**Response Actions:**
- Dataset taken offline December 19, 2023 (within hours of Stanford report)
- Partnership with safety organizations:
  - Internet Watch Foundation (IWF) - UK
  - Canadian Centre for Child Protection (C3P)
  - Stanford Internet Observatory (continued collaboration)
- **Re-LAION-5B released:** August 2024 with cleaned URLs
  - 2,236 links removed (includes Stanford's 1,008 + additional 1,228 found by partners)
  - First web-scale dataset "thoroughly cleaned of known links to suspected CSAM"
  - Caveat: "Known links" - hash matching not comprehensive (new/unreported CSAM may remain)

---

## Dataset Constitution History

### Collection Methodology (2021-2022)

**Source pipeline:**
1. **Common Crawl extraction:**
   - Start with Common Crawl HTML archives (2014-2022)
   - Extract image URLs + alt text from web pages
   - Result: ~50+ billion candidate image-text pairs

2. **Initial filtering:**
   - Drop samples: alt-text <5 characters OR image size <5 KB
   - URL-based deduplication (bloom filter)
   - Result: Still billions of candidates

3. **CLIP similarity filtering:**
   - English: ViT B/32 CLIP model, threshold 0.28
   - Multilingual: mCLIP model, threshold 0.26
   - Cosine similarity between image embedding and text embedding
   - Removes ~90% of samples (poor image-text alignment)
   - Result: 5.85 billion pairs passing threshold

4. **NSFW detection (NOT filtering):**
   - CLIP-based NSFW classifier assigns: {"UNLIKELY", "UNSURE", "NSFW"}
   - Continuous score 0-1 provided
   - **Critical:** NSFW tag provided but NOT used for exclusion
   - Users can filter based on NSFW score, but LAION includes all
   - LAION-400M (earlier version) attempted kids/teens category filtering via CLIP cosine similarity with category texts
   - LAION-5B: No explicit CSAM filtering

5. **Additional metadata:**
   - Watermark detection (CLIP-based)
   - Image dimensions, file format
   - Language detection for text

### Funding & Infrastructure

**LAION organization:**
- German non-profit (Large-scale Artificial Intelligence Open Network)
- Founded by Christoph Schuhmann and collaborators
- Mission: Democratize AI by providing open-source datasets

**Compute resources:**
- Donations from:
  - Stability AI (major contributor - compute + funding)
  - Other tech companies (names not fully disclosed)
- Processing 50+ billion candidates → 5.85 billion pairs requires massive compute
- Estimated cost: Likely $1-5M+ (infrastructure, storage, CLIP inference)

**Storage & distribution:**
- Hosted on LAION servers + Hugging Face
- **Federated structure:** Dataset provides URLs, not images
  - Users download images from original sources
  - LAION doesn't host images (reduces liability, storage cost)
  - Consequence: Can remove URLs but not cached/downloaded images

---

## Exclusion Criteria Analysis

### Documented Exclusions

**From Schuhmann et al. (2022) paper:**
1. **CLIP similarity threshold:**
   - Pairs below 0.28 (English) or 0.26 (multilingual) excluded
   - Rationale: Poor image-text alignment (text doesn't describe image)
   - Result: ~90% of candidates excluded (~45 billion pairs dropped)

2. **Minimum content requirements:**
   - Alt text <5 characters → excluded
   - Image size <5 KB → excluded
   - Rationale: Low-quality, unlikely to be meaningful pairs

3. **URL deduplication:**
   - Same URL seen multiple times in Common Crawl → kept once
   - Rationale: Avoid redundancy

4. **NSFW tagging (NOT exclusion):**
   - NSFW classifier run, score provided
   - But: NSFW images NOT excluded from LAION-5B
   - Rationale: Let users decide threshold (some research needs adult content)
   - Result: Pornography, sexually explicit content included

### CRITICAL UNDOCUMENTED/INADEQUATE EXCLUSIONS

**1. NO CSAM Pre-Publication Filtering**

**What was NOT done:**
- No PhotoDNA matching (Microsoft tool for known CSAM)
- No CSAI Match database checking (Canadian C3P tool)
- No NCMEC hash database checking (US National Center for Missing & Exploited Children)
- No human review of flagged content
- No partnership with child safety organizations (until AFTER discovery)

**Why not done (speculative - not documented in paper):**
- **Possible reason 1:** Cost/compute (hash matching adds overhead)
- **Possible reason 2:** False sense of security from NSFW filter ("we filtered adult content")
- **Possible reason 3:** "Let users filter downstream" philosophy
- **Possible reason 4:** Federated structure ("we're just providing URLs, not hosting images")
- **Actual reason:** Not publicly stated by LAION team

**Result:**
- 3,226 CSAM URLs in dataset (Stanford report)
- 1,008 externally validated as confirmed CSAM
- Distributed December 2022 - December 2023 (12+ months)
- Used to train Stable Diffusion, DALL-E clones, other generative models
- Millions of downloads before takedown

**2. NO Medical Privacy Filtering**

**What was NOT done:**
- No HIPAA-sensitive image detection
- No medical image classifier (X-rays, CT scans, surgical photos)
- No patient face detection in medical contexts
- No partnership with healthcare privacy organizations

**Result (not yet comprehensively documented, but known):**
- Private medical images from hospital data breaches scraped
- Patient faces visible in some medical images
- X-rays, CT scans, surgical photos with potentially identifying information
- HIPAA violations (if patients are US-based)
- Scale unknown (no systematic study like Stanford's CSAM report)

**3. NO Non-Consensual Intimate Images (NCII) Filtering**

**What was NOT done:**
- No "revenge porn" detection
- No intimate image consent verification
- No partnership with NCII organizations (Cyber Civil Rights Initiative, etc.)

**Result:**
- Unknown quantity of NCII in dataset
- "Revenge porn" sites scraped (if indexed by Common Crawl)
- Intimate images shared without subject consent
- No victim notification or removal mechanism (until August 2024)
- Scale unknown (no systematic study)

**4. NO Copyright/License Filtering**

**What was NOT done:**
- No Getty Images watermark filtering (despite detectability)
- No Shutterstock, Adobe Stock filtered
- No artist portfolio sites filtered (DeviantArt, ArtStation scraped)
- No licensing metadata checked

**Result:**
- Copyrighted images from professional photographers, artists, stock photo agencies
- Getty Images sued Stability AI (Feb 2023) for copyright infringement via LAION training
- Artists launched class-action lawsuit (Andersen v. Stability AI, 2023)
- No compensation to copyright holders

**5. NO Geographic/Cultural Bias Mitigation**

**Structural bias (like Common Crawl, ImageNet):**
- Common Crawl is Western/English-dominated (80%+ English pages)
- LAION-5B: 2.32B English pairs (40% of dataset)
- Non-Western visual culture under-represented
- Result: Models trained on LAION (Stable Diffusion) exhibit Western bias
  - "Professional attire" → Western business suit
  - "Wedding" → White Western wedding
  - Similar to ImageNet bias pattern

---

## Downstream Impact: Stable Diffusion

### Training Details

**Stable Diffusion (Aug 2022):**
- Trained by Stability AI (later partnered with LAION)
- Training data: Three LAION-5B subsets
  - LAION-2B-en (2 billion English pairs)
  - LAION-high-resolution (subset with high-res images)
  - LAION-Aesthetics v2 5+ (600M pairs, aesthetically filtered)
- Compute: 256 Nvidia A100 GPUs (AWS)
- Training time: 150,000 GPU-hours
- Cost: ~$600,000

**Release:** August 2022 (open-source model)
**Impact:** Most influential open-source text-to-image model (millions of users)

### CSAM Implications

**Timeline:**
- Aug 2022: Stable Diffusion released (trained on LAION subsets)
- Dec 2023: Stanford discovers 3,226 CSAM URLs in LAION-5B
- **Question:** Did Stable Diffusion training include CSAM?
  - Likely YES (subsets drawn from full LAION-5B)
  - Specific CSAM URLs in LAION-2B-en/LAION-Aesthetics unknown (not published)

**Model memorization risk:**
- Diffusion models can memorize training data (documented by researchers)
- If CSAM in training data → model could generate similar images
- Prompt: Generic text → output resembles memorized CSAM
- Legal risk: Generating CSAM is federal crime (even if synthetic/AI-generated)
- Ethical harm: Re-victimization of children depicted in original CSAM

**Stability AI response:**
- No public acknowledgment of CSAM in training data
- Model remains available (not retracted)
- Cannot "untrain" model (removing CSAM from weights infeasible)
- Future versions (Stable Diffusion 3, etc.) could use cleaned Re-LAION-5B

---

## Known Limitations

### Acknowledged by LAION (from paper & blog)

1. **CLIP bias:**
   - CLIP model has biases → propagated to LAION-5B
   - Western/English bias in CLIP training
   - CLIP similarity threshold (0.28) arbitrary choice (affects included pairs)

2. **Alt text quality:**
   - Alt text varies wildly (some descriptive, some useless "image.jpg")
   - Many web pages have poor/missing alt text
   - CLIP filters for alignment, but doesn't guarantee quality

3. **No content moderation:**
   - Explicitly open-source, no editorial control
   - Users responsible for filtering (NSFW scores provided)
   - "Democratization" philosophy → includes all content types

4. **Federated structure limitations:**
   - URLs may break (link rot) over time
   - Original images may be deleted by source sites
   - Cannot remove images already cached by users
   - Distribution control limited (URLs shared, can't revoke)

### Identified by Critics (Stanford, journalists, researchers)

1. **CSAM (Stanford Internet Observatory, Dec 2023):**
   - 3,226 CSAM URLs, 1,008 externally validated
   - No pre-publication CSAM filtering
   - 12+ months of distribution before takedown
   - Hash matching inadequate (only catches known CSAM, not new)

2. **Medical privacy violations (documented but not quantified):**
   - Private medical images scraped
   - HIPAA compliance not considered
   - Patient consent not obtained
   - Scale unknown (no systematic study)

3. **NCII/revenge porn (documented but not quantified):**
   - Non-consensual intimate images included
   - No victim notification
   - No removal mechanism until 2024
   - Scale unknown

4. **Copyright infringement (Getty lawsuit, Feb 2023):**
   - Getty Images, Shutterstock, photographer portfolios scraped
   - No licensing clearance
   - Watermarks present but not filtered
   - Stable Diffusion trained on copyrighted images → generates similar images

5. **Western/English bias:**
   - 40% English (2.32B pairs) despite English ~25% of web
   - Common Crawl bias inherited
   - Non-Western cultures under-represented
   - Same pattern as ImageNet, Common Crawl

---

## Controversy Timeline

### Phase 1: Creation and Release (2021-2022)

**2021:** LAION-400M released (predecessor to LAION-5B)
**March 2022:** LAION-5B announced, data collection finalized
**October 2022:** LAION-5B paper published (NeurIPS 2022)
**August 2022:** Stable Diffusion released (trained on LAION subsets)
**Status:** Celebrated as open-source breakthrough, democratizing AI

### Phase 2: Copyright Controversy (2023)

**February 2023:** Getty Images sues Stability AI for copyright infringement
- Alleges Stable Diffusion trained on Getty images via LAION
- Getty watermarks visible in some generated images
- Seeks damages + injunction

**January 2023:** Artists file class-action lawsuit (Andersen v. Stability AI)
- Artists: Sarah Andersen, Kelly McKernan, Karla Ortiz
- Alleges copyright infringement, right of publicity violations
- Trained on DeviantArt, ArtStation portfolios via LAION

**Community response:** Debate over fair use, transformative use, generative AI copyright

### Phase 3: CSAM Discovery & Takedown (December 2023)

**December 20, 2023:** Stanford Internet Observatory report published
- 3,226 CSAM URLs discovered in LAION-5B
- 1,008 externally validated by C3P, NCMEC guidance

**December 19, 2023:** LAION takes dataset offline
- Immediate response (within hours of Stanford report)
- Dataset removed from LAION servers, Hugging Face
- Public apology, commitment to fix

**Media coverage:**
- CNN, Bloomberg, Axios, The Verge, 404 Media
- "AI trained on child abuse images"
- Calls for regulation, content moderation

### Phase 4: Cleanup & Re-Release (2024)

**December 2023 - August 2024:** LAION partners with safety organizations
- Internet Watch Foundation (IWF)
- Canadian Centre for Child Protection (C3P)
- Stanford Internet Observatory
- Hash matching against CSAM databases
- 2,236 URLs removed (Stanford's 1,008 + additional 1,228)

**August 30, 2024:** Re-LAION-5B released
- "First web-scale dataset thoroughly cleaned of known links to suspected CSAM"
- Caveat: Only "known" CSAM (hash-matched), not comprehensive
- Federated structure unchanged (cached images still exist)

**Ongoing questions:**
- Should LAION-5B be re-released at all? (Critics argue yes/no)
- Is hash matching sufficient? (Only catches known CSAM)
- What about medical privacy, NCII, copyright? (Not addressed in re-release)
- Should models trained on original LAION-5B be retracted? (Stable Diffusion, etc.)

---

## Stakeholder Groups Analysis

### 1. LAION Team (Dataset Creators)
**Individuals:** Christoph Schuhmann (founder), ~16 co-authors on paper
**Interest:** Open-source AI, democratization, research enablement
**Impact:** Mixed
- Positive: Enabled open-source generative AI (Stable Diffusion, etc.)
- Negative: Legal liability (CSAM distribution), reputational damage
**Representation:** Full (they made all decisions)

### 2. Stability AI & Generative AI Companies
**Interest:** Training data for text-to-image models
**Impact:** Positive
- Stable Diffusion trained on LAION-5B subsets ($600K training cost)
- Commercial success (Stability AI valued at $1B+ in 2023)
- Open-source alternative to DALL-E, Midjourney
**Representation:** High (Stability AI major funder/partner with LAION)

### 3. Researchers & AI Community
**Interest:** Open-source datasets for research
**Impact:** Positive
- LAION-5B enabled CLIP research, multimodal models, image generation research
- Thousands of papers cite LAION datasets
**Representation:** High (academic researchers in LAION network)

### 4. Generative AI Users (Millions)
**Interest:** Create images via Stable Diffusion, DALL-E clones
**Impact:** Positive (creative tools) + Negative (unknowingly using models trained on CSAM)
**Representation:** None (downstream users, no voice in dataset decisions)

### 5. CHILDREN DEPICTED IN CSAM (CRITICAL ABSENT NODE - TIER 1 HARM)
**Population:** Unknown (3,226 CSAM URLs, multiple children per image likely)
**Interest:** PROTECTION FROM EXPLOITATION, removal of CSAM, prevention of AI-generated abuse
**Impact:** SEVERE HARM
- Re-victimization through dataset distribution (Dec 2022 - Dec 2023)
- CSAM distributed to millions of users worldwide
- Potential for AI model memorization → generation of similar content
- Legal: CSAM possession/distribution is federal crime (18 U.S.C. § 2252)
**Representation:** NONE
- Cannot consent (minors)
- Crime victims with no voice
- Not notified until Stanford report (if ever - most victims unidentified)
**Absent node:** MOST CRITICAL - child safety is absolute priority, not subject to utilitarian trade-offs

### 6. Medical Patients (HIPAA-Protected Imagery)
**Population:** Unknown (no systematic count, but documented)
**Interest:** Medical privacy, HIPAA compliance, consent for AI training use
**Impact:** NEGATIVE
- Private medical images exposed without consent
- HIPAA violations (if US patients)
- Dignity harm (medical imagery intimate, sensitive)
**Representation:** NONE
- No consent process
- No notification
- Images scraped from hospital breaches, patient portals
**Absent node:** Medical imagery in LAION-5B not addressed even in Re-LAION-5B cleanup

### 7. NCII Victims (Revenge Porn, Intimate Images)
**Population:** Unknown (no systematic count)
**Interest:** Privacy, consent, removal of non-consensual images
**Impact:** NEGATIVE
- Intimate images distributed without consent
- "Revenge porn" from abusive ex-partners scraped
- Re-victimization through AI training data
- Potential for model to generate similar images
**Representation:** NONE
- No consent process
- No removal mechanism until 2024
- Not addressed in Re-LAION-5B cleanup (only CSAM focused)
**Absent node:** NCII victims had no voice, no notification

### 8. Copyright Holders (Artists, Photographers, Stock Agencies)
**Population:** Millions (any image on web scraped via Common Crawl)
**Interest:** Copyright protection, attribution, compensation
**Impact:** NEGATIVE
- Copyrighted images used for training without permission
- Getty Images, Shutterstock, DeviantArt, ArtStation scraped
- No compensation (LAION non-profit, Stability AI commercial)
- Generative models compete with original artists
**Representation:** LOW
- Not consulted before scraping
- Legal recourse: Lawsuits filed (Getty, Andersen v. Stability AI)
**Absent node:** Copyright holders had no voice in dataset governance

### 9. Web Users Generally (Depicted in Scraped Images)
**Population:** Billions (anyone with image on web indexed by Common Crawl)
**Interest:** Privacy, consent for AI training use
**Impact:** VARIABLE
- Many unaware their images are in LAION-5B
- Vacation photos, social media posts, public events scraped
- Used to train generative models without consent
- "Public web" ≠ consent for AI training (expectation gap)
**Representation:** NONE
- No consent process
- No opt-out until 2024 (Re-LAION-5B allows removal requests)
**Absent node:** Billions of people depicted in LAION-5B had no voice

### 10. Non-Western Communities
**Population:** Billions (majority of world outside North America/Europe)
**Interest:** Fair representation in AI training data
**Impact:** NEGATIVE
- Under-represented (English/Western bias in Common Crawl → LAION)
- Models trained on LAION exhibit Western bias
- Non-Western visual culture marginalized
- Similar to ImageNet, Common Crawl pattern
**Representation:** NONE
- Not consulted in data collection methodology
- Common Crawl bias inherited without mitigation
**Absent node:** Geographic/cultural bias not addressed in LAION-5B design

---

## Harm Severity Analysis (ORP v0.2 Discovery)

### Tier 1: Safety/Criminal Harm (CSAM)
**Severity:** HIGHEST - Federal crime, child protection absolute
**Affected:** Children depicted in CSAM (cannot consent)
**Harm type:** Re-victimization, distribution of child abuse material
**Legal:** 18 U.S.C. § 2252 (CSAM possession/distribution)
**Remediation:** Partial (URLs removed, but cached images remain, models already trained)
**Irreversibility:** High (models can't be untrained, cached images distributed)

### Tier 2: Legal Harm (HIPAA, Copyright)
**Severity:** HIGH - Civil violations, regulatory compliance
**Affected:** Medical patients (HIPAA), copyright holders (infringement)
**Harm type:** Privacy violations, economic damages
**Legal:** HIPAA (US), GDPR (EU), copyright law
**Remediation:** Partial (medical images not addressed, copyright lawsuits ongoing)
**Irreversibility:** Moderate (can remove future, but past distribution permanent)

### Tier 3: Ethical Harm (NCII, Privacy, Consent)
**Severity:** MODERATE-HIGH - Dignity violations, consent issues
**Affected:** NCII victims, web users depicted without consent
**Harm type:** Privacy violations, dignity harm, consent bypass
**Legal:** Varies by jurisdiction (some US states have NCII laws)
**Remediation:** Minimal (NCII not addressed in Re-LAION-5B, consent still absent)
**Irreversibility:** Moderate (distributed images can't be recalled)

### Tier 4: Economic Harm (Copyright)
**Severity:** MODERATE - Financial damages, market disruption
**Affected:** Artists, photographers, stock agencies
**Harm type:** Lost revenue, unfair competition
**Legal:** Copyright infringement (lawsuits filed)
**Remediation:** Legal process ongoing (Getty, Andersen lawsuits)
**Irreversibility:** Low (future models can use licensed data, but past harm done)

### Tier 5: Bias Harm (Geographic/Cultural Under-Representation)
**Severity:** MODERATE - Fairness, representation
**Affected:** Non-Western communities (billions)
**Harm type:** Biased AI models, marginalization
**Legal:** None (ethical issue, not legal)
**Remediation:** Possible (future datasets can improve diversity)
**Irreversibility:** Low (bias can be corrected in future models)

**ORP INSIGHT:** Not all absent nodes equal - CSAM victims (Tier 1) require different treatment than copyright holders (Tier 4) or bias concerns (Tier 5). Current schema treats all absent nodes equally → inadequate for safety-critical issues.

---

## Decision Analysis (For Layer 4 - Accountability Ledger)

### Decision 1: Use Common Crawl as Source (~2021)
**Decision maker:** LAION team (Schuhmann, collaborators)
**Rationale:** Largest available web corpus, open-source, well-documented
**Alternative considered:** Curated sources (Flickr, stock photos) - rejected (smaller scale, API restrictions)
**Consequence:** Inherited Common Crawl's content (including CSAM, medical, NCII, copyright)

### Decision 2: CLIP Similarity Filtering (2021-2022)
**Decision maker:** LAION team
**Rationale:** Scalability (5 billion pairs), alignment quality (image matches text)
**Parameters:** Threshold 0.28 (English), 0.26 (multilingual)
**Alternative:** Human annotation (rejected: too expensive, too slow)
**Consequence:** Automated filtering → no human review → safety issues not caught

### Decision 3: NSFW Detection BUT NOT Filtering (2021-2022)
**Decision maker:** LAION team
**Rationale:** Let users decide threshold, some research needs adult content, "democratization"
**Result:** NSFW classifier run, tags provided, but NSFW images included
**Alternative:** Strict NSFW filtering (rejected: against open-access philosophy)
**Consequence:** Pornography included, NSFW filter ≠ CSAM filter

### Decision 4: NO CSAM Pre-Publication Filtering (2021-2022) - CRITICAL
**Decision maker:** LAION team
**Rationale:** [UNKNOWN - not documented in paper or public statements]
**Possible reasons (speculative):**
- Assumed NSFW filter sufficient (false: CSAM visually similar to adult content but legally distinct)
- Cost/compute overhead (hash matching adds latency)
- "Let users filter downstream" philosophy
- Federated structure ("we're just providing URLs, not hosting images")
- Didn't consider possibility of CSAM in Common Crawl
**Alternative considered:** [UNKNOWN - no evidence alternatives were discussed]
**PhotoDNA, CSAI Match, NCMEC hash databases:** Not used pre-publication
**Consequence:** 3,226 CSAM URLs in dataset, 12+ months distribution (Dec 2022 - Dec 2023), potential model memorization

### Decision 5: Federated Structure (URLs Only) (~2021)
**Decision maker:** LAION team
**Rationale:** Storage cost prohibitive (5.85B images = petabytes), legal liability (hosting vs linking)
**Alternative:** Host images directly (rejected: cost ~$10-50M+ for storage, single point of liability)
**Consequence:** Can remove URLs but not cached images, distribution uncontrollable after download

### Decision 6: Open Release (No Restrictions) (March 2022)
**Decision maker:** LAION team
**Rationale:** Democratize AI, maximize research impact, open-source philosophy
**Alternative:** Gated access (registration, review) - rejected (anti-open-source)
**Consequence:** Cannot track who downloaded, cannot notify of CSAM removal, CSAM distributed to unknown number of users

### Decision 7: Post-Discovery CSAM Removal (December 2023)
**Decision maker:** LAION team (responding to Stanford report)
**Timing:** Immediate (within hours of Stanford report release)
**Actions:** Dataset taken offline, partnerships with IWF/C3P/Stanford, hash matching cleanup
**Re-release:** August 2024 (Re-LAION-5B with 2,236 URLs removed)
**Limitation:** Only known CSAM removed (hash-matched), cannot retrieve cached images, models already trained

---

## Related Datasets and Variants (For Layer 5 - Fork Registry)

### 1. LAION-400M (2021) - Predecessor
**Relation:** Predecessor to LAION-5B
**Scale:** 400 million image-text pairs
**Method:** Similar (Common Crawl + CLIP filtering)
**Difference:** Smaller scale, English-only, attempted kids/teens category filtering
**Status:** Superseded by LAION-5B

### 2. LAION-Aesthetics (2022) - Quality Subset
**Relation:** Filtered subset of LAION-5B
**Scale:** ~600 million pairs
**Method:** CLIP + aesthetic predictor (high aesthetic quality scores)
**Used for:** Stable Diffusion final training stages
**Status:** Part of LAION-5B distribution
**Safety note:** Still contained CSAM (no additional safety filtering)

### 3. LAION-2B-en (2022) - English Subset
**Relation:** English-only subset of LAION-5B
**Scale:** 2.32 billion pairs
**Used for:** Stable Diffusion primary training
**Status:** Part of LAION-5B distribution
**Safety note:** Likely contained CSAM (subset of full dataset)

### 4. Re-LAION-5B (August 2024) - Safety Revision
**Relation:** MAJOR REVISION (ethical remediation)
**Scale:** 5.85 billion pairs minus 2,236 removed URLs
**Method:** Original LAION-5B + hash matching (PhotoDNA, CSAI Match, NCMEC)
**Partnerships:** IWF, C3P, Stanford Internet Observatory
**Changes:**
- 2,236 CSAM URLs removed (Stanford's 1,008 + additional 1,228)
- First web-scale dataset "thoroughly cleaned of known links to suspected CSAM"
**Limitations:**
- Only "known" CSAM (hash-matched against existing databases)
- New/unreported CSAM may remain
- Medical imagery, NCII, copyright NOT addressed
- Federated structure unchanged (cached images still exist)
**Status:** Current version available for download

### 5. DataComp (2023) - Curated Filtering
**Relation:** Alternative approach to dataset curation (not directly related to LAION, but uses CommonCrawl)
**Method:** Improved CLIP filtering, curation strategies
**Focus:** Quality over scale
**Research:** Who's in and who's out? (case study of CLIP filtering biases)

---

## Key Sources for Citations

### Primary Papers:
1. **Schuhmann et al. (2022):** LAION-5B: An open large-scale dataset for training next generation image-text models. NeurIPS 2022. arXiv:2210.08402

2. **Thiel (2023):** Identifying and Eliminating CSAM in Generative ML Training Data and Models. Stanford Internet Observatory. https://purl.stanford.edu/kh752sm9123

3. **LAION.ai (2024):** Releasing Re-LAION-5B: transparent iteration on LAION-5B with additional safety fixes. https://laion.ai/blog/relaion-5b/

### News Coverage:
- CNN (Dec 21, 2023): "Hundreds of images of child sexual abuse material were found in a massive dataset"
- Bloomberg (Dec 20, 2023): "Large AI Dataset Has Over 1,000 Child Abuse Images, Researchers Find"
- 404 Media (Dec 2023): "Largest Dataset Powering AI Images Removed After Discovery of Child Sexual Abuse Material"
- 404 Media (Aug 2024): "Massive AI Dataset Back Online After Being 'Cleaned' of Child Sexual Abuse Material"

### Legal Cases:
- Getty Images v. Stability AI (filed Feb 2023, ongoing)
- Andersen v. Stability AI (filed Jan 2023, class action, ongoing)

---

## Summary for ORP Document Creation

### What Makes LAION-5B a Critical ORP-Full Example:

1. **Layer 1 (Data Provenance):** Federated structure, Common Crawl source, CLIP filtering, **NO CSAM filtering pre-publication**

2. **Layer 2 (Consequence Simulation):** Clear downstream impacts - CSAM → model memorization → potential AI-generated abuse, medical/NCII privacy violations

3. **Layer 3 (Empathy Mapping):** **Worst-case absent nodes**:
   - Children (CSAM victims - cannot consent, federal crime)
   - Medical patients (HIPAA violations)
   - NCII victims (revenge porn)
   - **Harm severity taxonomy discovered:** Safety (criminal) > Legal (HIPAA) > Ethical (NCII) > Economic (copyright) > Bias (cultural)

4. **Layer 4 (Accountability Ledger):** Decision 4 (NO CSAM filtering) is **critical safety failure** - no documented alternatives considered, rationale unknown, consequence: federal crime distribution

5. **Layer 5 (Fork Registry):** Re-LAION-5B (Aug 2024) demonstrates post-hoc remediation (2,236 URLs removed), but **insufficient** (only known CSAM, cached images remain, models already trained)

### What LAION-5B Demonstrates About ORP's Value:

- **Safety harm ≠ ethical harm:** CSAM (criminal) requires different treatment than privacy (ethical) or bias (fairness)
- **Post-hoc remediation insufficient:** Removing URLs in 2024 doesn't undo 2023 distribution or model training
- **Federated structure limits control:** Can't retrieve cached images or untrain models
- **Harm severity taxonomy needed:** ORP v0.1 treats all absent nodes equally → inadequate for safety-critical issues like CSAM
- **Vulnerable populations require special protection:** Children cannot consent, require proactive safeguards not just post-hoc cleanup

---

**End of Research Notes**

**Next step:** Draft ORP-Full document (`examples/laion5b_training_data.yaml`) using this research foundation.
