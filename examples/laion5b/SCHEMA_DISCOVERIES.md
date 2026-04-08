# LAION-5B Schema Discoveries

**Example:** LAION-5B Training Data (5.85B image-text pairs, March 2022)
**Validation Date:** 2026-04-07
**Validator:** ORP v0.1 JSON Schema
**Result:** 88 validation errors
**Sprint:** 1.7.3.1

---

## Summary

Creating a comprehensive ORP-Full document for LAION-5B revealed **88 schema validation errors**, demonstrating that ORP v0.1 schema (designed theoretically) is inadequate for real-world AI training dataset constitution documentation.

These errors are **VALUABLE** - they reveal what the schema SHOULD support, not what we guessed it should support. Combined with ImageNet (85 errors), we have **173 cumulative errors** guiding ORP v0.2 design.

---

## Error Categories (88 Total)

### Category 1: Domain Taxonomy Insufficient (1 error)
**Error 1:** Field 'domain' must be one of: ['policy', 'ai-training', 'governance', 'other']

**Problem:** `ai-training` too broad. LAION-5B is specifically **image-text training data**, distinct from:
- Audio training data (speech recognition, music generation)
- Code training data (GitHub Copilot - Sprint 1.7.3.3)
- Text-only training data (Common Crawl LLM subsets)
- Video training data (future)

**Proposed v0.2 Solution:**
```yaml
domain:
  enum:
    - policy
    - ai-training-images
    - ai-training-text
    - ai-training-code
    - ai-training-audio
    - ai-training-video
    - ai-training-multimodal
    - governance
    - other
```

**Alternative:** Use nested structure `domain: ai-training`, `subdomain: images`

---

### Category 2: Author Roles for Post-Hoc Analysis (2 errors)
**Error 2:** Field 'authors.0.role' must be one of: ['author', 'contributor', 'reviewer']
**Error 3:** Additional properties not allowed ('affiliation' was unexpected)

**Problem:** LAION-5B document is **post-hoc reconstruction**, not authored by LAION team. Need roles:
- `analyst` - External researcher reconstructing constitution from public sources
- `attester` - Person verifying dataset provenance (distinct from author)
- `reconstructor` - Person creating ORP doc for pre-ORP dataset

**Problem 2:** `affiliation` critical for credibility (Public Reason Project vs LAION e.V. vs Stanford vs independent)

**Proposed v0.2 Solution:**
```yaml
authors:
  - name: "Asbjørn Ras"
    role: analyst  # NEW: Post-hoc reconstruction role
    affiliation: "Public Reason Project"  # NEW: Allow affiliation
    orcid: "0000-0000-0000-0000"  # OPTIONAL: Academic identifier
```

---

### Category 3: Layer 1 - Flexible Field Structures (30 errors, #4-33)

#### 3A: Inclusion Criteria (1 error, #4)
**Error 4:** Additional properties not allowed ('rationale' was unexpected)

**Current schema:**
```yaml
inclusion_criteria:
  description: "Images with CLIP > 0.28"  # Just description
```

**LAION-5B needs:**
```yaml
inclusion_criteria:
  description: "CLIP similarity > 0.28"
  rationale: "Maximize dataset size while maintaining relevance"  # Why this threshold?
  tools_used: ["OpenAI CLIP ViT-B/32", "CLIP ViT-L/14"]
  threshold_calibration: "Optimized on LAION-400M predecessor"
```

**Proposed v0.2:** Allow `additionalProperties: true` for inclusion_criteria

#### 3B: Exclusion Criteria (12 errors, #5-16)
**Errors 5-16:** Schema expects `{excluded, reason, potential_impact}`, LAION-5B uses `{criterion, method, rationale, affected_count, limitations}`

