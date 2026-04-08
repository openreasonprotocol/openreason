# OpenReason Protocol (ORP) v0.2 Specification

**Version**: 0.2.0
**Status**: Draft
**Release Date**: 2026-04-08
**Authors**: Asbjørn Ras (Public Reason Project)
**License**: Creative Commons CC-BY 4.0

---

## Abstract

ORP v0.2 introduces post-hoc reconstruction support, domain-specific extensions, and flexible schema validation while maintaining backward compatibility with v0.1 core required fields.

**Key Changes**:
- Post-hoc reconstruction flag and analyst role
- Extension registry for domain-specific fields
- Flexible schema (additionalProperties: true throughout)
- Granular confidence levels (7-point scale)
- Enhanced accountability gap documentation

**Design Philosophy**: "Strict core + flexible extensions" - required fields remain rigorous, but peripheral structures accept real-world variation.

---

## 1. Introduction

### 1.1 Version History

- **v0.1** (2026-01-15): Initial specification
- **v0.2** (2026-04-08): Post-hoc support + extensions

### 1.2 Design Goals for v0.2

1. **Support retrospective analysis**: Not all decisions documented prospectively
2. **Enable domain specialization**: AI training ≠ policy ≠ governance ≠ medical research
3. **Embrace real-world messiness**: Documents evolve richer structures naturally
4. **Maintain rigor**: Flexibility for unknowns, not excuses for omissions

**Empirical Validation**: v0.2 design based on validating 4 comprehensive AI training dataset examples (ImageNet, LAION-5B, Common Crawl, GitHub Copilot) totaling 8,328 lines. Initial v0.1 schema produced 311 validation errors, revealing need for post-hoc support and structural flexibility.

### 1.3 Backward Compatibility

**Guarantee**: v0.2 validators MUST validate v0.1 documents.

**Rationale**: All v0.1 required fields remain required in v0.2. New features are additive (optional fields, flexible types, extensions).

**Migration Path**: See `docs/specs/MIGRATION_V0.1_TO_V0.2.md`

---

## 2. Header (Required)

### 2.1 Core Required Fields

```yaml
orp_version: "0.2"         # REQUIRED: Must be "0.2"
document_id: string        # REQUIRED: Unique identifier (or null if fork)
title: string              # REQUIRED: Human-readable title
domain: enum               # REQUIRED: [policy, ai-training, governance, research, other]
authors: array             # REQUIRED: At least one author
created: date              # REQUIRED: ISO 8601 date
last_modified: date        # REQUIRED: ISO 8601 date
status: enum               # REQUIRED: [draft, open-for-comment, ratified, superseded]
summary: string            # REQUIRED: Plain language summary
```

**document_id**: Can be `null` for forks that don't have ORP documents (v0.2 flexibility).

### 2.2 New Optional Fields (v0.2)

```yaml
post_hoc: boolean          # NEW: Flags retrospective reconstruction
extensions: array          # NEW: Domain-specific extension IDs
                          # Format: "orp-{name}-v{version}"
                          # Example: ["orp-ai-training-v1", "orp-safety-v1"]
```

**post_hoc flag**:
- `true`: Document reconstructed from published sources (decision-making history unavailable)
- `false` or omitted: Prospective or contemporaneous documentation

**extensions array**:
- Declares which domain-specific extensions are used
- Extensions add fields without breaking schema validation
- Informational only in v0.2.0 (future versions may enforce extension schemas)

### 2.3 Author Structure (Enhanced)

```yaml
authors:
  - name: string           # REQUIRED
    role: enum             # REQUIRED: [author, contributor, reviewer, analyst, reconstructor]
    affiliation: string    # NEW (optional): Organization/institution
    email: string          # OPTIONAL
    orcid: string          # OPTIONAL
```

**New v0.2 Roles**:
- **analyst**: Post-hoc analysis from published sources (cannot attest L4 decisions)
- **reconstructor**: Retrospective documentation (similar to analyst but distinct intent)

**Role Attestation Rules**:
- `author`, `contributor`: Can attest to prospective L4 decisions
- `analyst`, `reconstructor`: Cannot attest to original decisions (use "UNKNOWN" or accountability_gap)
- `reviewer`: Validates work but doesn't create original content

---

## 3. Layer 1: Data Provenance (Required)

### 3.1 Core Structure

```yaml
l1_data_provenance:
  - dataset_id: string                    # REQUIRED: Unique identifier
    name: string                          # REQUIRED: Dataset name
    description: string                   # OPTIONAL (v0.2): Rich description
    source: string                        # REQUIRED: Where data originated
    collection_method: string             # OPTIONAL: How data was collected
    date_range: string | object           # OPTIONAL (v0.2: flexible)
    geographic_scope: string              # OPTIONAL: Geographic coverage

    # Inclusion/Exclusion (Recommended)
    inclusion_criteria: any               # v0.2: Accepts any structure
    exclusion_criteria: any               # v0.2: Accepts any structure
    cleaning_decisions: any               # v0.2: Accepts any structure

    # Limitations
    known_limitations: any                # v0.2: String | array | object

    # Access
    access:
      public: boolean | string            # v0.2: "partial", "conditional"
      license: string
      url: string
      # additionalProperties: true allows "conditions", "cost", etc.

    # Attestation
    attested_by:
      - name: string
        role: string
        date: date
        affiliation: string               # NEW v0.2 (optional)
        statement: string
        basis: string | null              # v0.2: Can be null if post_hoc
```

