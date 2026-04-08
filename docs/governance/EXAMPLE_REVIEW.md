# OpenReason Example Review Process

**Version:** 1.0
**Status:** Operational
**Last Updated:** 2026-04-07
**Governance Phase:** Phase 0 (Founder Stewardship)

---

## Purpose

This document defines how community-contributed ORP examples are reviewed, accepted, and published. It establishes quality standards without creating barriers to participation, recognizing that examples serve different purposes — from rigorous reference implementations to exploratory demonstrations.

**Core principles:**
1. **Three-tier system** — Official, Community, External (different standards for each)
2. **Validation required** — All examples must pass `orp validate`
3. **Quality over quantity** — Official examples are held to high standards
4. **Transparency** — Review criteria are public and documented
5. **No gatekeeping** — If your example validates, it can be listed (minimum: External tier)

---

## Three-Tier Example System

| Tier | Location | Quality Standard | Review Process | Purpose |
|------|----------|------------------|----------------|---------|
| **Official** | `examples/` in main repo | High - reference quality | Manual substantive review | Demonstrate ORP best practices |
| **Community** | Linked from docs site | Medium - validates + basic quality | Automated + light manual review | Show domain applications |
| **External** | Listed in registry | Low - must validate | Automated only | Broaden ecosystem visibility |

---

## Tier 1: Official Examples

### Purpose
Official examples are **reference implementations** that demonstrate ORP best practices. They serve as:
- Teaching materials for new users
- Test cases for validator development
- Evidence of ORP's applicability
- Models for domain-specific extensions

### Location
- Stored in: `examples/` directory in main repository
- Published on: docs.publicreasonproject.org/examples
- Maintained by: OpenReason project (updates with protocol versions)

### Quality Criteria

An Official Example must meet ALL of these criteria:

#### 1. Technical Validity ✓
- [ ] **Validates:** `orp validate example.yaml` passes without errors
- [ ] **Compliance level met:** If claiming ORP-Full, all 5 layers present
- [ ] **Schema conformance:** Follows JSON schema exactly
- [ ] **Version declared:** Includes `orp_version` field

#### 2. Substantive Content ✓
- [ ] **No placeholders:** All required fields have real content (not "TBD" or "TODO")
- [ ] **Meaningful data:** Layer 1 cites real data sources with verifiable provenance
- [ ] **Real scenarios:** Layer 2 models plausible consequences (not hypothetical nonsense)
- [ ] **Actual stakeholders:** Layer 3 identifies real affected parties
- [ ] **Genuine decisions:** Layer 4 logs actual methodology decisions (or reconstructed from sources)
- [ ] **Substantive forks:** Layer 5 documents real alternatives (if ORP-Full)

#### 3. Verifiable Sources ✓
- [ ] **Citations:** Layer 1 data provenance cites verifiable sources
- [ ] **Attestation:** Layer 1 includes real attestation (who documented this, when, how)
- [ ] **Checkable claims:** Major factual claims can be verified from cited sources
- [ ] **Transparency:** If reconstructed post-hoc, explicitly stated

#### 4. Demonstrates Something New ✓

Must demonstrate at least ONE of:
- [ ] **New domain:** First example in this domain (healthcare, climate, etc.)
- [ ] **New use case:** Novel application of ORP (agent reasoning, scientific publishing)
- [ ] **New depth:** Goes deeper than existing examples (e.g., more detailed L4 ledger)
- [ ] **New challenge:** Addresses a specific ORP challenge (handling uncertainty, absent data)

#### 5. Documentation Quality ✓
- [ ] **README included:** Explains context, methodology, limitations
- [ ] **Clear purpose:** States what this example demonstrates
- [ ] **Readable:** Well-formatted YAML with comments where helpful
- [ ] **Appropriate length:** Substantive but not unnecessarily verbose

#### 6. Tone and Framing ✓
- [ ] **Descriptive, not prescriptive:** Documents constitution, doesn't argue for policy
- [ ] **Neutral:** Doesn't promote specific interests or organizations
- [ ] **Respectful:** Doesn't attack individuals or groups
- [ ] **Educational:** Teaches ORP application, not advocacy

### Submission Process

**Step 1: Proposal (GitLab Issue)**
```markdown
Title: [Official Example Proposal] [Domain]: [Brief Description]

## Domain
[Policy / AI / Healthcare / Climate / Scientific Research / etc.]

## Compliance Level
[ ] ORP-Basic (L1 only)
[ ] ORP-Standard (L1-L3)
[ ] ORP-Full (L1-L5)

## What This Demonstrates
[What aspect of ORP does this showcase? What's new/different from existing examples?]

## Status
[ ] Draft (working on it)
[ ] Ready for review (complete)
[ ] Published elsewhere (link)

## Dataset/Decision Context
[Brief description of what this documents]

## Sources
[What sources will you use for Layer 1 provenance?]
```

