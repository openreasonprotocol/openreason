# Sprint 1.7.3.3: GitHub Copilot Training Data Example (ORP-Full)

**Version:** `sprint-1.7.3.2`
**Parent Sprint:** `sprint-1.7.3` (Foundation for Expansion - Worked Examples)
**Status:** Not Started
**Start Date:** 2026-04-22 (after Common Crawl completion)
**Target End Date:** 2026-04-29 (7 days)

**Code Target Version:** `v0.6.3`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Create a rigorous ORP-Full document for GitHub Copilot's training data (public code repositories, 2021), demonstrating that ORP applies to code datasets and surfacing license compliance issues (GPL, copyleft) that existing AI documentation standards do not adequately address. Tests ORP's **legal dimension** (beyond ethical/safety).

---

## Strategic Importance

This is **critical legal/licensing test** for ORP:
- **Code modality** (not images/text): Tests ORP on new data type
- **License crisis**: Open source developers vs AI companies (existential threat to open source ecosystem)
- **Legal dimension**: Copyright, GPL copyleft, derivative works (beyond ethics/safety)
- **Absent node: Future contributors**: Developers who stop contributing because AI trained on their code without attribution
- **Ecosystem degradation**: Open source sustainability crisis (tragedy of the commons)
- **Contemporary relevance**: Active litigation (GitHub Copilot class action, 2022-present)

---

## Why GitHub Copilot Is Different from ImageNet/LAION/Common Crawl

### Modality
- ImageNet/LAION: Images (visual recognition)
- Common Crawl: Text (natural language)
- **Copilot: Code** (programming languages, APIs, algorithms)

### Harm Type
- ImageNet: Bias (demographic), dignity (offensive labels)
- LAION: Safety (CSAM), privacy (medical imagery)
- Common Crawl: Cultural erasure (language extinction)
- **Copilot: Legal (copyright infringement), economic (free-riding), ecosystem (sustainability)**

### Absent Nodes
- ImageNet: AMT workers, depicted individuals
- LAION: CSAM victims, medical patients
- Common Crawl: Linguistic communities (6,900+ languages)
- **Copilot: Open source maintainers, future contributors, library ecosystems**

### Licensing Structure
- ImageNet/LAION: Images scraped (unclear copyright status)
- Common Crawl: Text (various licenses, often unclear)
- **Copilot: Code with explicit licenses** (MIT, GPL, Apache - legally binding)

### Legal Question
- ImageNet/LAION/CC: "Should have gotten consent" (ethical)
- **Copilot: "Did AI training violate license terms?"** (legal)

### ORP Challenge
Can ORP capture:
- **License obligations** (copyleft requires derivative works be open)
- **Attribution requirements** (many licenses require credit)
- **Legal risk** (copyright infringement, GPL violation)
- **Ecosystem effects** (developers leaving open source)
- **Future harms** (next generation of contributors deterred)

**Expected discovery**: ORP needs **"legal compliance layer"** or integration into L1/L4

---

## Scope

### In Scope
- **ORP-Full** (all 5 layers) for GitHub Copilot training data
- Focus on **constitutional decisions** (what code scraped, from where, license handling)
- License compliance analysis (MIT, GPL, Apache, proprietary)
- Demonstrates ORP's application to **legal/economic absent nodes**

### Dataset Choice: GitHub Copilot Training Data
**Training data:** Public GitHub repositories (estimated ~50-100 million repositories)
**Timeframe:** Pre-2021 (Copilot launched June 2021)
**Model:** OpenAI Codex (GPT-3 variant fine-tuned on code)
**Purpose:** AI pair programmer (suggests code completions)
**Impact:** Millions of developers use Copilot (2021-present)

**Why Copilot:**
- Most controversial code AI (active class action lawsuit)
- Explicitly trained on open source code
- License compliance central issue (GPL, attribution)
- Tests ORP on legal dimension (copyright, licensing)
- Demonstrates ecosystem harm (developer trust, sustainability)
- Public, documented controversy, citeable sources

**Scope limitation:**
- Focus on **training data** (GitHub repos), not Codex model architecture
- License compliance analysis, not full code content review
- Public repositories only (private repos excluded from training)

### Explicitly Out of Scope
- Codex model internals (model governance, not data governance)
- Copilot suggestions/outputs (deployment governance, not training data)
- Other code AI (CodeWhisperer, Tabnine, Bard) - focus on Copilot as exemplar
- Manual code review (too large - ~50M repos, billions of lines)
- Legal judgment (document facts, not litigate)