### 3.2 New v0.2 Fields

#### critical_undocumented_exclusions

```yaml
critical_undocumented_exclusions:       # NEW v0.2: Document unknowns
  - exclusion_gap: string               # What was excluded but not documented
    description: string
    affected_count: number              # Quantify impact
    consequences: array                 # List of harms/issues
    severity: string                    # High/medium/low
    accountability_gap: string          # WHO/WHY/WHAT unknown
```

**Purpose**: Post-hoc reconstruction often discovers exclusions not documented in original dataset creation.

**Example** (from LAION-5B):
```yaml
critical_undocumented_exclusions:
  - exclusion_gap: "CSAM URLs in training data"
    description: "3,226 CSAM URLs discovered post-publication (Stanford 2023)"
    affected_count: 3226
    consequences:
      - "Federal crime distribution (18 U.S.C. § 2252)"
      - "Victim re-traumatization"
    severity: "critical"
    accountability_gap: "No CSAM filtering applied; LAION unaware until Stanford report"
```

#### temporal_metadata

```yaml
temporal_metadata:                      # NEW v0.2: Living dataset timeline
  created: date
  last_updated: date
  update_frequency: string              # "monthly", "annually", "none"
  versions:
    - version: string
      date: date
      changes: string
```

**Use case**: Datasets that evolve over time (Common Crawl monthly snapshots, annual re-releases).

### 3.3 Flexibility Patterns (v0.2)

#### date_range

```yaml
# Simple (v0.1 style)
date_range: "2009-2017"

# Rich (v0.2 enhancement)
date_range:
  start: "2009-01-01"
  end: "2017-12-31"
  temporal_scope: "9 years"
```

#### exclusion_criteria

```yaml
# Simple (v0.1 style)
exclusion_criteria:
  - "Non-visual WordNet synsets excluded"
  - "Offensive labels removed in 2019"

# Rich (v0.2 enhancement)
exclusion_criteria:
  - excluded: "Non-visual WordNet synsets"
    reason: "Not photographable"
    potential_impact: "Limits definition of 'object recognition'"
    data_affected: "~30,000 synsets"
    affected_count: 30000
```

#### known_limitations

```yaml
# v0.1: Array of strings
known_limitations:
  - "Temporal decay (link rot)"
  - "Geographic bias (80%+ Western images)"

# v0.2: Array of objects
known_limitations:
  - limitation: "Temporal decay (link rot)"
    description: "URLs become unavailable over time"
    mitigation: "None (federated structure prevents remediation)"
    impact: "Dataset utility degrades, reproducibility suffers"
    severity: "high"
```

---

## 4. Layer 2: Consequence Simulation (Optional)

### 4.1 Core Structure

```yaml
l2_consequence_simulation:
  affected_population:              # REQUIRED
    description: string             # OPTIONAL (v0.2)
    size: number | string
    affected_count: number          # NEW v0.2: Quantify impact
    geographic_distribution: string
    temporal_scope: string | object # v0.2: Flexible format

  variables: any                    # v0.2: Flexible structure
    # Can be object {independent: [...], dependent: [...]}
    # OR array of variables
    # OR custom structure

  model:                            # OPTIONAL
    description: string             # NEW v0.2: Model explanation
    assumptions: array              # Recommended
    limitations: array              # NEW v0.2
    uncertainties: array            # NEW v0.2

  scenarios:                        # REQUIRED: At least 1
    - id: string                    # OPTIONAL (v0.2)
      scenario_id: string           # Alias for id
      description: string
      scenario: string              # Alias for description
      parameter_values: object      # NEW v0.2: Alternative to variable_values
      variable_values: object       # v0.1 term
      outcomes: any                 # v0.2: Flexible format

  primary_scenario: string          # OPTIONAL: Which scenario is baseline
  sensitivity_analysis: string | array | object  # NEW v0.2
  notes: string                     # NEW v0.2
```

### 4.2 affected_population (Enhanced)

**v0.2 Changes**:
- `description` now OPTIONAL (can have `size` without full description)
- `affected_count` NEW for quantification
- `temporal_scope` accepts string OR object

```yaml
# Minimal
affected_population:
  size: 14300000

# Rich
affected_population:
  description: |
    1.4 million image URLs × estimated 1-2B unique depicted individuals
  size: 14300000
  affected_count: 1000000000
  geographic_distribution: "Global, 80%+ North American/European"
  temporal_scope:
    start: "2009"
    end: "2024-present (ongoing model use)"
    duration: "15+ years"
```

