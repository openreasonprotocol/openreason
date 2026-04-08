# ORP Vocabulary Design (v0.1)

**Sprint:** 1.7.4
**Created:** 2026-04-08
**Status:** Draft
**Purpose:** Define custom ORP vocabulary terms for JSON-LD/RDF representation

---

## 1. Vocabulary Overview

**Namespace:** `https://openreason.org/vocab/`
**Prefix:** `orp`
**Version:** 0.1
**Format:** Lightweight RDF vocabulary (not full OWL ontology)

### Design Principles

1. **Reuse first** - Only define terms not covered by existing ontologies
2. **Subclass where applicable** - Extend PROV-O, DCAT, Schema.org classes
3. **Explicit semantics** - Clear definitions for all terms
4. **Version stability** - No breaking changes to published versions
5. **Human-readable** - Labels and comments in natural language

### Relationship to Existing Ontologies

```turtle
# ORP builds on established ontologies:
@prefix orp: <https://openreason.org/vocab/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dc: <http://purl.org/dc/terms/> .
@prefix schema: <http://schema.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
```

---

## 2. Core Classes

### 2.1 orp:Document

**Definition:** An OpenReason Protocol document providing transparent reasoning about a decision, policy, or system.

**Subclass of:** `prov:Entity`

**Properties:**
- All Dublin Core metadata (title, creator, created, etc.)
- `orp:complianceLevel` - Compliance level achieved
- `orp:orpVersion` - ORP protocol version used
- `orp:status` - Document status (draft, final, superseded)
- `orp:hasLayer1`, `orp:hasLayer2`, etc. - Links to layer content

**Example:**
```turtle
:dk-property-tax-reform-2024 a orp:Document, prov:Entity ;
    dc:title "Danish Property Tax Reform 2024" ;
    orp:complianceLevel "full" ;
    orp:orpVersion "0.1" ;
    orp:status "final" ;
    orp:hasLayer1 :l1-data-provenance ;
    orp:hasLayer2 :l2-consequence-simulation ;
    orp:hasLayer3 :l3-empathy-mapping ;
    orp:hasLayer4 :l4-accountability-ledger ;
    orp:hasLayer5 :l5-fork-registry .
```

---

### 2.2 orp:Dataset

**Definition:** A dataset documented in Layer 1 (Data Provenance) of an ORP document.

**Subclass of:** `dcat:Dataset`, `prov:Entity`

**Additional Properties:**
- `orp:exclusionCriterion` - What was excluded and why
- `orp:syntheticElements` - Synthetic or augmented data
- `orp:collectionMethodology` - How data was collected
- `orp:fundingSource` - Funding organizations/sources
- `orp:knownLimitation` - Documented limitations

**Example:**
```turtle
:danish-valuations-2023 a orp:Dataset, dcat:Dataset, prov:Entity ;
    dc:title "Danish Property Valuations 2023" ;
    dcat:temporalCoverage [ dcat:startDate "2023-01-01"^^xsd:date ] ;
    orp:exclusionCriterion [
        a orp:Exclusion ;
        orp:excludedCategory "Non-residential properties" ;
        orp:rationale "Outside scope of residential tax reform"
    ] ;
    orp:fundingSource :danish-tax-authority ;
    orp:knownLimitation "Valuation methodology changed in 2021, affecting comparability" .
```

---

### 2.3 orp:Stakeholder

**Definition:** An individual or group affected by a policy/decision documented in an ORP document.

**Subclass of:** `schema:Person` or `schema:Organization`

**Properties:**
- `orp:stakeholderGroup` - Group name/category
- `orp:representation` - Level of representation (None, Low, Medium, High)
- `orp:impactType` - Type of impact (direct, indirect, externality)
- `orp:estimatedPopulation` - Number of people affected
- `orp:netWelfareImpact` - Expected welfare impact
- `orp:confidence` - Confidence in impact estimate (Low, Medium, High)

**Example:**
```turtle
:homeowners-copenhagen a orp:Stakeholder, schema:Person ;
    orp:stakeholderGroup "Homeowners in Copenhagen" ;
    orp:representation "High" ;
    orp:impactType "direct" ;
    orp:estimatedPopulation 300000 ;
    orp:netWelfareImpact [
        a orp:WelfareImpact ;
        orp:direction "negative" ;
        orp:magnitude "moderate" ;
        orp:confidence "high"
    ] .
```

