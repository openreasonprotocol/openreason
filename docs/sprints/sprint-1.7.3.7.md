# Sprint 1.7.3.7: ORP v0.2 Specification and Migration Guide

**Sprint Goal**: Document ORP v0.2 specification and provide migration path from v0.1

**Status**: Not Started
**Duration**: 4-6 hours
**Dependencies**: Sprint 1.7.3.6 (all examples validating)

---

## Context

ORP v0.2 is now **functionally complete**:
- ✅ JSON Schema v0.2 implemented with flexibility patterns
- ✅ Validator supports v0.2 with auto-detection
- ✅ 4 AI training dataset examples validate successfully
- ✅ Post-hoc reconstruction support (post_hoc flag, analyst role, accountability_gap)
- ✅ Extension registry (orp-ai-training-v1, orp-safety-v1, orp-license-v1)

**Missing**: Formal specification and migration guidance for adopters.

---

## Scope

### In Scope
1. **ORP v0.2 Specification** (`docs/specs/ORP_V0.2_SPEC.md`)
   - Complete protocol specification
   - Changelog from v0.1
   - Breaking changes documentation
   - Extension system specification

2. **Migration Guide** (`docs/specs/MIGRATION_V0.1_TO_V0.2.md`)
   - Step-by-step upgrade path
   - Automated migration scripts (optional)
   - Common pitfalls and solutions
   - Backward compatibility notes

3. **Updated README**:
   - Add v0.2 release notes
   - Update examples to reference v0.2
   - Update validator installation instructions

### Out of Scope
- v0.2 blog post/announcement (separate task)
- API endpoint updates (handled separately)
- Python package release to PyPI (Sprint 1.7.3.8)
- Deprecation timeline for v0.1 (future decision)

---

## Tasks

### Task 1: Write ORP v0.2 Specification (3-4 hours)

**Objective**: Comprehensive specification documenting v0.2 protocol

**File**: `docs/specs/ORP_V0.2_SPEC.md`

**Structure**:

```markdown
# OpenReason Protocol (ORP) v0.2 Specification

**Version**: 0.2.0
**Status**: Draft
**Release Date**: TBD (2026-04-XX)
**Authors**: Asbjørn Ras (Public Reason Project)
**License**: Creative Commons CC-BY 4.0

---

## Abstract

ORP v0.2 introduces post-hoc reconstruction support, domain-specific extensions, and flexible schema validation while maintaining backward compatibility with v0.1 core required fields.

**Key Changes**:
- Post-hoc reconstruction flag and analyst role
- Extension registry for domain-specific fields
- Flexible schema (additionalProperties: true throughout)
- Granular confidence levels
- Enhanced accountability gap documentation

---

## 1. Introduction

### 1.1 Version History
- **v0.1** (2026-01-XX): Initial specification
- **v0.2** (2026-04-XX): Post-hoc support + extensions

### 1.2 Design Goals for v0.2
1. **Support retrospective analysis**: Not all decisions documented prospectively
2. **Enable domain specialization**: AI training ≠ policy ≠ governance
3. **Embrace real-world messiness**: Documents evolve richer structures over time
4. **Maintain rigor**: Flexibility for unknowns, not excuses for omissions

### 1.3 Backward Compatibility
v0.2 validators MUST validate v0.1 documents. All v0.1 required fields remain required.

---

## 2. Header (Required)

### 2.1 Core Required Fields

```yaml
orp_version: "0.2"         # REQUIRED: Must be "0.2"
document_id: string        # REQUIRED: Unique identifier
title: string              # REQUIRED: Human-readable title
domain: enum               # REQUIRED: [policy, ai-training, governance, research, other]
authors: array             # REQUIRED: At least one author
created: date              # REQUIRED: ISO 8601 date
last_modified: date        # REQUIRED: ISO 8601 date
status: enum               # REQUIRED: [draft, open-for-comment, ratified, superseded]
summary: string            # REQUIRED: Plain language summary
```

### 2.2 New Optional Fields (v0.2)

```yaml
post_hoc: boolean          # NEW: Flags retrospective reconstruction
extensions: array          # NEW: Domain-specific extension IDs
                          # Format: "orp-{name}-v{version}"
                          # Example: ["orp-ai-training-v1"]