---

## Key Research Questions

### For Layer 1 (Data Provenance):
1. What code was scraped? (All public GitHub? Filtered? License restrictions?)
2. Who funded Copilot development? (GitHub/Microsoft)
3. What license types in training data? (% MIT, GPL, Apache, proprietary, none)
4. Was license compliance reviewed? (Did GitHub/OpenAI check GPL compatibility?)
5. What exclusion criteria? (Private repos excluded, but public repos filtered?)

### For Layer 2 (Consequence Simulation):
1. If Copilot trained on GPL code → are suggestions derivative works?
2. If yes → does Copilot violate GPL (requires derivative works be open)?
3. Counterfactual: Copilot trained only on permissive licenses (MIT, Apache)?
4. What would this cost? (Smaller dataset, worse performance?)

### For Layer 3 (Empathy Mapping):
1. **Open source maintainers**: Code used without attribution - impact?
2. **GPL authors**: Copyleft intent violated - impact?
3. **Future contributors**: Deterred from open source - impact?
4. **Library ecosystems**: Sustainability crisis - impact?

### For Layer 4 (Accountability Ledger):
1. Who decided to train on all public GitHub? (OpenAI? GitHub? Microsoft?)
2. Who decided not to filter by license? (Cost-benefit analysis?)
3. Who decided attribution not required? (Legal review?)
4. What alternatives were considered? (Permissive-only? Compensate authors?)

### For Layer 5 (Fork Registry):
1. Post-lawsuit changes (filtering, attribution)?
2. Potential fork: "Copilot-Permissive" (MIT/Apache only)?
3. Potential fork: "Copilot-Attributed" (cite original authors)?

---

## Tasks

### Task 1: Research Copilot Training Data Constitution
**Owner:** Asbjørn
**Estimate:** 8 hours
**Priority:** Critical

**Description:**
Gather sources documenting Copilot's training data, with focus on license issues.

**Acceptance Criteria:**
- [ ] Read/review key sources:
  - GitHub Copilot announcement (June 2021) - training data description
  - OpenAI Codex paper (Chen et al., 2021) - technical details
  - Class action lawsuit: Doe v. GitHub (filed Nov 2022) - legal claims
  - GitHub response to lawsuit - defenses
  - Open source community response (blog posts, petitions)
  - License distribution research: Allamanis et al. (2013) "Mining Software Repositories"
  - GPL compliance analysis: Software Freedom Conservancy statements
- [ ] Document key facts:
  - Training data size (~50M repos, estimated)
  - License distribution (% MIT, GPL, Apache, none)
  - Funding (GitHub/Microsoft, OpenAI partnership)
  - Exclusion criteria (private repos, but public filtered?)
  - Attribution mechanism (none initially, "code referencing" added later)
  - Known limitations (memorization, license violations)
  - Legal controversy timeline (launch June 2021 → lawsuit Nov 2022)
- [ ] Create research notes: `examples/github_copilot/research_notes.md`

**Output:** Research notes with citations

**Key sources to locate:**
- Chen, M., et al. (2021). Evaluating Large Language Models Trained on Code. arXiv:2107.03374.
- Doe v. GitHub, Inc., Case No. 4:22-cv-06823 (N.D. Cal. filed Nov. 3, 2022).
- Software Freedom Conservancy: "Give Up GitHub" campaign (June 2022).
- Eliott et al. (2024): Research on Copilot memorization and license reproduction.

---

### Task 2: Draft Layer 1 - Data Provenance
**Owner:** Asbjørn
**Estimate:** 8 hours
**Priority:** Critical

**Description:**
Document Copilot training data constitution, emphasizing license handling.

**Acceptance Criteria:**

**L1.1: Dataset Overview**
- [ ] Dataset ID: `github-copilot-training-2021`
- [ ] Name: GitHub Public Repositories (Copilot Training Corpus)
- [ ] Description: ~50-100M public GitHub repositories, pre-2021, used to train OpenAI Codex
- [ ] Version: Static (pre-June 2021 snapshot)
- [ ] Access: Not public (training data proprietary, but source code public on GitHub)