**Problem:** Safety-critical datasets need MORE detail than schema allows:
```yaml
exclusion_criteria:
  # Current schema (too minimal):
  - excluded: "Hardcore pornography"
    reason: "Legal liability"
    potential_impact: "Distribution risk"

  # LAION-5B needs (actual):
  - criterion: "Hardcore pornography"  # More specific than "excluded"
    method: "CLIP-based NSFW classifier"  # HOW excluded
    rationale: "Avoid legal issues with sexually explicit content"  # WHY excluded
    affected_count: "2.5-5 billion pairs filtered"  # SCALE
    limitations: "Classifier cannot detect CSAM (age), NCII (consent)"  # GAPS
```

**Proposed v0.2:**
- Keep `excluded`, `reason`, `potential_impact` as REQUIRED (minimum compliance)
- Allow `additionalProperties: true` for domain-specific fields
- Add guidance: "Safety-critical domains should document method, limitations"

#### 3C: Critical Undocumented Exclusions (1 error, #33)
**Error 33:** Additional properties not allowed ('critical_undocumented_exclusions' was unexpected)

**Problem:** THIS IS THE MOST IMPORTANT FIELD FOR LAION-5B. Documents what SHOULD have been excluded but wasn't:
```yaml
critical_undocumented_exclusions:
  - exclusion_gap: "NO CSAM (Child Sexual Abuse Material) PRE-PUBLICATION FILTERING"
    description: |
      LAION-5B released March 2022 WITHOUT any CSAM detection. Result: 3,226 CSAM URLs
      distributed for 21 months before Stanford discovery (Dec 2023).
    tools_not_used:
      - "Microsoft PhotoDNA"
      - "NCMEC hash database"
    consequences:
      - "1,008 confirmed CSAM victims re-victimized"
      - "Federal crime distribution (18 U.S.C. § 2252)"
    severity: "TIER 1 - CRIMINAL/SAFETY HARM"
```

**This field is ESSENTIAL for ORP's value proposition** - surfacing absent safety measures at design time.

**Proposed v0.2:**
- Add `critical_undocumented_exclusions` as OPTIONAL field in Layer 1
- Structure: `{exclusion_gap, description, tools_not_used, rationale_for_omission, consequences, severity}`

#### 3D: Cleaning Decisions (9 errors, #17-25)
**Errors 17-25:** Schema expects `{decision, reason, alternatives_considered}`, LAION-5B uses `{decision, method, rationale, affected_scale, limitations}`

**Problem:** Similar to exclusion_criteria - need technical detail for reproducibility:
```yaml
cleaning_decisions:
  # LAION-5B actual:
  - decision: "URL-only distribution (federated)"
    method: "Store URLs + metadata, not images"
    rationale: "Cost savings ($20-100M), legal liability reduction (DMCA)"
    affected_scale: "100% of dataset (all 5.85B pairs)"
    limitations: "Cannot retrieve cached images, prevents CSAM remediation"
```

**Proposed v0.2:** Allow `additionalProperties: true`, keep `decision` + `reason` as required minimum

#### 3E: Known Limitations Structure (4 errors, #26-29)
**Errors 26-29:** Schema expects array of strings, LAION-5B uses objects `{limitation, description, mitigation, impact}`

**Current schema:**
```yaml
known_limitations:
  - "Link rot (50% URLs dead within 2 years)"  # Just string
  - "Geographic/linguistic bias"
```

**LAION-5B needs:**
```yaml
known_limitations:
  - limitation: "Link rot"
    description: "URLs become unavailable as websites shut down"
    mitigation: "None (federated structure prevents caching)"
    impact: "Dataset utility degrades, reproducibility suffers"
    estimated_scale: "50% URLs dead within 2 years"
```

**Proposed v0.2:** Allow both formats:
- `known_limitations: ["string", "string"]` (ORP-Basic)
- `known_limitations: [{limitation, description, mitigation, impact}]` (ORP-Full)

#### 3F: Access Structure (2 errors, #30-31)
**Error 30:** Field 'access.public' has wrong type (expected boolean)
**Error 31:** Additional properties not allowed ('availability', 'restrictions')

