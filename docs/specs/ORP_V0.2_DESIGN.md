# ORP v0.2 Schema Design

**Version:** 0.2 (Draft)
**Created:** 2026-04-08
**Status:** Design Phase
**Based on:** Empirical validation of 4 AI training dataset examples (311 errors analyzed)

---

## Design Philosophy

ORP v0.2 adopts a **"strict core, flexible extensions"** approach:

1. **Maintain rigor** on essential fields (minimum compliance)
2. **Enable flexibility** for domain-specific needs (extensions)
3. **Support post-hoc reconstruction** (analyst role, unknowns allowed)
4. **Accommodate real-world complexity** (array OR object, living datasets)
5. **Extensibility over time** (new domains add validated extensions without breaking core)

**Key Insight from Validation:** 311 errors revealed systematic schema gaps, not document bugs. ORP v0.1's rigidity (additionalProperties: false, object-only structures, prospective-only design) prevented real-world usage.

---

## Core Design Changes

### 1. additionalProperties: true (Throughout Schema)

**Problem:** 113 errors (36% of total) from undocumented fields not in schema

**Current v0.1:**
```json
{
  "type": "object",
  "required": ["excluded", "potential_impact"],
  "additionalProperties": false  // Rejects any unlisted field
}
```

**Proposed v0.2:**
```json
{
  "type": "object",
  "required": ["excluded", "potential_impact"],  // Strict minimum
  "properties": {
    "excluded": {"type": "string"},
    "potential_impact": {"type": "string"},
    // Recommended but not required:
    "affected_count": {"type": "number"},
    "confidence": {"enum": ["high", "medium", "low"]}
  },
  "additionalProperties": true  // Allow domain-specific fields
}
```

**Rationale:**
- Maintains compliance rigor (required fields enforced)
- Enables innovation (domain experts add fields without schema changes)
- Supports extensibility (orp-ai-training-v1 adds harm_tier without breaking core)

**Impact:** Eliminates 113 errors immediately (36% reduction)

---

### 2. Post-Hoc Reconstruction Support

**Problem:** 142 errors (46% of total) from fields unknowable in retrospective analysis

