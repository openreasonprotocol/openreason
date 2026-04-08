# Sprint 1.7.4: Machine-Readable Schema (JSON-LD)

**Version:** `sprint-1.7.4`
**Parent Epic:** `sprint-1.7.0` (Foundation for Expansion)
**Status:** Not Started
**Start Date:** 2026-04-10 (can run parallel with 1.7.3)
**Target End Date:** 2026-04-13 (3 days)

**Code Target Version:** `v0.6.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Extend ORP from a human-readable YAML format validated by JSON Schema to a semantic web-compatible format (JSON-LD) with RDF vocabulary — enabling programmatic querying, cross-document analysis, and integration with existing linked data ecosystems (W3C PROV, Dublin Core, Schema.org).

---

## Strategic Importance

**Current state:** ORP documents are YAML files validated by JSON Schema
- ✅ Human-readable
- ✅ Validates structure
- ❌ Not queryable across documents
- ❌ Not linked to existing ontologies
- ❌ Not interoperable with semantic web tools

**With JSON-LD:**
- ORP documents become nodes in a knowledge graph
- Layer 5 forks become queryable relationships
- Can ask: "Show all datasets funded by pharmaceutical companies with exclusions affecting population X"
- Integration with PROV-O (provenance ontology), DCAT (dataset catalog)
- Enables tools like SPARQL endpoints, visualization dashboards

**This transforms ORP from "documentation standard" to "epistemic infrastructure"**

---

## Scope

### In Scope
- JSON-LD context file (`@context` mapping ORP terms to URIs)
- RDF vocabulary (lightweight, not full OWL ontology)
- Mapping ORP layers to existing ontologies where applicable:
  - Layer 1 → PROV-O (W3C Provenance)
  - Layer 1 → DCAT (Data Catalog Vocabulary)
  - Metadata → Dublin Core, Schema.org
- Example: Danish property tax document as JSON-LD
- Example SPARQL queries showing what becomes possible
- Documentation for schema developers

### Explicitly Out of Scope
- Full OWL ontology with reasoning (too heavy, defer to Phase 2)
- Triple store implementation (just schema, not infrastructure)
- SPARQL endpoint deployment (just example queries)
- Conversion tooling (orp validate outputs JSON-LD, but manual for now)
- Linked data platform deployment (documentation only)

---

## Tasks

### Task 1: Research Existing Ontologies
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Critical

**Description:**
Review existing semantic web ontologies to identify reusable terms and avoid reinventing.

**Acceptance Criteria:**
- [ ] Review W3C PROV-O (Provenance Ontology):
  - What: Activity, Entity, Agent classes
  - Relevance to ORP: Layer 1 (provenance), Layer 4 (activities)
  - Reusable terms: prov:Entity, prov:wasGeneratedBy, prov:wasAttributedTo
- [ ] Review DCAT (Data Catalog Vocabulary):
  - What: Dataset, Distribution, CatalogRecord
  - Relevance to ORP: Layer 1 (dataset metadata)
  - Reusable terms: dcat:Dataset, dcat:distribution, dcat:temporalCoverage
- [ ] Review Dublin Core:
  - What: Generic metadata (creator, date, title, description)
  - Relevance to ORP: Header metadata
  - Reusable terms: dc:creator, dc:title, dc:description, dc:created
- [ ] Review Schema.org:
  - What: General-purpose vocabulary (widely adopted)
  - Relevance to ORP: Stakeholder mapping (schema:Person, schema:Organization)
  - Reusable terms: schema:author, schema:datePublished, schema:about
- [ ] Document: What each ontology covers vs what ORP needs to define
- [ ] Create mapping table: ORP field → Existing ontology term (where available)

**Output:** `schemas/ontology_mapping.md` with research notes

---

### Task 2: Design ORP Vocabulary Structure
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Critical

**Description:**
Define ORP-specific terms that don't exist in standard ontologies.

**Acceptance Criteria:**
- [ ] ORP namespace: `https://openreason.org/vocab/` (or similar)
- [ ] Core classes:
  - `orp:Document` (subclass of prov:Entity)
  - `orp:Layer1_DataProvenance` (subclass of prov:Entity)
  - `orp:Layer2_ConsequenceSimulation`
  - `orp:Layer3_EmpathyMapping`
  - `orp:Layer4_AccountabilityLedger` (related to prov:Activity)
  - `orp:Layer5_ForkRegistry`
  - `orp:Stakeholder` (subclass of schema:Person or schema:Organization)
  - `orp:Dataset` (subclass of dcat:Dataset)
  - `orp:Decision` (for Layer 4 entries)
  - `orp:Fork` (for Layer 5 relationships)
