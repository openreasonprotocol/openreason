# Testing the ORP JSON-LD Schema

This guide explains how to test that the JSON-LD schema is working correctly.

---

## Quick Test (No Installation Required)

Run the included test script:

```bash
python3 test_jsonld.py
```

This validates:
- ✅ JSON syntax is correct
- ✅ Context file has all required namespaces
- ✅ Example document has all required fields
- ✅ Field mappings are defined

**Output:**
```
✅ All tests passed!
```

---

## Full Test (With RDF Libraries)

For complete testing including RDF expansion and SPARQL queries:

### 1. Install RDFLib

```bash
# Create virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install rdflib
pip install rdflib
```

### 2. Run Full Test Suite

```bash
python3 test_jsonld.py
```

**Expected output:**
```
✅ JSON Validity: PASSED
✅ Context Structure: PASSED
✅ Example Structure: PASSED
✅ RDF Expansion: PASSED (152+ triples)
✅ SPARQL Queries: PASSED

Total: 5 passed, 0 failed, 0 skipped
```

---

## Online Testing (JSON-LD Playground)

The easiest way to visualize what's happening:

### Method 1: Test Example Document

1. Visit: https://json-ld.org/playground/
2. Copy contents of `examples/danish_property_tax_reform.jsonld`
3. Paste into the left panel
4. Click tabs to see transformations:
   - **Compacted**: Human-readable form
   - **Expanded**: Full RDF URIs
   - **N-Quads**: RDF triples (150+ triples)

**Expected result:** 150+ RDF triples showing all ORP layers converted to linked data

### Method 2: Test Context File

1. Visit: https://json-ld.org/playground/
2. Copy contents of `orp_validator/schemas/orp-context.jsonld`
3. Paste into left panel
4. Click "Compacted" tab
5. Should show no errors

**Expected result:** Context validates with no errors

---

## Manual Testing with Python

```python
from rdflib import Graph

# Load and parse the JSON-LD
g = Graph()
g.parse("examples/danish_property_tax_reform.jsonld", format="json-ld")

print(f"Generated {len(g)} RDF triples")
# Output: Generated 152 RDF triples

# Query for document title
query = """
PREFIX dc: <http://purl.org/dc/terms/>
SELECT ?title WHERE {
  ?doc dc:title ?title .
}
"""
for row in g.query(query):
    print(f"Title: {row.title}")
# Output: Title: Danish Property Tax Reform: LVT + Smoothed Profit Tax

# Query for stakeholders
query = """
PREFIX schema: <http://schema.org/>
SELECT ?name WHERE {
  ?stakeholder schema:name ?name .
}
"""
for row in g.query(query):
    print(f"Stakeholder: {row.name}")
# Output:
# Stakeholder: Homeowners (urban)
# Stakeholder: Renters
# Stakeholder: Small businesses
```

---

## Testing SPARQL Queries

All queries from `sparql_examples.md` should work:

```python
from rdflib import Graph

g = Graph()
g.parse("examples/danish_property_tax_reform.jsonld", format="json-ld")

# Query 1: Find all datasets
query = """
PREFIX orp: <https://openreason.org/vocab/>
PREFIX dc: <http://purl.org/dc/terms/>

SELECT ?dataset ?name WHERE {
  ?doc orp:hasLayer1 ?l1 .
  ?l1 orp:dataset ?dataset .
  ?dataset dc:title ?name .
}
"""
results = g.query(query)
print(f"Found {len(results)} datasets")
# Output: Found 2 datasets

# Query 2: Find stakeholders with no representation
query = """
PREFIX orp: <https://openreason.org/vocab/>
PREFIX schema: <http://schema.org/>

SELECT ?name ?population WHERE {
  ?stakeholder schema:name ?name ;
               orp:representation "None" ;
               orp:estimatedPopulation ?population .
}
"""
results = g.query(query)
for row in results:
    print(f"{row.name}: {row.population} people")
# Output: Renters: 2000000 people
```

---

## Expected Results Summary

### File Validation
- ✅ `orp-context.jsonld`: Valid JSON-LD 1.1
- ✅ `danish_property_tax_reform.jsonld`: Valid JSON-LD document
- ✅ All namespace URIs dereferenceable (PROV-O, DCAT, Dublin Core, Schema.org)

### RDF Expansion
- ✅ Generates 150+ RDF triples
- ✅ Document mapped to `orp:Document` class
- ✅ Datasets mapped to `dcat:Dataset` class
- ✅ Stakeholders mapped to `schema:Person` class
- ✅ Decisions mapped to `orp:Decision` class
- ✅ All 5 layers present in RDF graph

### SPARQL Queries
- ✅ Can query document metadata (title, authors, dates)
- ✅ Can query datasets by funding source
- ✅ Can find stakeholders with no representation
- ✅ Can track decision lineage
- ✅ Can compare temporal coverage across datasets

---

## Troubleshooting

### Error: "Context URL returns 404"
**Cause:** Context URL `https://openreason.org/context/v0.1` not yet hosted

**Solution:** For now, use local file reference or inline context:
```json
{
  "@context": "./orp_validator/schemas/orp-context.jsonld",
  ...
}
```

### Error: "No module named 'rdflib'"
**Cause:** RDFLib not installed

**Solution:**
```bash
pip install rdflib
```

### Error: "Invalid JSON"
**Cause:** Syntax error in JSON-LD file

**Solution:**
1. Run file through JSON validator: https://jsonlint.com/
2. Check for trailing commas, missing quotes, unescaped characters

### Error: "Expansion failed"
**Cause:** Invalid context or unknown prefix

**Solution:**
1. Verify all prefixes defined in `@context`
2. Check JSON-LD Playground for detailed error messages

---

## CI/CD Integration

Add to `.gitlab-ci.yml`:

```yaml
test:jsonld:
  stage: test
  script:
    - pip install rdflib
    - python3 test_jsonld.py
  only:
    changes:
      - orp_validator/schemas/*.jsonld
      - examples/*.jsonld
```

---

## What Each Test Verifies

### Test 1: JSON Validity
- Files parse as valid JSON
- No syntax errors

### Test 2: Context Structure
- JSON-LD version 1.1 specified
- All required namespaces present (orp, prov, dcat, dc, schema)
- 30+ terms mapped

### Test 3: Example Document Structure
- Has @context and @type
- Has all required header fields
- Has all 5 layers

### Test 4: RDF Expansion
- JSON-LD expands to RDF triples
- No expansion errors
- Generates expected number of triples (150+)

### Test 5: SPARQL Queries
- Can query document title via Dublin Core
- Can find stakeholders via Schema.org
- Can traverse layer relationships via ORP vocabulary

---

## Success Criteria

✅ **All tests pass** = JSON-LD schema is working
⚠️  **Some tests skipped** = Basic validation passed, install rdflib for full testing
❌ **Any test failed** = Fix errors before using schema

---

**Last updated:** 2026-04-08
**Schema version:** ORP JSON-LD v0.1
**Status:** ✅ All tests passing
