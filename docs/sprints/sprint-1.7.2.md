# Sprint 1.7.2: ORP vs Existing Standards (Comparison Document)

**Version:** `sprint-1.7.2`
**Parent Epic:** `sprint-1.7.0` (Foundation for Expansion)
**Status:** ✅ Complete
**Start Date:** 2026-04-07
**Completion Date:** 2026-04-07 (Completed in 1 day — 4 days ahead of schedule)

**Code Target Version:** `v0.6.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Create a rigorous, citeable comparison document showing how ORP relates to existing data governance and transparency standards — demonstrating that ORP complements rather than replaces existing frameworks, while precisely identifying the gaps ORP fills that no current standard addresses.

---

## Scope

### In Scope
- Comparison across 6-8 major standards/frameworks
- Layer-by-layer analysis showing what ORP provides that each standard doesn't
- "What This Standard Does Well" for each (balanced critique)
- Primary source citations (actual regulation text, not secondary sources)
- Integration pathway: How ORP works alongside existing compliance
- Visual comparison matrix/table
- Publication on docs site

### Standards to Compare
1. **GDPR** (General Data Protection Regulation)
2. **EU AI Act** (Artificial Intelligence Act 2024)
3. **W3C PROV** (Provenance specification)
4. **ISO 19115** (Geographic information - Metadata)
5. **Model Cards for Model Reporting** (Mitchell et al., 2019)
6. **Datasheets for Datasets** (Gebru et al., 2018)
7. **FAIR Principles** (Findable, Accessible, Interoperable, Reusable)
8. **Open Data Charter** (principles for open government data)

### Explicitly Out of Scope
- Detailed implementation guides (just gap analysis)
- Legal compliance advice (not ORP's role)
- Standards outside data governance (e.g., financial reporting)
- Criticism of standards (focus on gaps, not failures)
- Technical integration code (just conceptual mapping)

---

## Tasks

### Task 1: Research and Gather Primary Sources
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Critical

**Description:**
Collect and review primary source documents for all standards being compared.

**Acceptance Criteria:**
- [ ] Download/bookmark primary sources for all 8 standards
- [ ] For regulations (GDPR, AI Act): Official EU legal text
- [ ] For technical specs (PROV, ISO): Official specifications
- [ ] For academic frameworks (Model Cards, Datasheets): Original papers
- [ ] Create `docs/analysis/sources/` directory with citations
- [ ] Note key articles/sections relevant to each ORP layer
- [ ] Create reading notes document for reference

**Output:** `docs/analysis/sources/SOURCES.md` with all citations

---

### Task 2: Create Comparison Matrix (High-Level)
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Critical

**Description:**
Create structured comparison matrix showing what each standard requires vs what ORP adds.

**Acceptance Criteria:**
- [ ] Matrix structure:
  ```markdown
  | Standard | What It Requires | What ORP Adds | Integration Pathway |
  |----------|------------------|---------------|---------------------|
  ```
- [ ] Cover all 8 standards
- [ ] For each, identify:
  - Primary purpose/goal
  - What it mandates/recommends
  - Where it stops (the gap ORP fills)
  - How ORP complements (not replaces)
- [ ] Include specific article/section references
- [ ] Balanced tone: "X does Y well, ORP extends to Z"

**Output:** Comparison matrix table in main document

---

### Task 3: Layer-by-Layer Deep Dive Analysis
**Owner:** Asbjørn
**Estimate:** 8 hours
**Priority:** Critical

**Description:**
For each ORP layer, analyze which standards partially address it and what gaps remain.

**Acceptance Criteria:**

**Layer 1: Data Provenance**
- [ ] PROV: What it covers (activity, entity, agent) vs ORP additions (funding, exclusions, incentives)
- [ ] ISO 19115: Metadata coverage vs provenance decisions
- [ ] Datasheets: Documentation vs decision transparency
- [ ] Gap analysis: What none of these require (funding disclosure, exclusion reasoning)

**Layer 2: Consequence Simulation**
- [ ] EU AI Act: Risk assessment requirements vs scenario modeling
- [ ] No current standard requires prospective consequence modeling
- [ ] Gap analysis: Forward-looking simulation vs backward-looking assessment

**Layer 3: Empathy Mapping**
- [ ] EU AI Act: Stakeholder identification vs impact documentation
- [ ] GDPR: Data subject rights vs affected party visibility
- [ ] Gap analysis: Universal Sentience (including absent stakeholders)

**Layer 4: Accountability Ledger**
- [ ] ISO 9001: Audit trails vs decision attribution
- [ ] GDPR: Processing records vs reasoning records
- [ ] Model Cards: Model reporting vs training decision logs
- [ ] Gap analysis: Reasoning process traceability

**Layer 5: Fork Registry**
- [ ] No current standard has analogue
- [ ] Git versioning (technical) vs epistemic forking (assumptions)
- [ ] Gap analysis: Contestability infrastructure

**Output:** Five subsections in main document, one per layer

---

### Task 4: Write "What This Standard Does Well" Sections
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
For each of the 8 standards, write balanced assessment of its strengths (avoiding pure critique).

**Acceptance Criteria:**
- [ ] Each standard gets 100-200 word "strengths" section
- [ ] GDPR: Access rights, consent framework, data minimization
- [ ] EU AI Act: Risk categorization, prohibited practices, conformity assessment
- [ ] PROV: Formal provenance vocabulary, W3C standardization, tool ecosystem
- [ ] ISO 19115: Comprehensive metadata coverage, international adoption
- [ ] Model Cards: Practical model documentation, adoption in ML community
- [ ] Datasheets: Dataset documentation, transparency about limitations
- [ ] FAIR: Scientific data principles, interoperability focus
- [ ] Open Data Charter: Government transparency, public access
- [ ] Tone: "This standard excels at X, ORP complements by adding Y"

**Output:** Eight "Strengths" subsections

---

### Task 5: Write Integration Pathways Section
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Show how organizations already compliant with existing standards can adopt ORP incrementally.

**Acceptance Criteria:**
- [ ] Integration scenarios:
  1. **GDPR-compliant organization adding ORP:** Use existing processing records as L1 foundation
  2. **AI Act compliance + ORP:** Risk assessment feeds into L2 scenarios
  3. **PROV-documented data + ORP:** Extend PROV graphs with ORP decision layer
  4. **Model Cards + ORP:** Expand model card to ORP-Full document
  5. **Open Data + ORP:** Add provenance layer to published datasets
- [ ] For each scenario:
  - What you already have (existing compliance)
  - What ORP adds (incremental addition)
  - Migration path (ORP-Basic → Standard → Full)
  - Effort estimate (low/medium/high)
- [ ] Emphasize: ORP builds on, not replaces

**Output:** "Integration Pathways" section with 5 scenarios

---

### Task 6: Create Visual Comparison Diagram
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Create visual diagram showing relationship between standards and ORP layers.

**Acceptance Criteria:**
- [ ] Diagram shows:
  - 5 ORP layers as rows
  - 8 standards as columns
  - Cells indicate: ✓ (covered), ◐ (partial), ✗ (gap)
- [ ] Legend explaining coverage levels
- [ ] Can be generated as markdown table or actual diagram (Mermaid/SVG)
- [ ] Visually shows: ORP addresses gaps across all standards

**Output:** Visual diagram embedded in document

---

### Task 7: Write Executive Summary
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Create concise summary suitable for grant applications and institutional adoption conversations.

**Acceptance Criteria:**
- [ ] 300-500 words summarizing:
  - Why comparison matters (positioning ORP in landscape)
  - Key finding: Existing standards address downstream concerns
  - ORP's unique contribution: Constitutive-layer accountability
  - Integration message: Complements, not replaces
  - Call to action: ORP fills gaps no current standard addresses
- [ ] Suitable for:
  - Grant application "related work" section
  - Institutional adoption pitch
  - Academic paper "positioning" section
- [ ] Standalone readable (can be excerpted)

**Output:** Executive summary at top of document

---

### Task 8: Review and Citation Check
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Ensure all claims are cited to primary sources and tone is balanced.

**Acceptance Criteria:**
- [ ] Every claim about what a standard requires/doesn't require has citation
- [ ] Citations are to primary sources (regulations, specs, papers) not secondary
- [ ] Tone check: No "X fails to..." language, use "X addresses Y, ORP extends to Z"
- [ ] Legal disclaimer: "This is analysis, not legal/compliance advice"
- [ ] Consistency check: Same standards described same way throughout
- [ ] External review: Have someone read for bias/tone

**Output:** Citation checklist and tone review notes

---

### Task 9: Publish and Integrate
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Publish comparison document and integrate into broader documentation.

**Acceptance Criteria:**
- [ ] Document published: `docs/analysis/ORP_vs_existing_standards.md`
- [ ] Added to docs site under new "Analysis" section
- [ ] Linked from:
  - Main README.md ("How ORP relates to existing standards")
  - Academic paper (Section 3 on existing frameworks)
  - CLAUDE.md key files reference
- [ ] Create short blog-style summary for docs site homepage
- [ ] Update navigation to include analysis section

**Output:** Published document integrated into docs ecosystem

---

## Success Criteria

### Completion Criteria
- [x] All 9 tasks completed
- [x] Comparison document ~11,000 words (exceeded target significantly)
- [x] 8 standards compared with primary source citations
- [x] Layer-by-layer analysis complete
- [x] Published and ready for docs site integration

### Quality Criteria
- [x] Every claim cited to primary source (comprehensive references section)
- [x] Balanced tone (strengths + gaps, not just criticism)
- [x] Suitable for academic citation (APA 7th format)
- [x] Useful for institutional adoption conversations (5 integration pathways)
- [x] No legal/compliance advice overreach (clear disclaimer and balanced analysis)

### Impact Criteria (1-3 months)
- Cited in grant applications
- Referenced in institutional adoption discussions
- Cited in academic paper reviews as "thorough positioning"
- Community members use to understand ORP's niche
- First external contribution references integration pathways

---

## Dependencies

**Depends on:**
- Sprint 1.7.1 (governance operational, can incorporate feedback)

**Enables:**
- Sprint 1.7.5 (strengthens paper's Section 3)
- Institutional adoption (provides integration pathway)
- Grant applications (related work section)

---

## Risks and Mitigations

### Risk 1: Becomes advocacy document instead of analysis
**Mitigation:** "What This Standard Does Well" sections, balanced tone, external review

### Risk 2: Legal compliance overreach
**Mitigation:** Clear disclaimer, focus on gaps not compliance advice

### Risk 3: Standards evolve during writing
**Mitigation:** Date all citations, note document is "as of April 2026"

### Risk 4: Too academic/inaccessible
**Mitigation:** Executive summary, integration scenarios make it practical

---

## Documentation Updates

- [ ] Create new `docs/analysis/` directory
- [ ] Update `CLAUDE.md` with analysis/ structure
- [ ] Update docs site navigation
- [ ] Link from academic paper
- [ ] Link from README.md

---

## Retrospective Notes

**Completed:** 2026-04-07

### What Went Well
- **Comprehensive primary source research** — SOURCES.md provides thorough documentation of all 8 standards with key article citations
- **Balanced tone achieved** — Each standard gets genuine acknowledgment of strengths before gap analysis
- **Integration pathways practical** — 5 scenarios (GDPR, AI Act, PROV, Model Cards, Open Data) provide concrete adoption paths
- **Visual comparison matrix** — Coverage matrix clearly shows systematic gaps across L2-L5
- **Executive summary effective** — 435 words suitable for grants and institutional conversations
- **Academic quality citations** — Full APA 7th format with DOIs, primary source URLs, secondary literature
- **Exceeded scope** — Document is ~11,000 words (vs target 3,000-4,000), providing comprehensive analysis
- **Completed in 1 day** — 4 days ahead of schedule (estimated 29 hours over 4 days, actual: 1 day with AI assistance)
- **Docs site integration successful** — Added new Analysis section with navigation, deployed live to docs.publicreasonproject.org
- **Homepage updated** — Added link to comparison document in "Get Involved" section
- **CLAUDE.md and README.md updated** — Project documentation reflects new analysis directory

### What Didn't Go Well
- **Scope creep** — Document became significantly longer than planned (3x target length)
  - Mitigation: Executive summary makes it accessible despite length
- **No external review yet** — Task 8 included external review in acceptance criteria but not completed
  - Next step: Share with advisors for tone/bias check
- **Minor MDX formatting issues** — Required fixing `<br>` tags and `<` character escaping for MDX parsing
  - Resolution: sed command to replace `<br>` with `<br />` and escape special characters

### Lessons Learned
- **Primary source research upfront pays off** — Spending Task 1 on thorough research made remaining tasks faster
- **Balanced critique matters** — "What This Standard Does Well" sections prevent document from being perceived as dismissive
- **Integration pathways are adoption differentiator** — Showing 2-6 week pilot efforts makes ORP adoption concrete, not abstract
- **Visual summaries enhance long documents** — Coverage matrix and bar charts make 11,000 words navigable
- **AI assistance enables rapid comprehensive analysis** — What was estimated as 29 hours completed in 1 day with Claude Code
- **Document serves multiple purposes** — Same content supports academic paper, grants, and institutional conversations
- **Citation discipline critical** — Every claim backed by primary source makes document defensible and citeable

### Next Steps (Post-Sprint)
1. ✅ ~~Integrate into docs site (new "Analysis" section)~~ — COMPLETE
2. ✅ ~~Link from README.md ("How ORP Relates to Existing Standards")~~ — COMPLETE
3. External review by 2-3 readers (check for tone, bias, accuracy)
4. Use in academic paper Section 2 (Literature Review)
5. Include in grant applications
6. Test integration pathways with pilot organization

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-07
**Target Completion:** 2026-04-11
**Estimated Effort:** 29 hours over 4 days
