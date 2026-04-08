# Sprint 1.7.3.0: ImageNet Training Data Example (ORP-Full)

**Version:** `sprint-1.7.3`
**Parent Epic:** `sprint-1.7.0` (Foundation for Expansion)
**Status:** Not Started
**Start Date:** 2026-04-08 (can overlap with 1.7.2)
**Target End Date:** 2026-04-15 (7 days)

**Code Target Version:** `v0.6.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Create a rigorous ORP-Full document for the ImageNet dataset constitution, demonstrating that ORP applies to AI training data and surfacing constitutive-layer information (funding, exclusions, scope decisions) that existing dataset documentation standards (Model Cards, Datasheets) do not capture — strengthening the academic paper's empirical foundation.

---

## Strategic Importance

This is the **critical path** sprint for the epic:

- Second worked example proves cross-domain applicability (tax policy → AI training data)
- Demonstrates "absent node problem" and "scope capture" from academic paper
- Builds on Crawford & Paglen's "Excavating AI" analysis
- Shows ORP's value for AI governance (EU AI Act moment)
- Strengthens paper before submission (empirical evidence for theoretical claims)

---

## Scope

### In Scope

- **ORP-Full** (all 5 layers) for ImageNet-1K dataset
- Focus on **dataset constitution** (how ImageNet was built), not models trained on it
- Use existing research (Crawford & Paglen, Prabhu & Birhane) as L1 foundation
- Real data: Actual ImageNet history, decisions, exclusions
- Demonstrates all 5 REE principles in AI context

### Dataset Choice: ImageNet-1K

**Why ImageNet:**

- Most influential training dataset in AI history
- Well-documented constitution history (papers, blog posts, talks)
- Crawford & Paglen's work provides constitutive analysis
- Demonstrates all ORP concerns (scope capture, exclusions, incentives)
- Public, citeable, uncontroversial choice

**Scope limitation:**

- ImageNet-1K (1,000 categories, ~1.2M images) not ImageNet-22K
- Original 2009-2012 dataset, not subsequent versions
- Focus on dataset decisions, not ILSVRC competition

### Explicitly Out of Scope

- Models trained on ImageNet (ResNet, VGG, etc.) - that's model governance, not data governance
- ImageNet-V2, ImageNet-R, or other variants (could be L5 forks later)
- Technical validation of image labels (trust existing research)
- New primary research (use existing published sources)
- Policy recommendations (ORP describes, doesn't prescribe)

---

## Tasks

### Task 1: Research ImageNet Constitution History

**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Gather primary and secondary sources documenting how ImageNet was constituted.

**Acceptance Criteria:**

- [ ] Read/review key sources:
  - Deng et al. (2009): "ImageNet: A Large-Scale Hierarchical Image Database" (original paper)
  - Russakovsky et al. (2015): "ImageNet Large Scale Visual Recognition Challenge" (ILSVRC paper)
  - Crawford & Paglen (2021): "Excavating AI" (constitutive critique)
  - Prabhu & Birhane (2020): "Large image datasets: A pyrrhic win for computer vision?" (exclusions)
  - Yang et al. (2020): "Towards fairer datasets: Filtering and balancing..." (dataset biases)
- [ ] Document key facts:
  - Funding sources (NSF grants, university resources)
  - Dataset scope decisions (WordNet hierarchy, 1K vs 22K)
  - Collection methodology (Amazon Mechanical Turk, scraping)
  - Annotation decisions (verification process, label choices)
  - Exclusion criteria (what was filtered, what wasn't collected)
  - Known limitations (documented by creators)
  - Controversy timeline (when issues surfaced)
- [ ] Create research notes: `examples/imagenet/research_notes.md`

**Output:** Research notes with citations for all claims

---

### Task 2: Draft Layer 1 - Data Provenance

**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Document the constitutive conditions of ImageNet's creation.

**Acceptance Criteria:**

**L1.1: Dataset Overview**

- [ ] Dataset ID: `imagenet-1k-2012` or similar
- [ ] Name: ImageNet ILSVRC-2012-CLS (1,000-category classification dataset)
- [ ] Description: Large-scale image dataset for object recognition
- [ ] Version: 2012 (pre-cleaning)
- [ ] Access: Available via ImageNet website (registration required)

**L1.2: Provenance Details** (the critical section)

- [ ] **Source:** WordNet hierarchy + web image scraping (Google, Flickr, etc.)
- [ ] **Funding:** NSF grants (cite grant numbers), Princeton, Stanford
- [ ] **Collection methodology:**
  - WordNet synsets selected for visual recognizability
  - Images scraped from web via keyword search
  - Annotation via Amazon Mechanical Turk (AMT)
  - Quality control: Multiple annotators, majority vote
- [ ] **Collection period:** 2009-2012
- [ ] **Geographic scope:** Global web scraping, but...
- [ ] **Creators:** Fei-Fei Li, Jia Deng, et al. (Princeton → Stanford)

**L1.3: Inclusion/Exclusion Criteria** (the ORP contribution)

- [ ] **Documented exclusions:**
  - Non-visual WordNet categories excluded
  - Images below resolution threshold excluded
  - Copyrighted images (some) excluded
  - NSFW content filtered (to extent possible)
- [ ] **Undocumented/structural exclusions:**
  - Geographic bias: Web scraping favors Western internet
  - Language bias: English-language WordNet categories
  - Cultural bias: Categories reflect Western taxonomy
  - Socioeconomic bias: AMT worker demographics (Crawford & Paglen)
  - Temporal bias: 2009-2012 web, not representative of all time

**L1.4: Cleaning Decisions**

- [ ] Label verification process (AMT voting threshold)
- [ ] Image deduplication
- [ ] Removal of broken links
- [ ] Post-publication cleaning (offensive labels removed in 2019+)

**L1.5: Known Limitations** (cite creator acknowledgments + critics)

- [ ] Class imbalance (some categories over-represented)
- [ ] Label noise (acknowledged ~5-10% error rate)
- [ ] Geographic/cultural bias (not quantified initially)
- [ ] Offensive/problematic labels (discovered later)

**L1.6: Synthetic Elements**

- [ ] Present: false (real images)

**L1.7: Access**

- [ ] Public: true (with registration)
- [ ] License: Non-commercial research use

**L1.8: Attestation**

- [ ] Attested by: [Your name] (analyst, not creator)
- [ ] Date: 2026-04-XX
- [ ] Statement: "Provenance reconstructed from published sources [citations]"

**Output:** Layer 1 section in `examples/imagenet_training_data.yaml`

---

### Task 3: Draft Layer 2 - Consequence Simulation

**Owner:** Asbjørn
**Estimate:** 5 hours
**Priority:** Critical

**Description:**
Model how ImageNet's constitutive decisions affect downstream model behavior.

**Acceptance Criteria:**

**L2.1: Affected Population**

- [ ] **Primary:** AI researchers training models on ImageNet
- [ ] **Secondary:** Downstream users of ImageNet-trained models (facial recognition, object detection, etc.)
- [ ] **Tertiary:** People depicted in images (AMT workers, web scraped subjects)

**L2.2: Variables**

- [ ] Dataset composition (categories, images per category)
- [ ] Annotation quality (AMT worker agreement threshold)
- [ ] Exclusion criteria (cultural/geographic scope)
- [ ] Label taxonomy (WordNet hierarchy choices)

**L2.3: Scenarios** (how different constitutive choices → different outcomes)

**Scenario A: Current Constitution (as built)**

- [ ] Models trained on Western-biased image distribution
- [ ] Object categories reflect English WordNet taxonomy
- [ ] Offensive labels present (pre-2019)
- [ ] Geographic bias: Models perform worse on non-Western contexts
- [ ] Known outcome: Models trained on ImageNet show measurable bias (cite studies)

**Scenario B: Alternative - Global Representative Sampling**

- [ ] If: Images sampled proportionally from global web (not just English-speaking)
- [ ] If: WordNet taxonomy expanded with non-Western categories
- [ ] Expected outcome: Reduced geographic bias in trained models
- [ ] Uncertainty: High (no empirical data, but plausible)

**Scenario C: Alternative - Verified Non-Offensive Labels**

- [ ] If: All labels reviewed for cultural sensitivity before publication
- [ ] If: Community input on category choices
- [ ] Expected outcome: Fewer offensive category removals, earlier identification
- [ ] Uncertainty: Medium (process exists in other datasets)

**L2.4: Uncertainties**

- [ ] Exact impact of geographic bias on model performance (quantified for some models, not all)
- [ ] Counterfactual outcomes (Scenario B/C never implemented)
- [ ] Downstream amplification effects (how bias compounds in fine-tuned models)

**Output:** Layer 2 section demonstrating consequence modeling

---

### Task 4: Draft Layer 3 - Empathy Mapping

**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Critical

**Description:**
Identify affected stakeholders, including those absent from dataset governance.

**Acceptance Criteria:**

**L3.1: Stakeholder Groups**

**Group 1: Dataset Creators** (Fei-Fei Li, Deng, et al.)

- [ ] Interest: Scientific contribution, academic credit
- [ ] Impact: Positive (career advancement, field impact)
- [ ] Representation: Full (they made the decisions)

**Group 2: AI Researchers** (users of ImageNet)

- [ ] Interest: Training data for models
- [ ] Impact: Positive (enabled deep learning revolution)
- [ ] Representation: High (active community, feedback loops)

**Group 3: AMT Workers** (annotators)

- [ ] Interest: Compensation for labor
- [ ] Impact: Mixed (paid for work, but low wages, no credit)
- [ ] Representation: None (no input on dataset decisions)
- [ ] Absent node: Worker demographics shape annotation quality (Crawford & Paglen)

**Group 4: People Depicted in Images**

- [ ] Interest: Privacy, consent, dignified representation
- [ ] Impact: Negative potential (scraped without consent, some offensive labels)
- [ ] Representation: None (no consent process in 2009-2012)
- [ ] Absent node: Faces in dataset had no voice in inclusion

**Group 5: Non-Western Communities**

- [ ] Interest: Fair representation in AI training data
- [ ] Impact: Negative (underrepresented → biased models)
- [ ] Representation: None (not consulted in taxonomy/collection)
- [ ] Absent node: Categories reflect Western taxonomy, not universal

**Group 6: People Affected by ImageNet-Trained Models**

- [ ] Interest: Fair, unbiased AI systems
- [ ] Impact: Variable (depends on deployment)
- [ ] Representation: None (not considered during dataset constitution)
- [ ] Absent node: Downstream impacts not modeled

**L3.2: Minority Stakeholder Analysis**

- [ ] AMT workers: Low-wage digital labor, no ownership
- [ ] Depicted individuals: Privacy violations, no consent
- [ ] Non-Western communities: Systematic exclusion from taxonomy
- [ ] These are the "absent nodes" in the experiential graph

**Output:** Layer 3 section with 6 stakeholder groups

---

### Task 5: Draft Layer 4 - Accountability Ledger

**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Document major constitutive decisions made during ImageNet creation.

**Acceptance Criteria:**

**Decision 1: Taxonomy Source**

- [ ] Decision: Use WordNet hierarchy as category source
- [ ] Decision maker: Fei-Fei Li, Jia Deng (leads)
- [ ] Date: ~2009
- [ ] Rationale: WordNet is comprehensive, hierarchical, well-established
- [ ] Alternative considered: Custom taxonomy (rejected: too resource-intensive)
- [ ] Source: Deng et al. (2009) paper, Section 3

**Decision 2: Annotation Method**

- [ ] Decision: Use Amazon Mechanical Turk for labeling
- [ ] Decision maker: ImageNet team
- [ ] Date: ~2009
- [ ] Rationale: Scalable, cost-effective, proven for similar tasks
- [ ] Alternative considered: Expert annotators (rejected: too expensive/slow)
- [ ] Source: Deng et al. (2009), Section 4

**Decision 3: Quality Control Threshold**

- [ ] Decision: Multiple annotators per image, majority vote
- [ ] Decision maker: ImageNet team
- [ ] Date: ~2009
- [ ] Rationale: Balance accuracy and cost
- [ ] Parameters: [specific threshold from paper]
- [ ] Source: Deng et al. (2009), annotation protocol

**Decision 4: Offensive Label Removal**

- [ ] Decision: Remove offensive/derogatory category labels
- [ ] Decision maker: ImageNet team (post-publication)
- [ ] Date: 2019 (after criticism)
- [ ] Rationale: Ethical concerns raised by community
- [ ] Alternative considered: Full dataset review (ongoing)
- [ ] Source: ImageNet team blog post, news coverage

**Decision 5: Public Release vs Restricted Access**

- [ ] Decision: Require registration but make freely available for research
- [ ] Decision maker: ImageNet team
- [ ] Date: ~2010
- [ ] Rationale: Maximize research impact while tracking usage
- [ ] Alternative: Fully open (rejected: copyright/ethical concerns)

**L4 Meta-Note:**

- [ ] Acknowledge: This ledger is **reconstructed** from published sources
- [ ] Not a real-time log (dataset predates ORP)
- [ ] Demonstrates what L4 would capture if ORP existed in 2009

**Output:** Layer 4 section with 5+ major decisions

---

### Task 6: Draft Layer 5 - Fork Registry

**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Document ImageNet variants and how they address original dataset issues.

**Acceptance Criteria:**

**Fork 1: ImageNet-V2** (Recht et al., 2019)

- [ ] Fork type: Test set revision
- [ ] Rationale: Original test set potentially overfit
- [ ] Changes: New test images, same categories
- [ ] Status: Published, widely used
- [ ] Relationship: Sibling (fixes methodology, not constitution)

**Fork 2: ImageNet-R** (Hendrycks et al., 2020)

- [ ] Fork type: Robustness benchmark
- [ ] Rationale: Test model robustness to distribution shift
- [ ] Changes: Artistic renditions, sketches, not photos
- [ ] Relationship: Derivative (same categories, different image distribution)

**Fork 3: ImageNet with Cleaned Labels** (Northcutt et al., 2021)

- [ ] Fork type: Label correction
- [ ] Rationale: Identify and fix annotation errors
- [ ] Changes: Corrected labels for ~5-10% of images
- [ ] Relationship: Revision (addresses L1 known limitation)

**L5 Meta-Note:**

- [ ] These are technical forks (same governance, different data)
- [ ] No "constitutive forks" yet (alternative funding/taxonomy/scope)
- [ ] ORP L5 would enable: Someone proposing "Global Representative ImageNet" with different exclusion criteria

**Output:** Layer 5 section with 3 documented forks

---

### Task 7: Validate and Refine

**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Ensure ImageNet example validates and meets quality standards.

**Acceptance Criteria:**

- [ ] Run: `orp validate examples/imagenet_training_data.yaml`
- [ ] Result: Passes validation (ORP-Full compliant)
- [ ] All citations verified (papers exist, quotes accurate)
- [ ] Tone check: Descriptive not prescriptive (ORP doesn't say ImageNet is bad, just documents its constitution)
- [ ] Length check: Substantive in all layers (not placeholder text)
- [ ] Cross-reference: Claims align with academic paper arguments
- [ ] Comparison: As detailed as Danish property tax example

**Output:** Validated, high-quality ORP-Full document

---

### Task 8: Write Accompanying Documentation

**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Create README for ImageNet example explaining context and methodology.

**Acceptance Criteria:**

- [ ] Create: `examples/imagenet/README.md`
- [ ] Explains:
  - Why ImageNet was chosen (most influential AI training dataset)
  - What this example demonstrates (constitutive problem in AI training data)
  - Methodology: Reconstructed from published sources (not primary research)
  - Limitations: Post-hoc analysis, not real-time governance
  - How to use: Reference example for AI datasets
- [ ] Links to key sources (Crawford & Paglen, original papers)
- [ ] Notes: This is descriptive analysis, not critique of creators
- [ ] Comparison: How this differs from Model Cards/Datasheets

**Output:** `examples/imagenet/README.md`

---

### Task 9: Integrate into Documentation Ecosystem

**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Link ImageNet example throughout docs and update examples showcase.

**Acceptance Criteria:**

- [ ] Update main README.md:
  - Add ImageNet to examples list
  - "Two worked examples: policy (Danish tax) and AI (ImageNet)"
- [ ] Update docs site examples page:
  - ImageNet example with summary
  - Link to full YAML and README
  - Comparison table: Danish vs ImageNet (domain, compliance, depth)
- [ ] Update CLAUDE.md:
  - Add ImageNet to examples section
  - Note: Second domain demonstration complete
- [ ] Update academic paper:
  - Section 5 (ORP Operationalization): Add ImageNet case
  - Abstract: Note "demonstrated in policy and AI domains"

**Output:** ImageNet integrated across all docs

---

## Success Criteria

### Completion Criteria

- [ ] All 9 tasks completed
- [ ] `examples/imagenet_training_data.yaml` passes `orp validate`
- [ ] ORP-Full compliance (all 5 layers substantive)
- [ ] All claims cited to published sources
- [ ] Integrated into docs ecosystem

### Quality Criteria

- [ ] As detailed as Danish property tax example
- [ ] Demonstrates all 5 ORP layers meaningfully
- [ ] Shows "absent node problem" concretely
- [ ] Tone: Descriptive analysis, not critique
- [ ] Citations verifiable
- [ ] Suitable for academic paper inclusion

### Impact Criteria (Academic Paper)

- [ ] Strengthens paper's empirical foundation
- [ ] Demonstrates cross-domain applicability
- [ ] Shows ORP addresses AI governance gap
- [ ] Provides concrete example of constitutive problem
- [ ] Referenced in paper Section 5

---

## Dependencies

**Depends on:**

- Sprint 1.7.1 (governance docs, can cite example review process)
- Crawford & Paglen's "Excavating AI" (foundational research)

**Enables:**

- Sprint 1.7.5 (paper submission with 2 examples)
- Future Sprint: ORP-AI domain extension (ImageNet as reference)
- Community examples (demonstrates process for dataset analysis)

---

## Risks and Mitigations

### Risk 1: Sources incomplete/contradictory

**Mitigation:** Use multiple sources, cite uncertainties, note gaps in L2

### Risk 2: Appears as critique of Fei-Fei Li/creators

**Mitigation:** Tone check, note timing (2009 standards different), frame as system-level not individual-level

### Risk 3: Too time-consuming (7 days aggressive)

**Mitigation:** Start with ORP-Standard (L1-L3), expand to Full if time allows

### Risk 4: Citations become stale

**Mitigation:** All sources from 2009-2021 (stable historical record)

---

## Documentation Updates

- [ ] Add ImageNet to examples/ directory
- [ ] Update docs site examples showcase
- [ ] Update CLAUDE.md
- [ ] Update README.md
- [ ] Reference in academic paper

---

## Retrospective Notes

(To be completed at sprint end)

### What Went Well

- [TBD]

### What Didn't Go Well

- [TBD]

### Lessons Learned

- [TBD]

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-08
**Target Completion:** 2026-04-15
**Estimated Effort:** 33 hours over 7 days

---

## Research Starting Points

### Key Papers (to read first)

1. Deng et al. (2009): "ImageNet: A Large-Scale Hierarchical Image Database"
2. Crawford & Paglen (2021): "Excavating AI: The politics of images in machine learning training sets"
3. Prabhu & Birhane (2020): "Large image datasets: A pyrrhic win for computer vision?"

### Supplementary Sources

- Russakovsky et al. (2015): ILSVRC paper
- ImageNet website documentation
- Blog posts/talks by Fei-Fei Li on dataset creation
- News coverage of offensive label controversy (2019)
