# Sprint 1.7.0: Foundation for Expansion (EPIC)

**Version:** `sprint-1.7.0`
**Status:** In Progress
**Start Date:** 2026-04-04
**Target End Date:** 2026-04-18 (2 weeks)
**Type:** Epic (parent sprint with sub-sprints)

**Code Target Version:** `v0.6.0`
**Protocol Version Supported:** `0.1` → `0.2` (preparation)

---

## Epic Goal

Transform ORP from a single-domain demonstration into a multi-domain protocol with operational governance, clear positioning against existing standards, and expanded tooling — preparing for academic publication, public comment period, and institutional adoption.

**Success Criteria:**
- Operational governance processes documented and ready for community
- Second worked example (AI/ML domain) demonstrating cross-domain applicability
- Formal comparison showing ORP's relationship to existing standards
- Machine-readable schema enabling programmatic interoperability
- Academic paper submission-ready with strengthened empirical foundation

---

## Strategic Context

### Where We Are
- ✅ Phase 0 nearly complete: spec, philosophy, governance model, worked example (Danish tax)
- ✅ REST API production-ready with 96% test coverage
- ✅ Python package on PyPI (orp-validator 0.3.0)
- ✅ Documentation site live (docs.publicreasonproject.org)
- ✅ Academic paper draft complete (all 6 sections + manifesto)

### The Gap
- **Depth problem:** Only one worked example (limits generalizability claims)
- **Positioning problem:** Unclear how ORP relates to existing standards (GDPR, PROV, AI Act)
- **Governance problem:** Process documented but not operational
- **Adoption problem:** No machine-readable format for programmatic use
- **Legitimacy problem:** Academic paper needs stronger empirical foundation

### Where We're Going
This epic addresses all five gaps through focused sub-sprints, positioning ORP for:
1. **Academic legitimacy** (paper submission to Big Data & Society)
2. **Community formation** (60-day public comment period launch)
3. **Institutional adoption** (comparison doc shows integration path)
4. **Technical maturity** (machine-readable schema for tooling)
5. **Domain expansion** (AI/ML example proves cross-domain applicability)

---

## Sub-Sprint Structure

### Sprint 1.7.1: Operational Governance
**Target:** 2-3 days
**Deliverable:** Four governance process documents making community participation concrete

### Sprint 1.7.2: Comparison Document
**Target:** 3-4 days
**Deliverable:** Structured analysis of ORP vs existing standards (GDPR, PROV, AI Act, ISO)

### Sprint 1.7.3: ImageNet AI Training Data Example
**Target:** 5-7 days
**Deliverable:** ORP-Full document for ImageNet dataset constitution

### Sprint 1.7.4: Machine-Readable Schema (JSON-LD)
**Target:** 2-3 days
**Deliverable:** Semantic web-compatible schema with SPARQL examples

### Sprint 1.7.5: Academic Paper Submission Preparation
**Target:** 2-3 days
**Deliverable:** Paper submission-ready for Big Data & Society

**Total estimated time:** 14-20 days (overlapping work possible)

---

## Epic-Level Scope

### In Scope
- Governance operationalization (contribution, versioning, review processes)
- Second worked example in AI/ML domain (depth over breadth)
- Formal comparison with 5-8 existing standards
- JSON-LD context and basic RDF vocabulary
- Academic paper refinement and submission prep
- Documentation updates reflecting expanded scope

### Explicitly Out of Scope
- Third/fourth worked examples (pharmaceutical, climate - defer to 1.8.x)
- Full OWL ontology (light JSON-LD touch only)
- Public comment period launch (1.8.0 after paper submission)
- ORP-AI formal extension spec (defer until after ImageNet example)
- Video tutorials or educational content (Phase 2)
- Major API changes (API is stable at 1.6.0)
- Changes to core protocol spec (v0.1 remains stable)

---

## Dependencies Between Sub-Sprints

```
1.7.1 (Governance) ─┬─> 1.7.5 (Paper Prep)
                    │
1.7.2 (Comparison) ─┼─> 1.7.5 (Paper Prep)
                    │
1.7.3 (ImageNet)  ──┴─> 1.7.5 (Paper Prep)

1.7.4 (Schema) ─────> (independent, can run parallel)
```

**Critical path:** 1.7.3 (ImageNet example) is the longest task and gates paper submission

