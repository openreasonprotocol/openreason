"""Tests for ORP validator core functionality."""

import pytest
from pytest import fixture
from pathlib import Path
from orp_validator import validate, ValidationResult, ComplianceLevel


# Test fixtures

@fixture
def minimal_header():
    """Minimal valid header fields."""
    return {
        "orp_version": "0.1",
        "document_id": "test-001",
        "title": "Test Document",
        "domain": "policy",
        "authors": [{"name": "Test Author", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-25",
        "status": "draft",
        "forked_from": None,
        "summary": "This is a test document for validation testing purposes.",
    }


@fixture
def minimal_l1():
    """Minimal valid L1 data provenance."""
    return [
        {
            "dataset_id": "test-ds-001",
            "name": "Test Dataset",
            "description": "A test dataset for validation",
            "source": "government",
            "collection_method": "Test collection",
            "date_range": "2024",
            "geographic_scope": "Global",
            "inclusion_criteria": {"description": "All data"},
            "exclusion_criteria": [],
            "cleaning_decisions": [],
            "synthetic_elements": {"present": False},
            "known_limitations": ["Test limitation"],
            "access": {"public": True},
            "attested_by": [
                {
                    "name": "Test",
                    "role": "author",
                    "date": "2026-02-25",
                    "statement": "Accurate",
                }
            ],
        }
    ]


# Test cases

def test_empty_document():
    """Test validation of an empty document."""
    result = validate({})
    assert not result.valid
    assert result.compliance_level == ComplianceLevel.NONE
    assert len(result.errors) > 0


def test_header_only(minimal_header):
    """Test document with only header fields."""
    result = validate(minimal_header)
    assert not result.valid  # Need at least L1 for any compliance
    assert result.compliance_level == ComplianceLevel.NONE


def test_orp_basic_valid(minimal_header, minimal_l1):
    """Test valid ORP-Basic document."""
    doc = {**minimal_header, "compliance_level": "ORP-Basic", "l1_data_provenance": minimal_l1}
    result = validate(doc)

    assert result.valid
    assert result.compliance_level == ComplianceLevel.BASIC
    assert result.layers_present["l1_data_provenance"]
    assert not result.layers_present["l2_consequence_simulation"]


def test_missing_required_header_field(minimal_header, minimal_l1):
    """Test document missing a required header field."""
    doc = {**minimal_header, "l1_data_provenance": minimal_l1}
    del doc["title"]

    result = validate(doc)
    assert not result.valid
    assert any("title" in error.lower() for error in result.errors)


def test_invalid_domain(minimal_header):
    """Test document with invalid domain value."""
    doc = {**minimal_header}
    doc["domain"] = "invalid-domain"

    result = validate(doc)
    assert not result.valid
    assert any("domain" in error.lower() for error in result.errors)


def test_invalid_author_role(minimal_header):
    """Test document with invalid author role."""
    doc = {**minimal_header}
    doc["authors"] = [{"name": "Test", "role": "invalid-role"}]

    result = validate(doc)
    assert not result.valid


def test_empty_summary(minimal_header):
    """Test document with empty summary."""
    doc = {**minimal_header}
    doc["summary"] = ""

    result = validate(doc)
    assert not result.valid
    assert any("summary" in error.lower() for error in result.errors)


def test_l1_missing_required_field(minimal_header, minimal_l1):
    """Test L1 with missing required field."""
    doc = {**minimal_header, "l1_data_provenance": minimal_l1}
    del doc["l1_data_provenance"][0]["dataset_id"]

    result = validate(doc)
    assert not result.valid
    assert any("dataset_id" in error.lower() for error in result.errors)


def test_l1_synthetic_elements_without_description(minimal_header, minimal_l1):
    """Test L1 with synthetic elements but no description."""
    doc = {**minimal_header, "l1_data_provenance": minimal_l1}
    doc["l1_data_provenance"][0]["synthetic_elements"] = {"present": True}

    result = validate(doc)
    assert not result.valid


def test_compliance_level_detection(minimal_header, minimal_l1):
    """Test that compliance levels are correctly detected."""
    # ORP-Basic: Header + L1
    doc_basic = {**minimal_header, "l1_data_provenance": minimal_l1}
    result = validate(doc_basic)
    assert result.compliance_level == ComplianceLevel.BASIC

    # Add L2 and L3 for Standard (we'll just add minimal structures)
    doc_standard = {
        **doc_basic,
        "l2_consequence_simulation": {
            "affected_population": {
                "description": "Test pop",
                "size_estimate": "100"
            },
            "variables": {
                "independent": [
                    {
                        "variable": "var1",
                        "description": "Test var",
                        "range": "0-10",
                        "default_value": "5",
                    }
                ],
                "dependent": [
                    {"variable": "out1", "description": "Test", "unit": "units"}
                ],
            },
            "model": {
                "type": "Test model",
                "assumptions": [
                    {
                        "assumption": "Test",
                        "basis": "Test",
                        "sensitivity": "Low",
                    }
                ],
            },
            "scenarios": [
                {
                    "scenario_id": "S1",
                    "name": "Test",
                    "description": "Test",
                    "variable_values": {"var1": "5"},
                    "outcomes": {"out1": "10"},
                }
            ],
            "primary_scenario": "S1",
        },
        "l3_empathy_mapping": {
            "stakeholder_map": [
                {
                    "stakeholder": "Test",
                    "description": "Test",
                    "estimated_population": "100",
                    "relationship_to_proposal": "Test",
                    "impacts_by_scenario": [
                        {"scenario_id": "S1", "direction": "neutral"}
                    ],
                }
            ],
            "minority_stress_test": {
                "description": "Test",
                "groups_tested": [
                    {
                        "group": "Test",
                        "scenario_tested": "Test",
                        "outcome": "Test",
                        "mitigation": "None needed",
                    }
                ],
            },
            "unresolved_impacts": [],
            "net_welfare_assessment": {
                "methodology": "Test",
                "conclusion": "Test",
                "confidence": "medium",
                "confidence_basis": "Test",
            },
        },
    }

    result = validate(doc_standard)
    assert result.compliance_level == ComplianceLevel.STANDARD


def test_warnings_for_lower_compliance(minimal_header, minimal_l1):
    """Test that warnings are generated for documents that could achieve higher compliance."""
    doc = {**minimal_header, "compliance_level": "ORP-Basic", "l1_data_provenance": minimal_l1}
    result = validate(doc)

    assert result.valid
    assert len(result.warnings) > 0
    assert any("ORP-Standard" in warning for warning in result.warnings)


def test_declared_vs_actual_compliance(minimal_header, minimal_l1):
    """Test warning when declared compliance doesn't match actual."""
    doc = {
        **minimal_header,
        "compliance_level": "ORP-Full",  # Declared as Full
        "l1_data_provenance": minimal_l1,  # But only has L1 (Basic)
    }

    result = validate(doc)
    assert not result.valid  # Because Full requires L2-L5
    # Should have errors about missing layers


def test_layers_present_detection(minimal_header, minimal_l1):
    """Test that layers_present correctly identifies which layers exist."""
    doc = {**minimal_header, "l1_data_provenance": minimal_l1}
    result = validate(doc)

    assert result.layers_present["l1_data_provenance"]
    assert not result.layers_present["l2_consequence_simulation"]
    assert not result.layers_present["l3_empathy_mapping"]
    assert not result.layers_present["l4_accountability_ledger"]
    assert not result.layers_present["l5_fork_registry"]


def test_validation_result_to_dict(minimal_header, minimal_l1):
    """Test that ValidationResult can be serialized to dict."""
    doc = {**minimal_header, "l1_data_provenance": minimal_l1}
    result = validate(doc)

    result_dict = result.to_dict()
    assert isinstance(result_dict, dict)
    assert "valid" in result_dict
    assert "compliance_level" in result_dict
    assert "errors" in result_dict
    assert "warnings" in result_dict
    assert "layers_present" in result_dict