**Missing Fields in Post-Hoc:**
- `basis` for attestations (AMT workers not consulted, unknown)
- `alternatives_considered` (Google/Stanford didn't document, unknown)
- `decision_makers` individuals (hidden behind corporate entities, unknown)

**Proposed v0.2 Header Field:**
```yaml
orp_version: "0.2"
post_hoc: true  # NEW: Flags retrospective reconstruction
```

**Conditional Requirements:**
```json
{
  "if": {
    "properties": {"post_hoc": {"const": false}}
  },
  "then": {
    "required": ["basis", "alternatives_considered"]
  },
  "else": {
    // post_hoc: true → UNKNOWN allowed
    "properties": {
      "basis": {"type": ["string", "null"]},  // Can be null/UNKNOWN
      "accountability_gap": {"type": "string"}  // NEW: Document unknowns
    }
  }
}
```

**New Fields:**
- `post_hoc` (boolean, header) - Flags retrospective analysis
- `accountability_gap` (string, Layer 4) - Documents unknowns (WHO, WHY, WHAT alternatives)

**Impact:** Eliminates ~50 missing field errors (16% reduction)

---

### 3. Array OR Object Flexibility

**Problem:** 45 errors (14% of total) from rigid object-only structures

**Type Mismatches Found:**
- `scenarios.outcomes` - Natural as array, schema requires object
- `variables` - Could be array OR object (both make sense)
- `known_limitations` - Multiple limitations = array not string

**Proposed v0.2 Pattern (JSON Schema oneOf):**
```json
{
  "oneOf": [
    {
      "type": "array",
      "items": {"$ref": "#/definitions/outcome"}
    },
    {
      "type": "object",
      "additionalProperties": {"$ref": "#/definitions/outcome"}
    }
  ]
}
```

**Apply to:**
- `l2_consequence_simulation.scenarios.outcomes` (array OR object)
- `l2_consequence_simulation.variables` (array OR object)
- `l1_data_provenance.known_limitations` (array of strings OR object)

**Impact:** Eliminates 45 type mismatch errors (14% reduction)

---

### 4. Missing Enums Added

**Problem:** 11 enum violations from missing values

**Current v0.1 Enums:**
- `domain`: [policy, ai-training, governance, other]
- `authors.role`: [author, contributor, reviewer]
- `decision_type`: [data, methodology, assumption, exclusion, framing, other]
- `confidence`: [high, medium, low]

**Proposed v0.2 Additions:**

```json
{
  "domain": {
    "enum": ["policy", "ai-training", "governance", "research", "other"]
    // Added: "research" for academic papers
  },
  "authors.role": {
    "enum": ["author", "contributor", "reviewer", "analyst", "reconstructor"]
    // Added: "analyst" for post-hoc reconstruction, "reconstructor" for archival work
  },
  "decision_type": {
    "enum": ["data", "methodology", "assumption", "exclusion", "framing", "constitutive", "other"]
    // Added: "constitutive" for foundational dataset decisions (ImageNet categories, LAION scraping, etc.)
  },
  "confidence": {
    "enum": ["very-high", "high", "medium-high", "medium", "medium-low", "low", "very-low"]
    // Added: Granular confidence levels for nuanced assessments
  }
}
```

**Impact:** Eliminates 11 enum errors (4% reduction)

---

### 5. New Core Fields (P0 - All 4 Documents)

**Fields Present in All 4 Documents but Not in v0.1 Schema:**

#### Header
```yaml
affiliation: "Public Reason Project"  # NEW: Author institutional context
```

#### Layer 1 (Data Provenance)
```yaml
temporal_metadata:  # NEW: Living dataset timeline
  created: "2009-01-01"
  last_updated: "2024-12-15"
  update_frequency: "annual"
  versions:
    - version: "2009-2017"
      changes: "Annual image additions"
    - version: "2019"
      changes: "Offensive label removal"

critical_undocumented_exclusions:  # NEW: Post-hoc gap analysis
  - exclusion_gap: "NO CONSENT MECHANISM"
    affected_count: 14197122
    accountability_gap: "UNKNOWN - who decided no consent needed"
```

#### Layer 2 (Consequence Simulation)
```yaml
variables:
  - id: "dataset_size"
    confidence: "high"  # NEW: Variable certainty
    actual_value: 14197122  # NEW: Actual vs simulated

scenarios:
  - id: "S1_actual"
    outcomes:
      - outcome: "Bias harm"
        value: 0.15
        confidence: "medium"  # NEW: Outcome certainty
    comparison_to_actual: "baseline"  # NEW: Counterfactual comparison

  - id: "S2_consent"
    outcomes:
      - outcome: "Bias harm"
        value: 0.10
    comparison_to_actual: "S1 bias reduced 5pp, cost $50M"  # NEW

model:
  uncertainties:  # NEW: Model uncertainty documentation
    - "AMT worker labels 30% error rate (Shankar 2020)"
  sensitivity_analysis:  # NEW: Variable importance
    - variable: "western_bias"
      impact: "critical"
```

#### Layer 3 (Empathy Mapping)
```yaml
stakeholder_groups:  # NEW: More natural than stakeholder_map (array vs object)
  - id: "amt_workers"
    affected_count: 49000  # NEW: Quantify population
    vulnerable_population_flags:  # NEW: Minority stress test markers
      - "LABOR EXPLOITATION: $1-2/hour, no credit"

net_welfare_assessment:
  confidence: "medium-high"  # NEW: Granular confidence
```

#### Layer 4 (Accountability Ledger)
```yaml
entries:
  - decision: "Use AMT for labels"
    decision_type: "constitutive"  # NEW enum value
    consequences:  # NEW: Track outcomes
      intended:
        - "$50K labeling cost (vs $5M expert labels)"
      unintended:
        - "30% label error rate (Shankar 2020)"
        - "Worker exploitation ($1-2/hour, no attribution)"
    accountability_gap: |  # NEW: Document unknowns
      UNKNOWN:
      - WHO decided AMT acceptable (Fei-Fei Li? Stanford team? Funding agency?)
      - WHAT alternatives considered (expert labels? active learning? verification?)
      - WHY $1-2/hour wage justified (cost vs ethics analysis conducted?)
```

#### Layer 5 (Fork Registry)
```yaml
forks:  # RENAMED: known_forks → forks (allow both known + potential)
  - fork_id: "F1_consent_based"
    fork_type: "potential"  # NEW: known vs potential
    citation: "Crawford & Paglen (2019)"  # NEW: Academic citations
    affiliation: "AI Now Institute"  # NEW: Institutional context
```

**Impact:** Eliminates ~40 missing field errors + improves document quality

---

## Extension Registry Pattern

**Problem:** Domain-specific fields (harm_tier, license_compliance, linguistic_diversity) clutter core schema

**Proposed v0.2 Extension Mechanism:**

### Header Declaration
```yaml
orp_version: "0.2"
extensions:
  - orp-ai-training-v1  # Adds harm_tier, safety fields
  - orp-safety-v1       # Adds vulnerable_populations, CSAM detection
  - orp-license-v1      # Adds GPL compliance, attribution tracking
```

### Extension Schema Files

**orp-ai-training-v1.schema.json:**
```json
{
  "$id": "https://schemas.publicreasonproject.org/orp/extensions/ai-training/v1",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ORP AI Training Dataset Extension v1",
  "description": "Domain-specific fields for AI training dataset documentation",

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
    },
    "affected_scale": {
      "type": "object",
      "properties": {
        "population_size": {"type": "number"},
        "geographic_scope": {"type": "string"},
        "temporal_scope": {"type": "string"}
      }
    }
  },

  "layer_extensions": {
    "l1_data_provenance": {
      "properties": {
        "safety_filtering_tools": {"type": "array"},
        "data_removed_post_hoc": {"type": "object"}
      }
    },
    "l3_empathy_mapping": {
      "properties": {
        "highest_severity_harm": {"$ref": "#/definitions/harm_tier"},
        "affected_scale": {"$ref": "#/definitions/affected_scale"}
      }
    }
  }
}
```

**orp-license-v1.schema.json:**
```json
{
  "$id": "https://schemas.publicreasonproject.org/orp/extensions/license/v1",
  "title": "ORP License Compliance Extension v1",

  "definitions": {
    "license_distribution": {
      "type": "object",
      "properties": {
        "GPL": {"type": "number"},
        "MIT": {"type": "number"},
        "Apache": {"type": "number"}
      }
    },
    "GPL_compliance": {
      "type": "object",
      "properties": {
        "copyleft_honored": {"type": "boolean"},
        "attribution_preserved": {"type": "boolean"},
        "lawsuit_risk": {"type": "string"}
      }
    }
  }
}
```

### Validator Extension Loading

```python
def validate_with_extensions(document, base_schema, extension_schemas):
    """Validate document against base schema + declared extensions"""

    # Load base schema (ORP v0.2 core)
    validator = jsonschema.Draft7Validator(base_schema)

    # Load extension schemas if declared
    if 'extensions' in document:
        for ext_name in document['extensions']:
            ext_schema = load_extension(ext_name)  # Load from registry
            # Merge extension definitions into validator
            validator = merge_schema(validator, ext_schema)

    # Validate
    errors = list(validator.iter_errors(document))
    return errors
```

**Benefits:**
- Core schema stays focused (policy, governance, generic reasoning)
- Domain experts create extensions (AI safety community designs orp-safety-v1)
- Extensibility without fragmentation (extensions reference base schema)
- Backward compatible (documents without extensions still validate)

---

## Required vs Recommended Fields

**Problem:** Schema conflates minimum compliance (must-have) with best practice (should-have)

**Proposed v0.2 Distinction:**

### REQUIRED (Minimum ORP Compliance)

**Header:**
- orp_version, document_id, title, summary, domain, status, created, last_modified

**Authors:**
- name, role (at least 1 author)

**Layer 1:**
- dataset_id, name, sources (at least 1)

**Layer 2:**
- affected_population, scenarios (at least 1)

**Layer 3:**
- stakeholder_groups (at least 1), net_welfare_assessment

**Layer 4:**
- entries (at least 1 decision logged)

**Layer 5:**
- forks (can be empty array if no forks yet)

### RECOMMENDED (Best Practice)

**Header:**
- authors.affiliation, authors.contact

**Layer 1:**
- temporal_metadata, critical_undocumented_exclusions, known_limitations

**Layer 2:**
- variables, model.assumptions, sensitivity_analysis, uncertainties

**Layer 3:**
- vulnerable_population_flags, minority_stress_test

**Layer 4:**
- consequences, alternatives_considered, accountability_gap

**Layer 5:**
- potential_forks, citations

### Validator Behavior

```python
def validate(document, schema):
    errors = []
    warnings = []

    # Check REQUIRED fields
    for field in schema['required']:
        if field not in document:
            errors.append(f"Missing required field: {field}")

    # Check RECOMMENDED fields
    for field in schema['recommended']:
        if field not in document:
            warnings.append(f"Missing recommended field: {field}")

    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'warnings': warnings,
        'compliance_level': determine_level(errors, warnings)
    }
```

**Output Example:**
```
✗ Invalid (3 errors, 5 warnings)

Errors:
  1. Missing required field 'affected_population' at l2_consequence_simulation
  2. Missing required field 'stakeholder_groups' at l3_empathy_mapping
  3. Field 'confidence' must be one of [very-high, high, medium-high, ...]

Warnings:
  1. Missing recommended field 'alternatives_considered' at l4_accountability_ledger.entries.0
  2. Missing recommended field 'sensitivity_analysis' at l2_consequence_simulation
  3. Missing recommended field 'vulnerable_population_flags' at l3_empathy_mapping
  4. Missing recommended field 'temporal_metadata' at l1_data_provenance
  5. Missing recommended field 'accountability_gap' at l4_accountability_ledger.entries.0

Recommendation: Address errors to achieve ORP compliance. Consider adding recommended fields for best practice.
```

---

## Schema Version Migration

**Header Evolution:**

```yaml
# v0.1 (Prospective Only)
orp_version: "0.1"
document_id: "imagenet-ilsvrc-2012"
title: "ImageNet ILSVRC-2012 Training Data"
domain: "ai"  # Limited enum
authors:
  - name: "Fei-Fei Li"
    role: "author"  # No analyst role

# v0.2 (Post-Hoc Supported)
orp_version: "0.2"
document_id: "imagenet-ilsvrc-2012"
title: "ImageNet ILSVRC-2012 Training Data"
domain: "ai-training"  # Expanded enum
post_hoc: true  # NEW: Flags retrospective reconstruction
authors:
  - name: "Asbjørn Ras"
    role: "analyst"  # NEW: Post-hoc reconstruction role
    affiliation: "Public Reason Project"  # NEW
extensions:  # NEW: Domain-specific fields
  - orp-ai-training-v1
```

**Migration Tool:**
```bash
orp migrate imagenet-ilsvrc-2012-v0.1.yaml --to 0.2 --output imagenet-v0.2.yaml
```

**Migration Logic:**
1. Update `orp_version: "0.1"` → `"0.2"`
2. Add `post_hoc: true` if author role is analyst
3. Expand enum values where needed (ai → ai-training)
4. Detect domain-specific fields → suggest extensions
5. Add `additionalProperties: true` allowance note

---

## Compliance Levels

**ORP-Basic** (Minimum viable):
- Header + L1 + L2 (data + consequences documented)

**ORP-Standard** (Best practice):
- Header + L1 + L2 + L3 (stakeholder analysis added)

**ORP-Full** (Maximum transparency):
- Header + L1 + L2 + L3 + L4 + L5 (accountability + forks)

**v0.2 Addition - ORP-PostHoc:**
- ORP-Full with `post_hoc: true` flag
- Allows UNKNOWN for unknowable fields
- Requires `accountability_gap` documentation

---

## Expected Impact on Validation Errors

### Current State (v0.1)
- ImageNet: 85 errors
- LAION-5B: 88 errors
- Common Crawl: 71 errors
- GitHub Copilot: 67 errors
- **Total: 311 errors**

### After P0 Fixes (v0.2 Core Changes)
- additionalProperties: true → -113 errors
- Post-hoc support → -50 errors
- Array OR object flexibility → -45 errors
- Missing enums → -11 errors
- New core fields → -30 errors
- **Total eliminated: ~250 errors (80%)**
- **Remaining: ~60 errors**

### After P1 Fixes (Layer Enhancements)
- temporal_metadata, critical_undocumented_exclusions → -20 errors
- sensitivity_analysis, uncertainties → -10 errors
- stakeholder_groups, vulnerable_population_flags → -10 errors
- **Total eliminated: ~40 errors (13%)**
- **Remaining: ~20 errors**

### After P2 (Extensions)
- orp-ai-training-v1 (harm_tier, affected_scale) → -10 errors
- orp-license-v1 (GPL_compliance) → -5 errors
- orp-safety-v1 (data_removed) → -3 errors
- **Total eliminated: ~18 errors (6%)**
- **Remaining: <5 errors per document**

### Final State (All Phases)
- ImageNet: <5 errors (from 85)
- LAION-5B: <5 errors (from 88)
- Common Crawl: <5 errors (from 71)
- GitHub Copilot: <5 errors (from 67)
- **Success: 97% error reduction (311 → <20 total)**

---

## Next Steps

1. **Implement JSON Schema v0.2** (base + extensions)
2. **Update validator** (extension loading, warnings vs errors)
3. **Update CLI** (migrate command, extension commands)
4. **Update API** (version parameter, migration endpoint)
5. **Upgrade 4 examples** to v0.2 and validate
6. **Write migration guide** (v0.1 → v0.2 upgrade path)
7. **Document schema evolution** (retrospective on what we learned)

---

**Design Phase Complete:** 2026-04-08
**Next:** Phase 3 (Implementation)