### 4.3 model.assumptions (Enhanced)

```yaml
model:
  assumptions:
    - assumption: string            # REQUIRED
      justification: string         # OPTIONAL (recommended)
      basis: string                 # OPTIONAL
      evidence: string              # NEW v0.2
      sensitivity: string | null    # v0.2: Can be null if not computed
      confidence: enum              # NEW v0.2: Granular scale
        # [very-high, high, medium-high, medium, medium-low, low, very-low]
      notes: string                 # NEW v0.2
```

**confidence levels** (NEW v0.2):
- `very-high`: Empirical data, peer-reviewed
- `high`: Strong evidence, industry standards
- `medium-high`: Multiple corroborating sources
- `medium`: Reasonable inference, some evidence
- `medium-low`: Weak evidence, informed guess
- `low`: Speculative, little evidence
- `very-low`: Highly uncertain, placeholder

### 4.4 sensitivity_analysis (NEW v0.2)

```yaml
# String format (simple)
sensitivity_analysis: |
  CRITICAL VARIABLE: CSAM_filtering_methodology - changing from "none" to
  "hash_only" prevents Tier 1 harm at 5-10% of dataset cost.

# Array format (structured)
sensitivity_analysis:
  - variable: "CSAM_filtering_methodology"
    impact_magnitude: "EXTREME"
    description: "Small input change prevents federal crime"
    cost_difference: "$50K-$100K (5-10% of total)"

# Object format (detailed)
sensitivity_analysis:
  critical_variables:
    - name: "CSAM_filtering"
      sensitivity: "extreme"
  moderate_variables: [...]
  low_sensitivity_variables: [...]
```

---

## 5. Layer 3: Empathy Mapping (Optional)

### 5.1 Core Structure

```yaml
l3_empathy_mapping:
  # v0.2: stakeholder_groups array is primary format
  stakeholder_groups:               # OPTIONAL
    - id: string                    # OPTIONAL
      group_id: string              # Alias for id
      name: string                  # OPTIONAL
      stakeholder: string           # Alias for name
      description: string
      size: string | number
      population_size: number       # OPTIONAL
      affected_count: number        # NEW v0.2: Quantify impact
      representation_in_governance: string
      representation_in_decision_making: string  # Alias
      decision_power: string        # NEW v0.2

      # Flexible benefits/harms (v0.2)
      benefits: string | array      # v0.2: String OR array
      harms: string | array         # v0.2: String OR array

      # New v0.2 fields
      vulnerable_population_flags: array    # NEW: Minority stress markers
      confidence: string                    # NEW: Granular confidence
      notes: string                         # NEW

  # Alternative: stakeholder_map object (v0.1 format)
  stakeholder_map:                  # OPTIONAL (legacy v0.1 format)
    stakeholder_id:
      # ... properties ...

  # Minority Stress Test
  minority_stress_test:
    result: enum                    # [passed, failed, unclear]
    rationale: string
    vulnerable_populations_identified: array
    highest_severity_harm: string   # NEW v0.2
    notes: string                   # NEW v0.2

  # Net Welfare Assessment
  net_welfare_assessment:
    summary: string
    confidence: enum                # NEW v0.2: Granular
    limitations: string
    deontological_analysis: string  # NEW v0.2 (optional)
    utilitarian_analysis: string    # NEW v0.2 (optional)
    recommended_framework: string   # NEW v0.2 (optional)

  unresolved_impacts: array         # OPTIONAL
  notes: string                     # NEW v0.2
```

### 5.2 Flexible Benefits/Harms (v0.2)

```yaml
# String format (special case: NONE)
benefits: "NONE"
harms: "NONE (involuntary participants)"

# Simple array
benefits:
  - "Academic recognition"
  - "Community reputation"

# Rich array (v0.2 enhancement)
benefits:
  - benefit: "Enabled deep learning revolution"
    magnitude: "Transformative (positive)"
    affected_population: "Global AI research community (10,000+ researchers)"
    confidence: "very-high"
    evidence: "ImageNet Challenge results 2012-2017 (error rate 26% → 3%)"
    temporal_scope: "2012-present"

harms:
  - harm: "Geographic bias in trained models"
    magnitude: "Significant harm to Global South populations"
    affected_population: "~2 billion people in under-represented geographies"
    confidence: "high"
    evidence: "de Vries et al. 2019, Shankar et al. 2017"
    harm_tier: "TIER 6 - BIAS"  # Extension field
```

### 5.3 vulnerable_populations_identified (Enhanced)

```yaml
# Simple format
vulnerable_populations_identified:
  - "CSAM victims (children)"
  - "Medical patients (HIPAA-protected)"

# Rich format (v0.2 enhancement)
vulnerable_populations_identified:
  - population_type: "children"
    population_size: 3226
    harm_description: "CSAM URL distribution (18 U.S.C. § 2252)"
    harm_tier: "TIER 1 - EXISTENTIAL"
    consent_obtained: false
    consent_possible: false  # Minors cannot consent to CSAM
    remediation_status: "Partial (URLs removed Dec 2023, cached images remain)"
```

