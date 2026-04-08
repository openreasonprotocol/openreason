# Sprint 1.7.3.2: Common Crawl Training Data Example (ORP-Full)

**Version:** `sprint-1.7.3.2`
**Parent Sprint:** `sprint-1.7.3` (Foundation for Expansion - Worked Examples)
**Status:** Not Started
**Start Date:** 2026-04-15 (after LAION-5B completion)
**Target End Date:** 2026-04-22 (7 days)

**Code Target Version:** `v0.6.2`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Create a rigorous ORP-Full document for Common Crawl (petabyte-scale web corpus, 2008-present), demonstrating that ORP applies to continuously-evolving "living datasets" and surfacing linguistic/cultural exclusions that shape all modern Large Language Models (GPT, Claude, LLaMA, etc.).

---

## Strategic Importance

This is **critical scalability and temporal test** for ORP:
- **Largest dataset ever documented**: Petabytes of text (vs gigabytes for ImageNet/LAION)
- **Living dataset**: Monthly releases since 2008 (not static snapshot)
- **Universal LLM foundation**: Feeds GPT, Claude, LLaMA, PaLM, Gemini (virtually all language models)
- **Linguistic extinction crisis**: 90%+ English → low-resource languages disappearing
- **Tests ORP's temporal dimension**: How do you document a dataset that evolves monthly?
- **Tests ORP's scale limits**: Can provenance be documented for billions of documents?

---

## Why Common Crawl Is Different from ImageNet/LAION

### Scale
- ImageNet: 1.2M images (~150GB)
- LAION-5B: 5B image URLs (~240TB images if downloaded)
- **Common Crawl: 250+ billion pages** (~3 petabytes compressed, 2008-2024)

### Temporal Structure
- ImageNet: Static (2009-2012, frozen)
- LAION-5B: Static (March 2022 snapshot)
- **Common Crawl: Living** (monthly releases, continuous growth)

### Modality
- ImageNet/LAION: Images (visual)
- **Common Crawl: Text** (linguistic, cultural)

### Absent Nodes
- ImageNet: AMT workers, depicted individuals
- LAION: CSAM victims, medical patients
- **Common Crawl: Entire linguistic communities** (7,000+ languages, 90%+ excluded)

### Harm Type
- ImageNet: Bias (demographic), dignity (offensive labels)
- LAION: Safety (CSAM), legal (HIPAA)
- **Common Crawl: Cultural erasure** (language death, knowledge loss)