**L1.2: Provenance Details**
- [ ] **Source:** GitHub public repositories (all publicly accessible code)
- [ ] **Funding:** Microsoft (owns GitHub), OpenAI partnership
- [ ] **Collection methodology:**
  - Scraped all public GitHub repositories (pre-2021)
  - Excluded private repositories (GitHub terms compliance)
  - No license filtering (included MIT, GPL, Apache, proprietary, no-license)
  - No author consent process (relied on "public = fair use" argument)
- [ ] **Collection period:** Pre-2021 (exact timeframe not publicly disclosed)
- [ ] **Geographic scope:** Global (GitHub users worldwide)
- [ ] **Creators:** OpenAI (model), GitHub/Microsoft (data access)

**L1.3: Inclusion/Exclusion Criteria**

**Documented inclusions:**
- [ ] Any public GitHub repository (accessible without login)
- [ ] All programming languages (Python, JavaScript, Java, C++, etc.)
- [ ] All licenses (MIT, GPL, Apache, proprietary, none)
- [ ] README files, documentation, code comments

**Documented exclusions:**
- [ ] Private repositories (cannot access - GitHub terms compliance)
- [ ] Repositories with DMCA takedowns (legally required removal)

**CRITICAL UNDOCUMENTED/INADEQUATE EXCLUSIONS:**
- [ ] **GPL code NOT filtered** (copyleft requires derivative works be open-source)
  - GPL-2.0, GPL-3.0, AGPL widely represented in training data
  - Copilot suggestions potentially derivative works (legal question)
  - If derivative, Copilot violates GPL (commercial closed-source tool)
- [ ] **No attribution mechanism** (many licenses require credit to authors)
  - MIT, Apache, BSD require attribution in derivative works
  - Copilot provides no attribution initially (added "code referencing" later, limited)
  - Violates license terms even for permissive licenses
- [ ] **No author consent** (public ≠ consent for AI training)
  - Authors published under specific licenses (expectation: terms respected)
  - AI training not contemplated when licenses written (1990s-2010s)
  - Retroactive interpretation: "public = fair use for AI" contested
- [ ] **No compensation** (authors receive nothing despite commercial product)
  - GitHub Copilot is paid service ($10/month, $100/year per user)
  - Millions of users → hundreds of millions in revenue
  - Original authors: $0 compensation, no royalties, no acknowledgment

**L1.4: Cleaning Decisions**
- [ ] Deduplication: Repository-level (same repo counted once)
- [ ] Language filtering: Included all programming languages
- [ ] Size filtering: Unknown (very large files excluded? Not documented)
- [ ] Quality filtering: Unknown (low-quality code included? Not documented)

