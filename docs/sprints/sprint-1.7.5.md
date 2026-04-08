# Sprint 1.7.5: Academic Paper Submission Preparation

**Version:** `sprint-1.7.5`
**Parent Epic:** `sprint-1.7.0` (Foundation for Expansion)
**Status:** Not Started
**Start Date:** 2026-04-15
**Target End Date:** 2026-04-18 (3 days)

**Code Target Version:** `v0.6.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Finalize the academic paper "Data Before Models: Epistemic Transparency, Incentive Distortion, and the Case for Provenance-Grounded Governance" for submission to **Big Data & Society** journal — incorporating insights from Sprints 1.7.1-1.7.4, strengthening empirical foundation with two worked examples, and ensuring submission-readiness with proper formatting, citations, and compliance with journal guidelines.

---

## Strategic Importance

This sprint is the **culmination** of Epic 1.7:
- Converts theoretical work (academic paper draft) into submission-ready artifact
- Establishes academic legitimacy for ORP
- Creates citeable foundation for protocol
- Positions ORP in data governance scholarly discourse
- Opens door to research community engagement

**Why Big Data & Society:**
- Interdisciplinary (philosophy + CS + governance)
- Open access (wider reach)
- Receptive to critical infrastructure arguments
- Recent relevant publications (Crawford, Selbst, etc.)
- Fast review turnaround (3-4 months typical)

---

## Scope

### In Scope
- Integration of ImageNet example into Section 5
- Updates to Section 3 based on comparison document
- Reference to operational governance (Section 6)
- Citation check and bibliography cleanup
- Abstract refinement
- Journal formatting (Big Data & Society style)
- Cover letter draft
- Final proofreading and submission

### Explicitly Out of Scope
- New sections (paper structure is stable)
- Major rewrites (content is solid)
- Response to peer review (that's post-submission)
- Supplementary materials (keep paper self-contained)
- Alternative venue submissions (focus on primary choice)

---

## Tasks

### Task 1: Integrate ImageNet Example into Section 5
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Critical

**Description:**
Add ImageNet case to Section 5.3 (demonstration section), showing ORP works in AI domain.

**Acceptance Criteria:**
- [ ] **New subsection:** 5.3.2 "AI Training Data: ImageNet"
- [ ] Parallel structure to 5.3.1 (Danish property tax):
  - Brief context (why ImageNet matters)
  - How ORP-Full applies (all 5 layers)
  - What ORP surfaces that existing standards (Model Cards, Datasheets) don't
  - Key finding: Funding/exclusion/scope decisions invisible in current documentation
- [ ] Length: 800-1,000 words (proportional to Danish example)
- [ ] Citations: Crawford & Paglen, original ImageNet papers, Model Cards paper
- [ ] Connects to Section 2 (constitutive problem) and Section 3 (framework gaps)
- [ ] Demonstrates cross-domain applicability (policy → AI)
- [ ] Update Section 5 introduction: "demonstrated through two cases..."
- [ ] Update Abstract: "demonstrated in policy and AI training data governance"

**Output:** Updated Section 5 with ImageNet case integrated

---

### Task 2: Update Section 3 with Comparison Insights
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Strengthen Section 3 (existing frameworks) with specific examples from comparison document.

**Acceptance Criteria:**
- [ ] Section 3.1 (GDPR): Add specific example of what GDPR doesn't require
  - Example: "GDPR Article 30 requires records of processing activities but not provenance of dataset constitution"
  - Cite specific article numbers from comparison doc
- [ ] Section 3.2 (Algorithmic Accountability): Reference EU AI Act specifically
  - Example: "AI Act Article 13 requires training data documentation but not funding disclosure"
- [ ] Section 3.3 (Open Data): Reference FAIR principles gap
  - Example: "FAIR principles ensure data is Findable/Accessible but not that provenance includes exclusion criteria"
- [ ] Add visual: Comparison matrix table (reduced version from comparison doc)
  - Table: Standards vs ORP Layers, showing gaps
  - Refer readers to full comparison document for details
- [ ] Ensure all claims cited to primary sources (use comparison doc citations)
- [ ] Maintain argumentative flow (don't let examples bog down narrative)

**Output:** Updated Section 3 with concrete examples and citations

---

### Task 3: Update Section 6 with Governance Reference
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Reference operational governance in Section 6.4 (open questions).

**Acceptance Criteria:**
- [ ] Section 6.4 (Open Questions): Add governance note
  - "ORP's governance documentation (operational as of April 2026) provides contribution, versioning, and example review processes, establishing the procedural foundation for community formation."
  - Cite: governance docs URL or footnote
- [ ] Section 6.1 (Implications): Note governance model as implementation detail
  - "The operational governance framework enables community participation through transparent decision-making (documented in governance ledger compliant with Layer 4 requirements)"
- [ ] Don't over-emphasize: Governance is supportive infrastructure, not paper's main argument
- [ ] Maintains academic tone (not project promotion)

**Output:** Brief governance references in Section 6

---

### Task 4: Refine Abstract and Keywords
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** High

**Description:**
Update abstract to reflect strengthened empirical foundation and finalize keywords.

**Acceptance Criteria:**
- [ ] Abstract updates:
  - Mention "two cases" (Danish property tax, ImageNet training data)
  - Update "demonstrates ORP's operation" to "demonstrates through policy and AI governance"
  - Keep within word limit (150-250 words for Big Data & Society)
- [ ] Keywords refinement:
  - Current: data governance, epistemic transparency, data provenance, algorithmic accountability, information ethics, constitutive problem, REE, OpenReason Protocol
  - Ensure alignment with Big Data & Society indexing
  - Add: AI training data, dataset documentation (if space)
  - Max 6-8 keywords typical
- [ ] Consistency check: Abstract accurately reflects paper content
- [ ] Compelling: Abstract should motivate reading (not just summarize)

**Output:** Finalized abstract and keywords

---

### Task 5: Citation and Bibliography Check
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Critical

**Description:**
Ensure all citations are complete, consistent, and properly formatted.

**Acceptance Criteria:**
- [ ] **Citation audit:**
  - Every claim has citation (no unsupported assertions)
  - All citations in text appear in bibliography
  - All bibliography entries cited in text (no orphans)
  - Primary sources used where possible (not secondary)
- [ ] **Format consistency:**
  - Big Data & Society uses APA 7th edition
  - Check: Author (Year) in-text format
  - Check: Bibliography entries complete (DOI, page numbers, etc.)
  - Check: Journal article vs book vs report formatting
- [ ] **ORP self-citations:**
  - OpenReason Protocol Specification v0.1 (2025)
  - REE Philosophy Document (2025)
  - ImageNet example (2026)
  - Danish Property Tax example (2025)
  - Format as: Public Reason Project. (Year). Title. URL
- [ ] **Key citations present:**
  - Crawford & Paglen (2021) - Excavating AI
  - Selbst et al. (2019) - Fairness and abstraction
  - Ioannidis (2005) - Why most research is false
  - Floridi (2013) - Ethics of Information
  - GDPR, EU AI Act (official sources)
  - Model Cards, Datasheets papers
- [ ] Use citation manager or verify manually

**Output:** Complete, formatted bibliography (currently in abstract_and_bibliography.md)

---

### Task 6: Journal Formatting and Style Compliance
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Format paper according to Big Data & Society submission guidelines.

**Acceptance Criteria:**
- [ ] **Review submission guidelines:**
  - URL: https://journals.sagepub.com/author-instructions/BDS
  - Check: Word count (aim for 4,500-5,000 words excluding references)
  - Check: File format (Word .docx or LaTeX)
  - Check: Anonymization (if required - check blind review policy)
  - Check: Section structure requirements
- [ ] **Formatting:**
  - Font: Times New Roman 12pt or similar
  - Spacing: Double-spaced
  - Margins: 1 inch all sides
  - Page numbers: Include
  - Headings: Consistent hierarchy (Section 1 → 1.1 → 1.1.1)
- [ ] **Anonymization (if blind review):**
  - Remove author names from paper body
  - Remove identifying references ("our protocol" → "the protocol")
  - Create separate title page with author info
  - Check: Self-citations are allowed but not identifying
- [ ] **Word count check:**
  - Target: 4,500-5,000 words
  - Exclude: References, abstract, title page
  - If over: Trim without losing substance
  - If under: Perfectly fine (quality over quantity)
- [ ] **Figures/tables:**
  - Comparison matrix table (from Section 3)
  - Ensure high resolution, clear labels
  - Caption and number properly

**Output:** Formatted manuscript ready for submission

---

### Task 7: Write Cover Letter
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** High

**Description:**
Draft cover letter to journal editor explaining paper's contribution and fit.

**Acceptance Criteria:**
- [ ] **Structure:**
  - Dear Editor [name if known, or "Editors of Big Data & Society"]
  - Paper title and brief description
  - Why it fits Big Data & Society (interdisciplinary, critical, infrastructure)
  - Key contribution (filling gap in data governance literature)
  - Confirmation of original work, not under review elsewhere
  - Contact information
  - Thank you / look forward to review
- [ ] **Content highlights:**
  - Addresses gap: All existing frameworks downstream of data constitution
  - Introduces: REE philosophical framework + ORP procedural implementation
  - Demonstrates: Through two domain cases (policy, AI)
  - Timeliness: EU AI Act, AI governance debates
  - Interdisciplinary: Philosophy, computer science, governance
- [ ] **Tone:** Professional, confident but not overselling
- [ ] **Length:** 1 page max (300-400 words)
- [ ] **Format:** Letterhead or plain text (check journal preference)

**Output:** Cover letter draft

---

### Task 8: Final Proofreading and Consistency Check
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Final pass for typos, consistency, clarity, and flow.

**Acceptance Criteria:**
- [ ] **Typo/grammar check:**
  - Run spell checker
  - Read aloud sections (catches awkward phrasing)
  - Check: Commonly confused words (affect/effect, its/it's)
- [ ] **Consistency check:**
  - Terminology: Same terms used throughout (e.g., "constitutive problem" not "constitution problem")
  - Acronyms: Defined on first use in each section if needed
  - Capitalization: ORP, REE, GDPR consistent
  - Formatting: Section headings, figure captions consistent
- [ ] **Clarity check:**
  - Each paragraph has clear topic sentence
  - No jargon without explanation
  - Transitions between sections smooth
  - Argument flow is logical (intro → problem → gaps → REE → ORP → implications)
- [ ] **Citation check:**
  - Correct citation format throughout
  - All URLs work (check ORP docs links)
- [ ] **External review (optional but recommended):**
  - Have trusted colleague/friend read abstract + intro
  - Check: Does argument make sense to non-expert?
  - Incorporate feedback

**Output:** Polished, submission-ready manuscript

---

### Task 9: Prepare Submission Package
**Owner:** Asbjørn
**Estimate:** 1 hour
**Priority:** Medium

**Description:**
Assemble all materials required for journal submission.

**Acceptance Criteria:**
- [ ] **Submission package includes:**
  1. Main manuscript (anonymized if required)
  2. Title page (with author names, affiliations, contact)
  3. Cover letter
  4. Author bio (if required)
  5. Conflict of interest statement (none expected)
  6. Funding statement (unfunded or OpenReason Project internal)
  7. Data availability statement (ORP docs publicly available at URL)
  8. Any required forms (check journal submission system)
- [ ] **Final checklist:**
  - [ ] Word count within limits
  - [ ] All figures/tables included
  - [ ] Bibliography complete
  - [ ] Format compliant
  - [ ] Cover letter addressed to journal
  - [ ] Files named appropriately
- [ ] **Backup:** Save all files in multiple locations
- [ ] **Submission system:** Create account if needed, prepare to upload

**Output:** Complete submission package ready to submit

---

### Task 10: Submit Paper
**Owner:** Asbjørn
**Estimate:** 1 hour
**Priority:** High

**Description:**
Submit paper through journal submission system.

**Acceptance Criteria:**
- [ ] Create account on Big Data & Society submission system (SAGE Track)
- [ ] Upload manuscript files
- [ ] Upload cover letter
- [ ] Enter metadata (title, abstract, keywords, authors)
- [ ] Confirm compliance statements
- [ ] Suggest reviewers (optional, 3-5 names with expertise in data governance, AI ethics, information ethics)
- [ ] Exclude reviewers (if any conflicts)
- [ ] Review submission preview (PDF as journal will see it)
- [ ] Submit and confirm receipt
- [ ] Save confirmation email
- [ ] Record submission date in decision log (GOV-2026-XXX)

**Output:** Paper submitted, confirmation received

---

## Success Criteria

### Completion Criteria
- [ ] All 10 tasks completed
- [ ] Paper submitted to Big Data & Society
- [ ] Submission confirmation received
- [ ] Backup copies saved

### Quality Criteria
- [ ] Two worked examples integrated (Danish + ImageNet)
- [ ] All claims cited to primary sources
- [ ] Word count within guidelines (4,500-5,000)
- [ ] Journal formatting compliant
- [ ] No typos or grammatical errors
- [ ] Argument is clear and compelling

### Impact Criteria (3-6 months)
- Paper in review at Big Data & Society
- First round of reviewer comments received
- Revisions completed if needed
- Paper accepted (target: within 6 months)
- Published and citeable (target: within 9 months)

---

## Dependencies

**Depends on:**
- Sprint 1.7.1 (governance operational - cited in paper)
- Sprint 1.7.2 (comparison document - strengthens Section 3)
- Sprint 1.7.3 (ImageNet example - critical for Section 5)

**Enables:**
- Academic legitimacy for ORP
- Grant applications (published/under review paper)
- Public comment period (can reference "under academic review")
- Community building (academic community engagement)

---

## Risks and Mitigations

### Risk 1: Paper rejected (doesn't fit journal scope)
**Mitigation:** Carefully review Big Data & Society scope and recent publications; prepare backup venue (AI & Society)

### Risk 2: Word count exceeds limit
**Mitigation:** Start checking now (current draft ~4,800 words); trim examples if needed

### Risk 3: Reviewer suggestions require major revisions
**Mitigation:** Expected and normal; plan for revision sprint (1.8.x) after review

### Risk 4: ImageNet integration disrupts flow
**Mitigation:** Parallel structure to Danish example; keep concise

---

## Alternative Venues (Backup Plan)

If Big Data & Society doesn't feel right or rejects:

**Primary backup:** AI & Society (Springer)
- Similar interdisciplinary scope
- Receptive to philosophical-technical work
- Slightly slower review (6 months typical)

**Secondary backup:** Philosophy & Technology (Springer)
- Stronger on REE philosophical grounding
- Less emphasis on ORP implementation

**Conference option:** FAccT 2027
- Fast feedback (3 month review)
- Conference proceedings (lower prestige but higher visibility)
- Shorter format (8-10 pages)

---

## Post-Submission Actions

After submission:
1. Record in DECISION_LOG.md: GOV-2026-XXX "Academic paper submitted"
2. Update ROADMAP.md: "Academic paper under review at Big Data & Society"
3. Update docs site: Note paper status
4. Prepare for Sprint 1.8.0: Public comment period launch
5. Monitor submission system for reviewer assignment
6. Typical timeline: 3-6 months to first decision

---

## Documentation Updates

- [ ] Update ROADMAP.md (paper status)
- [ ] Update CLAUDE.md (paper submitted)
- [ ] Update docs/academic/README.md (submission status)
- [ ] Create DECISION_LOG.md entry
- [ ] Update docs site (paper under review)

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
**Start Date:** 2026-04-15
**Target Completion:** 2026-04-18
**Estimated Effort:** 24 hours over 3 days

---

## Journal Information

**Big Data & Society**
- Publisher: SAGE
- Open Access: Yes (APC required, check institutional coverage)
- Submission system: SAGE Track
- Author guidelines: https://journals.sagepub.com/author-instructions/BDS
- Recent relevant publications:
  - Crawford & Paglen (2021)
  - Selbst et al. (2019)
  - Critical AI/data governance work
- Impact factor: ~6.0 (strong for interdisciplinary field)
- Review timeline: 3-4 months typical for first decision