**Problem:** LAION-5B access complex - not simple true/false:
```yaml
access:
  public: true (March 2022 - Dec 2023)  # Not boolean!
  public: false (Dec 2023 - Aug 2024)   # Temporal changes
  public: true (Aug 2024 - present)     # Re-LAION-5B
```

**Proposed v0.2:**
```yaml
access:
  public: boolean  # REQUIRED (current status)
  public_history: [  # OPTIONAL (temporal changes)
    {status: true, date_range: "2022-03 to 2023-12"},
    {status: false, date_range: "2023-12 to 2024-08", reason: "CSAM takedown"},
    {status: true, date_range: "2024-08 to present", note: "Re-LAION-5B"}
  ]
  availability: string  # OPTIONAL (how to access)
  restrictions: string  # OPTIONAL (legal/ethical constraints)
```

#### 3G: Attested By Affiliation (1 error, #32)
**Error 32:** Additional properties not allowed ('affiliation' was unexpected)

**Same issue as author affiliation** - credibility requires knowing who attests and their institutional backing.

---

### Category 4: Layer 2 - Consequence Simulation Flexibility (14 errors, #34-47)

#### 4A: Missing Model Field (1 error, #34)
**Error 34:** Missing required field 'model' at l2_consequence_simulation

**Problem:** LAION-5B models **dataset constitution**, not policy/economic model. Schema assumes `model: "CGE model"` or `model: "agent-based simulation"`, but AI training data uses different approach:
- Model: "Counterfactual scenario comparison"
- Method: "Cost-benefit analysis of safety filtering alternatives"

**Proposed v0.2:** Make `model` OPTIONAL, or expand guidance:
```yaml
model:
  type: string
  description: "Analytical model or framework used (e.g., 'CGE', 'agent-based', 'counterfactual comparison', 'cost-benefit analysis')"
  examples: ["CGE model", "Counterfactual scenarios", "Monte Carlo simulation"]
```

#### 4B: Missing Primary Scenario (1 error, #35)
**Error 35:** Missing required field 'primary_scenario' at l2_consequence_simulation

**Problem:** LAION-5B has **4 equally important scenarios** (S1 actual, S2 hash matching, S3 comprehensive, S4 consent). No single "primary" scenario - they're alternatives for comparison.

**Proposed v0.2:** Make `primary_scenario` OPTIONAL, or change to:
```yaml
baseline_scenario: "S1_actual_constitution"  # The "as-built" scenario for comparison
alternative_scenarios: ["S2_hash_matching", "S3_comprehensive_safety", "S4_consent_based"]
```

#### 4C: Affected Population Structure (3 errors, #36-38)
**Errors 36-38:** Schema expects `{description, size_estimate}`, LAION-5B uses `{total, breakdown, direct_stakeholders, indirect_stakeholders}`

**Problem:** AI training data affects BILLIONS across multiple categories. Simple `description` + `size_estimate` insufficient:

**Proposed v0.2:**
```yaml
affected_population:
  total_scale: string  # "billions", "millions", "thousands"
  description: string  # REQUIRED (brief overview)
  size_estimate: string  # OPTIONAL (numeric if available)
  breakdown: array  # OPTIONAL (detailed categories)
  geographic_scope: string  # OPTIONAL
  temporal_scope: string  # OPTIONAL
```

#### 4D: Variables as Object vs List (1 error, #39)
**Error 39:** Field 'l2_consequence_simulation.variables' has wrong type (expected object)

**Problem:** LAION-5B has **5 key variables** (CSAM filtering, medical privacy, consent, human review, distribution structure). Natural representation is **list of variables**, not object with variable names as keys.

**Current schema expects:**
```yaml
variables:
  CSAM_filtering_methodology:  # Key = variable name
    type: categorical
    actual_value: "none"
```

**LAION-5B uses:**
```yaml
variables:
  - variable_id: VAR1_csam_filtering  # List item
    name: "CSAM_filtering_methodology"
    type: categorical
    actual_value: "none"
```