---

### 2.4 orp:Decision

**Definition:** A methodological decision made during policy analysis, documented in Layer 4 (Accountability Ledger).

**Subclass of:** `prov:Activity`

**Properties:**
- `prov:wasAssociatedWith` - Decision-maker (Agent)
- `prov:used` - Datasets/inputs used
- `prov:startedAtTime` - When decision was made
- `orp:rationale` - Why decision was made
- `orp:constitutiveLogic` - "If this assumption is wrong, the conclusion changes"
- `orp:affectedSections` - Which layers/sections were affected

**Example:**
```turtle
:decision-001 a orp:Decision, prov:Activity ;
    prov:wasAssociatedWith :asbjorn-ras ;
    prov:startedAtTime "2024-01-15T14:30:00"^^xsd:dateTime ;
    dc:description "Excluded non-residential properties from simulation" ;
    orp:rationale "Reform targets residential taxation only" ;
    orp:constitutiveLogic "If commercial properties are later included, tax incidence shifts significantly to business owners" ;
    orp:affectedSections "l2_consequence_simulation", "l3_empathy_mapping" .
```

---

### 2.5 orp:Fork

**Definition:** An alternative or derivative ORP document that builds on or critiques another document.

**Subclass of:** `orp:Document`, `prov:Entity`

**Properties:**
- `prov:wasDerivedFrom` - Parent document
- `orp:forkType` - Type of fork (critique, alternative, amendment, response)
- `orp:keyDifferences` - Summary of what changed
- `orp:respondsTo` - Original document being critiqued (if fork_type is "response")

**Example:**
```turtle
:dk-property-tax-alternative-2024 a orp:Fork, orp:Document, prov:Entity ;
    prov:wasDerivedFrom :dk-property-tax-reform-2024 ;
    orp:forkType "alternative" ;
    dc:title "Alternative Property Tax Reform (Progressive Rates)" ;
    orp:keyDifferences "Uses progressive tax rates instead of flat 1.2% rate. Changes distributional impacts significantly." .
```

---

## 3. Layer-Specific Classes

### 3.1 orp:DataProvenance (Layer 1)

**Definition:** Layer 1 content - collection of datasets with provenance information.

**Properties:**
- `orp:dataset` - Link to orp:Dataset instances

### 3.2 orp:ConsequenceSimulation (Layer 2)

**Definition:** Layer 2 content - simulation of policy outcomes.

**Properties:**
- `orp:affectedPopulation` - Description of affected population
- `orp:independentVariable` - Variables that can be changed
- `orp:dependentVariable` - Variables that are measured
- `orp:scenario` - Simulated scenarios
- `orp:outcome` - Simulation outcomes

### 3.3 orp:EmpathyMapping (Layer 3)

**Definition:** Layer 3 content - stakeholder impact analysis.

**Properties:**
- `orp:stakeholder` - Link to orp:Stakeholder instances
- `orp:minorityStressTesting` - Minority groups specifically tested

### 3.4 orp:AccountabilityLedger (Layer 4)

**Definition:** Layer 4 content - immutable log of decisions.

**Properties:**
- `orp:decision` - Link to orp:Decision instances

### 3.5 orp:ForkRegistry (Layer 5)

**Definition:** Layer 5 content - registry of related documents.

**Properties:**
- `orp:fork` - Link to orp:Fork instances
- `orp:relatedDocument` - Other related documents

---

## 4. Core Properties

### 4.1 Document-Level Properties

| Property | Domain | Range | Definition |
|----------|--------|-------|------------|
| `orp:complianceLevel` | orp:Document | Literal | Compliance level: "basic", "standard", "full", "posthoc" |
| `orp:orpVersion` | orp:Document | Literal | ORP protocol version: "0.1", "0.2", etc. |
| `orp:status` | orp:Document | Literal | Document status: "draft", "final", "superseded" |
| `orp:domain` | orp:Document | Literal | Policy domain: "taxation", "healthcare", "ai-training", etc. |
| `orp:hasLayer1` | orp:Document | orp:DataProvenance | Link to Layer 1 content |
| `orp:hasLayer2` | orp:Document | orp:ConsequenceSimulation | Link to Layer 2 content |
| `orp:hasLayer3` | orp:Document | orp:EmpathyMapping | Link to Layer 3 content |
| `orp:hasLayer4` | orp:Document | orp:AccountabilityLedger | Link to Layer 4 content |
| `orp:hasLayer5` | orp:Document | orp:ForkRegistry | Link to Layer 5 content |

