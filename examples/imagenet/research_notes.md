# ImageNet Training Data - Research Notes

**Purpose:** Background research for ORP-Full document on ImageNet-1K dataset constitution
**Date:** 2026-04-07
**Researcher:** Asbjørn

---

## Primary Sources

### 1. Deng et al. (2009) - Original ImageNet Paper

**Citation:** Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., & Fei-Fei, L. (2009). ImageNet: A Large-Scale Hierarchical Image Database. *2009 IEEE Conference on Computer Vision and Pattern Recognition*, 248-255. https://doi.org/10.1109/CVPR.2009.5206848

**PDF:** https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf

**Key Information:**
- **Authors:** Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei (Princeton University, Dept. of Computer Science)
- **Publication date:** June 2009 (CVPR 2009, Miami, FL)
- **Dataset scope at publication:** 12 subtrees with 5,247 synsets and 3.2 million images
- **Goal:** Populate majority of 80,000 WordNet synsets with 500-1000 clean, full-resolution images each
- **Backbone:** Built upon WordNet hierarchical structure
- **Collection method:** Amazon Mechanical Turk for image annotation and verification

### 2. Russakovsky et al. (2015) - ILSVRC Paper

**Citation:** Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z., Karpathy, A., Khosla, A., Bernstein, M., Berg, A. C., & Fei-Fei, L. (2015). ImageNet Large Scale Visual Recognition Challenge. *International Journal of Computer Vision*, 115, 211-252. https://doi.org/10.1007/s11263-015-0816-y

**Also available:** arXiv:1409.0575 (v3 dated January 30, 2015)

**Key Information:**
- **Full author list:** Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg, and Li Fei-Fei
- **Focus:** Annual ImageNet Large Scale Visual Recognition Challenge (ILSVRC) from 2010-present
- **Challenge dataset:** Benchmark on hundreds of object categories with millions of images
- **Significance:** Documents advances in object recognition enabled by ImageNet

### 3. Crawford & Paglen (2021) - Excavating AI

**Citation:** Crawford, K., & Paglen, T. (2021). Excavating AI: The politics of images in machine learning training sets. *AI & Society*, 36, 1-28. https://doi.org/10.1007/s00146-021-01162-8

**Earlier version:** Originally published September 19, 2019 at http://www.excavating.ai
**Exhibition:** "Training Humans" at Fondazione Prada Osservatorio, Milan (September 12, 2019 - February 24, 2020)

**Key Information:**
- **Focus:** Political and social dimensions of classification in ImageNet
- **Critical findings:**
  - ImageNet person categories contained problematic labels
  - Example: Woman in bikini labeled "slattern, slut, slovenly woman, trollop"
  - Example: Young man drinking beer labeled "alcoholic, alky, dipsomaniac, boozer, lush, soaker, souse"
  - Example: Child wearing sunglasses labeled "failure, loser, non-starter, unsuccessful person"
- **Methodology:** ImageNet Roulette art project went viral, exposing bias to public
- **Core argument:** Automated image interpretation is inherently social and political project
- **Key questions addressed:**
  - What work images do in computer vision systems
  - How taxonomies order foundational concepts determining system interpretation
  - How humans tell computers which words relate to images
  - What's at stake in AI systems classifying humans by race, gender, emotions, ability, sexuality, personality

### 4. Prabhu & Birhane (2020/2021) - Large Image Datasets: A Pyrrhic Win

**Citation:** Prabhu, V. U., & Birhane, A. (2021). Large image datasets: A pyrrhic win for computer vision? *2021 IEEE Winter Conference on Applications of Computer Vision (WACV)*. arXiv:2006.16923 (posted June 24, 2020)

**Key Information:**
- **Focus:** Problematic practices and consequences of large-scale vision datasets (LSVDs)
- **Primary case study:** ImageNet-ILSVRC-2012 dataset
- **Methodology:** Cross-sectional model-based quantitative census covering:
  - Age, gender
  - NSFW content scoring
  - Class-wise accuracy
  - Human-cardinality-analysis
  - Semanticity of image class information