**Step 2: Initial Review (1-3 days)**
- Reviewer: Founder (Phase 0) or Example Review Working Group (Post-Phase 0)
- Check: Does this fit Official tier criteria? (domain novelty, feasible scope)
- Outcome:
  - ✅ "Proceed" — contributor develops full example
  - ⏸️ "Revise proposal" — needs clarification
  - ❌ "Suggest Community tier" — valuable but not Official standard

**Step 3: Development**
- Contributor writes ORP document
- Runs `orp validate` to ensure technical validity
- Writes README explaining context

**Step 4: Submission (Attach to Issue or MR)**
- Attach: `example.yaml` + `README.md`
- Post as comment on proposal issue OR open merge request

**Step 5: Automated Review (Instant)**
```bash
# Automated checks:
orp validate example.yaml                    # Must pass
orp check example.yaml --compliance full     # Verify compliance level
yamllint example.yaml                        # YAML formatting
```

If automated checks fail → back to contributor for fixes

**Step 6: Manual Substantive Review (7-14 days)**

Reviewer evaluates:
- All 6 quality criteria above
- Reads example in full
- Checks source citations (spot check, not exhaustive)
- Assesses educational value
- Checks tone/framing

Review outcome documented as comment on issue:
```markdown
## Review: [Example Title]
**Reviewer:** [Name]
**Date:** [YYYY-MM-DD]

### Automated Checks
- [x] Validates with `orp validate`
- [x] Compliance level met (ORP-Full)
- [x] YAML formatting clean

### Quality Criteria
- [x] No placeholders
- [x] Meaningful substantive content
- [x] Sources cited and verifiable
- [x] Demonstrates new domain (AI training data)
- [x] README clear and helpful
- [x] Tone appropriate (descriptive)

### Decision: **ACCEPT** | REVISE | REJECT

### Reasoning
[Why this decision was made]

### Suggested Improvements (if REVISE)
1. [Specific actionable feedback]
2. [...]

### Next Steps
[What happens next]
```

**Step 7: Feedback Loop**
- If **ACCEPT** → merge to `examples/`, publish docs, announce
- If **REVISE** → contributor addresses feedback, resubmits
- If **REJECT** → documented reasoning + suggestion (Community tier? Fork?)

**Step 8: Publication**
- Merged to `examples/` directory
- Added to docs site examples showcase
- Announced in project communications
- Contributor credited in CONTRIBUTORS.md
- Decision logged in DECISION_LOG.md

### Timeline
- Proposal → Initial review: 1-3 days
- Submission → Manual review: 7-14 days
- Revisions (if needed): variable
- Total: 2-6 weeks typically

### Current Official Examples
1. ✅ **Danish Property Tax Reform 2024** (Policy, ORP-Full)
2. 🚧 **ImageNet Training Data Constitution** (AI, ORP-Full) — In development

---

## Tier 2: Community Examples

### Purpose
Community examples are **validated applications** that show ORP in use across domains. Lower bar than Official, but still quality-checked.