**Proposed v0.2:** Allow both formats (object OR array)

#### 4E: Outcomes as Object vs List (3 errors, #40, 42, 44)
**Errors 40, 42, 44:** Field 'scenarios.X.outcomes' has wrong type (expected object)

**Same issue as variables** - LAION-5B scenarios have multiple outcomes, naturally represented as list:
```yaml
scenarios:
  - scenario_id: S1_actual
    outcomes:
      - outcome: "CSAM distribution (3,226 URLs)"
        magnitude: "Severe (Tier 1 harm)"
        confidence: very-high
      - outcome: "Medical privacy violations"
        magnitude: "Moderate (Tier 2-3 harm)"
        confidence: medium
```

**Proposed v0.2:** Allow outcomes as array OR object

#### 4F: Additional Scenario Fields (3 errors, #41, 43, 45)
**Errors 41, 43, 45:** Additional properties not allowed ('comparison_to_actual')

**Problem:** Counterfactual scenarios (S2, S3, S4) MUST compare to actual (S1) for cost-benefit analysis:
```yaml
scenarios:
  - scenario_id: S2_hash_matching
    # ... outcomes ...
    comparison_to_actual: |
      BENEFIT-COST RATIO: Prevent federal crime ($0 financial value, infinite moral value) vs.
      $50-100K + 2-3 months delay. Ratio: INFINITE (no amount of cost justifies CSAM distribution).
```

**This field is CRITICAL for ORP's value** - showing missed opportunities at negligible cost.

**Proposed v0.2:** Add `comparison_to_actual` as OPTIONAL field in scenarios

#### 4G: Additional Layer 2 Fields (1 error, #47)
**Error 47:** Additional properties not allowed ('assumptions', 'limitations_and_unknowns', 'notes', 'sensitivity_analysis')

**Problem:** These fields are ESSENTIAL for robust consequence simulation:
- `assumptions`: Document what's taken for granted (e.g., "publicly accessible = consented")
- `sensitivity_analysis`: Show which variables matter most (e.g., CSAM filtering EXTREME sensitivity)
- `limitations_and_unknowns`: Acknowledge gaps (e.g., "Cannot quantify medical patients, no audit performed")
- `notes`: Summary insights

**Proposed v0.2:** Add these as OPTIONAL fields in Layer 2

---

### Category 5: Layer 3 - Empathy Mapping Flexibility (11 errors, #48-58)

#### 5A: Missing Stakeholder Map (1 error, #48)
**Error 48:** Missing required field 'stakeholder_map' at l3_empathy_mapping

**Problem:** LAION-5B uses `stakeholder_groups` (list of 10 groups with detailed analysis), schema expects `stakeholder_map` (unclear what structure expected).

**Proposed v0.2:** Accept EITHER:
- `stakeholder_map`: object (keyed by group ID)
- `stakeholder_groups`: array (list of groups) ← LAION-5B / ImageNet use this

#### 5B: Minority Stress Test Structure (4 errors, #50-52)
**Errors 50-52:** Schema expects `{description, groups_tested}`, LAION-5B uses `{test_description, vulnerable_populations_identified, comparative_analysis, minority_stress_test_conclusion}`

**Problem:** LAION-5B stress test is **comprehensive analysis** (500+ lines), not simple description:
- Identifies 4 vulnerable groups (CSAM victims, medical patients, NCII victims, Global South)
- Compares privileged vs vulnerable (representation gap, harm distribution)
- Tests if constitutive decisions systematically disadvantaged minorities (answer: YES, FAILED)
- Concludes with ORP's value (would have surfaced disparity before publication)

**Proposed v0.2:**
```yaml
minority_stress_test:
  description: string  # REQUIRED (brief overview)
  groups_tested: array  # REQUIRED (list of group IDs)
  test_description: string  # OPTIONAL (methodology)
  vulnerable_populations_identified: array  # OPTIONAL (detailed findings)
  comparative_analysis: string  # OPTIONAL (privileged vs vulnerable)
  stress_test_result: string  # OPTIONAL ("PASSED" or "FAILED")
  conclusion: string  # OPTIONAL (synthesis)
```