```

### 2.3 Author Structure (Enhanced)

```yaml
authors:
  - name: string           # REQUIRED
    role: enum             # REQUIRED: [author, contributor, reviewer, analyst, reconstructor]
                          # NEW: analyst, reconstructor roles
    affiliation: string    # NEW (optional): Organization/institution
    email: string          # OPTIONAL
    orcid: string          # OPTIONAL
```

**v0.2 Roles**:
- `analyst`: Post-hoc analysis from published sources (cannot attest L4 decisions)
- `reconstructor`: Retrospective documentation (similar to analyst but distinct intent)

---

## 3. Layer 1: Data Provenance (Required)

### 3.1 Core Structure

```yaml
l1_data_provenance:
  - dataset_id: string                    # REQUIRED
    name: string                          # REQUIRED
    description: string                   # REQUIRED
    source: string                        # REQUIRED
    collection_method: string             # REQUIRED
    date_range: string                    # REQUIRED
    geographic_scope: string              # REQUIRED

    # Inclusion/Exclusion (Recommended)
    inclusion_criteria: string | object   # v0.2: String OR object
    exclusion_criteria: array             # v0.2: Array of strings OR objects
    cleaning_decisions: array             # v0.2: Array of strings OR objects

    # New v0.2 Fields
    critical_undocumented_exclusions: array  # NEW: Document unknowns
    temporal_metadata:                       # NEW (optional): Collection timing
      start_date: date
      end_date: date
      collection_frequency: string
```

### 3.2 Flexibility Patterns (v0.2)

**exclusion_criteria** accepts both:

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
```

**critical_undocumented_exclusions** (NEW in v0.2):

```yaml
critical_undocumented_exclusions:
  - exclusion_gap: "Geographic distribution of training images"
    description: "80%+ North American/European images, but exact breakdown unknown"
    affected_count: 1200000
    consequences:
      - "Models underperform on Global South images"
    severity: "high"
    accountability_gap: "LAION did not publish geographic metadata"
```

### 3.3 known_limitations (Enhanced)

```yaml
# v0.1: Array of strings
known_limitations:
  - "Temporal decay (link rot)"

# v0.2: Also accepts array of objects
known_limitations:
  - limitation: "Temporal decay (link rot)"
    description: "URLs unavailable over time"
    mitigation: "None (federated structure)"
    impact: "Dataset utility degrades, reproducibility suffers"
```

---

## 4. Layer 2: Consequence Simulation (Optional)

### 4.1 Core Structure

```yaml
l2_consequence_simulation:
  affected_population:              # REQUIRED
    description: string             # v0.2: Now OPTIONAL (can have size without description)
    size: number                    # OPTIONAL
    affected_count: number          # NEW v0.2: Quantify impact
    geographic_distribution: string
    temporal_scope: string

  variables:                        # v0.2: Flexible structure (no strict schema)
    # Can be object with independent/dependent
    # OR array of variables
    # OR custom structure

  scenarios:                        # REQUIRED: At least 1
    - id: string                    # OPTIONAL (v0.2)
      scenario: string              # Alias for description
      description: string
      outcomes: flexible            # v0.2: String/object/array accepted
      comparison_to_actual: string  # NEW v0.2: Counterfactual comparison
      uncertainties: array          # NEW v0.2: Document unknowns
```

### 4.2 New v0.2 Fields

```yaml
# Enhanced confidence tracking
confidence: enum                    # NEW: [very-high, high, medium-high, medium,
                                   #       medium-low, low, very-low]

# Sensitivity analysis
sensitivity_analysis:               # NEW (optional): Object OR array
  variable: string
  impact_magnitude: string
  confidence: string

# Model documentation
model:
  assumptions: array
  limitations: array
  uncertainties: array              # NEW v0.2
```

---

## 5. Layer 3: Empathy Mapping (Optional)

### 5.1 Core Structure