---

## 6. Layer 4: Accountability Ledger (Optional)

### 6.1 Core Structure (v0.2 Flexible)

```yaml
l4_accountability_ledger:
  # v0.2: Accepts flexible structure
  # Recommended: entries array

  entries:                          # OPTIONAL
    - entry_id: string              # OPTIONAL
      decision: string              # REQUIRED
      decision_type: enum           # [data, methodology, assumption,
                                   #  exclusion, framing, constitutive, other]

      # Decision timing
      timestamp: string             # Date, year, or "UNKNOWN"
      decision_date: string         # Alias for timestamp
      decision_date_confidence: string   # NEW v0.2

      # Decision makers
      decided_by: string | array    # v0.2: "UNKNOWN" allowed
      decision_maker: string        # Alias

      # Rationale
      basis: string                 # v0.1 term
      rationale: string             # Alias for basis
      rationale_stated: string      # NEW v0.2: From primary sources
      rationale_inferred: string    # NEW v0.2: Analyst inference

      # Alternatives
      alternatives_considered: string | array | null   # v0.2: Can be null

      # Consequences
      consequences: string | object # v0.2: Flexible
      intended_consequences: array  # NEW v0.2
      unintended_consequences: array # NEW v0.2

      # Gap documentation
      accountability_gap: string    # NEW v0.2: Document unknowns
      source: string                # NEW v0.2: Citation for post-hoc

  # Alternative: decisions array (v0.1 format)
  decisions: array                  # OPTIONAL (legacy)

  # Post-hoc documentation
  post_hoc_reconstruction_notes: string  # NEW v0.2
  attested_by: array               # NEW v0.2 (optional)
```

### 6.2 decision_type (Enhanced)

**v0.2 NEW type**: `constitutive`

**constitutive decisions**: Foundational choices that define the nature of the entire project

**Examples**:
- ImageNet: "Use WordNet 3.0 as taxonomy" (constitutive - defines what "object" means)
- LAION-5B: "Federated URL-only distribution" (constitutive - determines remediation capability)
- Common Crawl: "Seed from Alexa Top 1M" (constitutive - determines geographic distribution)

### 6.3 accountability_gap (NEW v0.2)

**Purpose**: Document what is unknowable in post-hoc reconstruction

**Required when**: `post_hoc: true` AND L4 present

**Format**: WHO + WHY + WHAT structure

**Example** (ImageNet WordNet decision):
```yaml
accountability_gap: |
  WHO: Unknown who specifically decided to use WordNet 3.0 (2007 decision pre-dates
  published papers). INFERRED: Likely Fei-Fei Li in consultation with Christiane
  Fellbaum (WordNet creator) based on Li's Princeton affiliation and biography sources.

  WHY: WordNet's comprehensive taxonomy (21,841 synsets) and Princeton institutional
  connection made it natural choice. Alternative taxonomies (e.g., Cyc, DBpedia)
  incomplete or unsuitable for image classification in 2007.

  WHAT: No documentation of whether alternatives seriously evaluated. Meeting notes
  from 2006-2007 not publicly available. Decision likely made informally given WordNet's
  academic prestige and institutional proximity.
```

### 6.4 rationale_stated vs rationale_inferred (NEW v0.2)

**Use case**: Distinguish primary sources from analyst interpretation

```yaml
rationale_stated: |
  From Deng et al. (2009): "WordNet provides a rich taxonomy with well-defined
  semantic hierarchies, making it ideal for hierarchical image classification."

rationale_inferred: |
  ANALYST INFERENCE: WordNet chosen for three reasons: (1) Academic prestige at
  Princeton, (2) Christiane Fellbaum institutional connection, (3) No comparable
  alternatives in 2007. Decision likely made 2006-2007 based on project timeline,
  though exact date undocumented.

source: "Deng et al. (2009), Li biography (2023), Princeton CS department archives"
```

---

## 7. Layer 5: Fork Registry (Optional)

### 7.1 Core Structure

```yaml
l5_fork_registry:
  # Known forks (existing responses/alternatives)
  known_forks:
    - document_id: string | null    # v0.2: Can be null if no ORP doc
      fork_id: string               # NEW v0.2: Alternative identifier
      name: string
      title: string                 # Alias for name
      fork_type: string             # NEW v0.2: [critique, enhancement, alternative]
      author: string
      created_by: string            # Alias
      created: date
      fork_reason: string
      reason: string                # Alias
      url: string
      citation: string              # NEW v0.2: Academic format

  # Potential forks (hypothetical alternatives)
  potential_forks:                  # NEW v0.2
    - fork_id: string
      fork_title: string
      motivation: string
      key_differences: array
      expected_outcomes: string
      feasibility: string           # OPTIONAL
      estimated_cost: string        # OPTIONAL

  # This document metadata
  this_document:                    # OPTIONAL (v0.1 format)
    canonical: boolean
    parent_document_id: string | null

  notes: string                     # NEW v0.2
```