### 4.2 Dataset Properties (Layer 1)

| Property | Domain | Range | Definition |
|----------|--------|-------|------------|
| `orp:exclusionCriterion` | orp:Dataset | orp:Exclusion | What was excluded from dataset |
| `orp:syntheticElements` | orp:Dataset | Literal | Description of synthetic data |
| `orp:collectionMethodology` | orp:Dataset | Literal | How data was collected |
| `orp:fundingSource` | orp:Dataset | schema:Organization | Funding organization |
| `orp:knownLimitation` | orp:Dataset | Literal | Documented dataset limitation |

### 4.3 Stakeholder Properties (Layer 3)

| Property | Domain | Range | Definition |
|----------|--------|-------|------------|
| `orp:stakeholderGroup` | orp:Stakeholder | Literal | Group name (e.g., "Renters in Copenhagen") |
| `orp:representation` | orp:Stakeholder | Literal | Representation level: "None", "Low", "Medium", "High" |
| `orp:impactType` | orp:Stakeholder | Literal | Impact type: "direct", "indirect", "externality" |
| `orp:estimatedPopulation` | orp:Stakeholder | xsd:integer | Number of people in group |
| `orp:netWelfareImpact` | orp:Stakeholder | orp:WelfareImpact | Expected welfare change |
| `orp:confidence` | orp:Stakeholder | Literal | Confidence: "low", "medium", "high" |

### 4.4 Decision Properties (Layer 4)

| Property | Domain | Range | Definition |
|----------|--------|-------|------------|
| `orp:rationale` | orp:Decision | Literal | Why decision was made |
| `orp:constitutiveLogic` | orp:Decision | Literal | "If X is wrong, conclusion changes" |
| `orp:affectedSections` | orp:Decision | Literal | Which sections were affected |

### 4.5 Fork Properties (Layer 5)

| Property | Domain | Range | Definition |
|----------|--------|-------|------------|
| `orp:forkType` | orp:Fork | Literal | Fork type: "critique", "alternative", "amendment", "response" |
| `orp:keyDifferences` | orp:Fork | Literal | Summary of changes from parent |
| `orp:respondsTo` | orp:Fork | orp:Document | Document being critiqued (if fork_type="response") |

---

## 5. Supporting Classes

### 5.1 orp:Exclusion

**Definition:** Something excluded from a dataset.

**Properties:**
- `orp:excludedCategory` - What was excluded (e.g., "Non-residential properties")
- `orp:rationale` - Why it was excluded
- `orp:affectedPopulation` - How many entities were excluded

### 5.2 orp:WelfareImpact

**Definition:** Expected welfare impact on a stakeholder group.

**Properties:**
- `orp:direction` - "positive", "negative", "neutral", "mixed"
- `orp:magnitude` - "negligible", "minor", "moderate", "major"
- `orp:confidence` - "low", "medium", "high"

### 5.3 orp:Scenario

**Definition:** A simulated scenario in Layer 2.

**Properties:**
- `orp:scenarioName` - Name (e.g., "Baseline", "Reform Implemented")
- `orp:assumptions` - Key assumptions
- `orp:outcome` - Simulation results

### 5.4 orp:Variable

**Definition:** A variable in Layer 2 simulation.

**Properties:**
- `orp:variableName` - Name of variable
- `orp:variableType` - "independent" or "dependent"
- `orp:dataType` - Data type (continuous, categorical, binary)

---

## 6. Class Hierarchy (RDF/Turtle)

```turtle
# Core classes
orp:Document rdfs:subClassOf prov:Entity .
orp:Dataset rdfs:subClassOf dcat:Dataset, prov:Entity .
orp:Stakeholder rdfs:subClassOf schema:Person .
orp:Decision rdfs:subClassOf prov:Activity .
orp:Fork rdfs:subClassOf orp:Document .

# Layer classes
orp:DataProvenance rdfs:subClassOf rdfs:Resource .
orp:ConsequenceSimulation rdfs:subClassOf rdfs:Resource .
orp:EmpathyMapping rdfs:subClassOf rdfs:Resource .
orp:AccountabilityLedger rdfs:subClassOf rdfs:Resource .
orp:ForkRegistry rdfs:subClassOf rdfs:Resource .

# Supporting classes
orp:Exclusion rdfs:subClassOf rdfs:Resource .
orp:WelfareImpact rdfs:subClassOf rdfs:Resource .
orp:Scenario rdfs:subClassOf rdfs:Resource .
orp:Variable rdfs:subClassOf rdfs:Resource .
```