```yaml
l3_empathy_mapping:
  stakeholder_groups:               # v0.2: Array format (more natural)
    - id: string                    # OPTIONAL (v0.2)
      name: string                  # OPTIONAL (v0.2)
      stakeholder: string           # Alias for name
      description: string
      population_size: number | string
      affected_count: number        # NEW v0.2: Quantify impact

      # Flexible benefits/harms (v0.2)
      benefits: array               # String OR object items
      harms: array                  # String OR object items

      # New v0.2 fields
      vulnerable_population_flags: array    # NEW: Minority stress markers
      confidence: string                    # NEW: Granular confidence
```

### 5.2 Flexible Benefits/Harms (v0.2)

```yaml
# Simple format
benefits:
  - "Enabled deep learning revolution"

# Rich format (v0.2 enhancement)
benefits:
  - benefit: "Enabled deep learning revolution"
    magnitude: "Transformative (positive)"
    affected_population: "Global AI research community"
    confidence: "very-high"
    evidence: "ImageNet Challenge results 2012-2017"

harms:
  - harm: "Geographic bias in trained models"
    magnitude: "Significant harm to Global South"
    affected_population: "~2 billion people"
    confidence: "high"
    evidence: "de Vries et al. 2019, Shankar et al. 2017"
```

### 5.3 Minority Stress Test (Enhanced)

```yaml
minority_stress_test:
  result: enum                      # [passed, failed, unclear]
  rationale: string

  # v0.2: Accepts string OR object
  vulnerable_populations_identified:
    - "CSAM victims (children)"    # Simple
    - population_type: "children"  # Rich
      population_size: 3226
      harm_description: "CSAM URL distribution (18 U.S.C. § 2252)"
      consent_obtained: false

  highest_severity_harm: string     # NEW v0.2: Document worst harm
```

---

## 6. Layer 4: Accountability Ledger (Optional)

### 6.1 Core Structure (v0.2 Flexible)

```yaml
l4_accountability_ledger:
  # v0.2: Accepts object OR array, flexible internal structure
  # Recommended: object with entries array

  entries:
    - entry_id: string
      decision: string
      decision_type: enum           # [data, methodology, assumption,
                                   #  exclusion, framing, constitutive, other]
                                   # NEW: constitutive (foundational decisions)

      # Decision timing
      timestamp: string             # Date or year
      decision_date: string         # Alias for timestamp
      decision_date_confidence: string   # NEW v0.2: Indicate uncertainty

      # Decision makers
      decided_by: string | array    # v0.2: "UNKNOWN" OR array of decision makers

      # Rationale
      basis: string                 # OLD v0.1 term
      rationale: string             # Alias for basis
      rationale_stated: string      # NEW v0.2: Explicit from sources
      rationale_inferred: string    # NEW v0.2: Analyst inference

      # Alternatives
      alternatives_considered: string | array | null   # v0.2: Can be null if post_hoc

      # Consequences
      consequences:                 # NEW v0.2 (optional)
        intended: array
        unintended: array
        harms_by_tier: array        # Link to harm taxonomy

      # Gap documentation
      accountability_gap: string    # NEW v0.2: Document unknowns (WHO/WHY/WHAT)
      source: string                # NEW v0.2: Citation for post-hoc reconstruction
```

### 6.2 accountability_gap (New v0.2)

**Purpose**: Document what is unknowable in post-hoc reconstruction

**Required when**: post_hoc: true AND L4 present

**Example**:
```yaml
accountability_gap: |
  UNKNOWN: Who specifically decided to use WordNet 3.0 (2007 decision, pre-dates
  published papers). INFERRED: Likely Fei-Fei Li in consultation with Christiane
  Fellbaum based on meeting documented in biography sources. WHY: WordNet's
  comprehensive taxonomy and Princeton institutional connection made it natural choice.
  WHAT: No documentation of whether alternative taxonomies were seriously evaluated.
```

---

## 7. Layer 5: Fork Registry (Optional)

### 7.1 Core Structure

```yaml
l5_fork_registry:
  known_forks:
    - document_id: string | null    # v0.2: Can be null if no ORP document
      fork_id: string               # NEW v0.2: Alternative identifier
      name: string
      fork_type: string             # NEW v0.2: Categorize fork types
      author: string
      created: date                 # Optional if potential fork
      created_by: string            # Alias for author
      fork_reason: string
      url: string
      citation: string              # NEW v0.2: Academic citation format

  potential_forks:                  # NEW v0.2: Hypothetical alternatives
    - fork_id: string
      fork_title: string
      motivation: string
      key_differences: array
      expected_outcomes: string
```