### 7.2 fork_type (NEW v0.2)

**Types**:
- **critique**: Challenge assumptions/conclusions
- **enhancement**: Add data/analysis to existing work
- **alternative**: Different methodology/framing
- **correction**: Fix errors in original
- **replication**: Reproduce results independently

### 7.3 potential_forks (NEW v0.2)

**Purpose**: Document hypothetical alternatives for transparency

**Example** (LAION-5B potential fork):
```yaml
potential_forks:
  - fork_id: "laion-5b-consent-based"
    fork_title: "LAION-5B Consent-Based Alternative"
    motivation: |
      Eliminate non-consensual content (CSAM, medical, NCII) by using only
      explicitly licensed/consented images (e.g., Creative Commons, opt-in databases).

    key_differences:
      - "Use only CC-licensed images (~250M available vs 5.85B)"
      - "Explicit consent verification (photographer/subject permission)"
      - "Human review of 0.1% sample (catches edge cases)"
      - "Hosted distribution (enables remediation)"

    expected_outcomes:
      pros:
        - "Zero CSAM/medical/NCII (consent verified)"
        - "Remediable (hosted images, not cached URLs)"
        - "Legally defensible (explicit licensing)"
      cons:
        - "95%+ scale reduction (5.85B → 250M)"
        - "Cost increase ($1-5M → $5-10M for consent verification)"
        - "Unknown model quality (untested at this scale)"
      unknowns:
        - "Does 250M consented images train comparable models?"
        - "Long-tail diversity critical for generative models?"

    feasibility: "Technically feasible, economically expensive, empirically untested"
    estimated_cost: "$5-10M (human review + hosting + licensing)"
```

---

## 8. Extension System (NEW v0.2)

### 8.1 Extension Declaration

```yaml
orp_version: "0.2"
extensions:
  - orp-ai-training-v1
  - orp-safety-v1
  - orp-license-v1
```

### 8.2 Extension Naming Convention

**Format**: `orp-{domain}-v{version}`

**Examples**:
- `orp-ai-training-v1`: AI training dataset fields
- `orp-safety-v1`: Safety-critical dataset fields (CSAM, vulnerable populations)
- `orp-license-v1`: Software license compliance (GPL, MIT, Apache)
- `orp-medical-v1`: Medical research provenance (HIPAA, IRB)
- `orp-policy-v1`: Public policy decision fields
- `orp-environmental-v1`: Environmental impact assessments

**Versioning**: Extensions use semantic versioning independently of ORP core versions.

### 8.3 Extension Schema Location

Extensions stored in: `orp_validator/schemas/extensions/{extension-name}.schema.json`

**Example**: `orp_validator/schemas/extensions/orp-ai-training-v1.schema.json`

### 8.4 orp-ai-training-v1 Extension

**Purpose**: AI training dataset provenance fields

**Fields**:

**L1 additions**:
```yaml
safety_filtering_tools:
  tools_used: array           # E.g., ["NSFW classifier", "PhotoDNA"]
  tools_not_used: array       # E.g., ["CSAM detection", "medical filter"]
  effectiveness: string       # Assessment of filtering quality
  false_positive_rate: number # OPTIONAL
  false_negative_rate: number # OPTIONAL
```

**L3 additions**:
```yaml
highest_severity_harm:        # Harm tier classification
  enum:
    - "TIER 1 - EXISTENTIAL"  # Language death, cultural extinction
    - "TIER 2 - LEGAL"        # Federal crimes (CSAM, copyright)
    - "TIER 3 - ECONOMIC"     # Financial harm, labor exploitation
    - "TIER 4 - ECOSYSTEM"    # Market concentration, vendor lock-in
    - "TIER 5 - SECURITY"     # Privacy breaches, data leaks
    - "TIER 6 - BIAS"         # Discrimination, representation gaps
    - "TIER 7 - DIGNITY"      # Ethical harms, consent violations
```

### 8.5 orp-safety-v1 Extension

**Purpose**: Safety-critical dataset fields (CSAM, vulnerable populations)

**Fields**:
```yaml
csam_detection:
  tools_used: array
  detection_date: date        # When CSAM discovered
  affected_count: number      # Number of CSAM instances
  remediation_actions: array
  law_enforcement_notified: boolean

vulnerable_population_protection:
  populations_identified: array
  consent_obtained: boolean
  consent_possible: boolean   # E.g., false for minors
  opt_out_mechanism: string
  notification_sent: boolean
```

### 8.6 orp-license-v1 Extension

**Purpose**: Software license compliance (code training datasets)

**Fields**:
```yaml
license_distribution:        # Breakdown by license type
  MIT: number
  Apache-2.0: number
  GPL-2.0: number
  GPL-3.0: number
  Proprietary: number
  Unknown: number

license_compliance:
  copyleft_violations: array  # GPL code used in non-GPL models
  attribution_provided: boolean
  source_disclosure: boolean  # Required by GPL
  derivative_work_classification: string
```