- **Broad issues examined:**
  - Question of consent
  - Justice concerns
  - Inclusion of verifiably pornographic images
- **Findings:** Statistical investigation of extent and subtleties of ethical transgressions

### 5. Yang et al. (2020) - Dataset Biases

**Citation:** Yang, K., Qinami, K., Fei-Fei, L., Deng, J., & Russakovsky, O. (2020). Towards fairer datasets: Filtering and balancing the distribution of the people subtree in the ImageNet hierarchy. *Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency*, 547-558. https://doi.org/10.1145/3351095.3375709

**Note:** This paper was developed by ImageNet creators themselves (includes Fei-Fei Li, Jia Deng, Olga Russakovsky) responding to criticism

**Key Information:**
- **Context:** Researchers from Princeton and Stanford (ImageNet creators) developing mitigation tool
- **Tool:** Allows users to specify and retrieve image sets balanced by age, gender expression, skin color
- **Acknowledgment:** ImageNet content reflects considerable bias
- **Biases identified:**
  - Dark-skinned people underrepresented across most categories
  - Females underrepresented
  - Adults over 40 underrepresented
  - Example: "groom" category shows mostly white people

---

## Funding Sources

### Documented Funding (from Deng et al. 2009)

The original ImageNet paper credits:
- **National Science Foundation (NSF)** - specific grant numbers not provided in abstract
- **Google**
- **Intel**
- **Microsoft**
- **Yahoo!**

### Funding Application History

From Fei-Fei Li biography sources:
- **Failed federal grant applications:** Li stated the project failed to win federal grants initially, with comments that it was "shameful" Princeton would research this topic
- **Despite initial rejections:** NSF eventually provided funding support (credited in 2009 paper)
- **Institutional support:** Princeton University and Stanford University provided resources

### Timeline Context

- **2006:** Fei-Fei Li begins working on ImageNet idea (at University of Illinois Urbana-Champaign)
- **2007:** Li joins Princeton as assistant professor, starts building team
- **2007:** Li meets with Christiane Fellbaum (WordNet co-creator at Princeton)
- **2009:** Original paper published (CVPR 2009)
- **2009:** Li joins Stanford University
- **2013-2018:** Li serves as director of Stanford Artificial Intelligence Lab (SAIL)

---

## Dataset Scope Decisions

### 1. Taxonomy Source: WordNet

**Decision:** Use WordNet hierarchy as category source

**Rationale (from Deng et al. 2009):**
- WordNet is comprehensive (80,000+ synsets)
- Hierarchical structure enables scalable organization
- Well-established linguistic database
- Created by Princeton linguists (Fellbaum et al.)

**Implications:**
- Categories reflect English-language taxonomy
- Inherits WordNet's cultural and linguistic biases
- Focus on nouns (objects, not actions or contexts)
- Western philosophical tradition of categorization

### 2. Synset Selection Criteria

**Decision:** Select visually recognizable categories from WordNet

**From original paper:**
- Not all WordNet synsets are visual (e.g., abstract concepts)
- Selected subset focused on concrete, photographable objects
- Final ILSVRC-2012: 1,000 categories selected from ~22,000 candidate synsets

**Implications:**
- Bias toward concrete objects over abstract concepts
- Bias toward Western-familiar objects (more likely to be photographed on English-speaking web)

### 3. ImageNet-1K vs ImageNet-22K

**ImageNet-22K (Full):** ~22,000 categories, 14+ million images
**ImageNet-1K (ILSVRC-2012):** 1,000 categories, ~1.2 million training images

**Why 1,000 for ILSVRC:**
- Computationally tractable for competition
- Covers broad range of object types
- Balanced across major WordNet subtrees

---

## Collection Methodology

### Image Source: Web Scraping