---

## 8. Extension System (New v0.2)

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
- `orp-medical-v1`: Medical research provenance
- `orp-policy-v1`: Public policy decision fields

### 8.3 Extension Schema Location

Extensions stored in: `orp_validator/schemas/extensions/{extension-name}.schema.json`

**Example**: `orp_validator/schemas/extensions/orp-ai-training-v1.schema.json`

### 8.4 Extension Structure

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://schemas.publicreasonproject.org/orp/extensions/ai-training/v1",
  "title": "ORP AI Training Dataset Extension v1",
  "version": "1.0.0",

  "definitions": {
    "harm_tier": {
      "type": "string",
      "enum": [
        "TIER 1 - EXISTENTIAL",
        "TIER 2 - LEGAL",
        "TIER 3 - ECONOMIC",
        "TIER 4 - ECOSYSTEM",
        "TIER 5 - SECURITY",
        "TIER 6 - BIAS",
        "TIER 7 - DIGNITY"
      ]
    }
  },

  "layer_extensions": {
    "l1_data_provenance": {
      "properties": {
        "safety_filtering_tools": {"$ref": "#/definitions/safety_filtering"}
      }
    },
    "l3_empathy_mapping": {
      "properties": {
        "highest_severity_harm": {"$ref": "#/definitions/harm_tier"}
      }
    }
  }
}
```

### 8.5 Extension Validation (v0.2.0)

**Current behavior**: Extensions are **informational only**
- Validator tracks which extensions are declared
- No schema enforcement (extensions don't break validation)
- Warning issued if extensions declared

**Future (v0.3+)**: Optional strict extension validation

---

## 9. Compliance Levels

### 9.1 ORP-Basic
- Header (all required fields)
- L1 Data Provenance

### 9.2 ORP-Standard
- Header + L1 + L2 + L3

### 9.3 ORP-Full
- Header + L1 + L2 + L3 + L4 + L5

### 9.4 ORP-PostHoc (NEW v0.2)
**Trigger**: `post_hoc: true` flag in header

**Characteristics**:
- Any compliance level (Basic/Standard/Full) + post_hoc flag
- Allows "UNKNOWN" for decision makers, alternatives, dates
- Requires `accountability_gap` documentation in L4 if present
- Author role typically `analyst` or `reconstructor`

**Display**: `ORP-PostHoc` (compliance level reflects layer completeness)

---

## 10. Schema Validation Rules

### 10.1 Required Field Philosophy

**v0.1**: Strict required fields throughout

**v0.2**: "Strict core + flexible everything else"
- **Header required fields**: Never optional (structural identifiers)
- **Layer required fields**: Minimal (only truly essential)
- **Descriptive fields**: Recommended but not required

### 10.2 additionalProperties: true

**Location**: Every object throughout schema

**Rationale**:
1. Documents evolve richer structures naturally
2. Post-hoc reconstruction has unknowns
3. Extensions add fields without schema updates
4. Real-world messiness > theoretical purity

**Constraint**: Required fields still enforced

### 10.3 Type Flexibility Patterns

#### Pattern 1: String OR Object

**Use case**: Simple descriptions vs. structured detail

```yaml
# Accepts both
exclusion_criteria:
  - "Simple string description"      # OK
  - excluded: "Category X"           # OK
    reason: "Not relevant"
    impact: "Reduces scope"
```

#### Pattern 2: Array OR Object

**Use case**: List vs. categorized structure

```yaml
# Accepts both
variables:
  - var1                              # OK (array)
  - var2

variables:                            # OK (object)
  independent: [...]
  dependent: [...]
```

#### Pattern 3: Type OR Null

**Use case**: Unknown values in post-hoc

```yaml
document_id: string | null            # Can be null if fork lacks ORP doc
alternatives_considered: array | null  # Can be null if post_hoc and unknown
```

---

## 11. Migration from v0.1

See: `docs/specs/MIGRATION_V0.1_TO_V0.2.md`

---

## 12. JSON Schema Conformance

- **JSON Schema Version**: Draft-07
- **Schema Location**: `orp_validator/schemas/orp-v0.2.schema.json`
- **Validation Tool**: jsonschema library (Python)
- **Schema URI**: `https://schemas.publicreasonproject.org/orp/v0.2/orp.schema.json` (future)

