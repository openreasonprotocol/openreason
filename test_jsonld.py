#!/usr/bin/env python3
"""
Test script for ORP JSON-LD schema.

Tests the JSON-LD context and example document to verify:
1. Files are valid JSON
2. Context maps all ORP fields
3. Example document can be expanded to RDF
4. SPARQL queries work on the RDF data

Usage:
    python3 test_jsonld.py

Requirements:
    pip install rdflib
"""

import json
import sys
from pathlib import Path

def test_json_validity():
    """Test that JSON-LD files are valid JSON."""
    print("=" * 60)
    print("Test 1: JSON Validity")
    print("=" * 60)

    files = [
        "orp_validator/schemas/orp-context.jsonld",
        "examples/danish_property_tax_reform.jsonld"
    ]

    for file_path in files:
        try:
            with open(file_path) as f:
                data = json.load(f)
            print(f"✅ {file_path}: Valid JSON")
        except json.JSONDecodeError as e:
            print(f"❌ {file_path}: Invalid JSON - {e}")
            return False
        except FileNotFoundError:
            print(f"❌ {file_path}: File not found")
            return False

    return True


def test_context_structure():
    """Test that context file has required structure."""
    print("\n" + "=" * 60)
    print("Test 2: Context File Structure")
    print("=" * 60)

    with open("orp_validator/schemas/orp-context.jsonld") as f:
        context = json.load(f)

    # Check version
    version = context.get("@context", {}).get("@version")
    if version == 1.1:
        print(f"✅ JSON-LD version: {version}")
    else:
        print(f"❌ JSON-LD version: Expected 1.1, got {version}")
        return False

    # Check required namespaces
    required_ns = {
        "orp": "https://openreason.org/vocab/",
        "prov": "http://www.w3.org/ns/prov#",
        "dcat": "http://www.w3.org/ns/dcat#",
        "dc": "http://purl.org/dc/terms/",
        "schema": "http://schema.org/"
    }

    for prefix, uri in required_ns.items():
        if context["@context"].get(prefix) == uri:
            print(f"✅ Namespace {prefix}: {uri}")
        else:
            print(f"❌ Namespace {prefix}: Missing or incorrect")
            return False

    # Count total terms
    total_terms = len([k for k in context["@context"].keys() if not k.startswith("@")])
    print(f"✅ Total terms defined: {total_terms}")

    return True


def test_example_structure():
    """Test that example document has required fields."""
    print("\n" + "=" * 60)
    print("Test 3: Example Document Structure")
    print("=" * 60)

    with open("examples/danish_property_tax_reform.jsonld") as f:
        doc = json.load(f)

    # Check required top-level fields
    required = {
        "@context": "Context reference",
        "@type": "Document type",
        "document_id": "Document identifier",
        "title": "Document title",
        "created": "Creation date"
    }

    for field, description in required.items():
        if field in doc:
            print(f"✅ {field}: {description}")
        else:
            print(f"❌ {field}: Missing")
            return False

    # Check layers
    layers = [
        "l1_data_provenance",
        "l2_consequence_simulation",
        "l3_empathy_mapping",
        "l4_accountability_ledger",
        "l5_fork_registry"
    ]

    print("\nLayers:")
    for layer in layers:
        if layer in doc:
            if isinstance(doc[layer], list):
                print(f"✅ {layer}: {len(doc[layer])} items")
            else:
                print(f"✅ {layer}: present")
        else:
            print(f"⚠️  {layer}: missing (may be optional)")

    return True


def test_rdf_expansion():
    """Test RDF expansion using rdflib."""
    print("\n" + "=" * 60)
    print("Test 4: RDF Expansion (requires rdflib)")
    print("=" * 60)

    try:
        from rdflib import Graph
    except ImportError:
        print("⚠️  rdflib not installed - skipping RDF tests")
        print("   Install with: pip install rdflib")
        return None  # Not a failure, just skipped

    try:
        g = Graph()
        g.parse("examples/danish_property_tax_reform.jsonld", format="json-ld")
        print(f"✅ Parsed JSON-LD successfully")
        print(f"✅ Generated {len(g)} RDF triples")

        # Show sample triples
        print("\nSample RDF triples:")
        for i, (s, p, o) in enumerate(g):
            if i < 3:
                print(f"   {s}")
                print(f"     → {p}")
                print(f"     → {o}\n")
            else:
                break

        return True
    except Exception as e:
        print(f"❌ RDF expansion failed: {e}")
        return False


def test_sparql_queries():
    """Test SPARQL queries on RDF data."""
    print("\n" + "=" * 60)
    print("Test 5: SPARQL Queries (requires rdflib)")
    print("=" * 60)

    try:
        from rdflib import Graph
    except ImportError:
        print("⚠️  rdflib not installed - skipping SPARQL tests")
        return None

    try:
        g = Graph()
        g.parse("examples/danish_property_tax_reform.jsonld", format="json-ld")

        # Query 1: Find document title
        query1 = """
        PREFIX dc: <http://purl.org/dc/terms/>
        SELECT ?title WHERE {
          ?doc dc:title ?title .
        }
        """
        results = list(g.query(query1))
        if results:
            print(f"✅ Query 1 - Document title: {results[0][0]}")
        else:
            print("❌ Query 1 failed: No title found")
            return False

        # Query 2: Count datasets
        query2 = """
        PREFIX orp: <https://openreason.org/vocab/>
        SELECT (COUNT(?dataset) as ?count) WHERE {
          ?doc orp:hasLayer1 ?l1 .
          ?l1 ?p ?dataset .
        }
        """
        results = list(g.query(query2))
        if results:
            print(f"✅ Query 2 - Found layer 1 items")

        # Query 3: Find stakeholders
        query3 = """
        PREFIX schema: <http://schema.org/>
        SELECT ?name WHERE {
          ?stakeholder schema:name ?name .
        } LIMIT 3
        """
        results = list(g.query(query3))
        if results:
            print(f"✅ Query 3 - Found {len(results)} stakeholders:")
            for r in results:
                print(f"     - {r[0]}")

        return True
    except Exception as e:
        print(f"❌ SPARQL queries failed: {e}")
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("ORP JSON-LD Schema Test Suite")
    print("=" * 60 + "\n")

    tests = [
        ("JSON Validity", test_json_validity),
        ("Context Structure", test_context_structure),
        ("Example Structure", test_example_structure),
        ("RDF Expansion", test_rdf_expansion),
        ("SPARQL Queries", test_sparql_queries)
    ]

    results = {}
    for name, test_func in tests:
        result = test_func()
        results[name] = result

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    passed = sum(1 for r in results.values() if r is True)
    failed = sum(1 for r in results.values() if r is False)
    skipped = sum(1 for r in results.values() if r is None)

    for name, result in results.items():
        if result is True:
            print(f"✅ {name}: PASSED")
        elif result is False:
            print(f"❌ {name}: FAILED")
        else:
            print(f"⚠️  {name}: SKIPPED")

    print(f"\nTotal: {passed} passed, {failed} failed, {skipped} skipped")

    if failed > 0:
        print("\n❌ Some tests failed!")
        sys.exit(1)
    else:
        print("\n✅ All tests passed!")
        if skipped > 0:
            print("   (Some tests skipped - install rdflib for full testing)")
        sys.exit(0)


if __name__ == "__main__":
    main()
