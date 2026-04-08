# SPARQL Query Examples for ORP Documents

**Sprint:** 1.7.4
**Created:** 2026-04-08
**Purpose:** Demonstrate cross-document querying enabled by ORP JSON-LD/RDF representation

---

## Overview

When ORP documents are represented as RDF (via JSON-LD), they become queryable nodes in a knowledge graph. SPARQL (SPARQL Protocol and RDF Query Language) enables powerful cross-document analysis that would be impossible with isolated YAML files.

**What SPARQL enables:**
- Find all datasets funded by specific organizations
- Identify stakeholders marked as "absent nodes" across multiple policies
- Trace fork relationships and compare alternative proposals
- Discover datasets with similar exclusion patterns
- Find decisions affecting specific policy domains

---

## Prerequisites

### Triple Store

To run these queries, you need an RDF triple store loaded with ORP documents:

**Options:**
- [Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/) (open-source, Java-based)
- [GraphDB](https://graphdb.ontotext.com/) (free edition available)
- [Virtuoso](https://virtuoso.openlinksw.com/) (open-source)
- [RDFLib](https://rdflib.readthedocs.io/) (Python library for in-memory graphs)

### Loading Documents

```bash
# Example: Load JSON-LD into Fuseki
curl -X POST -H "Content-Type: application/ld+json" \
  --data-binary @danish_property_tax_reform.jsonld \
  http://localhost:3030/orp/data
```

### Common Prefixes

All queries below use these namespace prefixes:

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX schema: <http://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
```

---

## Query 1: Find All Documents by Compliance Level

**Use Case:** Identify which ORP documents meet full compliance vs basic

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?title ?compliance
WHERE {
  ?document a orp:Document ;
            dc:title ?title ;
            orp:complianceLevel ?compliance .
  FILTER(?compliance = "full")
}
ORDER BY ?title
```

**Returns:** All ORP-Full documents with titles

---

## Query 2: Find All Datasets Funded by Government

**Use Case:** Identify datasets with government funding to assess potential bias

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX schema: <http://schema.org/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?dataset ?datasetName ?funder
WHERE {
  ?document orp:hasLayer1 ?l1 .
  ?l1 orp:dataset ?dataset .
  ?dataset dc:title ?datasetName ;
           orp:fundingSource ?funder .
  ?funder schema:name ?funderName .
  FILTER(CONTAINS(LCASE(?funderName), "government"))
}
```

**Returns:** Datasets funded by entities with "government" in their name

---

## Query 3: Find Stakeholders with No Representation (Absent Nodes)

**Use Case:** Discover vulnerable populations systematically excluded from policy consideration

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX schema: <http://schema.org/>

SELECT ?document ?docTitle ?stakeholder ?stakeholderName ?estimatedPop
WHERE {
  ?document a orp:Document ;
            dc:title ?docTitle ;
            orp:hasLayer3 ?l3 .
  ?l3 orp:stakeholder ?stakeholder .
  ?stakeholder schema:name ?stakeholderName ;
               orp:representation "None" ;
               orp:estimatedPopulation ?estimatedPop .
}
ORDER BY DESC(?estimatedPop)
```

**Returns:** All stakeholder groups with zero representation, sorted by population size

**Impact:** Reveals systematic bias toward well-represented groups

---

## Query 4: Find All Documents Forked from a Specific Document

**Use Case:** Track alternative proposals and critiques to understand policy debate

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?fork ?forkTitle ?forkType ?keyDifferences
WHERE {
  ?fork a orp:Fork ;
        prov:wasDerivedFrom <orp-dk-property-tax-001> ;
        dc:title ?forkTitle ;
        orp:forkType ?forkType ;
        orp:keyDifferences ?keyDifferences .
}
```

**Returns:** All forks of the Danish property tax reform document

---

## Query 5: Find Datasets with Geographic Exclusions

**Use Case:** Identify datasets that exclude specific geographic regions, potentially indicating bias

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?dataset ?datasetName ?exclusion ?rationale
WHERE {
  ?document orp:hasLayer1 ?l1 .
  ?l1 orp:dataset ?dataset .
  ?dataset dc:title ?datasetName ;
           orp:exclusionCriterion ?exc .
  ?exc orp:excludedCategory ?exclusion ;
       orp:rationale ?rationale .
  FILTER(CONTAINS(LCASE(?exclusion), "geographic") ||
         CONTAINS(LCASE(?exclusion), "region") ||
         CONTAINS(LCASE(?exclusion), "rural") ||
         CONTAINS(LCASE(?exclusion), "urban"))
}
```

**Returns:** Datasets with geographic/regional exclusions and justifications

---

## Query 6: Find Decisions Made by Specific Person

**Use Case:** Track all methodological decisions attributed to a specific analyst

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX schema: <http://schema.org/>

SELECT ?document ?decision ?decisionText ?timestamp ?constitutiveLogic
WHERE {
  ?document orp:hasLayer4 ?l4 .
  ?l4 orp:decision ?decisionNode .
  ?decisionNode a orp:Decision ;
                prov:wasAssociatedWith ?agent ;
                dc:description ?decisionText ;
                prov:atTime ?timestamp ;
                orp:constitutiveLogic ?constitutiveLogic .
  ?agent schema:name "Asbjørn" .
}
ORDER BY ?timestamp
```

**Returns:** All decisions made by Asbjørn across all ORP documents, chronologically

---

## Query 7: Find Documents Using Synthetic Data

**Use Case:** Identify datasets with synthetic or augmented elements

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?docTitle ?dataset ?datasetName ?syntheticType ?syntheticDescription
WHERE {
  ?document a orp:Document ;
            dc:title ?docTitle ;
            orp:hasLayer1 ?l1 .
  ?l1 orp:dataset ?dataset .
  ?dataset dc:title ?datasetName ;
           orp:syntheticElements ?synthNode .
  ?synthNode orp:syntheticType ?syntheticType ;
             dc:description ?syntheticDescription .
}
```

**Returns:** Documents using synthetic data, with details on type and methodology

---

## Query 8: Find Stakeholders with Negative Welfare Impact

**Use Case:** Identify groups harmed by proposed policies

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX schema: <http://schema.org/>

SELECT ?document ?docTitle ?stakeholder ?stakeholderName ?magnitude ?rationale
WHERE {
  ?document a orp:Document ;
            dc:title ?docTitle ;
            orp:hasLayer3 ?l3 .
  ?l3 orp:stakeholder ?stakeholder .
  ?stakeholder schema:name ?stakeholderName ;
               orp:netWelfareImpact ?impact .
  ?impact orp:direction "negative" ;
          orp:magnitude ?magnitude ;
          orp:rationale ?rationale .
}
ORDER BY ?magnitude
```

**Returns:** All negatively-affected stakeholder groups with impact details

---

## Query 9: Find All Forks by Fork Type

**Use Case:** Categorize alternative proposals (critiques vs amendments vs alternatives)

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?forkType (COUNT(?fork) AS ?count)
WHERE {
  ?fork a orp:Fork ;
        orp:forkType ?forkType .
}
GROUP BY ?forkType
ORDER BY DESC(?count)
```

**Returns:** Distribution of fork types across all ORP documents

---

## Query 10: Find Documents with High Confidence Negative Impacts

**Use Case:** Identify policies where analysts are confident about harm to specific groups

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>
PREFIX schema: <http://schema.org/>

SELECT ?document ?docTitle ?stakeholder ?stakeholderName ?magnitude ?rationale
WHERE {
  ?document a orp:Document ;
            dc:title ?docTitle ;
            orp:hasLayer3 ?l3 .
  ?l3 orp:stakeholder ?stakeholder .
  ?stakeholder schema:name ?stakeholderName ;
               orp:netWelfareImpact ?impact .
  ?impact orp:direction "negative" ;
          orp:magnitude ?magnitude ;
          orp:confidence "high" ;
          orp:rationale ?rationale .
}
```

**Returns:** Stakeholders with high-confidence negative impacts (policy red flags)

---

## Query 11: Find Documents in Specific Policy Domain

**Use Case:** Filter ORP documents by policy area (taxation, healthcare, ai-training, etc.)

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?title ?author ?created
WHERE {
  ?document a orp:Document ;
            dc:title ?title ;
            dc:subject "taxation" ;
            dc:creator ?authorNode ;
            dc:created ?created .
  ?authorNode schema:name ?author .
}
ORDER BY DESC(?created)
```

**Returns:** All taxation policy documents, most recent first

---

## Query 12: Find Datasets with Pharmaceutical Funding

**Use Case:** Identify potential conflicts of interest in healthcare/medical research datasets

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX schema: <http://schema.org/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?dataset ?datasetName ?funder ?funderName
WHERE {
  ?document orp:hasLayer1 ?l1 .
  ?l1 orp:dataset ?dataset .
  ?dataset dc:title ?datasetName ;
           orp:fundingSource ?funder .
  ?funder schema:name ?funderName .
  FILTER(CONTAINS(LCASE(?funderName), "pharma") ||
         CONTAINS(LCASE(?funderName), "pharmaceutical") ||
         CONTAINS(LCASE(?funderName), "drug"))
}
```

**Returns:** Datasets funded by pharmaceutical companies

---

## Query 13: Compare Scenarios Across Documents

**Use Case:** Find documents using similar scenario modeling approaches

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?docTitle ?scenario ?scenarioName ?outcome
WHERE {
  ?document a orp:Document ;
            dc:title ?docTitle ;
            orp:hasLayer2 ?l2 .
  ?l2 orp:scenario ?scenario .
  ?scenario orp:scenarioName ?scenarioName ;
            orp:outcome ?outcome .
}
```

**Returns:** All scenarios across all documents (enables cross-document comparison)

---

## Query 14: Find Post-Hoc Reconstructions

**Use Case:** Identify documents that are retrospective analyses (ORP v0.2 feature)

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?title ?domain
WHERE {
  ?document a orp:Document ;
            dc:title ?title ;
            dc:subject ?domain ;
            orp:postHoc true .
}
```

**Returns:** All post-hoc reconstruction documents (e.g., AI training datasets)

---

## Query 15: Find Decisions with Constitutive Logic

**Use Case:** Identify methodological choices where "if assumption X is wrong, conclusion changes"

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?docTitle ?decision ?constitutiveLogic
WHERE {
  ?document a orp:Document ;
            dc:title ?docTitle ;
            orp:hasLayer4 ?l4 .
  ?l4 orp:decision ?decisionNode .
  ?decisionNode dc:description ?decision ;
                orp:constitutiveLogic ?constitutiveLogic .
}
```

**Returns:** All decisions where assumptions are explicitly flagged as constitutive

**Impact:** Makes assumptions testable and forkable

---

## Advanced Query: Fork Network Analysis

**Use Case:** Visualize the entire fork tree for a policy proposal

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX dc: <http://purl.org/dc/terms/>

CONSTRUCT {
  ?fork prov:wasDerivedFrom ?parent .
  ?fork dc:title ?forkTitle .
  ?fork orp:forkType ?forkType .
  ?parent dc:title ?parentTitle .
}
WHERE {
  ?fork a orp:Fork ;
        prov:wasDerivedFrom ?parent ;
        dc:title ?forkTitle ;
        orp:forkType ?forkType .
  ?parent dc:title ?parentTitle .
}
```

**Returns:** RDF graph of fork relationships (visualizable in RDF graph tools)

---

## Aggregation Query: Stakeholder Impact Summary

**Use Case:** Count stakeholders by impact direction across all documents

```sparql
PREFIX orp: <https://openreason.org/vocab/>

SELECT ?impactDirection (COUNT(?stakeholder) AS ?count) (SUM(?population) AS ?totalAffected)
WHERE {
  ?document orp:hasLayer3 ?l3 .
  ?l3 orp:stakeholder ?stakeholder .
  ?stakeholder orp:netWelfareImpact ?impact ;
               orp:estimatedPopulation ?population .
  ?impact orp:direction ?impactDirection .
}
GROUP BY ?impactDirection
ORDER BY DESC(?totalAffected)
```

**Returns:** Distribution of positive/negative/neutral/mixed impacts across all stakeholders

---

## Federation Query: Cross-Repository Search

**Use Case:** Query ORP documents across multiple SPARQL endpoints (federated query)

```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?document ?title ?source
WHERE {
  {
    SERVICE <http://localhost:3030/orp/sparql> {
      ?document a orp:Document ;
                dc:title ?title .
      BIND("local" AS ?source)
    }
  }
  UNION
  {
    SERVICE <https://orp-registry.example.org/sparql> {
      ?document a orp:Document ;
                dc:title ?title .
      BIND("registry" AS ?source)
    }
  }
}
```

**Returns:** All ORP documents from both local and remote repositories

---

## What SPARQL Enables

### 1. Cross-Document Analysis
- "Find all stakeholders with representation='None' across all healthcare policies"
- "Which datasets are used in both taxation and healthcare domains?"

### 2. Pattern Discovery
- "What are the most common exclusion criteria across all datasets?"
- "Which decision-makers appear most frequently across documents?"

### 3. Fork Tracking
- "Show me all alternative proposals and their key differences"
- "Which fork types are most common (critique vs alternative)?"

### 4. Transparency Auditing
- "Which documents lack Layer 4 (accountability) despite claiming ORP-Full?"
- "Find all post-hoc reconstructions with accountability gaps"

### 5. Impact Assessment
- "How many people are marked as negatively affected across all current proposals?"
- "Which vulnerable groups appear in minority stress testing?"

---

## Tools for Visualization

**RDF Graph Visualization:**
- [RDF Grapher](http://www.ldf.fi/service/rdf-grapher)
- [WebVOWL](http://vowl.visualdataweb.org/webvowl.html)
- [Cytoscape](https://cytoscape.org/) (with RDF plugin)

**SPARQL Clients:**
- [Yasgui](https://yasgui.triply.cc/) (web-based)
- [RDF4J Workbench](https://rdf4j.org/documentation/tools/workbench/)
- [GraphDB Workbench](https://graphdb.ontotext.com/)

---

## Next Steps

1. **Set up a triple store** (Fuseki, GraphDB, etc.)
2. **Load ORP JSON-LD documents** into the store
3. **Run example queries** to understand RDF structure
4. **Customize queries** for your use case
5. **Build dashboards** visualizing ORP data across documents

---

**Created:** 2026-04-08
**Author:** Asbjørn (with Claude Code assistance)
**Next:** Validate JSON-LD with tools (Task 7)