**Parallel opportunities:**
- 1.7.1 and 1.7.4 can run simultaneously (different skill sets)
- 1.7.2 can start before 1.7.3 completes

---

## Success Metrics

### Completion Criteria
- [ ] All 5 sub-sprints completed and closed
- [ ] At least 2 worked examples in repository (Danish + ImageNet)
- [ ] Governance processes documented and tested
- [ ] Comparison document published on docs site
- [ ] JSON-LD schema in `schemas/` directory
- [ ] Academic paper submitted to journal

### Quality Criteria
- [ ] ImageNet example validated by `orp validate` CLI
- [ ] ImageNet example demonstrates all 5 layers with depth
- [ ] Comparison document cites primary sources for all standards
- [ ] JSON-LD validates against schema.org and PROV-O
- [ ] Governance documents include worked examples/templates
- [ ] Paper strengthened with empirical evidence from examples

### Impact Criteria (3-6 months)
- Academic paper accepted/in review at Big Data & Society
- Public comment period launched with 10+ substantive submissions
- First external contribution using operational governance process
- First external tool using JSON-LD schema
- Citations of comparison document in adoption conversations

---

## Risks and Mitigations

### Risk 1: ImageNet example too complex/time-consuming
**Likelihood:** Medium | **Impact:** High

**Mitigation:**
- Start with ORP-Standard (L1-L3) not ORP-Full
- Use Crawford & Paglen's existing analysis for L1 foundation
- Limit scope to ImageNet-1K (not full 22K categories)
- Template approach: adapt Danish example structure

### Risk 2: Comparison document becomes advocacy not analysis
**Likelihood:** Medium | **Impact:** Medium

**Mitigation:**
- Cite primary sources (actual regulations/specs)
- Include "What This Standard Does Well" for each
- Frame as "gaps and complements" not "failures"
- Have external reviewer check tone

### Risk 3: Academic paper scope creep during revision
**Likelihood:** High | **Impact:** Medium

**Mitigation:**
- Paper revision limited to: adding ImageNet example, updating comparison section
- No new sections added
- Target word count remains 4,500-5,000
- Set hard deadline: submission by end of 1.7.5

### Risk 4: Governance docs remain abstract despite effort
**Likelihood:** Medium | **Impact:** Medium

**Mitigation:**
- Each governance doc must include worked example/template
- Test process by creating a fake community contribution
- Have someone external read and attempt to follow process

---

## Resources and Constraints

### Time Budget
- **Available:** 7-10 full work days over 2 weeks
- **Required:** 14-20 days estimated (aggressive but achievable with focus)
- **Strategy:** Parallel work where possible, ruthless scope control

### Knowledge Requirements
- AI/ML dataset knowledge (ImageNet specifics) - research required
- Standards familiarity (GDPR, PROV, AI Act) - reading required
- Semantic web (JSON-LD, RDF) - documentation available
- Academic publishing (submission process) - straightforward

### External Dependencies
- None (all work is internal documentation/examples)
- Optional: External reviewer for paper/comparison doc

---

## Communication Plan

### Documentation Updates
- Update `CHANGELOG.md` at completion of epic
- Update `ROADMAP.md` to reflect completed Phase 0 items
- Update `CLAUDE.md` with new structure (governance/, analysis/, examples/)
- Update docs site with new content from all sub-sprints

### Community Communication
- No external announcements during epic (internal build phase)
- After epic completion: announcement post about expanded examples/governance
- Use expanded foundation to launch public comment (Sprint 1.8.0)

---

## Next Steps After Epic

### Sprint 1.8.0: Public Comment Period Launch
- 60-day structured comment period
- Community engagement campaign
- Process for incorporating feedback
- Preparation for v0.2 protocol version

### Sprint 1.9.0: Third Worked Example (Pharmaceutical)
- Clinical trial data from ClinicalTrials.gov
- Demonstrates scope capture and funding distortion
- Most politically potent example

### Sprint 1.10.0: ORP-AI Domain Extension
- Formal specification for AI-specific requirements
- Builds on ImageNet example
- Connection to EU AI Act compliance

---

## Retrospective Template

(To be completed at end of epic)

### What Went Well
- [TBD]

### What Didn't Go Well
- [TBD]

### What We Learned
- [TBD]

### Action Items for Next Epic
- [TBD]

---

**Epic Owner:** Asbjørn
**Contributors:** Claude (documentation support)
**Start Date:** 2026-04-04
**Target Completion:** 2026-04-18
