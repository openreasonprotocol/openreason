# OpenReason Protocol Specification
## ORP v0.1 — Draft for Public Comment

---

## Overview

This document defines the OpenReason Protocol (ORP) — a standardised schema for documenting, sharing, and challenging the reasoning behind consequential decisions in policy, AI, and democratic governance.

An ORP-compliant document is not a static report. It is a **simulatable object**: a structured representation of reasoning that any party can inspect, fork, and re-run with different assumptions to produce a comparable output.

---

## Design principles

- **Layered** — each layer is independently useful and auditable
- **Machine-readable** — structured for both human reading and automated processing
- **Forkable** — any compliant document can be forked, modified, and published as a derivative
- **Diff-able** — differences between an original and a fork are explicit and locatable
- **Incomplete by design** — v0.1 defines the core schema; extensions are expected through community contribution

---

## Document structure

An ORP-compliant document consists of five layers plus a header block.

```
ORP Document
├── Header
├── L1: Data Provenance
├── L2: Consequence Simulation
├── L3: Empathy Mapping
├── L4: Accountability Ledger
└── L5: Fork Registry
```

---

## Header block

Every ORP document begins with a structured header.

```yaml
orp_version: "0.1"
document_id: "[unique identifier]"
title: "[human-readable title]"
domain: "[policy | ai-training | governance | other]"
authors:
  - name: "[name or pseudonym]"
    role: "[author | contributor | reviewer]"
created: "[ISO 8601 date]"
last_modified: "[ISO 8601 date]"
status: "[draft | open-for-comment | ratified | superseded]"
forked_from: "[document_id or null]"
summary: |
  [Plain language description of what this document proposes,
  in 3-5 sentences. Written for a general audience.]
```

---

## L1: Data Provenance

**Purpose:** Document every dataset used in the reasoning, including how it was collected, cleaned, and what was excluded. This is the most critical layer — bias lives here, not in the algorithms.

### Required fields per dataset

```yaml
l1_data_provenance:
  - dataset_id: "[identifier]"
    name: "[human-readable name]"
    description: "[what this dataset contains and why it was used]"
    source: "[origin — government, academic, commercial, synthetic]"
    collection_method: "[how data was gathered]"
    date_range: "[period covered]"
    geographic_scope: "[countries, regions, municipalities]"
    
    inclusion_criteria:
      description: "[what was included and why]"
      
    exclusion_criteria:
      - excluded: "[what was excluded]"
        reason: "[explicit justification]"
        potential_impact: "[how exclusion may affect outcomes]"
        
    cleaning_decisions:
      - decision: "[what was done]"
        reason: "[why]"
        alternatives_considered: "[other approaches considered]"
        
    synthetic_elements:
      present: "[true | false]"
      description: "[if true: what was synthesised, how, and with what assumptions]"
      
    known_limitations:
      - "[explicit statement of what this dataset does not capture well]"
      
    access:
      public: "[true | false]"
      url: "[link if public]"
      license: "[data license]"
```

### L1 attestation

```yaml
    attested_by:
      - name: "[name]"
        role: "[role]"
        date: "[ISO 8601]"
        statement: "[I confirm the above documentation is accurate and complete to the best of my knowledge]"
```

---

## L2: Consequence Simulation

**Purpose:** Define the population affected, the variables modelled, the outcomes measured, and the assumptions used to weight them. Any party should be able to replicate or challenge the simulation using this specification.

```yaml
l2_consequence_simulation:
  
  affected_population:
    description: "[who is affected by this proposal]"
    size_estimate: "[approximate number of people or entities]"
    segments:
      - segment: "[name]"
        description: "[characteristics]"
        estimated_size: "[number or percentage]"
  
  variables:
    independent:
      - variable: "[name]"
        description: "[what it represents]"
        range: "[min to max or set of values]"
        default_value: "[value used in primary simulation]"
        
    dependent:
      - variable: "[name]"
        description: "[what outcome it measures]"
        unit: "[DKK, years, percentage, etc.]"
  
  model:
    type: "[description of modelling approach]"
    assumptions:
      - assumption: "[explicit statement]"
        basis: "[why this assumption was made]"
        sensitivity: "[how much does the outcome change if this assumption is wrong]"
        
  scenarios:
    - scenario_id: "[identifier]"
      name: "[human-readable name]"
      description: "[what this scenario represents]"
      variable_values:
        "[variable_name]": "[value]"
      outcomes:
        "[outcome_variable]": "[result]"
        
  primary_scenario: "[scenario_id of the recommended or base case]"
  
  model_code:
    available: "[true | false]"
    repository: "[url if available]"
    language: "[Python | R | Julia | other]"
```

---

## L3: Empathy Mapping