**Method:**
- Query search engines (Google, Flickr, other image search platforms)
- Use WordNet synset terms as search keywords
- Collect candidate images from public web

**Timeline:** Primary collection 2009-2012

**Scale:**
- AMT workers evaluated over 160 million candidate images
- Filtered down to 3.2 million images (2009 paper), later expanded
- ILSVRC-2012: ~1.2 million training images, 50,000 validation images, 100,000 test images

### Geographic and Temporal Scope

**Geographic:**
- Images scraped from global web, but...
- 80%+ of images from North America and Europe (documented in bias research)
- Reason: English-language queries on Western-dominated web platforms (2009-2012)

**Temporal:**
- Images scraped 2009-2012 (ILSVRC dataset freeze in 2012)
- Reflects visual culture of late 2000s, early 2010s internet
- Does not represent earlier or later time periods

### Cultural and Language Bias

**English-language bias:**
- Search keywords derived from English WordNet
- Image search engines biased toward English queries
- Flickr tags, Google Images results reflect English-speaking web

**Cultural representation:**
- Western objects, scenes, contexts over-represented
- Non-Western cultural artifacts under-represented
- Example: "Wedding" category shows predominantly Western white weddings

---

## Annotation Decisions

### Amazon Mechanical Turk (AMT) Methodology

**Timeline:** July 2008 - April 2010 (primary annotation period)

**Worker scale:**
- 49,000 workers from 167 countries
- ImageNet was world's largest academic user of AMT in 2012
- Average worker identified 50 images per minute

**Task design:**
1. **"Contains task":** Annotators shown class descriptions (with Wikipedia links) and grid of candidate images
2. **Selection:** Annotators select all images containing object of that class
3. **Instructions:** Explicit instructions to ignore clutter and occlusions

**Quality control:**
- **Multiple annotators:** Each image shown to multiple workers
- **Majority vote:** Only images with "convincing majority" of votes included
- **Per-class thresholds:** Estimated using small pool of annotators
- **Validation study:** 80 synsets randomly sampled, independent verification achieved 99.7% precision

**Known annotation issues (from later research):**
- ~5-10% label error rate (acknowledged by creators)
- Northcutt et al. (2021): Identified 2,916 errors (6%) in validation set using confident learning
- Errors include: wrong class, multiple valid classes, ambiguous images

### Annotator Demographics (from Crawford & Paglen critique)

**Issue:** AMT worker demographics shape annotation quality
- Socioeconomic factors: Low-wage digital labor ($0.01-$0.10 per task)
- Geographic factors: Workers predominantly from US, India, other English-speaking regions
- Cultural factors: Workers' cultural backgrounds influence category judgments
- No attribution: Workers receive no credit for contributions

---

## Inclusion/Exclusion Criteria

### Documented Exclusions (from original paper)

**Image quality filters:**
- Minimum resolution threshold (images must be "full resolution")
- Broken links excluded
- Duplicate images removed

**Content filters:**
- "Photos only, no painting, no drawings" (explicit instruction to annotators)
- NSFW content filtered "to extent possible"
- Copyright: Some copyrighted images excluded (but not comprehensive)

### Undocumented/Structural Exclusions (from bias research)

**Geographic exclusions:**
- Non-Western geographies systematically under-represented
- Result of English-language queries + Western web dominance
- Not intentional exclusion, but structural consequence

**Cultural exclusions:**
- Non-Western cultural artifacts, practices, objects under-represented
- WordNet taxonomy reflects Western categorization
- Example: Food categories skew toward Western cuisines

**Socioeconomic exclusions:**
- Objects common in higher-income contexts over-represented
- Luxury goods, Western consumer products prominent
- Objects from lower-income contexts under-represented

**Temporal exclusions:**
- Only images available on web 2009-2012
- Historical objects, obsolete technologies under-represented
- Future objects/technologies not present (by definition)

**Language exclusions:**
- Non-English categories systematically excluded
- WordNet is English-language resource
- Concepts without English equivalent not represented