---

## 7. Property Domains and Ranges (Summary)

```turtle
# Document properties
orp:complianceLevel rdfs:domain orp:Document ; rdfs:range xsd:string .
orp:orpVersion rdfs:domain orp:Document ; rdfs:range xsd:string .
orp:status rdfs:domain orp:Document ; rdfs:range xsd:string .
orp:domain rdfs:domain orp:Document ; rdfs:range xsd:string .
orp:hasLayer1 rdfs:domain orp:Document ; rdfs:range orp:DataProvenance .
orp:hasLayer2 rdfs:domain orp:Document ; rdfs:range orp:ConsequenceSimulation .
orp:hasLayer3 rdfs:domain orp:Document ; rdfs:range orp:EmpathyMapping .
orp:hasLayer4 rdfs:domain orp:Document ; rdfs:range orp:AccountabilityLedger .
orp:hasLayer5 rdfs:domain orp:Document ; rdfs:range orp:ForkRegistry .

# Dataset properties
orp:exclusionCriterion rdfs:domain orp:Dataset ; rdfs:range orp:Exclusion .
orp:syntheticElements rdfs:domain orp:Dataset ; rdfs:range xsd:string .
orp:collectionMethodology rdfs:domain orp:Dataset ; rdfs:range xsd:string .
orp:fundingSource rdfs:domain orp:Dataset ; rdfs:range schema:Organization .
orp:knownLimitation rdfs:domain orp:Dataset ; rdfs:range xsd:string .

# Stakeholder properties
orp:stakeholderGroup rdfs:domain orp:Stakeholder ; rdfs:range xsd:string .
orp:representation rdfs:domain orp:Stakeholder ; rdfs:range xsd:string .
orp:impactType rdfs:domain orp:Stakeholder ; rdfs:range xsd:string .
orp:estimatedPopulation rdfs:domain orp:Stakeholder ; rdfs:range xsd:integer .
orp:netWelfareImpact rdfs:domain orp:Stakeholder ; rdfs:range orp:WelfareImpact .
orp:confidence rdfs:domain orp:Stakeholder ; rdfs:range xsd:string .

# Decision properties
orp:rationale rdfs:domain orp:Decision ; rdfs:range xsd:string .
orp:constitutiveLogic rdfs:domain orp:Decision ; rdfs:range xsd:string .
orp:affectedSections rdfs:domain orp:Decision ; rdfs:range xsd:string .

# Fork properties
orp:forkType rdfs:domain orp:Fork ; rdfs:range xsd:string .
orp:keyDifferences rdfs:domain orp:Fork ; rdfs:range xsd:string .
orp:respondsTo rdfs:domain orp:Fork ; rdfs:range orp:Document .
```

---

## 8. Controlled Vocabularies

### Compliance Levels
- `"basic"` - ORP-Basic (Layer 1 only)
- `"standard"` - ORP-Standard (Layers 1-3)
- `"full"` - ORP-Full (All 5 layers)
- `"posthoc"` - ORP-PostHoc (Retrospective reconstruction)

### Document Status
- `"draft"` - Work in progress
- `"final"` - Published version
- `"superseded"` - Replaced by newer version

### Representation Levels
- `"None"` - Absent node (no representation)
- `"Low"` - Minimal representation
- `"Medium"` - Moderate representation
- `"High"` - Strong representation

### Impact Types
- `"direct"` - Directly affected by policy
- `"indirect"` - Affected through secondary effects
- `"externality"` - Affected by spillovers/side effects

### Fork Types
- `"critique"` - Challenges assumptions/methodology
- `"alternative"` - Proposes different approach
- `"amendment"` - Suggests modifications
- `"response"` - Responds to critique

### Confidence Levels
- `"low"` - Low confidence in estimate
- `"medium"` - Moderate confidence
- `"high"` - High confidence

### Welfare Impact Direction
- `"positive"` - Net welfare gain
- `"negative"` - Net welfare loss
- `"neutral"` - No significant impact
- `"mixed"` - Some gain, some loss