#### 5C: Net Welfare Assessment Structure (4 errors, #53-57)
**Errors 53-57:** Schema expects `{methodology, conclusion, confidence, confidence_basis}`, LAION-5B uses `{overall_assessment, benefits_summary, harms_summary, utilitarian_analysis, deontological_analysis, harm_prioritization, net_welfare_conclusion}`

**Problem:** LAION-5B welfare assessment is **philosophical analysis** (300+ lines):
- Utilitarian calculation (benefits vs harms in aggregate)
- Critique of utilitarianism (Tier 1 harms not tradeable)
- Deontological analysis (Kantian dignity violated)
- Harm prioritization by tier (TIER 1 absolute priority)
- Distributional justice (Rawlsian principle violated)

**Proposed v0.2:** Allow `additionalProperties: true`, keep `conclusion` + `confidence` as minimum

#### 5D: Additional Layer 3 Fields (1 error, #58)
**Error 58:** Additional properties not allowed ('affected_population', 'stakeholder_groups')

**These are core fields!** `affected_population` (overview) + `stakeholder_groups` (detailed analysis) are the PRIMARY content of Layer 3.

**Proposed v0.2:** Add these as standard fields in Layer 3

---

### Category 6: Layer 4 - Accountability Ledger as List vs Object (1 error, #59)

**Error 59:** Field 'l4_accountability_ledger' has wrong type (expected object)

**Problem:** LAION-5B has **7 constitutive decisions** (D1-D7), naturally represented as **list of decisions**:
```yaml
l4_accountability_ledger:
  - decision_id: D1_clip_filtering
    date: "2021-09-01"
    decision_makers: [{name: "Christoph Schuhmann", ...}]
    decision: "Use CLIP similarity > 0.28 as primary criterion"
    rationale: "..."
    alternatives_not_considered: [...]
    consequences: {intended: [...], unintended: [...]}

  - decision_id: D2_no_csam_filtering
    # CRITICAL: Most consequential decision, completely undocumented
    rationale: UNKNOWN
    # ...
```

**Current schema expects object** (unclear what structure - keyed by decision ID? single decision?).

**Proposed v0.2:** Accept accountability ledger as **array of decisions**, each with:
- `decision_id`, `date`, `decision_makers`, `decision`, `rationale`
- `alternatives_considered`, `alternatives_not_considered` (both OPTIONAL)
- `consequences` (intended, unintended, harm_tier)
- `reversibility`, `decision_transparency`
- `accountability_gap` (OPTIONAL, for documenting undocumented decisions - CRITICAL for LAION-5B)

---

### Category 7: Layer 5 - Fork Registry Complete Mismatch (29 errors, #60-88)

#### 7A: This Document Structure (4 errors, #60-63)
**Errors 60-63:** Schema expects `{forked_from, fork_reason, key_differences}`, LAION-5B uses `{document_id, version, created, status, note}`