---

## 13. Versioning Policy

### 13.1 ORP Version Format

**Format**: `{major}.{minor}`

**Examples**: "0.1", "0.2", "1.0"

### 13.2 Version Compatibility

- **Minor version increase** (0.1 → 0.2): Backward compatible, new features
- **Major version increase** (0.x → 1.0): May break compatibility

### 13.3 Validator Support

Validators MUST support:
- Current version (v0.2)
- One previous major version (v0.1)

### 13.4 Deprecation Policy

- v0.1 remains supported through 2026
- Deprecation announced 6 months in advance
- Migration guide provided before deprecation

---

## 14. Changelog (v0.1 → v0.2)

### 14.1 Breaking Changes
**NONE** - v0.2 is backward compatible

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

**L2 Consequence Simulation**:
- `affected_population.affected_count: number`
- `confidence: string`
- `comparison_to_actual: string`
- `uncertainties: array`
- `sensitivity_analysis: object | array`

**L3 Empathy Mapping**:
- `stakeholder_groups[].affected_count: number`
- `stakeholder_groups[].vulnerable_population_flags: array`
- `minority_stress_test.highest_severity_harm: string`

**L4 Accountability Ledger**:
- `entries[].decision_date_confidence: string`
- `entries[].rationale_stated: string`
- `entries[].rationale_inferred: string`
- `entries[].consequences: object`
- `entries[].accountability_gap: string`
- `entries[].source: string`

**L5 Fork Registry**:
- `known_forks[].fork_id: string`
- `known_forks[].fork_type: string`
- `known_forks[].citation: string`
- `potential_forks: array`

### 14.4 New Enums

**authors.role**:
- Added: `analyst`, `reconstructor`

**decision_type**:
- Added: `constitutive`

**confidence levels**:
- Added: `very-high`, `medium-high`, `medium-low`, `very-low`
- (v0.1 had only: `high`, `medium`, `low`)

### 14.5 Flexibility Changes

**Changed from string to string | object**:
- `inclusion_criteria`
- `exclusion_criteria` items
- `cleaning_decisions` items
- `known_limitations` items
- `benefits` items
- `harms` items
- `vulnerable_populations_identified` items

**Changed from required to optional**:
- `l2_consequence_simulation.affected_population.description`

**Changed from strict structure to flexible**:
- `l2_consequence_simulation.variables`
- `l2_consequence_simulation.scenarios[].outcomes`
- `l4_accountability_ledger` (entire structure)

**Changed from string to string | null**:
- `l5_fork_registry.known_forks[].document_id`

---

## 15. References

- **ORP v0.1 Specification**: `docs/specs/ORP_SPEC.md`
- **ORP v0.2 Design Document**: `docs/specs/ORP_V0.2_DESIGN.md`
- **Migration Guide**: `docs/specs/MIGRATION_V0.1_TO_V0.2.md`
- **JSON Schema Draft-07**: https://json-schema.org/draft-07/schema
- **REE Philosophy**: `docs/specs/REE_PHILOSOPHY.md`

---

## Appendix A: Complete v0.2 Example

See: `examples/imagenet_training_data.yaml`

---

## Appendix B: Extension Registry

| Extension | Version | Domain | Status |
|-----------|---------|--------|--------|
| orp-ai-training-v1 | 1.0.0 | AI training datasets | Draft |
| orp-safety-v1 | 1.0.0 | Safety-critical data | Draft |
| orp-license-v1 | 1.0.0 | Software license compliance | Draft |

*Registry maintained at: https://schemas.publicreasonproject.org/orp/extensions/*
```

---

### Task 2: Write Migration Guide (1-2 hours)

**Objective**: Step-by-step guide for upgrading v0.1 documents to v0.2

**File**: `docs/specs/MIGRATION_V0.1_TO_V0.2.md`

**Structure**:

```markdown
# Migration Guide: ORP v0.1 → v0.2

**Target Audience**: Document authors, tool developers, validators