---

## Cleaning Decisions

### Initial Cleaning (2009-2012)

**From Deng et al. (2009) and Russakovsky et al. (2015):**
1. Label verification process via AMT majority voting
2. Image deduplication (remove exact duplicates)
3. Removal of broken links
4. Quality threshold filtering (only images passing annotator agreement threshold)

### Post-Publication Cleaning (2019-2020)

**Trigger:** Crawford & Paglen's "Excavating AI" and ImageNet Roulette art project (September 2019)

**ImageNet team response:**
- Identified 438 "unsafe" and "offensive" person categories
- Identified additional 1,155 "sensitive" or potentially offensive labels
- **Scale:** 1,593 of 2,832 person categories found problematic (54%)
- **Action:** Removed ~600,000 images from "person" categories (half of 1.5M person images)
- **Date:** Announced late 2019, implemented 2019-2020

**Examples of removed labels (from news coverage):**
- Racial slurs
- Derogatory terms for women
- Offensive labels for professions, body types, ages
- Pejorative psychological/medical terms

---

## Known Limitations

### Acknowledged by Creators (from original papers)

**From Deng et al. (2009) and Russakovsky et al. (2015):**
1. **Class imbalance:** Some categories have more/better images than others
2. **Label noise:** Acknowledged ~5-10% error rate in annotations
3. **Single-label limitation:** Images often contain multiple objects, but labeled with single primary object
4. **Ambiguity:** Some images are genuinely ambiguous (multiple valid interpretations)

### Identified by Critics (from bias research literature)

**From Crawford & Paglen (2021), Prabhu & Birhane (2021), Yang et al. (2020):**

1. **Geographic/cultural bias:**
   - Not quantified initially by creators
   - Later research: 80%+ images from North America/Europe
   - Non-Western contexts systematically under-represented

2. **Demographic bias in person categories:**
   - Dark-skinned people under-represented
   - Females under-represented
   - Adults over 40 under-represented
   - Western appearance norms dominate

3. **Offensive/problematic labels:**
   - 54% of person categories (1,593 of 2,832) identified as problematic
   - Reflects WordNet's inclusion of derogatory terms
   - Not caught during initial dataset creation

4. **Consent and privacy issues:**
   - Images scraped without explicit consent
   - Faces included without knowledge/permission
   - No mechanism for depicted individuals to opt out (initially)

5. **Socioeconomic bias:**
   - Higher-income contexts over-represented
   - Western consumer goods prominent
   - Global South objects/contexts under-represented

---

## Synthetic Elements

**Answer:** None (present: false)

**Clarification:**
- All images are real photographs scraped from web
- No synthetic/generated images in original ImageNet
- No simulated data
- Later work (e.g., ImageNet-D) adds synthetic test sets, but not part of original ILSVRC-2012

---

## Access and Licensing

### Access Policy