### Location
- Stored: External (contributor's repo, organization site, etc.)
- Linked from: docs.publicreasonproject.org/examples/community
- Format: Title, description, link, domain tag, compliance level

### Quality Criteria

A Community Example must meet:

#### 1. Technical Validity ✓
- [ ] **Validates:** `orp validate example.yaml` passes
- [ ] **Version declared:** Includes `orp_version` field

#### 2. Basic Substantive Quality ✓
- [ ] **Not entirely placeholder:** At least 50% of fields have real content
- [ ] **Makes sense:** Content is coherent and relates to stated purpose
- [ ] **Not offensive:** No hate speech, harassment, or harmful content

#### 3. Documentation ✓
- [ ] **Brief description:** What this documents (1-2 sentences)
- [ ] **Compliance level stated:** ORP-Basic/Standard/Full

**Note:** No requirement for cited sources, novel contribution, or reference quality. The bar is "validates + coherent."

### Submission Process

**Step 1: Submit via GitLab Issue**
```markdown
Title: [Community Example] [Domain]: [Title]

## Link
[URL to your ORP document]

## Domain
[Policy / AI / Healthcare / etc.]

## Compliance Level
[ ] ORP-Basic
[ ] ORP-Standard
[ ] ORP-Full

## Brief Description (1-2 sentences)
[What this documents]

## Validation Output
[Paste output of `orp validate your_example.yaml`]
```

**Step 2: Automated Validation (Instant)**
- Bot/reviewer runs `orp validate` on submitted URL
- If passes → proceed
- If fails → back to contributor

**Step 3: Light Manual Check (1-3 days)**
- Reviewer spot-checks: not spam, not harmful, coherent
- **No deep review** — just basic sanity check

**Step 4: Listing**
- Added to Community Examples page on docs site:
  ```markdown
  ### [Example Title](link)
  **Domain:** AI Training Data | **Level:** ORP-Standard
  [Brief description from submission]
  Contributed by: [Name/Organization]
  ```

### Timeline
- Submission → Listing: 3-5 days

---

## Tier 3: External Registry

### Purpose
External examples are **anything that validates**. No quality judgment. Pure discoverability.

### Location
- Stored: `docs/examples/external_registry.json` (machine-readable)
- Displayed: docs.publicreasonproject.org/examples/external (auto-generated from JSON)

### Quality Criteria

**Only requirement:**
- [ ] **Validates:** `orp validate example.yaml` passes

**No other requirements.** If it validates, it can be listed.

### Submission Process

**Step 1: Automated Submission**
- API endpoint (future): POST to `/examples/register` with URL
- Manual (current): Open issue with URL

**Step 2: Automated Validation**
- Bot fetches URL and runs `orp validate`
- If passes → added to registry immediately
- If fails → submission rejected (no manual appeal)

**Step 3: Listing**
Format:
```json
{
  "title": "Example Title",
  "url": "https://example.com/document.yaml",
  "domain": "healthcare",
  "compliance_level": "Basic",
  "submitted": "2026-04-07",
  "validates": true
}
```

### Timeline
- Submission → Listing: Instant (automated)

**Note:** No editorial control. Spam/abuse handled by removing entries post-hoc.

---

## Review Rubric (Official Examples)

Reviewers use this checklist:

### Automated (Pass/Fail)
- [ ] `orp validate` passes (no errors)
- [ ] `orp check --compliance [level]` passes
- [ ] YAML linting passes (valid syntax)

### Substantive Content (Score: 0-5)
0 = All placeholders, meaningless
5 = Rich, detailed, real content throughout

- [ ] Layer 1: Real data sources, cited, verifiable (not "TBD")
- [ ] Layer 2: Plausible scenarios, meaningful variables
- [ ] Layer 3: Real stakeholders, thoughtful impact analysis
- [ ] Layer 4: Genuine decisions logged (or explicitly reconstructed)
- [ ] Layer 5: Real forks documented (if ORP-Full)

**Minimum score for Official: 4/5** (excellent throughout)

### Verifiability (Pass/Fail)
- [ ] Layer 1 sources are real (spot-check 3 citations)
- [ ] Major claims are checkable (not fabricated)
- [ ] Attestation is credible

### Novelty (At least 1)
- [ ] New domain not represented
- [ ] New use case not shown before
- [ ] New depth (more detailed than existing examples)
- [ ] Addresses specific ORP challenge

### Documentation Quality (Score: 0-5)
- [ ] README explains context clearly
- [ ] Purpose/limitations stated
- [ ] Methodology transparent
- [ ] Well-formatted, readable

**Minimum score for Official: 4/5**

### Tone (Pass/Fail)
- [ ] Descriptive not prescriptive
- [ ] Neutral (no advocacy)
- [ ] Respectful (no attacks)

**Decision:**
- **ACCEPT:** All automated pass + Substantive 4+ + Novelty 1+ + Documentation 4+ + Tone pass
- **REVISE:** Close to acceptance but needs specific improvements
- **REJECT (suggest Community):** Validates but doesn't meet Official bar
- **REJECT (not suitable):** Doesn't validate or serious issues

---

## Common Rejection Reasons (and How to Address)

### "Layer 1 sources not verifiable"
**Problem:** Citations are generic ("government data") or don't exist
**Fix:** Add specific URLs, papers, dataset IDs that someone could verify

### "Layer 4 has no real decisions"
**Problem:** Accountability ledger says "TBD" or is generic placeholders
**Fix:** Reconstruct decisions from methodology (or state explicitly: "reconstructed from published sources")

### "Doesn't demonstrate anything new"
**Problem:** Duplicates existing example in same domain without added depth
**Fix:** Either: go deeper than existing examples, or target Community tier instead

### "Tone is prescriptive/advocacy"
**Problem:** Document argues for specific policy rather than documenting constitution
**Fix:** Reframe as descriptive analysis; ORP documents constitution, doesn't prescribe outcomes

### "Too sparse/incomplete"
**Problem:** Most fields are placeholders or minimal content
**Fix:** Flesh out with real content, or target lower compliance level (Standard instead of Full)

---

## Example Migration Between Tiers

Examples can **move up** (rarely down):

**External → Community:**
- Contributor improves quality, adds documentation
- Submits for Community listing (light manual review)

**Community → Official:**
- Contributor brings to Official-tier quality
- Submits through Official process (full review)
- If accepted, moved to `examples/` directory

**Official → Community/External:**
- If example becomes outdated and not maintained
- Decision documented, moved to Community with deprecation notice
- Extremely rare — Official examples are maintained by project

---

## Quality vs. Inclusivity Balance

**Key tension:** High standards (Official tier) vs. broad participation (External tier)

**Resolution:** Three-tier system
- **High bar** exists (Official) for reference quality
- **Low bar** exists (External) for broad participation
- **Middle ground** (Community) for good-enough validated examples

**Philosophy:**
- Better to have 5 excellent Official examples than 50 mediocre ones
- But also better to have 50 validated External examples than to reject them
- Quality tier is transparent — users decide what standard they need

---

## Reviewer Guidelines

### What Reviewers Should Do
- ✅ Assess against documented criteria
- ✅ Provide specific, actionable feedback
- ✅ Suggest improvements (if REVISE)
- ✅ Explain reasoning (if REJECT)
- ✅ Be respectful and constructive
- ✅ Focus on content quality, not contributor identity

### What Reviewers Should NOT Do
- ❌ Reject based on political disagreement with conclusions
- ❌ Accept based on personal/organizational relationships
- ❌ Require perfection (no example is perfect)
- ❌ Gatekeep without documented reasoning
- ❌ Reject without suggesting alternative tier

**Reviewers have conflict of interest if:**
- They work for organization that produced the documented dataset
- They have strong personal/political stake in the example's conclusions
- They are competing with contributor professionally

**If conflict:** Disclose and recuse from review

---

## Handling Controversial Examples

**What if an example documents a contentious topic?**

Examples are **descriptive**, not **prescriptive**. They document the constitutive conditions of data/decisions, not whether those conditions were good or bad.

**Review criteria remain the same:**
- Does it validate?
- Are sources verifiable?
- Is tone descriptive (not advocacy)?
- Does it meet quality criteria?

**Political neutrality:** ORP doesn't take positions on policy. An example documenting a controversial decision is acceptable if it meets quality standards, regardless of the reviewer's view on that decision.

**If community objects:** Fork and create alternative documentation. Layer 5 exists for this.

---

## Appeals Process

**If contributor disagrees with rejection:**

**Step 1: Request Reconsideration**
- Post comment on issue with: new evidence, addressed concerns, or argument for reconsideration
- Reviewer responds within 7 days

**Step 2: Second Review (if substantial new information)**
- Different reviewer evaluates
- Fresh assessment against criteria
- Final decision

**Step 3: Accept Alternative Tier**
- If Official tier not met, Community or External listing available
- No example is rejected entirely (unless it doesn't validate)

**Step 4: Fork** (if still disagree)
- Create fork of ORP with different example standards
- Document reasoning in fork's governance
- Community decides which approach works better

---

## Phase Transition

**When Stewardship Council forms:**
- Example Review Working Group takes over reviews
- This policy reviewed and potentially revised
- Reviewer pool expanded beyond founder
- Decision-making distributed

**Current Status (Phase 0):**
- Founder reviews all Official examples
- Community/External tiers largely automated
- Process tested with first few examples, refined based on experience

---

## Document History

- **v1.0** (2026-04-07): Initial operational version (Sprint 1.7.1)
- Created by: Asbjørn (founder, Phase 0)
- Status: Operational during Phase 0, subject to Working Group review post-handover

---

## Related Documents

- [CONTRIBUTION_PROCESS.md](./CONTRIBUTION_PROCESS.md) — Overall contribution workflow
- [DECISION_LOG.md](./DECISION_LOG.md) — Record of example acceptance decisions
- [GOVERNANCE.md](./GOVERNANCE.md) — High-level governance model
- [ORP_SPEC.md](../specs/ORP_SPEC.md) — Protocol specification
- Examples showcase: https://docs.publicreasonproject.org/examples

---

*This review process is itself subject to contribution. If you think the standards are too high or too low, propose changes through the Governance Changes process.*