**Difficulty**: Easy (backward compatible)

**Time Estimate**: 5-30 minutes per document (depending on complexity)

---

## Overview

ORP v0.2 is **fully backward compatible** with v0.1. All v0.1 documents are valid v0.2 documents with minimal header changes.

**Migration Types**:
1. **Minimal Migration**: Update version, continue using document (5 minutes)
2. **Enhanced Migration**: Add v0.2 features (post_hoc, extensions) (15-30 minutes)
3. **Full Migration**: Leverage v0.2 flexibility for richer structures (1-2 hours)

---

## Quick Start: Minimal Migration

### Step 1: Update orp_version

```diff
- orp_version: "0.1"
+ orp_version: "0.2"
```

### Step 2: Update last_modified

```yaml
last_modified: "2026-04-08"  # Today's date
```

### Step 3: Validate

```bash
orp-validate my-document.yaml
```

**That's it!** Your v0.1 document is now a valid v0.2 document.

---

## Enhanced Migration: Add v0.2 Features

### When to Use Enhanced Migration

- Document is post-hoc reconstruction
- Document uses domain-specific fields
- Want to leverage v0.2 flexibility

### Step 1: Add post_hoc Flag (If Applicable)

```yaml
orp_version: "0.2"
post_hoc: true  # NEW: Flags retrospective reconstruction
```

**Use post_hoc: true when**:
- Document reconstructed from published sources
- Decision-making history unavailable
- Author role is analyst/reconstructor

### Step 2: Add extensions (If Applicable)

```yaml
orp_version: "0.2"
extensions:
  - orp-ai-training-v1  # If AI training dataset
  - orp-safety-v1       # If safety-critical content
```

### Step 3: Update Author Roles

```diff
authors:
  - name: John Doe
-   role: author
+   role: analyst          # If post-hoc reconstruction
+   affiliation: University of Example  # Optional but recommended
```

### Step 4: Add Extension Fields (Optional)

```yaml
# If using orp-ai-training-v1
l1_data_provenance:
  - dataset_id: imagenet-2012
    # ... existing fields ...
    safety_filtering_tools:  # NEW extension field
      tools_used: []
      tools_not_used: ["PhotoDNA", "CSAM detection"]
      effectiveness: "None - post-hoc reconstruction"

l3_empathy_mapping:
  # ... existing fields ...
  highest_severity_harm: "TIER 6 - BIAS"  # NEW extension field
```

---

## Full Migration: Leverage v0.2 Flexibility

### Upgrade Simple Strings to Rich Objects

#### exclusion_criteria

**Before (v0.1)**:
```yaml
exclusion_criteria:
  - "Non-visual WordNet synsets excluded"
  - "Offensive labels removed in 2019"
```

**After (v0.2 enhanced)**:
```yaml
exclusion_criteria:
  - excluded: "Non-visual WordNet synsets"
    reason: "Not photographable"
    potential_impact: "Limits definition of 'object recognition'"
    data_affected: "~30,000 synsets"

  - excluded: "Offensive person category labels"
    reason: "Violated ethical standards"
    potential_impact: "Removed 600,000 images, 54% of person categories"
    data_affected: "1,593 categories"
```

#### benefits/harms

**Before (v0.1)**:
```yaml
benefits:
  - "Enabled deep learning revolution"
  - "Improved accuracy"

harms:
  - "Geographic bias in models"
  - "Labor exploitation"
```

**After (v0.2 enhanced)**:
```yaml
benefits:
  - benefit: "Enabled deep learning revolution"
    magnitude: "Transformative (positive)"
    affected_population: "Global AI research community"
    confidence: "very-high"
    evidence: "ImageNet Challenge results 2012-2017"

harms:
  - harm: "Geographic bias in trained models"
    magnitude: "Significant harm to Global South populations"
    affected_population: "~2 billion people in under-represented geographies"
    confidence: "high"
    evidence: "de Vries et al. 2019, Shankar et al. 2017"
```

### Add New v0.2 Fields

#### critical_undocumented_exclusions (L1)