### Welfare Impact Magnitude
- `"negligible"` - Minimal impact
- `"minor"` - Small impact
- `"moderate"` - Medium impact
- `"major"` - Large impact

---

## 9. Example: Complete Document as RDF

```turtle
@prefix orp: <https://openreason.org/vocab/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dc: <http://purl.org/dc/terms/> .
@prefix schema: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# Document
:dk-property-tax-reform-2024 a orp:Document, prov:Entity ;
    dc:identifier "dk-property-tax-reform-2024" ;
    dc:title "Danish Property Tax Reform 2024" ;
    dc:description "Analysis of proposed property tax reform affecting 2.5M Danish homeowners" ;
    dc:creator :asbjorn-ras ;
    dc:created "2024-01-10"^^xsd:date ;
    dc:modified "2024-03-15"^^xsd:date ;
    orp:complianceLevel "full" ;
    orp:orpVersion "0.1" ;
    orp:status "final" ;
    orp:domain "taxation" ;
    orp:hasLayer1 :l1 ;
    orp:hasLayer2 :l2 ;
    orp:hasLayer3 :l3 ;
    orp:hasLayer4 :l4 ;
    orp:hasLayer5 :l5 .

# Layer 1: Dataset
:l1 a orp:DataProvenance ;
    orp:dataset :danish-valuations-2023 .

:danish-valuations-2023 a orp:Dataset, dcat:Dataset, prov:Entity ;
    dc:title "Danish Property Valuations 2023" ;
    prov:wasAttributedTo :danish-tax-authority ;
    orp:fundingSource :danish-tax-authority ;
    orp:exclusionCriterion [
        a orp:Exclusion ;
        orp:excludedCategory "Non-residential properties" ;
        orp:rationale "Reform targets residential taxation only"
    ] .

# Layer 3: Stakeholder
:l3 a orp:EmpathyMapping ;
    orp:stakeholder :homeowners-copenhagen .

:homeowners-copenhagen a orp:Stakeholder, schema:Person ;
    orp:stakeholderGroup "Homeowners in Copenhagen" ;
    orp:representation "High" ;
    orp:impactType "direct" ;
    orp:estimatedPopulation 300000 ;
    orp:netWelfareImpact [
        a orp:WelfareImpact ;
        orp:direction "negative" ;
        orp:magnitude "moderate" ;
        orp:confidence "high"
    ] .

# Layer 4: Decision
:l4 a orp:AccountabilityLedger ;
    orp:decision :decision-001 .

:decision-001 a orp:Decision, prov:Activity ;
    prov:wasAssociatedWith :asbjorn-ras ;
    prov:startedAtTime "2024-01-15T14:30:00"^^xsd:dateTime ;
    dc:description "Excluded non-residential properties" ;
    orp:rationale "Reform targets residential taxation only" ;
    orp:constitutiveLogic "If commercial properties are included later, tax incidence shifts to business owners" ;
    orp:affectedSections "l2_consequence_simulation", "l3_empathy_mapping" .

# Layer 5: Fork
:l5 a orp:ForkRegistry ;
    orp:fork :alternative-progressive-rates .

:alternative-progressive-rates a orp:Fork, orp:Document ;
    prov:wasDerivedFrom :dk-property-tax-reform-2024 ;
    orp:forkType "alternative" ;
    dc:title "Alternative: Progressive Rate Structure" ;
    orp:keyDifferences "Uses progressive rates (0.8%-1.5%) instead of flat 1.2%" .

# Agents
:asbjorn-ras a schema:Person, prov:Agent ;
    schema:name "Asbjørn Ras" ;
    schema:email "asbjorn@example.com" ;
    schema:affiliation :public-reason-project .

:danish-tax-authority a schema:Organization, prov:Agent ;
    schema:name "Danish Tax Authority" .
```

---

## 10. Next Steps (Task 3)

With vocabulary design complete, Task 3 will:
1. Create JSON-LD `@context` file mapping YAML fields to URIs
2. Include both ORP custom terms and reused ontology terms
3. Validate context file as JSON-LD
4. Prepare for example document conversion

**Output:** `orp-context.jsonld` file ready for use

---

**Design completed:** 2026-04-08
**Designer:** Asbjørn (with Claude Code assistance)
**Next task:** Create JSON-LD context file