**Purpose:** Explicitly document who is affected, how, and whether minority or marginalised interests have been stress-tested. This operationalises the REE principle of Universal Sentience — no affected party should be invisible.

```yaml
l3_empathy_mapping:

  stakeholder_map:
    - stakeholder: "[name or category]"
      description: "[who they are]"
      estimated_population: "[size]"
      relationship_to_proposal: "[how they interact with or are affected by this]"
      
      impacts_by_scenario:
        - scenario_id: "[reference to L2 scenario]"
          financial_impact: "[quantified if possible]"
          quality_of_life_impact: "[qualitative description]"
          direction: "[benefits | harmed | neutral | mixed]"
          
      vulnerability_flags:
        - "[flag if this group is elderly, low-income, minority, geographically isolated, etc.]"
        
  minority_stress_test:
    description: "[explicit account of how minority and marginalised interests were tested]"
    groups_tested:
      - group: "[name]"
        scenario_tested: "[what edge case or scenario was run]"
        outcome: "[what happened]"
        mitigation: "[if harmed, how is this addressed]"
        
  unresolved_impacts:
    - "[explicit statement of stakeholder groups whose impacts could not be adequately modelled and why]"
    
  net_welfare_assessment:
    methodology: "[how overall welfare impact was assessed across stakeholders]"
    conclusion: "[plain language summary]"
    confidence: "[high | medium | low]"
    confidence_basis: "[why]"
```

---

## L4: Accountability Ledger

**Purpose:** An append-only log of every significant decision made in the reasoning process — what was decided, by whom, when, and on what basis. Enables learning, challenge, and accountability over time.

```yaml
l4_accountability_ledger:

  entries:
    - entry_id: "[sequential identifier]"
      timestamp: "[ISO 8601]"
      decision_type: "[data | methodology | assumption | exclusion | framing | other]"
      description: "[what was decided]"
      decided_by:
        - name: "[name or role]"
      basis: "[what evidence or reasoning supported this decision]"
      alternatives_considered: "[other options that were considered]"
      dissenting_views: "[if any participant disagreed, summarise their position]"
      
  review_history:
    - review_id: "[identifier]"
      date: "[ISO 8601]"
      reviewer: "[name or organisation]"
      scope: "[what was reviewed]"
      findings: "[summary of findings]"
      changes_resulting: "[entry_ids of ledger entries created as a result]"
```

---

## L5: Fork Registry

**Purpose:** Track the lineage of ORP documents — forks, derivatives, and responses. Makes the public conversation about reasoning navigable and auditable.

```yaml
l5_fork_registry:

  this_document:
    document_id: "[identifier]"
    forked_from: "[parent document_id or null if original]"
    fork_reason: "[why this fork was created]"
    key_differences: "[plain language summary of what changed and why]"
    
  known_forks:
    - document_id: "[identifier of fork]"
      author: "[name or organisation]"
      created: "[ISO 8601]"
      fork_reason: "[why they forked]"
      key_differences: "[plain language summary]"
      url: "[where to find it]"
      
  responses:
    - response_id: "[identifier]"
      type: "[critique | endorsement | amendment-proposal | question]"
      author: "[name or organisation]"
      date: "[ISO 8601]"
      summary: "[plain language summary]"
      url: "[where to find the full response]"
      resolution: "[how the original document responded, if at all]"
```

---

## Compliance levels

ORP defines three compliance levels to allow progressive adoption.

| Level | Requirements |
|-------|-------------|
| **ORP-Basic** | Header + L1 (Data Provenance) complete |
| **ORP-Standard** | Header + L1 + L2 + L3 complete |
| **ORP-Full** | All five layers complete |

A document should declare its compliance level in the header. Incomplete layers must be explicitly flagged as incomplete rather than omitted silently.

---

## Validation

An ORP document is considered valid if:

1. All required fields for its declared compliance level are present
2. No fields are falsified or misleading — attestation provides accountability for this
3. Exclusions and limitations are explicitly documented rather than hidden
4. The fork registry accurately reflects the document's lineage

Automated validation tooling for ORP-compliant documents is planned for v0.2.

---

## Extensions

ORP v0.1 defines the core schema. Domain-specific extensions are expected for:

- AI training data documentation
- Environmental impact assessment
- Healthcare policy
- Economic modelling

Extensions must be backwards compatible with the core schema and submitted through the contribution process defined in [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Changelog

| Version | Date | Summary |
|---------|------|---------|
| 0.1 | 2026-02 | Initial draft for public comment |

---

*This specification is itself an ORP-compliant document. Its own provenance, assumptions, and limitations are documented in [ORP_META.md](ORP_META.md) — forthcoming in v0.2.*