```yaml
l1_data_provenance:
  - dataset_id: laion-5b
    # ... existing fields ...

    critical_undocumented_exclusions:  # NEW v0.2
      - exclusion_gap: "CSAM URLs in training data"
        description: "3,226 CSAM URLs discovered post-publication"
        affected_count: 3226
        consequences:
          - "Federal crime distribution (18 U.S.C. § 2252)"
          - "Victim re-traumatization"
        severity: "critical"
        accountability_gap: "No safety filtering applied pre-publication"
```

#### accountability_gap (L4)

```yaml
l4_accountability_ledger:
  entries:
    - entry_id: "001"
      decision: "Use WordNet 3.0 as taxonomy source"
      decision_type: "constitutive"
      timestamp: "2007"
      decided_by: "UNKNOWN"  # v0.2 allows UNKNOWN

      accountability_gap: |  # NEW v0.2
        UNKNOWN: Who specifically decided to use WordNet 3.0 (pre-dates
        published papers). INFERRED: Likely Fei-Fei Li based on biography
        sources. WHY: WordNet's comprehensive taxonomy made it natural choice.
        WHAT: No documentation of alternative taxonomies considered.

      source: "Inferred from Deng et al. (2009) and Li biography sources"  # NEW v0.2
```

#### comparison_to_actual (L2)

```yaml
l2_consequence_simulation:
  scenarios:
    - scenario_id: "counterfactual-global-sampling"
      description: "What if ImageNet used proportional global image sampling?"

      comparison_to_actual: |  # NEW v0.2
        ACTUAL: 80%+ North American/European images, 10-20pp accuracy gap
        on non-Western test sets. COUNTERFACTUAL: Estimated 5-10pp gap if
        globally representative. Harm reduction: ~1 billion people affected
        by reduced model failures.
```

---

## Automated Migration Script (Optional)

```python
#!/usr/bin/env python3
"""
Automated ORP v0.1 → v0.2 migration script

Usage:
    python migrate_v0.1_to_v0.2.py my-document.yaml

What it does:
- Updates orp_version to "0.2"
- Updates last_modified to today
- Optionally adds post_hoc flag (prompts user)
- Validates migrated document
"""

import sys
import yaml
from datetime import date
from pathlib import Path

def migrate_document(file_path: Path):
    # Load document
    with open(file_path) as f:
        doc = yaml.safe_load(f)

    # Check current version
    if doc.get('orp_version') != '0.1':
        print(f"Error: Document version is {doc.get('orp_version')}, expected 0.1")
        sys.exit(1)

    # Update version
    doc['orp_version'] = '0.2'

    # Update last_modified
    doc['last_modified'] = str(date.today())

    # Prompt for post_hoc
    is_post_hoc = input("Is this a post-hoc reconstruction? (y/n): ").lower() == 'y'
    if is_post_hoc:
        doc['post_hoc'] = True

    # Prompt for extensions
    domain = doc.get('domain', '')
    if 'ai' in domain.lower():
        add_ext = input("Add orp-ai-training-v1 extension? (y/n): ").lower() == 'y'
        if add_ext:
            doc['extensions'] = ['orp-ai-training-v1']

    # Save migrated document
    backup_path = file_path.with_suffix('.yaml.v0.1.backup')
    file_path.rename(backup_path)
    print(f"Backup saved: {backup_path}")

    with open(file_path, 'w') as f:
        yaml.dump(doc, f, default_flow_style=False, allow_unicode=True)

    print(f"Migrated document saved: {file_path}")
    print("\nNext steps:")
    print(f"1. Review changes: diff {backup_path} {file_path}")
    print(f"2. Validate: orp-validate {file_path}")
    print("3. Consider adding v0.2 features (see migration guide)")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python migrate_v0.1_to_v0.2.py document.yaml")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    migrate_document(file_path)
```

---

## Common Pitfalls

### Pitfall 1: Forgetting to Update last_modified

**Problem**: Version updated but last_modified still shows v0.1 date

**Solution**:
```yaml
last_modified: "2026-04-08"  # Today's date
```

### Pitfall 2: Adding post_hoc Without Updating Author Role

**Problem**: Document flagged post_hoc but author role still "author"

**Solution**:
```yaml
post_hoc: true
authors:
  - name: Jane Analyst
    role: analyst  # Not "author"
```

### Pitfall 3: Extension Typo