**Current (as of 2012-present):**
- Available via ImageNet website (https://www.image-net.org/)
- **Registration required:** Users must create account and agree to terms
- **Purpose:** Tracking usage while enabling research access
- **Download:** Free for academic/research purposes

**Alternative considered (from Li interviews):**
- Fully open release without registration
- Rejected due to:
  - Copyright concerns (some images may have unclear copyright status)
  - Ethical concerns (person images, privacy issues)
  - Desire to track research impact

### License

**Original license:** Non-commercial research use only

**Restrictions:**
- No commercial use without separate licensing
- Cannot redistribute
- Must cite original papers
- Must follow ImageNet terms of service

**Rationale:**
- Enable academic research
- Prevent commercial exploitation without permission
- Allow tracking of dataset usage and impact

---

## Controversy Timeline

### Phase 1: Creation and Growth (2009-2018)

**2009:** Original paper published, dataset released
**2010:** First ImageNet Large Scale Visual Recognition Challenge (ILSVRC)
**2012:** AlexNet wins ILSVRC, triggers deep learning revolution
**2012:** ILSVRC-2012 dataset becomes de facto standard for computer vision
**2013-2017:** ImageNet enables rapid progress in object recognition, becomes most-cited dataset in computer vision

**Status:** Widely celebrated, minimal public criticism

### Phase 2: Critical Examination (2019-2020)

**September 2019:** Crawford & Paglen release "Excavating AI" and ImageNet Roulette art project
**September 2019:** ImageNet Roulette goes viral, exposing offensive person category labels
**Late 2019:** ImageNet team announces review and removal of problematic categories
**2020:** Prabhu & Birhane paper documents ethical transgressions in ImageNet (arXiv June 2020)
**2020:** Yang et al. (including ImageNet creators) release bias mitigation tool
**2021:** Prabhu & Birhane paper published at WACV 2021
**2021:** Northcutt et al. document pervasive label errors (6% of validation set)

**Status:** Heightened scrutiny, dataset still widely used but with greater awareness of limitations

### Phase 3: Ongoing Debate (2021-present)

**Ongoing issues:**
- Continued use despite known biases (too embedded in research infrastructure to abandon)
- Debate over whether to fix vs. replace vs. supplement
- Development of alternative/complementary datasets
- Creation of variants (ImageNet-V2, ImageNet-R, cleaned labels)

---

## Related Work and Variants (for Layer 5 - Fork Registry)

### 1. ImageNet-V2 (Recht et al., 2019)

**Citation:** Recht, B., Roelofs, R., Schmidt, L., & Shankar, V. (2019). Do ImageNet classifiers generalize to ImageNet? *Proceedings of the 36th International Conference on Machine Learning*, 5389-5400. arXiv:1902.10811

**Type:** Test set revision (not a fork of constitution, but fork of evaluation methodology)

**Rationale:**
- Original test set potentially overfit (models trained and tested on same distribution)
- Test distribution shift robustness

**Changes:**
- 10,000 new images per test set (3 test sets: Threshold0.7, MatchedFrequency, TopImages)
- Same 1,000 categories as ILSVRC-2012
- Collected ~10 years after original (2019 vs 2009-2012)
- Closely followed original collection process

**Findings:**
- Accuracy drops of 11-14% on new test set
- Suggests models don't fully generalize, have learned dataset-specific patterns

**Relationship to ORP:** Sibling dataset (same categories, different image distribution for testing)

### 2. ImageNet-R (Hendrycks et al., 2021)

**Citation:** Hendrycks, D., Basart, S., Mu, N., Kadavath, S., Wang, F., Dorundo, E., Desai, R., Zhu, T., Parajuli, S., Guo, M., Song, D., Steinhardt, J., & Gilmer, J. (2021). The many faces of robustness: A critical analysis of out-of-distribution generalization. *Proceedings of the International Conference on Computer Vision (ICCV)*.

**GitHub:** https://github.com/hendrycks/imagenet-r

**Type:** Robustness benchmark (derivative dataset with different image modalities)

**Rationale:**
- Test model robustness to naturally occurring distribution shifts
- Original ImageNet instruction: "photos only, no painting, no drawings"
- ImageNet-R does opposite: artistic renditions only

**Changes:**
- 200 ImageNet classes (subset of 1,000)
- 30,000 images total
- Image types: art, cartoons, deviantart, graffiti, embroidery, graphics, origami, paintings, patterns, plastic objects, plush objects, sculptures, sketches, tattoos, toys, video game renditions
- Explicitly excludes photographic images

**Findings:**
- Models trained on photographic ImageNet perform poorly on artistic renditions
- Highlights texture bias in CNN models

**Relationship to ORP:** Derivative dataset (same categories, radically different image distribution and collection method)

### 3. Cleaned ImageNet Labels (Northcutt et al., 2021)

**Citation:** Northcutt, C. G., Athalye, A., & Mueller, J. (2021). Pervasive label errors in test sets destabilize machine learning benchmarks. *Advances in Neural Information Processing Systems*, 34, 2259-2270. arXiv:2103.14749

**Website:** https://labelerrors.com
**GitHub:** https://github.com/cleanlab/label-errors

**Type:** Label correction (fork addressing L1 known limitation: annotation errors)

**Rationale:**
- Identify and fix annotation errors using confident learning algorithms
- Human-validate algorithmically-flagged errors via crowdsourcing

**Changes:**
- Identified 2,916 label errors (6%) in 50,000-image validation set
- Corrected labels made publicly available
- No changes to images, only label corrections

**Findings:**
- 51% of algorithmically-flagged candidates confirmed as errors by humans
- Higher-capacity models reflect systematic label errors more than smaller models
- Benchmark rankings relatively stable, but absolute performance metrics unstable

**Relationship to ORP:** Revision dataset (same images, corrected labels addressing known L1 limitation)

### 4. ImageNet with Removed Person Categories (ImageNet Team, 2019-2020)

**Type:** Content moderation / ethical cleaning

**Rationale:**
- Remove offensive and problematic person category labels
- Address privacy and consent concerns

**Changes:**
- Removed 1,593 person categories (54% of 2,832 person categories)
- ~600,000 images removed from dataset
- Remaining person categories retained

**Status:**
- Implemented by ImageNet team in response to Crawford & Paglen criticism
- This is the "current" ImageNet available for download

**Relationship to ORP:** Major revision (ethical/content-based exclusions changing dataset constitution)

### 5. Potential Future Forks (not yet created)

**ORP Layer 5 enables proposals like:**
- **"Global Representative ImageNet":** Different exclusion criteria prioritizing geographic balance
- **"Consent-Based ImageNet":** Only images with explicit consent from depicted individuals
- **"Culturally Inclusive ImageNet":** Expanded taxonomy beyond WordNet, incorporating non-Western categorizations
- **"Participatory ImageNet":** Dataset constitution via community governance, not just research team

**Note:** These are hypothetical forks enabled by ORP's Fork Registry concept, not existing datasets

---

## Key Decisions Timeline (for Layer 4 - Accountability Ledger)

### Decision 1: Use WordNet as Taxonomy Source (~2007)

**Decision maker:** Fei-Fei Li (PI), in consultation with Christiane Fellbaum (WordNet co-creator)
**Date:** 2007 (Li meets with Fellbaum at Princeton)
**Rationale:** WordNet comprehensive, hierarchical, well-established
**Alternative considered:** Custom taxonomy (rejected: too resource-intensive)
**Source:** Deng et al. (2009) paper, Section 3; Li biography sources

### Decision 2: Use Amazon Mechanical Turk for Annotation (~2008)

**Decision maker:** ImageNet team (Li, Deng, et al.)
**Date:** 2008 (AMT annotation begins July 2008)
**Rationale:** Scalable, cost-effective, proven for similar tasks
**Alternative considered:** Expert annotators (rejected: too expensive/slow), fully automated (rejected: insufficient accuracy)
**Source:** Deng et al. (2009), Section 4

### Decision 3: Multiple-Annotator Quality Control (~2008)

**Decision maker:** ImageNet team
**Date:** 2008 (design of AMT tasks)
**Rationale:** Balance accuracy and cost
**Parameters:** "Convincing majority" threshold, per-class thresholds estimated using pilot study
**Source:** Deng et al. (2009), annotation protocol

### Decision 4: Select 1,000 Categories for ILSVRC (~2010)

**Decision maker:** ImageNet team + ILSVRC organizers
**Date:** ~2010 (first ILSVRC competition)
**Rationale:** Computationally tractable, broad object coverage, balanced across subtrees
**Alternative:** Use all 22K categories (rejected: too large for competition)
**Source:** Russakovsky et al. (2015), ILSVRC paper

### Decision 5: Public Release with Registration (~2009-2010)

**Decision maker:** ImageNet team (Li, Deng, et al.)
**Date:** 2009-2010 (initial public release)
**Rationale:** Maximize research impact while tracking usage
**Alternatives considered:**
  - Fully open with no registration (rejected: copyright/ethical concerns)
  - Closed/limited access (rejected: reduces research impact)
**Source:** Li interviews, ImageNet website terms

### Decision 6: Remove Offensive Person Categories (2019)

**Decision maker:** ImageNet team (Deng, Li, et al.) in response to community criticism
**Date:** Late 2019 (announced after ImageNet Roulette controversy)
**Rationale:** Ethical concerns raised by Crawford & Paglen and public response
**Scale:** 1,593 categories removed (54% of person categories), ~600,000 images
**Alternative considered:**
  - Full dataset review and reconstruction (rejected: too resource-intensive)
  - Do nothing (rejected: ethically untenable after public exposure)
**Source:** News coverage (The Art Newspaper, Artsy, VentureBeat), ImageNet team statements

---

## Stakeholder Groups (for Layer 3 - Empathy Mapping)

### 1. Dataset Creators

**Individuals:** Fei-Fei Li, Jia Deng, Kai Li, and team (~10-20 researchers at Princeton, then Stanford)
**Interest:** Scientific contribution, academic credit, enabling AI research
**Impact:** Positive (career advancement, field impact, most-cited dataset in computer vision)
**Representation:** Full (they made all constitutive decisions)

### 2. Funding Organizations

**Organizations:** NSF, Google, Intel, Microsoft, Yahoo!
**Interest:** Advance computer vision research, demonstrate ROI on research investment
**Impact:** Positive (ImageNet enabled deep learning revolution, generated enormous research value)
**Representation:** Moderate (funded project, but did not direct day-to-day decisions)

### 3. AI Researchers (Dataset Users)

**Population:** Thousands of computer vision researchers worldwide
**Interest:** High-quality training data for object recognition models
**Impact:** Massively positive (enabled AlexNet and deep learning revolution, countless publications)
**Representation:** High (active community, ILSVRC competition provided feedback loop)

### 4. Amazon Mechanical Turk Workers

**Population:** 49,000 workers from 167 countries (2008-2010)
**Interest:** Compensation for labor
**Impact:** Mixed:
  - Positive: Paid for work (~$0.01-$0.10 per task)
  - Negative: Low wages, no academic credit, no ownership, no decision-making power
**Representation:** None (no input on dataset decisions, categorization choices, or governance)
**Absent node:** Worker demographics shape annotation quality, but workers invisible in papers and credit

### 5. People Depicted in Images

**Population:** Unknown (millions of individuals in ~1.2M training images)
**Interest:** Privacy, consent, dignified representation
**Impact:** Negative potential:
  - Scraped from public web without explicit consent
  - Some offensive labels applied (pre-2019 removal)
  - No mechanism to opt out initially
  - Privacy concerns (faces, identities)
**Representation:** None (no consent process in 2009-2012, no voice in dataset governance)
**Absent node:** Faces in dataset had no knowledge of inclusion or ability to object

### 6. Non-Western Communities

**Population:** Billions of people outside North America and Europe
**Interest:** Fair representation in AI training data
**Impact:** Negative:
  - Systematically under-represented (only ~20% of images from outside NA/Europe)
  - Models trained on ImageNet perform worse on non-Western contexts
  - Western objects, scenes, cultural norms dominate
**Representation:** None (not consulted in taxonomy/collection decisions)
**Absent node:** Categories reflect Western taxonomy (WordNet), not universal or multi-cultural taxonomy

### 7. Minority Demographic Groups (Within Person Categories)

**Population:** People of color, women, elderly, non-Western appearance norms
**Interest:** Fair representation without bias
**Impact:** Negative:
  - Dark-skinned people under-represented (Yang et al. 2020)
  - Females under-represented
  - Adults over 40 under-represented
  - Offensive labels disproportionately applied (documented in Crawford & Paglen)
**Representation:** None (not consulted during dataset creation)
**Absent node:** Demographic bias not measured initially, discovered years later

### 8. People Affected by ImageNet-Trained Models (Downstream)

**Population:** Anyone encountering AI systems trained on ImageNet (billions globally)
**Interest:** Fair, unbiased AI systems in computer vision applications
**Impact:** Variable:
  - Positive: Improved object recognition in many applications
  - Negative: Biased models (geographic, demographic biases propagate to applications)
  - Examples: Facial recognition, hiring AI, content moderation, autonomous vehicles
**Representation:** None (downstream impacts not modeled during dataset constitution)
**Absent node:** Constitutive decisions made without considering how biases would propagate through ML pipeline

---

## Notes on Reconstructing Accountability

**Important caveat:** This ORP document is **post-hoc reconstruction**, not real-time governance.

- ImageNet was created 2007-2012, before ORP existed
- Decisions documented from published papers, interviews, retrospective accounts
- We cannot know all internal deliberations (only what was published)
- This demonstrates what Layer 4 (Accountability Ledger) would capture if ORP had existed in 2007

**Attestation:**
- Document created by [analyst name], not original creators
- Based on published sources, not internal knowledge
- Cannot verify unpublished decision processes
- Represents best-effort reconstruction from available evidence

---

## Additional References for Deeper Research

### Model Cards and Datasheets Comparison

**Model Cards (Mitchell et al., 2019):**
- Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D., & Gebru, T. (2019). Model cards for model reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220-229. https://doi.org/10.1145/3287560.3287596

**Datasheets for Datasets (Gebru et al., 2018):**
- Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2018). Datasheets for datasets. *Communications of the ACM*, 64(12), 86-92. arXiv:1803.09010