- [ ] Core properties:
  - `orp:hasLayer1` / `hasLayer2` / etc.
  - `orp:complianceLevel` (Basic/Standard/Full)
  - `orp:orpVersion` (0.1, 0.2, etc.)
  - `orp:fundingSource` (Layer 1 specific)
  - `orp:exclusionCriterion` (Layer 1 specific)
  - `orp:affectedStakeholder` (Layer 3 specific)
  - `orp:constitutiveDecision` (Layer 4 specific)
  - `orp:forkedFrom` / `forkType` (Layer 5 specific)
- [ ] Reuse existing terms where possible (don't redefine dc:creator, etc.)
- [ ] Design principle: Light vocabulary, not full ontology

**Output:** Vocabulary design document

---

### Task 3: Create JSON-LD Context File
**Owner:** Asbjørn
**Estimate:** 4 hours
**Priority:** Critical

**Description:**
Create `@context` file mapping ORP YAML fields to RDF URIs.

**Acceptance Criteria:**
- [ ] File: `schemas/orp-context.jsonld`
- [ ] Structure:
  ```json
  {
    "@context": {
      "orp": "https://openreason.org/vocab/",
      "prov": "http://www.w3.org/ns/prov#",
      "dcat": "http://www.w3.org/ns/dcat#",
      "dc": "http://purl.org/dc/terms/",
      "schema": "http://schema.org/",

      "document_id": "@id",
      "title": "dc:title",
      "authors": {
        "@id": "dc:creator",
        "@type": "@id"
      },
      "created": {
        "@id": "dc:created",
        "@type": "http://www.w3.org/2001/XMLSchema#date"
      },
      "l1_data_provenance": {
        "@id": "orp:hasLayer1",
        "@type": "@id"
      },
      ...
    }
  }
  ```
- [ ] Maps all ORP header fields to Dublin Core/Schema.org
- [ ] Maps Layer 1 dataset fields to DCAT where applicable
- [ ] Maps Layer 4 decisions to PROV-O activities
- [ ] Maps Layer 5 forks to custom orp:forkedFrom relationships
- [ ] Validates as JSON-LD (use JSON-LD Playground)
- [ ] Includes version field (`"@context": "https://openreason.org/context/v0.1"`)

**Output:** `schemas/orp-context.jsonld`

---

### Task 4: Convert Example Document to JSON-LD
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Convert Danish property tax YAML to JSON-LD using new context.

**Acceptance Criteria:**
- [ ] File: `examples/danish_property_tax_reform.jsonld`
- [ ] Structure:
  ```json
  {
    "@context": "https://openreason.org/context/v0.1",
    "@type": "orp:Document",
    "document_id": "dk-property-tax-reform-2024",
    "title": "Danish Property Tax Reform 2024",
    "authors": [...],
    "l1_data_provenance": [
      {
        "@type": "orp:Dataset",
        "dataset_id": "danish-property-valuations-2023",
        "name": "...",
        "funding_sources": [
          {
            "@type": "schema:Organization",
            "name": "Danish Tax Authority"
          }
        ],
        ...
      }
    ],
    ...
  }
  ```
- [ ] Validates as JSON-LD (JSON-LD Playground)
- [ ] Expands to N-Triples (shows RDF graph structure)
- [ ] Maintains all information from YAML version
- [ ] Human-readable (not just machine-parseable)

**Output:** `examples/danish_property_tax_reform.jsonld`

---

### Task 5: Write Example SPARQL Queries
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** High

**Description:**
Create example SPARQL queries showing what JSON-LD enables.

**Acceptance Criteria:**

**Query 1: Find all datasets with pharmaceutical funding**
```sparql
PREFIX orp: <https://openreason.org/vocab/>
PREFIX schema: <http://schema.org/>

SELECT ?dataset ?name ?funder
WHERE {
  ?doc orp:hasLayer1 ?l1 .
  ?l1 orp:dataset ?dataset .
  ?dataset dcat:name ?name .
  ?dataset orp:fundingSource ?funder .
  ?funder schema:name ?funderName .
  FILTER(CONTAINS(LCASE(?funderName), "pharma"))
}
```

**Query 2: Find all stakeholders marked as "absent nodes"**
```sparql
PREFIX orp: <https://openreason.org/vocab/>

SELECT ?doc ?stakeholder ?representation
WHERE {
  ?doc orp:hasLayer3 ?l3 .
  ?l3 orp:affectedStakeholder ?stakeholder .
  ?stakeholder orp:representation "None" .
}
```

**Query 3: Find all documents forked from a specific document**
```sparql
PREFIX orp: <https://openreason.org/vocab/>

SELECT ?fork ?forkType ?description
WHERE {
  ?fork orp:forkedFrom <dk-property-tax-reform-2024> .
  ?fork orp:forkType ?forkType .
  ?fork dc:description ?description .
}
```

**Query 4: Find all datasets with geographic exclusions**
```sparql
PREFIX orp: <https://openreason.org/vocab/>

SELECT ?dataset ?exclusion
WHERE {
  ?doc orp:hasLayer1 ?l1 .
  ?l1 orp:dataset ?dataset .
  ?dataset orp:exclusionCriterion ?exclusion .
  FILTER(CONTAINS(?exclusion, "geographic"))
}
```

- [ ] Create: `schemas/sparql_examples.md`
- [ ] Include 5-7 useful queries
- [ ] Explain what each query finds and why it's useful
- [ ] Note: These work on RDF representation of ORP documents

**Output:** `schemas/sparql_examples.md`

---

### Task 6: Document JSON-LD Schema for Developers
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Medium

**Description:**
Create developer documentation explaining how to use ORP JSON-LD.

**Acceptance Criteria:**
- [ ] File: `schemas/JSON_LD_GUIDE.md`
- [ ] Sections:
  1. **Why JSON-LD?** (interoperability, querying, linked data)
  2. **ORP Vocabulary Overview** (classes, properties)
  3. **Reused Ontologies** (PROV-O, DCAT, Dublin Core, Schema.org)
  4. **Using the Context File** (how to apply `@context`)
  5. **Converting YAML to JSON-LD** (manual process, future tooling)
  6. **Querying with SPARQL** (examples, triple store setup)
  7. **Visualization** (RDF graphs, fork relationships)
  8. **Integration Points** (how to use with PROV, DCAT catalogs)
- [ ] Include code examples
- [ ] Link to W3C specifications
- [ ] Note current limitations (no automated conversion yet)

**Output:** `schemas/JSON_LD_GUIDE.md`

---

### Task 7: Validate with JSON-LD Tools
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Test JSON-LD context and example with standard tools.

**Acceptance Criteria:**
- [ ] Use JSON-LD Playground (json-ld.org/playground)
  - Paste `orp-context.jsonld` → validates
  - Paste `danish_property_tax_reform.jsonld` → expands to N-Triples
  - View as RDF graph visualization
- [ ] Use RDF validator (e.g., W3C RDF Validator)
  - Expanded JSON-LD validates as RDF
  - No syntax errors
- [ ] Use SPARQL.js or similar to test queries
  - Load example document as RDF
  - Run example queries → return expected results
- [ ] Document any issues/limitations found
- [ ] Fix context file if errors discovered

**Output:** Validation report and any fixes needed

---

### Task 8: Update Validator CLI for JSON-LD Output
**Owner:** Asbjørn
**Estimate:** 3 hours
**Priority:** Low (nice-to-have)

**Description:**
Add `--format jsonld` option to `orp validate` command (optional task).

**Acceptance Criteria:**
- [ ] Command: `orp validate document.yaml --format jsonld`
- [ ] Output: JSON-LD representation with `@context` included
- [ ] Uses `orp-context.jsonld` automatically
- [ ] Validates both YAML structure AND JSON-LD output
- [ ] Update CLI help text
- [ ] Add test case

**Note:** This is optional — can defer to 1.8.x if time constrained

**Output:** CLI enhancement (if time permits)

---

### Task 9: Publish and Document
**Owner:** Asbjørn
**Estimate:** 2 hours
**Priority:** Medium

**Description:**
Publish JSON-LD schema and integrate into docs.

**Acceptance Criteria:**
- [ ] Publish to `schemas/` directory:
  - `orp-context.jsonld`
  - `orp-vocabulary.ttl` (RDF/Turtle representation, optional)
  - `JSON_LD_GUIDE.md`
  - `sparql_examples.md`
  - `ontology_mapping.md`
- [ ] Host context file at stable URL:
  - `https://openreason.org/context/v0.1` (or similar)
  - Redirect to actual file location
- [ ] Update docs site:
  - New "Technical Specifications" section
  - JSON-LD guide
  - SPARQL examples page
- [ ] Update CLAUDE.md:
  - Note JSON-LD schema availability
  - Link to JSON_LD_GUIDE
- [ ] Update README.md:
  - Mention machine-readable format
  - Link to schema docs

**Output:** Published schema with documentation

---

## Success Criteria

### Completion Criteria
- [ ] All 9 tasks completed (Task 8 optional)
- [ ] `orp-context.jsonld` validates as JSON-LD
- [ ] Danish example converted to JSON-LD successfully
- [ ] SPARQL queries work on RDF representation
- [ ] Developer guide published

### Quality Criteria
- [ ] Reuses existing ontologies where appropriate (not NIH syndrome)
- [ ] JSON-LD is human-readable (not just machine)
- [ ] Context file is stable (URL won't break)
- [ ] Documentation is clear for developers unfamiliar with RDF

### Impact Criteria (3-6 months)
- External tool built using JSON-LD format
- ORP documents added to linked data catalog
- SPARQL endpoint deployed (by community or us)
- Citation in semantic web / linked data context
- Integration with PROV-O ecosystem

---

## Dependencies

**Depends on:**
- None (can run parallel with other sprints)

**Enables:**
- Advanced querying across ORP documents
- Integration with linked data platforms
- Visualization tools (RDF graph viewers)
- Programmatic analysis of fork relationships

---

## Risks and Mitigations

### Risk 1: Over-engineering (full OWL ontology)
**Mitigation:** Stick to JSON-LD context + light vocabulary, defer OWL to Phase 2

### Risk 2: Breaking changes to context file
**Mitigation:** Version context URL (`/context/v0.1`), never modify published versions

### Risk 3: Semantic web expertise gap
**Mitigation:** Start simple, use existing ontologies, consult W3C specs

### Risk 4: Low adoption (too technical)
**Mitigation:** Make optional (YAML remains primary), good documentation

---

## Documentation Updates

- [ ] Create `schemas/` directory structure
- [ ] Update CLAUDE.md with schema info
- [ ] Update docs site technical specs section
- [ ] Link from README.md
- [ ] Reference in comparison document (ORP + PROV integration)

---

## Learning Resources

### JSON-LD Basics
- JSON-LD 1.1 spec: https://www.w3.org/TR/json-ld11/
- JSON-LD Playground: https://json-ld.org/playground/
- Linked Data tutorial: https://www.w3.org/DesignIssues/LinkedData.html

### Existing Ontologies
- PROV-O: https://www.w3.org/TR/prov-o/
- DCAT: https://www.w3.org/TR/vocab-dcat-2/
- Dublin Core: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- Schema.org: https://schema.org/

### Tools
- RDF validator: http://www.w3.org/RDF/Validator/
- SPARQL.js: https://github.com/RubenVerborgh/SPARQL.js/
- RDF visualization: http://www.ldf.fi/service/rdf-grapher

---

## Retrospective Notes

(To be completed at sprint end)

### What Went Well
- [TBD]

### What Didn't Go Well
- [TBD]

### Lessons Learned
- [TBD]

---

**Sprint Owner:** Asbjørn
**Start Date:** 2026-04-10
**Target Completion:** 2026-04-13
**Estimated Effort:** 27 hours over 3 days (excluding optional Task 8)