**Problem**: Extension name incorrect (e.g., "ai-training-v1" instead of "orp-ai-training-v1")

**Solution**: Follow naming convention exactly:
```yaml
extensions:
  - orp-ai-training-v1  # Correct
  # NOT: ai-training-v1
  # NOT: orp-ai-training-1
```

### Pitfall 4: Assuming Extensions Auto-Validate

**Problem**: Added extension fields but no schema validation

**Solution**: v0.2.0 extensions are **informational only**. Future versions will support strict validation.

---

## Compatibility Matrix

| Document Version | Validator v0.1 | Validator v0.2 |
|------------------|----------------|----------------|
| ORP v0.1 | ✅ Valid | ✅ Valid (backward compatible) |
| ORP v0.2 | ❌ Invalid (unknown fields) | ✅ Valid |

**Recommendation**: Upgrade validator to v0.2 before migrating documents.

---

## Rollback Procedure

If migration causes issues:

1. Restore backup:
   ```bash
   mv my-document.yaml.v0.1.backup my-document.yaml
   ```

2. Validate with v0.1:
   ```bash
   orp-validate --orp-version 0.1 my-document.yaml
   ```

3. Report issue: https://github.com/publicreason/orp/issues

---

## Further Reading

- **ORP v0.2 Specification**: `docs/specs/ORP_V0.2_SPEC.md`
- **ORP v0.2 Design Document**: `docs/specs/ORP_V0.2_DESIGN.md`
- **Extension Documentation**: `orp_validator/schemas/extensions/README.md`
```

---

### Task 3: Update README (30 minutes)

**Objective**: Add v0.2 release notes to main README

**File**: `README.md`

**Changes**:

```markdown
## Version History

### v0.2.0 (2026-04-XX) - Post-Hoc Reconstruction Support

**New Features**:
- 🔬 **Post-hoc reconstruction support**: `post_hoc` flag and `analyst` role
- 🧩 **Extension system**: Domain-specific fields (orp-ai-training-v1, orp-safety-v1)
- 📊 **Granular confidence levels**: 7-point scale (very-high to very-low)
- 🔍 **Accountability gap documentation**: Document unknowns in retrospective analysis
- 🎯 **Flexible schema**: additionalProperties: true throughout

**Breaking Changes**: None (fully backward compatible)

**Migration**: See `docs/specs/MIGRATION_V0.1_TO_V0.2.md`

### v0.1.0 (2026-01-XX) - Initial Release

**Core Features**:
- 5-layer transparency framework
- JSON Schema validation
- CLI validator
- Danish Property Tax Reform example
```

---

## Success Criteria

### Must Have
- [ ] ORP v0.2 specification complete (15+ pages, comprehensive)
- [ ] Migration guide complete with automated script
- [ ] README updated with v0.2 release notes
- [ ] All links/references valid

### Nice to Have
- [ ] Video walkthrough of migration process
- [ ] Interactive migration checklist
- [ ] Diff examples (v0.1 vs v0.2 side-by-side)

---

## Deliverables

1. `docs/specs/ORP_V0.2_SPEC.md` (complete specification)
2. `docs/specs/MIGRATION_V0.1_TO_V0.2.md` (migration guide)
3. `README.md` (updated with v0.2 notes)
4. `scripts/migrate_v0.1_to_v0.2.py` (optional automated migration)

---

## Notes

**Documentation Philosophy**:
> "Specifications should be comprehensive enough for independent implementation, but readable enough for casual adopters."

**Target Audiences**:
1. **Document authors**: Need quick migration path
2. **Tool developers**: Need complete technical specification
3. **Validators**: Need compliance criteria
4. **Extensions authors**: Need extension patterns

**Style Guidelines**:
- Use examples liberally
- Explain "why" not just "what"
- Include common pitfalls
- Provide migration paths for every breaking change (even though v0.2 has none)

---

## Retrospective (Post-Sprint)

*To be filled after sprint completion*

### What Went Well
-

### What Didn't Go Well
-

### Lessons Learned
-

### Next Steps
- Sprint 1.7.3.8: Release ORP v0.2 to PyPI
- Sprint 1.7.3.9: Update REST API for v0.2