### ORP Challenge
Can ORP document:
- **Temporal evolution** (how do layers change month-to-month?)
- **Scale-appropriate provenance** (can't enumerate billions, need statistical sampling)
- **Linguistic diversity metrics** (how do you quantify language exclusion?)
- **Ecosystem-level consequences** (language death, not just model bias)

**Expected discovery**: ORP needs **"ORP-Living" compliance level** and **sampling methodology**

---

## Scope

### In Scope
- **ORP-Full** (all 5 layers) for Common Crawl corpus
- Focus on **constitutional decisions** (what gets crawled, how, by whom)
- Time scope: **2008-2024** (full history to present)
- Linguistic diversity analysis (7,000+ languages → 90% English reality)
- Demonstrates ORP's application to **living, petabyte-scale datasets**

### Dataset Choice: Common Crawl
**Full name:** Common Crawl Open Repository of Web Crawl Data
**Started:** 2008 (originally at University of Maryland, now non-profit)
**Scale:** 250+ billion web pages, 3+ petabytes compressed
**Purpose:** Open corpus of web data for research (alternative to proprietary crawls)
**Impact:** Training data for GPT-2/3/4, Claude, LLaMA, PaLM, Gemini, virtually all LLMs

**Why Common Crawl:**
- Most influential text dataset in AI history
- Feeds virtually all major language models
- Living dataset (tests ORP's temporal handling)
- Extreme scale (tests ORP's scalability limits)
- Linguistic exclusion (demonstrates cultural erasure)
- Public, transparent, citeable

**Scope limitation:**
- Focus on **crawl methodology and exclusions**, not content analysis (too large)
- Sample-based analysis (representative snapshots, not exhaustive)
- Linguistic diversity focus (7,000+ languages vs 90% English reality)

### Explicitly Out of Scope
- GPT/Claude/LLaMA models (that's model governance, not data governance)
- Specific Common Crawl archives (CC-MAIN-2024-01, etc.) - document methodology, not each snapshot
- Content moderation decisions (too large to enumerate)
- Individual website inclusion/exclusion (billions of sites, document criteria not list)
- New primary research (use existing linguistic studies, Common Crawl statistics)

---

## Key Research Questions

### For Layer 1 (Data Provenance):
1. Who funds Common Crawl? (Non-profit, but donors?)
2. What is crawl methodology? (Breadth-first? Seed URLs? Politeness?)
3. What gets crawled? (Entire web? Filtered? Language restrictions?)
4. What gets **excluded**? (Paywalls, robots.txt, non-English bias?)
5. How is linguistic diversity measured? (What % of 7,000+ languages represented?)
6. Who attests to data quality? (Common Crawl Foundation)

### For Layer 2 (Consequence Simulation):
1. If 90% English → what happens to low-resource languages in LLMs?
2. Counterfactual: Common Crawl with proportional linguistic diversity?
3. What is cost of linguistic inclusivity? (Crawl non-English web, compute, storage)
4. Downstream: How does CC linguistic bias → GPT linguistic bias?

### For Layer 3 (Empathy Mapping):
1. **Linguistic communities** (7,000+ languages): Who are absent nodes?
2. **Low-resource languages** (endangered, <1M speakers): Impact of exclusion?
3. **Global South web** (under-indexed, under-crawled): What gets missed?
4. **Future generations**: What knowledge is lost (not archived)?

### For Layer 4 (Accountability Ledger):
1. Who decided crawl methodology? (Common Crawl Foundation, when?)
2. Who decided seed URL list? (Starting points for crawl)
3. Who decided politeness policy? (Request rate limits)
4. Who decided language neutrality? (Or lack thereof - English bias structural?)
5. Who decided monthly release cycle? (Frequency vs thoroughness trade-off)

### For Layer 5 (Fork Registry):
1. Are CC-MAIN-2024-01, CC-MAIN-2024-02, etc. "forks" or "versions"?
2. Filtered subsets (C4, mC4, The Pile): Are these forks?
3. Potential fork: "Common Crawl Multilingual" with proportional language sampling?

---

## Tasks

### Task 1: Research Common Crawl Constitution History
**Owner:** Asbjørn
**Estimate:** 8 hours
**Priority:** Critical

**Description:**
Gather sources documenting Common Crawl's constitution, with focus on linguistic exclusions.

**Acceptance Criteria:**
- [ ] Read/review key sources:
  - Common Crawl Foundation: "About" page, blog posts (methodology)
  - Academic papers using Common Crawl (how they describe it)
  - Linguistic studies: Bender et al. (2021) "On the Dangers of Stochastic Parrots"
  - Joshi et al. (2020): "The State and Fate of Linguistic Diversity and Inclusion in the NLP World"
  - Bender (2019): "The #BenderRule: On Naming the Languages We Study"
  - Common Crawl statistics pages (size, language distribution)
  - OpenAI GPT-2/3 papers (describe CC as training data)
- [ ] Document key facts:
  - Funding sources (who pays for petabyte-scale crawling?)
  - Crawl methodology (breadth-first, seed URLs, politeness, frequency)
  - Language distribution (% English, % other languages)
  - Temporal evolution (how has CC changed 2008-2024?)
  - Exclusion criteria (robots.txt, paywalls, what else?)
  - Known limitations (documented by CC Foundation)
  - Linguistic bias (how much of 7,000+ languages are represented?)
- [ ] Create research notes: `examples/common_crawl/research_notes.md`

**Output:** Research notes with citations

**Key sources to locate:**
- Common Crawl Foundation website documentation
- Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the Dangers of Stochastic Parrots. FAccT 2021.
- Joshi, P., Santy, S., Budhiraja, A., et al. (2020). The State and Fate of Linguistic Diversity and Inclusion in the NLP World. ACL 2020.
- Brown et al. (2020). GPT-3 paper (describes Common Crawl use)

---

### Task 2: Draft Layer 1 - Data Provenance
**Owner:** Asbjørn
**Estimate:** 8 hours
**Priority:** Critical

**Description:**
Document Common Crawl's constitution, with emphasis on scale and linguistic exclusions.

**Acceptance Criteria:**

**L1.1: Dataset Overview**
- [ ] Dataset ID: `common-crawl-2008-2024` (full corpus)
- [ ] Name: Common Crawl Open Repository of Web Crawl Data
- [ ] Description: Monthly web crawl archives (2008-present), 250B+ pages, 3PB+ compressed
- [ ] Version: **Living dataset** (monthly releases: CC-MAIN-YYYY-MM)
- [ ] Access: Open (S3 buckets, free via AWS Open Data Program)

**L1.2: Provenance Details**
- [ ] **Source:** Public web (global, but English-dominated)
- [ ] **Funding:** Common Crawl Foundation (non-profit), AWS (S3 hosting), undisclosed donors
- [ ] **Collection methodology:**
  - Breadth-first web crawl (seed URLs → follow links)
  - Monthly crawl cycles (typically 1st-15th of month)
  - Politeness policy (respect robots.txt, rate limits)
  - No language filtering (but English-dominated seed URLs?)
  - No content filtering (archive as-is, including spam/malware/hate speech)
- [ ] **Collection period:** 2008-present (16+ years, ongoing)
- [ ] **Geographic scope:** Global web, but Western/English-speaking heavily over-represented
- [ ] **Creators:** Common Crawl Foundation, volunteers, infrastructure partners

**L1.3: Inclusion/Exclusion Criteria**

**Documented inclusions:**
- [ ] Any public web page (HTTP/HTTPS accessible)
- [ ] Respects robots.txt (won't crawl disallowed pages)
- [ ] All languages (in principle)
- [ ] HTML, PDF, other document formats

**Documented exclusions:**
- [ ] Paywalled content (can't access)
- [ ] Authenticated content (login required)
- [ ] Robots.txt disallowed (respects webmaster preferences)
- [ ] Rate-limited sites (politeness policy prevents aggressive crawling)
- [ ] Dynamic content (JavaScript-rendered, may be incomplete)

**CRITICAL UNDOCUMENTED/STRUCTURAL EXCLUSIONS:**
- [ ] **90%+ English content** (despite 7,000+ languages globally)
  - Cause: Seed URLs English-biased (start with major English sites)
  - Cause: Web itself English-dominated (but not 90% - more like 60%)
  - Result: Low-resource languages systematically under-represented
- [ ] **Global South web under-crawled**
  - Cause: Fewer outbound links from Western web
  - Cause: Infrastructure (slower servers, less stable hosting)
  - Result: African, Central Asian, Pacific Island content missed
- [ ] **Endangered languages virtually absent**
  - 7,000+ languages globally
  - ~3,000 endangered (<10K speakers)
  - Common Crawl: <100 languages with substantive content
  - Result: **Language death accelerated** (not archived before extinction)
- [ ] **Historical web lost**
  - Common Crawl started 2008, web started 1991
  - 17 years of web history not archived (unless via Internet Archive)
  - Result: Pre-2008 cultural artifacts, languages, knowledge lost
- [ ] **Ephemeral content missed**
  - Social media (Twitter/X, Facebook, Reddit) heavily restricted via robots.txt or API
  - Monthly crawl cycle misses short-lived content (deleted posts, temporary pages)
  - Result: Conversational language, informal registers under-represented

**L1.4: Cleaning Decisions**
- [ ] **No cleaning** (archive as-is - spam, malware, hate speech all included)
- [ ] Deduplication: URL-based (same URL → one entry per crawl)
- [ ] Format: WARC (Web ARChive format - standard)
- [ ] Post-crawl processing: Users extract/clean (Common Crawl provides raw data)

**L1.5: Known Limitations**
- [ ] **English bias** (acknowledged by researchers, not CC Foundation prominently)
- [ ] **Dynamic content incomplete** (JavaScript rendering challenges)
- [ ] **Spam and low-quality content** (not filtered - users must clean)
- [ ] **Temporal gaps** (sites that change/delete between monthly crawls)
- [ ] **Crawl coverage incomplete** (can't reach entire web in one month)

**L1.6: Synthetic Elements**
- [ ] Present: false (real web pages, though may include AI-generated content on web)

**L1.7: Access**
- [ ] Public: true (S3 buckets, free download)
- [ ] License: Various (each page retains original license, CC doesn't claim copyright)
- [ ] Structure: **Living dataset** (monthly releases, S3 paths: s3://commoncrawl/crawl-data/CC-MAIN-YYYY-WW/)

**L1.8: Attestation**
- [ ] Attested by: [Your name] (analyst)
- [ ] Date: 2026-04-XX
- [ ] Statement: "Provenance reconstructed from Common Crawl Foundation docs, academic papers, linguistic diversity research. Linguistic exclusion claims based on statistical studies (Joshi et al. 2020, Bender 2021). Common Crawl Foundation's responses minimal (limited public communication)."

**ORP DISCOVERY**: Need **"living dataset" methodology** - how to document temporal evolution?

**Output:** Layer 1 section in `examples/common_crawl_training_data.yaml`

---

### Task 3: Draft Layer 2 - Consequence Simulation
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Model how Common Crawl's linguistic exclusions shape all downstream language models.

**Acceptance Criteria:**

**L2.1: Affected Population**
- [ ] **Primary:** AI researchers training language models (OpenAI, Anthropic, Meta, Google, etc.)
- [ ] **Secondary:** Billions using LLMs (GPT, Claude, LLaMA, Gemini, etc.)
- [ ] **Tertiary - CRITICAL ABSENT NODES:**
  - **Low-resource language communities** (6,900+ languages with <1% representation)
  - **Endangered language speakers** (~3,000 languages, <10K speakers each)
  - **Future generations** (languages going extinct before archived)

**L2.2: Variables**
- [ ] **Independent variables:**
  - Seed URL diversity (English-only vs multilingual starting points)
  - Crawl frequency (monthly vs continuous)
  - Linguistic inclusion target (90% English vs proportional diversity)
  - Infrastructure investment (more crawlers in Global South)
  - Partnership with linguistic archives (OLAC, Endangered Languages Project)
- [ ] **Dependent variables:**
  - Language distribution in CC (% of 7,000 languages represented)
  - LLM performance by language (accuracy, fluency, cultural appropriateness)
  - Language vitality (extinction rate, intergenerational transmission)
  - Cultural knowledge preservation (indigenous knowledge, oral traditions)

**L2.3: Scenarios**

**Scenario A: Current Constitution (2008-2024)**
- [ ] 90%+ English content (despite 7,000+ languages globally)
- [ ] <100 languages with substantive representation
- [ ] Monthly crawl (1-month cycle)
- [ ] Western-biased seed URLs
- [ ] Outcome: LLMs English-dominant, low-resource languages unusable, cultural knowledge lost

**Scenario B: Alternative - Proportional Linguistic Diversity**
- [ ] If: Seed URLs proportional to global speakers (Mandarin 15%, Spanish 6%, English 5%, Hindi 5%, etc.)
- [ ] If: Active crawling of low-resource language sites (partner with linguistic archives)
- [ ] Expected outcome: 1,000+ languages with usable representation (vs <100)
- [ ] Cost: 3-5x crawl infrastructure (more regions, more starting points), ~$10-50M annually
- [ ] Benefit: LLMs functional in majority of world's languages

**Scenario C: Alternative - Continuous Crawl (Not Monthly)**
- [ ] If: Continuous crawling (real-time, not 1-month batches)
- [ ] Then: Ephemeral content captured (social media, temporary pages)
- [ ] Cost: 10x infrastructure (always-on crawling vs monthly batches)
- [ ] Benefit: More complete linguistic diversity (informal registers, conversational language)

**Scenario D: Alternative - Partnership with Linguistic Archives**
- [ ] If: Integrate OLAC, Endangered Languages Project, indigenous language archives
- [ ] Then: Endangered languages archived before extinction
- [ ] Cost: Partnership overhead, storage for low-volume languages (~$1-5M annually)
- [ ] Benefit: Cultural preservation, 3,000+ endangered languages documented

**L2.4: Uncertainties**
- [ ] Exact language distribution in CC (not published, must be estimated)
- [ ] Counterfactual LLM performance (no model trained on proportionally diverse CC)
- [ ] Language extinction rate (accelerating, but exact numbers uncertain)
- [ ] Infrastructure cost (estimates vary widely)

**Output:** Layer 2 section demonstrating linguistic exclusion consequences

---

### Task 3: Draft Layer 3 - Empathy Mapping
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Identify stakeholders, with emphasis on **linguistic communities as absent nodes**.

**Acceptance Criteria:**

**L3.1: Stakeholder Groups**

**Group 1: Common Crawl Foundation**
- [ ] Interest: Open web archive, research infrastructure
- [ ] Impact: Positive (enabled open LLM ecosystem)
- [ ] Representation: Full (they make all decisions)

**Group 2: AI Labs** (OpenAI, Anthropic, Meta, Google, etc.)
- [ ] Interest: Training data for language models
- [ ] Impact: Positive (free, large-scale, open)
- [ ] Representation: High (major users, provide feedback)

**Group 3: English-Speaking Users** (billions)
- [ ] Interest: Functional LLMs in native language
- [ ] Impact: Massively positive (GPT/Claude work well in English)
- [ ] Representation: Structural (web/CC English-dominated)

**Group 4: LOW-RESOURCE LANGUAGE COMMUNITIES** (CRITICAL ABSENT NODE)
- [ ] Population: 6,900+ languages with <1% CC representation
- [ ] Interest: **Linguistic survival, cultural preservation, access to AI**
- [ ] Impact: **SEVERE HARM** - languages going extinct unarchived, LLMs unusable in native language
- [ ] Representation: **NONE** - not consulted in crawl methodology, seed URL selection
- [ ] Absent node: **Entire linguistic communities invisible**

**Group 5: ENDANGERED LANGUAGE SPEAKERS** (CRITICAL ABSENT NODE)
- [ ] Population: ~3,000 languages (<10K speakers), ~200M people
- [ ] Interest: **Language preservation before extinction**
- [ ] Impact: **IRREVERSIBLE HARM** - languages dying before archived
- [ ] Representation: **NONE**
- [ ] Absent node: Examples:
  - Ainu (Japan): ~10 speakers, not in CC
  - Navajo (USA): 170K speakers, minimal CC presence
  - Hundreds of Pacific Island languages: disappearing unarchived

**Group 6: Global South Web Publishers**
- [ ] Interest: Content discoverable, archived for posterity
- [ ] Impact: Mixed (in CC but under-represented due to crawl bias)
- [ ] Representation: Low (infrastructure barriers, fewer outbound links)

**Group 7: Future Generations**
- [ ] Interest: Access to ancestors' linguistic/cultural heritage
- [ ] Impact: Negative - languages/knowledge lost before archiving
- [ ] Representation: None (can't speak for unborn)
- [ ] Absent node: Inter-generational knowledge transfer broken

**Group 8: Linguists/Language Researchers**
- [ ] Interest: Preserve linguistic diversity for study
- [ ] Impact: Negative - data loss (can't study languages not archived)
- [ ] Representation: Low (some partnership with Endangered Languages Project, but minimal)

**L3.2: Harm Severity - CULTURAL ERASURE**

**NEW HARM TYPE** (beyond ImageNet bias, LAION safety):
- [ ] **Language death** = **cultural genocide** (UN definition)
- [ ] Harm is **irreversible** (once language extinct, cannot recover)
- [ ] Harm is **systemic** (not individual bias, but elimination of entire worldviews)

**Comparison**:
- ImageNet: Dignity harm (offensive labels) → **remediable** (remove labels)
- LAION: Safety harm (CSAM) → **remediable** (remove images)
- Common Crawl: **Existential harm** (language extinction) → **IRREVERSIBLE**

**L3.3: Net Welfare Assessment**
- [ ] Common Crawl enabled open LLM ecosystem (enormous benefit)
- [ ] English speakers benefit massively
- [ ] BUT: **6,900+ linguistic communities left behind**
- [ ] **3,000 languages at risk of extinction unarchived**
- [ ] Utilitarian calculation: Benefit to billions vs loss of 3,000 cultures?
- [ ] Conclusion: **Innovation does not justify cultural erasure**

**ORP DISCOVERY**: Need **"existential harm" category** (irreversible, eliminates entire communities)

**Output:** Layer 3 section with 8 stakeholder groups, **linguistic communities as absent nodes**

---

### Task 4: Draft Layer 4 - Accountability Ledger
**Owner:** Asbjørn
**Estimate:** 5 hours
**Priority:** High

**Description:**
Document Common Crawl's constitutive decisions, with focus on linguistic exclusions.

**Acceptance Criteria:**

**Decision 1: Breadth-First Crawl Methodology**
- [ ] Decision: Use breadth-first (vs depth-first) crawling
- [ ] Decision maker: Common Crawl Foundation
- [ ] Date: ~2008
- [ ] Rationale: Maximize coverage (reach many sites) vs depth (fully crawl fewer sites)
- [ ] Alternative: Depth-first (rejected: would miss long tail)
- [ ] Consequence: Favors well-linked sites (Western, English) over isolated sites (Global South, low-resource languages)

**Decision 2: Seed URL Selection**
- [ ] Decision: Starting point URLs for crawl
- [ ] Decision maker: Common Crawl Foundation
- [ ] Date: ~2008 (evolving)
- [ ] Rationale: [UNKNOWN - not publicly documented]
- [ ] Likely: Major sites (Wikipedia, news, popular domains)
- [ ] **CRITICAL GAP**: Seed URLs likely English-biased (not published, can't verify)
- [ ] Consequence: English-dominated results (90%+ English despite global web ~60% English)

**Decision 3: Monthly Crawl Cycle**
- [ ] Decision: Crawl once per month (not continuous)
- [ ] Decision maker: Common Crawl Foundation
- [ ] Date: ~2008
- [ ] Rationale: Balance thoroughness (complete crawl) vs freshness (frequent updates)
- [ ] Alternative: Continuous crawl (rejected: cost prohibitive)
- [ ] Consequence: Ephemeral content missed (deleted pages, temporary sites)

**Decision 4: No Content Filtering**
- [ ] Decision: Archive as-is (no spam filtering, no hate speech removal)
- [ ] Decision maker: Common Crawl Foundation
- [ ] Date: ~2008
- [ ] Rationale: Neutrality (don't editorialize), let users filter
- [ ] Alternative: Pre-filter (rejected: subjective, expensive)
- [ ] Consequence: Spam/malware/hate speech included (users must clean)

**Decision 5: No Linguistic Diversity Target**
- [ ] Decision: Crawl web "as-is," no proportional language sampling
- [ ] Decision maker: Common Crawl Foundation (implicit - no stated policy)
- [ ] Date: ~2008-present
- [ ] Rationale: [UNKNOWN - not addressed in public docs]
- [ ] Alternative: Proportional linguistic sampling (never considered? Never mentioned)
- [ ] **Consequence: 90%+ English, 6,900+ languages <1% representation**
- [ ] **This is the critical absent decision** - linguistic diversity never prioritized

**Decision 6: AWS Hosting Partnership**
- [ ] Decision: Host on AWS S3 (Open Data Program)
- [ ] Decision maker: Common Crawl Foundation + AWS
- [ ] Date: ~2010-2011
- [ ] Rationale: Free hosting (AWS sponsor), scalable infrastructure
- [ ] Alternative: Self-hosted (rejected: cost prohibitive)
- [ ] Consequence: Dependent on AWS (single point of failure), but enables scale

**Decision 7: Open Access (No Restrictions)**
- [ ] Decision: Free, unrestricted download
- [ ] Decision maker: Common Crawl Foundation
- [ ] Date: ~2008
- [ ] Rationale: Open web should be openly accessible
- [ ] Alternative: Gated access (rejected: anti-open-web philosophy)
- [ ] Consequence: Enables open LLMs (positive), but also malicious uses (negative)

**Output:** Layer 4 section with 7 decisions, **Decision 5 flagged as critical linguistic exclusion**

---

### Task 5: Draft Layer 5 - Fork Registry
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Medium

**Description:**
Document Common Crawl variants and potential linguistic inclusion forks.

**Acceptance Criteria:**

**Fork 1: C4 (Colossal Clean Crawled Corpus)** (Raffel et al., 2020)
- [ ] Fork type: Cleaned subset
- [ ] Creators: Google (T5 paper)
- [ ] Rationale: Remove spam, boilerplate, duplicates from Common Crawl
- [ ] Changes: ~156GB (vs 3PB raw CC), English-only, cleaned
- [ ] Status: Published, widely used (T5, GPT-Neo, etc.)
- [ ] Relationship: Filtered derivative
- [ ] **Linguistic note**: English-only subset (reduces diversity further)

**Fork 2: mC4 (Multilingual C4)** (Xue et al., 2021)
- [ ] Fork type: Multilingual cleaned subset
- [ ] Creators: Google (mT5 paper)
- [ ] Rationale: Extend C4 to 101 languages
- [ ] Changes: ~9.7TB across 101 languages (vs C4 English-only)
- [ ] Status: Published, used for mT5
- [ ] Relationship: Multilingual extension
- [ ] **Linguistic note**: 101 languages is improvement (vs 1) but still <2% of 7,000+ languages

**Fork 3: The Pile** (Gao et al., 2020)
- [ ] Fork type: Curated corpus including CC subset
- [ ] Creators: EleutherAI
- [ ] Rationale: Diverse text sources (CC + books + GitHub + arXiv + more)
- [ ] Changes: 825GB, curated domains
- [ ] Status: Published, used for GPT-NeoX
- [ ] Relationship: Integrates CC with other sources
- [ ] **Linguistic note**: English-dominant (like CC)

**Temporal "Forks" (Monthly Releases):**
- [ ] CC-MAIN-2024-01, CC-MAIN-2024-02, etc.
- [ ] Question: Are these "forks" or "versions"?
- [ ] **ORP decision**: Treat as versions (same methodology, temporal snapshots)
- [ ] Enables: **Version history tracking** (how has web/CC evolved over time?)

**Potential Forks (not yet created):**

**Potential Fork: Common Crawl Multilingual (CC-Multi)**
- [ ] Proposed: Proportional linguistic diversity target
- [ ] Methodology: Seed URLs proportional to global speakers, active crawling of low-resource sites
- [ ] Expected outcome: 1,000+ languages with substantive content (vs <100)
- [ ] Cost: 3-5x infrastructure (~$10-50M annually)
- [ ] Benefit: LLMs functional in majority of world's languages

**Potential Fork: Common Crawl Endangered (CC-Endangered)**
- [ ] Proposed: Partner with linguistic archives (OLAC, Endangered Languages Project)
- [ ] Methodology: Integrate archived linguistic data, actively crawl indigenous language sites
- [ ] Expected outcome: 3,000 endangered languages archived before extinction
- [ ] Cost: Partnership overhead (~$1-5M annually)
- [ ] Benefit: Cultural preservation, linguistic diversity for future

**Potential Fork: Common Crawl Continuous (CC-Live)**
- [ ] Proposed: Continuous crawling (not monthly batches)
- [ ] Methodology: Always-on distributed crawlers
- [ ] Expected outcome: Ephemeral content captured, fresher data
- [ ] Cost: 10x infrastructure (~$100M+ annually)
- [ ] Benefit: Social media, conversational language, informal registers

**Output:** Layer 5 section with 3 existing forks + temporal versioning + 3 potential forks

---

### Task 6: Validate and Document Schema Discoveries
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Document what Common Crawl revealed about ORP schema.

**Acceptance Criteria:**
- [ ] Run validation (expect errors)
- [ ] Document new discoveries:
  - **Living dataset methodology** (temporal evolution, version history)
  - **Scale-appropriate provenance** (statistical sampling vs enumeration)
  - **Linguistic diversity metrics** (how to quantify 7,000+ languages)
  - **Existential harm category** (language extinction, cultural erasure)
  - **Version vs fork distinction** (monthly releases)
- [ ] Estimate: Common Crawl adds 40-60 new schema issues
- [ ] Recommendations for ORP v0.2

**Output:** Validation report + schema discoveries

---

### Task 7: Write Accompanying Documentation
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Medium

**Description:**
Create README explaining Common Crawl example.

**Acceptance Criteria:**
- [ ] Create: `examples/common_crawl/README.md`
- [ ] Explains:
  - Why Common Crawl (universal LLM foundation)
  - Living dataset challenges
  - Linguistic exclusion as cultural erasure
  - Scale: petabytes vs gigabytes
  - Temporal evolution (2008-2024)
- [ ] Links to linguistic diversity research
- [ ] Comparison: ImageNet (bias), LAION (safety), Common Crawl (cultural erasure)

**Output:** `examples/common_crawl/README.md`

---

### Task 8: Schema Discovery Documentation
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** High

**Description:**
Document Common Crawl-specific schema discoveries.

**Acceptance Criteria:**
- [ ] Create: `docs/sprints/sprint-1.7.3.2-schema-discoveries.md`
- [ ] New issues:
  - Living dataset handling
  - Temporal version tracking
  - Scale-appropriate methods
  - Linguistic diversity metrics
  - Existential harm taxonomy
- [ ] Compare: ImageNet (85 errors), LAION (30-50), Common Crawl (40-60)
- [ ] Total: ~155-195 schema issues across 3 AI examples

**Output:** Schema discovery report

---

## Success Criteria

### Completion Criteria
- [ ] All 8 tasks completed
- [ ] `examples/common_crawl_training_data.yaml` created (ORP-Full)
- [ ] Living dataset methodology documented
- [ ] Linguistic exclusion demonstrated
- [ ] Schema discoveries documented

### Quality Criteria
- [ ] Tests ORP at extreme scale (petabytes)
- [ ] Tests ORP on temporal evolution (2008-2024)
- [ ] Shows existential harm (language extinction)
- [ ] Demonstrates cultural erasure consequences

### Impact Criteria
- [ ] Reveals ORP's scalability limits
- [ ] Reveals ORP's temporal handling needs
- [ ] Strengthens paper (demonstrates pattern: bias → safety → erasure)

---

## Dependencies

**Depends on:**
- Sprint 1.7.3.1 (LAION-5B - provides safety harm template)

**Enables:**
- Sprint 1.7.3.3 (GitHub Copilot - tests code modality)
- Sprint 1.7.3.4 (Schema revision - consolidates all discoveries)

---

## Risks and Mitigations

### Risk 1: Common Crawl Data Not Public
**Mitigation:** Language distribution statistics from academic research (Joshi et al., Bender). Use estimates, document uncertainties.

### Risk 2: Linguistic Extinction Claims Contested
**Mitigation:** Cite UNESCO endangered language classifications, linguistic diversity research. Acknowledge debate over language vs dialect.

### Risk 3: Scale Overwhelming
**Mitigation:** Sample-based analysis, representative snapshots. Document methodology limitations.

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-15
**Target Completion:** 2026-04-22
**Estimated Effort:** 45 hours over 7 days