**Problem:** `this_document` is NOT a fork (it's post-hoc reconstruction). Schema assumes every ORP document is a fork of something, but:
- Policy documents originate from scratch
- Post-hoc reconstructions (LAION-5B, ImageNet) document pre-ORP datasets

**Proposed v0.2:**
```yaml
this_document:
  document_id: string  # REQUIRED
  version: string  # REQUIRED
  created: date  # REQUIRED
  status: enum  # REQUIRED (draft, final, archived)

  # IF this is a fork:
  forked_from: string  # OPTIONAL
  fork_reason: string  # OPTIONAL
  key_differences: array  # OPTIONAL

  # General notes:
  note: string  # OPTIONAL (e.g., "Post-hoc reconstruction, not official documentation")
```

#### 7B: Known Forks Structure (24 errors, #64-87)
**Errors 64-87:** Schema expects `{document_id, author, created, key_differences, url}`, LAION-5B uses `{fork_id, fork_name, forked_by, fork_date, fork_reason, key_changes, improvements_over_original, limitations, fork_url, fork_status}`

**Problem:** LAION-5B forks are **dataset forks** (Re-LAION-5B removed CSAM, LAION-2B-en subset for Stable Diffusion), not **document forks**. Need different fields:

**Proposed v0.2:**
```yaml
known_forks:
  # For dataset forks:
  - fork_id: string
    fork_name: string
    forked_by: array  # [{name, affiliation}]
    fork_date: date
    fork_reason: string
    key_changes: array  # What changed from original
    improvements_over_original: array  # Benefits
    limitations: array  # Remaining issues
    fork_url: string
    fork_status: enum  # active, archived, superseded

  # For document forks (if someone forks this ORP doc):
  - document_id: string
    author: string
    created: date
    key_differences: array
    url: string
```

#### 7C: Additional Layer 5 Fields (1 error, #88)
**Error 88:** Additional properties not allowed ('fork_encouragement', 'notes', 'potential_forks')

**Problem:** These fields are ESSENTIAL for ORP's fork-first philosophy:
- `potential_forks`: Document alternatives NOT pursued (LAION-Safe, LAION-Consent, LAION-Global, LAION-Living) with cost-benefit analysis
- `fork_encouragement`: Invite community to fork if they disagree
- `notes`: Synthesis of Layer 5's value for generative critique

**Proposed v0.2:** Add these as standard fields in Layer 5

---

## Cross-Cutting Issues

### Issue 1: Flexibility vs Validation Trade-Off
**Pattern:** Errors #4, 8, 12, 16, 19, 22, 25, 31, 33, 41-43, 47, 52, 57, 58, 88

Many errors are "Additional properties not allowed" for fields that are ESSENTIAL for domain-specific analysis. Current schema too restrictive.

**Root Cause:** JSON Schema `additionalProperties: false` blocks extensions.

**Proposed Solution (Sprint 1.7.3.4):**
1. **Core fields strict** (required for minimum compliance)
2. **Extensions flexible** (`additionalProperties: true` at appropriate levels)
3. **Validation warnings** (flag potential typos, log extensions for schema evolution)
4. **Extension registry** (optional, for domains wanting stricter validation)

### Issue 2: List vs Object Ambiguity
**Pattern:** Errors #39, 40, 42, 44, 59

Schema expects objects where natural representation is lists (variables, outcomes, decisions). Causes friction for authors.

**Proposed Solution:**
- Allow **both formats** (object OR array) where sensible
- Provide guidance: "Use array for sequential decisions, object for keyed lookup"
- Validator accepts either, normalizes internally

### Issue 3: Post-Hoc Reconstruction Not Anticipated
**Pattern:** Errors #2-3, 32, 60-63

Schema designed for prospective ORP documents (created during decision-making). LAION-5B and ImageNet are **retrospective** (analyzing pre-ORP datasets).

**Proposed Solution:**
- Add `analyst`, `reconstructor`, `attester` roles
- Add `affiliation` field for credibility
- Add `post_hoc: boolean` flag in header
- Add `accountability_gap` field in Layer 4 for documenting undocumented decisions

### Issue 4: Safety-Critical Domains Need More Detail
**Pattern:** Errors #4-33 (Layer 1), #33 (critical_undocumented_exclusions), #41-43 (comparison_to_actual)

AI training datasets with safety implications (CSAM, HIPAA, NCII) require more detail than policy documents:
- Exclusion methods and limitations
- Tools not used (PhotoDNA, NCMEC)
- Harm severity tiers
- Cost-benefit comparison of alternatives

**Proposed Solution:**
- Expand Layer 1 to support safety-specific fields
- Add `critical_undocumented_exclusions` as standard field
- Add `comparison_to_actual` in Layer 2 scenarios
- Add `harm_tier` classification

---

## Schema Evolution Tracking

### Errors by Layer:
- **Header:** 3 errors (domain, author role, affiliation)
- **Layer 1:** 30 errors (flexibility, safety fields, access structure)
- **Layer 2:** 14 errors (model, primary scenario, variables/outcomes structure, extensions)
- **Layer 3:** 11 errors (stakeholder map, stress test, welfare assessment structure)
- **Layer 4:** 1 error (list vs object)
- **Layer 5:** 29 errors (fork registry structure, potential forks, fork encouragement)

### Most Critical Errors (Must Fix for ORP v0.2):
1. **Error #33** - `critical_undocumented_exclusions` (core value of LAION-5B analysis)
2. **Errors #41-43** - `comparison_to_actual` (counterfactual cost-benefit)
3. **Error #59** - Accountability ledger as list (natural for multiple decisions)
4. **Errors #60-88** - Fork registry structure (dataset forks vs document forks)
5. **Errors #2-3, #32** - Author roles and affiliation (post-hoc reconstruction)

### Least Critical Errors (Can Defer):
- **Error #35** - `primary_scenario` (can work around by choosing baseline)
- **Errors #26-29** - Known limitations structure (strings vs objects, both useful)
- **Error #30** - Access boolean (can simplify to current status if needed)

---

## Comparison to ImageNet

**ImageNet:** 85 errors (Sprint 1.7.3, completed 2026-04-07)
**LAION-5B:** 88 errors (Sprint 1.7.3.1, completed 2026-04-07)
**Cumulative:** 173 errors (with overlap expected)

**Overlap Expected:**
- Domain taxonomy (both need `ai-training-images`)
- Author roles (both post-hoc reconstruction)
- Layer 1 flexibility (both need detailed exclusion criteria)
- Layer 4 list structure (both have multiple decisions)
- Layer 5 fork registry (both document dataset forks)

**LAION-5B Unique Discoveries:**
- `critical_undocumented_exclusions` (safety gaps more severe than ImageNet)
- Harm severity tiers (TIER 1 CSAM vs TIER 5 bias)
- Vulnerable populations flagging (children, medical patients, NCII victims)
- `comparison_to_actual` (counterfactual analysis more prominent)
- Federated dataset challenges (link rot, remediation impossibility)

---

## Next Steps

### For Sprint 1.7.3.2 (Common Crawl):
Expected 40-60 new errors, focus areas:
- Living datasets (temporal evolution, monthly releases)
- Linguistic diversity metrics (7,000+ languages, extinction tracking)
- Scale-appropriate provenance (petabyte scale, statistical sampling)
- Existential harm category (language death, irreversible)

### For Sprint 1.7.3.3 (GitHub Copilot):
Expected 20-40 new errors, focus areas:
- Code modality (not images/text)
- License compliance (GPL copyleft, MIT attribution, Apache notices)
- Legal risk assessment (IP, contractual obligations)
- Economic fairness (compensation, revenue sharing)
- Ecosystem harm (sustainability, future contributors)

### For Sprint 1.7.3.4 (Schema Consolidation):
**Goal:** Analyze 175-235 cumulative errors → ORP v0.2 design

**Tasks:**
1. Categorize all errors (required field, wrong type, additional property, structure mismatch)
2. Identify patterns (flexibility, list vs object, post-hoc, safety domains)
3. Design v0.2 schema with:
   - Core fields strict (minimum compliance)
   - Extensions flexible (`additionalProperties: true`)
   - Guidance for domain-specific fields
   - Extension registry pattern (optional)
4. Update validator to handle flexible schema
5. Validate all 5 examples against v0.2 (target: <5 errors each)
6. Write migration guide (v0.1 → v0.2)
7. Document schema evolution methodology (applied research approach)

---

**Document Owner:** Asbjørn Ras
**Last Updated:** 2026-04-07
**Sprint:** 1.7.3.1 (LAION-5B) COMPLETE
**Next:** Sprint 1.7.3.2 (Common Crawl) starts 2026-04-08