### 8.7 Extension Validation (v0.2.0)

**Current behavior**: Extensions are **informational only**
- Validator tracks which extensions are declared
- No schema enforcement (extensions don't break validation)
- Warning issued if extensions declared: "Extensions are informational only in v0.2"

**Future (v0.3+)**: Optional strict extension validation
- `--strict-extensions` flag enables extension schema validation
- Invalid extension fields fail validation
- Allows gradual adoption without breaking v0.2 documents

---

## 9. Compliance Levels

### 9.1 ORP-Basic
**Requirements**:
- Header (all required fields)
- L1 Data Provenance (at least 1 dataset)

**Use case**: Minimal transparency for small datasets or simple decisions

### 9.2 ORP-Standard
**Requirements**:
- Header + L1 + L2 + L3

**Use case**: Policy decisions, research provenance, business analytics

### 9.3 ORP-Full
**Requirements**:
- Header + L1 + L2 + L3 + L4 + L5

**Use case**: High-stakes decisions, controversial datasets, public accountability

### 9.4 ORP-PostHoc (NEW v0.2)

**Trigger**: `post_hoc: true` flag in header

**Characteristics**:
- Any compliance level (Basic/Standard/Full) + post_hoc flag
- Allows "UNKNOWN" for decision makers, alternatives, dates
- Requires `accountability_gap` documentation in L4 if present
- Author role typically `analyst` or `reconstructor`

**Display**: Compliance level reflects layer completeness (e.g., "ORP-PostHoc" if L1-L3 present)

**Rationale**: Post-hoc reconstruction cannot attest to unknowable information. Flagging documents as post-hoc prevents false precision.

---

## 10. Schema Validation Rules

### 10.1 Required Field Philosophy

**v0.1**: Strict required fields throughout

**v0.2**: "Strict core + flexible everything else"
- **Header required fields**: Never optional (structural identifiers)
- **Layer required fields**: Minimal (only truly essential)
- **Descriptive fields**: Recommended but not required
- **Unknown values**: Use "UNKNOWN" string or null (not omission)

### 10.2 additionalProperties: true

**Location**: Every object throughout schema

**Rationale**:
1. Documents evolve richer structures naturally (empirical finding from 4 examples)
2. Post-hoc reconstruction has unknowns (cannot attest to unlisted fields)
3. Extensions add fields without schema updates (extensibility)
4. Real-world messiness > theoretical purity (pragmatism)

**Constraint**: Required fields still enforced

**Example**:
```yaml
# Schema allows this even though "impact_on_inferences" not in v0.1 spec
cleaning_decisions:
  - decision: "Remove duplicates"
    method: "Fuzzy matching"
    data_removed: "10% of dataset"
    impact_on_inferences: "Minimal (duplicates provide no new info)"
    rationale_stated: "Reduce training time"
```

### 10.3 Type Flexibility Patterns

#### Pattern 1: String OR Object

**Use case**: Simple descriptions vs. structured detail

**Schema**:
```json
{
  "oneOf": [
    {"type": "string"},
    {"type": "object", "additionalProperties": true}
  ]
}
```

**Example**:
```yaml
# Both accepted
inclusion_criteria: "All publicly accessible web pages"

inclusion_criteria:
  description: "All publicly accessible web pages"
  criteria:
    - "HTTP/HTTPS URLs"
    - "Not blocked by robots.txt"
  exceptions: "Authentication-required content excluded"
```

#### Pattern 2: Array OR Object

**Use case**: List vs. categorized structure

**Example**:
```yaml
# Both accepted
variables:
  - "CSAM_filtering_methodology"
  - "Human_review_percentage"

variables:
  independent: ["CSAM_filtering_methodology", "Human_review_percentage"]
  dependent: ["CSAM_count_in_dataset", "Total_cost"]
  control: ["Dataset_size", "Collection_method"]
```

#### Pattern 3: Type OR Null

**Use case**: Unknown values in post-hoc

**Example**:
```yaml
document_id: null  # Allowed for forks without ORP documents
alternatives_considered: null  # Allowed if post_hoc and unknown
```

#### Pattern 4: String OR String | Object

**Use case**: "NONE" as special case, otherwise rich structure

**Example**:
```yaml
# All accepted
benefits: "NONE"  # Special case for involuntary participants

benefits:
  - "Academic recognition"

benefits:
  - benefit: "Academic recognition"
    magnitude: "Significant"
```

### 10.4 No Strict Enums Unless Critical

**v0.1 approach**: Many string enums (domain, role, decision_type, etc.)

**v0.2 approach**: Enums only for critical fields where validation matters

**Rationale**: Real-world documents use domain-specific terminology. Strict enums break extensibility.

**Exception**: compliance_level, orp_version (structural identifiers)

---

## 11. Migration from v0.1

See: `docs/specs/MIGRATION_V0.1_TO_V0.2.md`

**Quick summary**:
1. Update `orp_version: "0.1"` → `"0.2"`
2. Update `last_modified` to today
3. Optionally add `post_hoc: true` and `extensions: []`
4. Validate with `orp-validate document.yaml`

**Breaking changes**: None (fully backward compatible)

---

## 12. JSON Schema Conformance

- **JSON Schema Version**: Draft-07
- **Schema Location**: `orp_validator/schemas/orp-v0.2.schema.json`
- **Validation Tool**: jsonschema library (Python 3.9+)
- **Schema URI**: `https://schemas.publicreasonproject.org/orp/v0.2/orp.schema.json` (future)

**Schema Size**: 714 lines (v0.2 main schema) + 3 extension schemas (311 lines total)

---

## 13. Versioning Policy

### 13.1 ORP Version Format

**Format**: `{major}.{minor}`

**Examples**: "0.1", "0.2", "1.0"

### 13.2 Version Compatibility

- **Minor version increase** (0.1 → 0.2): Backward compatible, new optional features
- **Major version increase** (0.x → 1.0): May break compatibility, requires migration

### 13.3 Validator Support

Validators MUST support:
- Current version (v0.2)
- One previous major version (v0.1)

**Rationale**: Allows gradual migration without forcing immediate updates.

### 13.4 Deprecation Policy

- v0.1 remains supported through 2026
- Deprecation announced 6 months in advance
- Migration guide provided before deprecation
- Validator warnings 3 months before deprecation

---

## 14. Changelog (v0.1 → v0.2)

### 14.1 Breaking Changes

**NONE** - v0.2 is fully backward compatible

### 14.2 New Required Fields

**NONE** - All v0.1 required fields remain required

### 14.3 New Optional Fields

**Header**:
- `post_hoc: boolean`
- `extensions: array`
- `authors[].affiliation: string`

**L1 Data Provenance**:
- `critical_undocumented_exclusions: array`
- `temporal_metadata: object`
- `dataset_type: string`
- `methodology_changes: array`

**L2 Consequence Simulation**:
- `affected_population.affected_count: number`
- `confidence: enum` (7-point scale)
- `comparison_to_actual: string`
- `comparison_to_baseline: string`
- `uncertainties: array`
- `sensitivity_analysis: string | array | object`
- `model.description: string`
- `model.limitations: array`
- `model.uncertainties: array`
- `notes: string`

**L3 Empathy Mapping**:
- `stakeholder_groups[].affected_count: number`
- `stakeholder_groups[].decision_power: string`
- `stakeholder_groups[].vulnerable_population_flags: array`
- `stakeholder_groups[].confidence: enum`
- `minority_stress_test.highest_severity_harm: string`
- `minority_stress_test.notes: string`
- `net_welfare_assessment.deontological_analysis: string`
- `net_welfare_assessment.utilitarian_analysis: string`
- `net_welfare_assessment.recommended_framework: string`
- `notes: string`

**L4 Accountability Ledger**:
- `entries[].decision_date_confidence: string`
- `entries[].rationale_stated: string`
- `entries[].rationale_inferred: string`
- `entries[].consequences: object`
- `entries[].accountability_gap: string`
- `entries[].source: string`
- `post_hoc_reconstruction_notes: string`
- `attested_by: array`

**L5 Fork Registry**:
- `known_forks[].fork_id: string`
- `known_forks[].fork_type: string`
- `known_forks[].citation: string`
- `potential_forks: array`
- `notes: string`

### 14.4 New Enums

**authors.role**:
- Added: `analyst`, `reconstructor`

**decision_type**:
- Added: `constitutive`

**confidence levels**:
- Added: `very-high`, `medium-high`, `medium-low`, `very-low`
- (v0.1 had only: `high`, `medium`, `low`)

### 14.5 Flexibility Changes

**Changed from string to (string | object)**:
- `inclusion_criteria`
- `date_range`
- `access.public` (boolean | string)

**Changed from array of strings to (array of strings | array of objects)**:
- `exclusion_criteria` items
- `cleaning_decisions` items
- `known_limitations` items
- `benefits` items (also accepts string "NONE")
- `harms` items (also accepts string "NONE")
- `vulnerable_populations_identified` items

**Changed from required to optional**:
- `l2_consequence_simulation.affected_population.description`

**Changed from strict structure to flexible (any)**:
- `l2_consequence_simulation.variables`
- `l2_consequence_simulation.scenarios[].outcomes`
- `l4_accountability_ledger` (entire structure)
- `l1_data_provenance[].inclusion_criteria`
- `l1_data_provenance[].exclusion_criteria`
- `l1_data_provenance[].cleaning_decisions`
- `l1_data_provenance[].known_limitations`

**Changed from string to (string | null)**:
- `l5_fork_registry.known_forks[].document_id`
- `l4_accountability_ledger.entries[].alternatives_considered`

**Changed from string to (string | object)**:
- `l2_consequence_simulation.affected_population.temporal_scope`

---

## 15. Implementation Notes

### 15.1 Validator Requirements

Validators implementing ORP v0.2 MUST:
1. Auto-detect document version from `orp_version` field
2. Validate v0.1 documents correctly (backward compatibility)
3. Accept additionalProperties in all objects
4. Display "ORP-PostHoc" when `post_hoc: true`
5. Track extensions declared (informational warning)

Validators implementing ORP v0.2 SHOULD:
1. Provide helpful error messages (actionable, not cryptic)
2. Suggest v0.2 features when appropriate (e.g., accountability_gap if post_hoc)
3. Validate extension schemas when `--strict-extensions` flag used (future)

### 15.2 Extension Authors

When creating new extensions:
1. Use naming convention: `orp-{domain}-v{version}`
2. Create JSON Schema in `extensions/` directory
3. Document extension in registry
4. Provide examples of extension usage
5. Specify which layers extension modifies

### 15.3 Document Authors

When writing ORP v0.2 documents:
1. Use `post_hoc: true` for retrospective analysis
2. Document accountability gaps explicitly (don't hide unknowns)
3. Use rich object formats when detail matters
4. Declare extensions used
5. Link to primary sources when making claims

---

## 16. References

- **ORP v0.1 Specification**: `docs/specs/ORP_SPEC.md`
- **ORP v0.2 Design Document**: `docs/specs/ORP_V0.2_DESIGN.md`
- **Migration Guide**: `docs/specs/MIGRATION_V0.1_TO_V0.2.md`
- **JSON Schema Draft-07**: https://json-schema.org/draft-07/schema
- **REE Philosophy**: `docs/specs/REE_PHILOSOPHY.md`
- **Empirical Validation Report**: `docs/sprints/sprint-1.7.3.4-validation-report.md`

---

## Appendix A: Complete v0.2 Examples

### A.1 ORP-PostHoc Example (AI Training Dataset)

See: `examples/imagenet_training_data.yaml`

**Highlights**:
- 1,513 lines, ORP-Full + post_hoc
- Demonstrates `accountability_gap` usage
- Shows rich object formats (benefits/harms)
- Uses `orp-ai-training-v1` extension

### A.2 ORP-PostHoc Example (Large-scale Dataset)

See: `examples/laion5b_training_data.yaml`

**Highlights**:
- 2,162 lines, demonstrates scale
- `critical_undocumented_exclusions` (CSAM discovery)
- String format for `sensitivity_analysis`
- Benefits: "NONE" usage

### A.3 ORP-PostHoc Example (Complex Scenarios)

See: `examples/common_crawl_training_data.yaml`

**Highlights**:
- 2,232 lines, 4 counterfactual scenarios
- Object format for `date_range`, `temporal_scope`
- Rich `stakeholder_groups` with 11 groups
- Tier 1 existential harm (language extinction)

### A.4 ORP-PostHoc Example (License Violations)

See: `examples/github_copilot_training_data.yaml`

**Highlights**:
- 2,421 lines, `orp-license-v1` extension
- GPL compliance analysis
- Economic harm quantification
- Deontological vs utilitarian welfare assessment

---

## Appendix B: Extension Registry

| Extension | Version | Domain | Status | Schema Location |
|-----------|---------|--------|--------|-----------------|
| orp-ai-training-v1 | 1.0.0 | AI training datasets | Draft | `extensions/orp-ai-training-v1.schema.json` |
| orp-safety-v1 | 1.0.0 | Safety-critical data | Draft | `extensions/orp-safety-v1.schema.json` |
| orp-license-v1 | 1.0.0 | Software license compliance | Draft | `extensions/orp-license-v1.schema.json` |

**Registry maintained at**: https://schemas.publicreasonproject.org/orp/extensions/ (future)

**Propose new extensions**: https://github.com/publicreason/orp/issues (use "Extension Proposal" template)

---

## Appendix C: Validation Statistics

**ORP v0.2 Schema Development**:
- **Empirical validation**: 4 documents, 8,328 lines total
- **Errors discovered**: 311 (v0.1 schema)
- **Errors resolved**: 311 (v0.2 schema)
- **Validation success rate**: 100% (4/4 documents validate)

**Error Categories (v0.1 → v0.2 fixes)**:
- additionalProperties violations: 113 errors (36%) → Fixed by `additionalProperties: true`
- Missing required fields: 142 errors (46%) → Fixed by making fields optional or allowing null
- Type mismatches: 45 errors (14%) → Fixed by oneOf flexibility patterns
- Enum violations: 11 errors (4%) → Fixed by adding new enum values or removing strict enums

**Schema Metrics**:
- v0.2 main schema: 714 lines
- Extension schemas: 311 lines (3 extensions)
- Total schema size: 1,025 lines
- Flexibility changes: 9 major patterns applied

---

*Document Version: 1.0*
*Last Modified: 2026-04-08*
*Status: Draft (pending public comment)*