### Additional Bias and Ethics Research

**On ImageNet's genealogy:**
- Denton, E., Hanna, A., Amironesei, R., Smart, A., & Nicole, H. (2021). On the genealogy of machine learning datasets: A critical history of ImageNet. *Big Data & Society*, 8(2). https://doi.org/10.1177/20539517211035955

**Geographic bias:**
- de Vries, T., Misra, I., Wang, C., & van der Maaten, L. (2019). Does object recognition work for everyone? *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops*, 52-59.

**Cultural bias in computer vision:**
- Shankar, S., Halpern, Y., Breck, E., Atwood, J., Wilson, J., & Sculley, D. (2017). No classification without representation: Assessing geodiversity issues in open data sets for the developing world. *NIPS Workshop on Machine Learning for the Developing World*.

---

## Summary for ORP Document Creation

### What makes ImageNet a good ORP-Full example:

1. **Layer 1 (Data Provenance):** Rich documentation of funding, collection methodology, exclusions (both documented and structural)
2. **Layer 2 (Consequence Simulation):** Clear downstream impacts (model biases traced to dataset constitution)
3. **Layer 3 (Empathy Mapping):** Multiple absent stakeholder groups (AMT workers, depicted individuals, non-Western communities, downstream users)
4. **Layer 4 (Accountability Ledger):** Major decisions documented in papers and retrospectives (taxonomy choice, AMT, offensive label removal)
5. **Layer 5 (Fork Registry):** Multiple variants exist (ImageNet-V2, ImageNet-R, cleaned labels) demonstrating fork concept

### What ImageNet demonstrates about ORP's value:

- **Constitutive transparency matters:** Decisions made in 2007-2009 (WordNet taxonomy, web scraping, AMT annotation) shaped AI systems for a decade
- **Absent nodes are real:** Multiple stakeholder groups systematically excluded from governance
- **Post-hoc fixes are costly:** Removing 600,000 images in 2019 much harder than designing inclusively in 2007
- **Downstream impacts compound:** Dataset biases propagate through ML pipeline to real-world applications
- **Forks enable improvement:** Variants (V2, R, cleaned) show how contestability improves datasets

---

**End of Research Notes**