**L1.5: Known Limitations**
- [ ] **Memorization**: Copilot sometimes reproduces training code verbatim (license violation if code not permissive)
- [ ] **License blindness**: Copilot cannot identify license of suggested code (user doesn't know if GPL)
- [ ] **No attribution**: Even for licenses requiring it (MIT, Apache)
- [ ] **Bias**: Training data reflects GitHub demographics (Western, male-dominated)

**L1.6: Synthetic Elements**
- [ ] Present: false (real code from GitHub, though may include AI-generated code posted on GitHub)

**L1.7: Access**
- [ ] Public: false (training data proprietary)
- [ ] Original source: public (GitHub repositories accessible)
- [ ] License: Various (each repo retains original license, GitHub/OpenAI do not claim copyright on training data)

**L1.8: Attestation**
- [ ] Attested by: [Your name] (analyst)
- [ ] Date: 2026-04-XX
- [ ] Statement: "Provenance reconstructed from GitHub/OpenAI announcements, Codex paper, legal filings (Doe v. GitHub), open source community analysis. License distribution estimated from GitHub statistics. GitHub/OpenAI have not disclosed full training data methodology."

**ORP DISCOVERY**: Need **"license compliance" fields** in L1 (license distribution, compliance review, attribution mechanism)

**Output:** Layer 1 section in `examples/github_copilot_training_data.yaml`

---

### Task 3: Draft Layer 2 - Consequence Simulation
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Model how Copilot's license decisions affect open source ecosystem.

**Acceptance Criteria:**

**L2.1: Affected Population**
- [ ] **Primary:** Open source developers (millions on GitHub)
- [ ] **Secondary:** Copilot users (millions, may unknowingly use GPL-derived code)
- [ ] **Tertiary - CRITICAL ABSENT NODES:**
  - **GPL authors** (intent: copyleft → keep code open, violated by closed Copilot)
  - **Future contributors** (deterred from open source if AI free-rides)
  - **Library maintainers** (sustainability crisis: labor extracted, no compensation)

**L2.2: Variables**
- [ ] **Independent variables:**
  - License filtering (all vs permissive-only vs compensated)
  - Attribution mechanism (none vs code referencing vs full credit)
  - Compensation model (free-ride vs revenue-share vs flat fee)
  - Opt-out mechanism (none vs post-training vs pre-training)
- [ ] **Dependent variables:**
  - GPL compliance (violation vs compliant)
  - Developer trust (% willing to contribute to open source)
  - Ecosystem sustainability (maintainer burnout, project abandonment)
  - Legal liability (copyright infringement risk)

**L2.3: Scenarios**

**Scenario A: Current Constitution (as built - June 2021)**
- [ ] All public GitHub code (no license filtering)
- [ ] No attribution mechanism initially (added "code referencing" later, limited)
- [ ] No compensation (free-ride on open source labor)
- [ ] No pre-training opt-out
- [ ] Outcome: GPL potential violation, developer backlash, lawsuit filed

**Scenario B: Alternative - Permissive Licenses Only**
- [ ] If: Train only on MIT, Apache, BSD (no GPL, no AGPL)
- [ ] Then: GPL compliance not an issue
- [ ] Cost: Smaller dataset (~40-50% of GitHub), potentially worse performance
- [ ] Benefit: Legal risk minimized, GPL community appeased
- [ ] Uncertainty: Would performance degradation be significant?

**Scenario C: Alternative - Attribution Required**
- [ ] If: Copilot cites original authors when suggesting code
- [ ] Then: License compliance improved (MIT, Apache require attribution)
- [ ] Cost: UI complexity (show attribution per suggestion), performance (lookup overhead)
- [ ] Benefit: Respects author intent, builds developer trust
- [ ] Implemented partially: "Code referencing" (June 2022), but limited (only exact matches)

**Scenario D: Alternative - Revenue Sharing**
- [ ] If: GitHub/Microsoft shares Copilot revenue with code authors
- [ ] Then: Economic fairness, ecosystem sustainability
- [ ] Cost: ~$100M+ annually (millions of users × $100/year = $100M+, share with millions of authors)
- [ ] Complexity: How to attribute contributions (lines of code? Repo influence?)
- [ ] Benefit: Developer trust restored, open source sustainability
- [ ] Precedent: YouTube revenue sharing, Spotify royalties

**L2.4: Uncertainties**
- [ ] Legal precedent: Is AI training "fair use"? (courts haven't decided definitively)
- [ ] GPL interpretation: Are Copilot suggestions "derivative works"? (legal debate)
- [ ] Performance impact: Would permissive-only training significantly degrade quality? (untested)
- [ ] Developer response: Would revenue-sharing restore trust? (sentiment surveys suggest yes, but hypothetical)

**Output:** Layer 2 section demonstrating license compliance trade-offs

---

### Task 4: Draft Layer 3 - Empathy Mapping
**Owner:** Asbjørn
**Estimate:** 6 hours
**Priority:** Critical

**Description:**
Identify stakeholders, emphasizing **open source ecosystem as absent nodes**.

**Acceptance Criteria:**

**L3.1: Stakeholder Groups**

**Group 1: GitHub/Microsoft**
- [ ] Interest: Monetize GitHub data, competitive AI products
- [ ] Impact: Positive (revenue from Copilot, strategic AI advantage)
- [ ] Representation: Full (they made all decisions)

**Group 2: OpenAI**
- [ ] Interest: Codex model development, partnership with Microsoft
- [ ] Impact: Positive (technical advancement, training data access)
- [ ] Representation: Full (partnership with GitHub)

**Group 3: Copilot Users** (millions)
- [ ] Interest: Productivity (code suggestions), learning
- [ ] Impact: Positive (faster coding) + Negative (legal liability if suggestions GPL-derived)
- [ ] Representation: Customer voice (feedback loops)

**Group 4: GPL AUTHORS** (CRITICAL ABSENT NODE)
- [ ] Population: Millions of developers who chose GPL (copyleft intent)
- [ ] Interest: **Copyleft enforcement** (derivative works must be open)
- [ ] Impact: **SEVERE HARM** - intent violated (GPL code → closed commercial product)
- [ ] Representation: **NONE** - not consulted before training
- [ ] Absent node: Examples:
  - Linus Torvalds (Linux kernel, GPL-2.0) - not consulted
  - Richard Stallman (GNU, GPL-3.0) - not consulted
  - Thousands of GPL library authors - not consulted
- [ ] Legal status: GPL is legally binding contract (derivative works must be GPL)

**Group 5: OPEN SOURCE MAINTAINERS** (CRITICAL ABSENT NODE)
- [ ] Population: Millions of unpaid/underpaid maintainers
- [ ] Interest: **Recognition, sustainability, compensation**
- [ ] Impact: **ECONOMIC HARM** - labor extracted, no compensation, no credit
- [ ] Representation: **NONE**
- [ ] Absent node: Maintainer burnout crisis worsened
  - xkcd cartoon "Dependency": Modern infrastructure depends on unpaid maintainer
  - Copilot monetizes their labor → $0 return
  - Example: core-js maintainer Denis Pushkarev (millions of downloads, near-bankrupt)

**Group 6: FUTURE CONTRIBUTORS** (CRITICAL ABSENT NODE)
- [ ] Population: Next generation of open source developers
- [ ] Interest: **Incentive to contribute** (currently: learning, community, résumé)
- [ ] Impact: **DETERRENCE** - if AI free-rides, why contribute?
- [ ] Representation: **NONE** (cannot speak for unborn)
- [ ] Absent node: Tragedy of the commons
  - Current: Contribute → community benefits → I benefit
  - Copilot: Contribute → AI trained → Microsoft profits → I get nothing
  - Rational response: Don't contribute (ecosystem collapses)

**Group 7: Permissive License Authors** (MIT, Apache, BSD)
- [ ] Interest: Attribution (MIT requires credit)
- [ ] Impact: Negative (no attribution mechanism initially)
- [ ] Representation: Low (not consulted)
- [ ] Absent node: Even permissive licenses have conditions (attribution)

**Group 8: Software Freedom Community**
- [ ] Interest: Copyleft enforcement, open source sustainability
- [ ] Impact: Negative (GPL violated, ecosystem threatened)
- [ ] Representation: External critics (Software Freedom Conservancy, FSF)
- [ ] Outcome: "Give Up GitHub" campaign (June 2022) - boycott call

**L3.2: Harm Severity - ECOSYSTEM DEGRADATION**

**NEW HARM TYPE** (beyond bias, safety, cultural erasure):
- [ ] **Ecosystem harm** = **tragedy of the commons**
- [ ] Harm is **systemic** (not individual, but collective rationality breakdown)
- [ ] Harm is **future-oriented** (deterring next generation of contributors)
- [ ] Harm is **economic** (labor extracted without compensation)

**Comparison**:
- ImageNet: Dignity harm (offensive labels) → individual
- LAION: Safety harm (CSAM) → individual victims
- Common Crawl: Cultural harm (language death) → communities
- **Copilot: Ecosystem harm (sustainability crisis)** → **collective future**

**L3.3: Net Welfare Assessment**
- [ ] Copilot benefits users (productivity, learning)
- [ ] Copilot benefits GitHub/Microsoft (revenue, competitive advantage)
- [ ] BUT: **Open source ecosystem threatened**
  - GPL authors: Intent violated (copyleft → closed product)
  - Maintainers: Labor extracted (no compensation, burnout)
  - Future contributors: Deterred (rational to free-ride)
- [ ] Tragedy of the commons: Individual rationality (free-ride on AI) → collective harm (ecosystem collapse)
- [ ] Conclusion: **Short-term productivity gains do not justify long-term ecosystem destruction**

**ORP DISCOVERY**: Need **"ecosystem harm" category** (future-oriented, collective, sustainability)

**Output:** Layer 3 section with 8 stakeholder groups, **open source ecosystem as absent node**

---

### Task 5: Draft Layer 4 - Accountability Ledger
**Owner:** Asbjørn
**Estimate:** 5 hours
**Priority:** High

**Description:**
Document Copilot's constitutive decisions, focus on license handling.

**Acceptance Criteria:**

**Decision 1: Train on All Public GitHub**
- [ ] Decision: Scrape all public repositories (no license filtering)
- [ ] Decision maker: OpenAI + GitHub/Microsoft
- [ ] Date: ~2020-2021 (pre-launch)
- [ ] Rationale: Maximize dataset size, maximize performance
- [ ] Alternative considered: Permissive-only (rejected: smaller dataset, worse performance assumed)
- [ ] **CRITICAL: No evidence alternatives were seriously considered** (not documented publicly)
- [ ] Consequence: GPL potential violation, developer backlash, lawsuit

**Decision 2: No Pre-Training Author Consent**
- [ ] Decision: Do not seek author permission before training
- [ ] Decision maker: OpenAI + GitHub/Microsoft
- [ ] Date: ~2020-2021
- [ ] Rationale: "Public = fair use" legal theory, impractical to contact millions
- [ ] Alternative: Opt-in (rejected: too few would opt-in), Opt-out (not offered until after launch)
- [ ] Consequence: Violated author expectations (published under license ≠ consent for AI)

**Decision 3: No Attribution Mechanism (Initially)**
- [ ] Decision: Copilot suggestions provide no credit to original authors
- [ ] Decision maker: OpenAI + GitHub/Microsoft
- [ ] Date: June 2021 (launch)
- [ ] Rationale: Technical complexity (hard to attribute code snippets to original authors)
- [ ] Alternative: Full attribution (rejected: UX complexity, performance overhead)
- [ ] Consequence: Violates MIT, Apache, BSD license terms (attribution required)
- [ ] **Partial reversal**: "Code referencing" feature added June 2022 (shows matches if >150 characters, rarely triggers)

**Decision 4: Commercial Pricing (No Revenue Sharing)**
- [ ] Decision: Charge users $10/month, $100/year (no revenue share with code authors)
- [ ] Decision maker: GitHub/Microsoft
- [ ] Date: June 2021
- [ ] Rationale: Standard commercial AI pricing, free-ride on open source "tragedy of the commons" (everyone does it)
- [ ] Alternative: Revenue sharing (never publicly discussed - not considered?)
- [ ] Consequence: Economic exploitation perception, maintainer burnout worsened

**Decision 5: No Legal Review of GPL Compliance (Apparent)**
- [ ] Decision: Launch without definitive GPL legal opinion (or ignored opinion)
- [ ] Decision maker: GitHub/Microsoft legal + executives
- [ ] Date: Pre-June 2021
- [ ] Rationale: [UNKNOWN - not disclosed]
- [ ] Possibilities: (1) Believed "fair use" defensible, (2) Calculated risk (lawsuit manageable), (3) Didn't consider GPL issue
- [ ] Consequence: Class action lawsuit filed Nov 2022 (Doe v. GitHub)

**Decision 6: Post-Launch Changes (After Criticism)**
- [ ] Decision: Add "code referencing" feature (limited attribution), add public code filter option
- [ ] Decision maker: GitHub (responding to community backlash)
- [ ] Date: June 2022 (1 year after launch)
- [ ] Rationale: Damage control, appease critics
- [ ] But: No opt-out for past training, no compensation, GPL issue unresolved
- [ ] Consequence: Insufficient to restore community trust

**Output:** Layer 4 section with 6 decisions, **Decision 1 and 5 flagged as critical failures**

---

### Task 6: Draft Layer 5 - Fork Registry
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Medium

**Description:**
Document Copilot variants and potential license-compliant forks.

**Acceptance Criteria:**

**Post-Launch Changes (Not True "Forks"):**
- [ ] Copilot with "code referencing" (June 2022)
- [ ] Copilot with "public code filter" option (users can exclude public code matches)
- [ ] Status: Same training data, different inference-time filtering

**Potential Forks (not yet created):**

**Potential Fork: Copilot-Permissive**
- [ ] Proposed: Train only on MIT, Apache, BSD licensed code (no GPL)
- [ ] Methodology: Filter training data by license before training
- [ ] Expected outcome: GPL compliance assured, dataset ~50% smaller
- [ ] Cost: Retrain model (~$1-5M compute), potentially worse performance
- [ ] Benefit: Legal risk eliminated, GPL community satisfied

**Potential Fork: Copilot-Attributed**
- [ ] Proposed: Full attribution for all suggestions
- [ ] Methodology: Maintain provenance database (code snippet → original repo/author)
- [ ] Expected outcome: License compliance (MIT, Apache, BSD attribution requirements met)
- [ ] Cost: Large database (~100GB+), lookup overhead (latency), UX complexity
- [ ] Benefit: Respects license terms, builds developer trust

**Potential Fork: Copilot-Compensated**
- [ ] Proposed: Revenue sharing with code authors
- [ ] Methodology: Track code influence on suggestions → distribute % of Copilot revenue
- [ ] Expected outcome: Economic fairness, ecosystem sustainability
- [ ] Cost: ~$50-100M annually (50% of estimated Copilot revenue)
- [ ] Complexity: Attribution algorithm (how much did each author contribute?)
- [ ] Benefit: Restores open source incentive, prevents tragedy of the commons

**Alternative Models (Different Approach):**
- [ ] **Tabnine**: Trains on permissive-only, offers private model option (train on your own code)
- [ ] **CodeWhisperer** (Amazon): Similar to Copilot, but "code reference" feature more prominent
- [ ] **Open-source alternatives** (e.g., StarCoder): Trained on The Stack (filtered dataset with license info)

**Output:** Layer 5 section with post-launch changes + 3 potential forks + alternative models

---

### Task 7: Validate and Document Schema Discoveries
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Document what Copilot revealed about ORP schema.

**Acceptance Criteria:**
- [ ] Run validation (expect errors)
- [ ] Document new discoveries:
  - **License compliance fields** (L1: license distribution, compliance review)
  - **Legal risk assessment** (L4: legal opinions, IP risk)
  - **Ecosystem harm** (L3: future-oriented, collective, sustainability)
  - **Economic fairness** (L3: compensation, revenue sharing)
  - **Attribution mechanism** (L1: how credit provided, or not)
- [ ] Estimate: Copilot adds 20-40 new schema issues
- [ ] Recommendations for ORP v0.2

**Output:** Validation report + schema discoveries

---

### Task 8: Write Accompanying Documentation
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Medium

**Description:**
Create README explaining Copilot example.

**Acceptance Criteria:**
- [ ] Create: `examples/github_copilot/README.md`
- [ ] Explains:
  - Why Copilot (code modality, license crisis)
  - GPL copyleft intent vs Copilot practice
  - Open source sustainability crisis
  - Ecosystem harm (tragedy of the commons)
  - Legal context (Doe v. GitHub lawsuit)
- [ ] Links to legal filings, Software Freedom Conservancy, GPL text
- [ ] Comparison: ImageNet (bias), LAION (safety), Common Crawl (erasure), Copilot (ecosystem)

**Output:** `examples/github_copilot/README.md`

---

### Task 9: Schema Discovery Documentation
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** High

**Description:**
Document Copilot-specific schema discoveries.

**Acceptance Criteria:**
- [ ] Create: `docs/sprints/sprint-1.7.3.3-schema-discoveries.md`
- [ ] New issues:
  - License compliance tracking
  - Legal risk assessment
  - Ecosystem harm taxonomy
  - Economic fairness fields
  - Attribution mechanisms
- [ ] Compare: ImageNet (85), LAION (30-50), Common Crawl (40-60), Copilot (20-40)
- [ ] Total: ~175-235 schema issues across 4 AI examples

**Output:** Schema discovery report

---

## Success Criteria

### Completion Criteria
- [ ] All 9 tasks completed
- [ ] `examples/github_copilot_training_data.yaml` created (ORP-Full)
- [ ] License compliance documented
- [ ] Ecosystem harm demonstrated
- [ ] Schema discoveries documented

### Quality Criteria
- [ ] Tests ORP on code modality (not just images/text)
- [ ] Tests ORP on legal dimension (license compliance)
- [ ] Shows ecosystem harm (sustainability, future contributors)

### Impact Criteria
- [ ] Reveals ORP's legal/economic dimensions
- [ ] Demonstrates pattern: bias → safety → erasure → ecosystem
- [ ] Strengthens paper (4 domains: policy + 3 AI sub-domains)

---

## Dependencies

**Depends on:**
- Sprint 1.7.3.2 (Common Crawl - provides ecosystem harm template)

**Enables:**
- Sprint 1.7.3.4 (Schema revision - consolidates all 4 AI discoveries)

---

## Risks and Mitigations

### Risk 1: Active Litigation (Doe v. GitHub)
**Mitigation:** Cite public court filings, avoid legal judgment. Document facts, note "legal question undecided." Include legal disclaimer.

### Risk 2: GitHub/Microsoft Perception
**Mitigation:** Frame as system-level analysis, not accusation. Acknowledge complexity (fair use debates). Note: ORP would make trade-offs explicit prospectively.

### Risk 3: GPL Interpretation Debates
**Mitigation:** Present both sides (GPL community vs GitHub), document uncertainty. Cite legal scholars on both sides.

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-22
**Target Completion:** 2026-04-29
**Estimated Effort:** 45 hours over 7 days
