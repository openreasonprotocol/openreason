"""Tests for orp validate command."""

import json

import pytest
import yaml
from click.testing import CliRunner

from orp_validator.main import cli


@pytest.fixture
def runner():
    """Click CLI test runner."""
    return CliRunner()


@pytest.fixture
def valid_basic_doc(tmp_path):
    """Create a valid ORP-Basic document."""
    doc = {
        "orp_version": "0.1",
        "document_id": "test-001",
        "title": "Test Document",
        "domain": "policy",
        "authors": [{"name": "Test Author", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-25",
        "status": "draft",
        "compliance_level": "ORP-Basic",
        "summary": "Test summary for validation",
        "l1_data_provenance": [
            {
                "dataset_id": "test-ds",
                "name": "Test Dataset",
                "description": "A test dataset",
                "source": "government",
                "collection_method": "Survey",
                "date_range": "2024-2025",
                "geographic_scope": "National",
                "inclusion_criteria": {"description": "All participants"},
                "exclusion_criteria": [],
                "cleaning_decisions": [],
                "synthetic_elements": {"present": False},
                "known_limitations": ["Sample size"],
                "access": {"public": True},
                "attested_by": [
                    {
                        "name": "Data Officer",
                        "role": "data-steward",
                        "date": "2026-02-25",
                        "statement": "Accurate to best of knowledge",
                    }
                ],
            }
        ],
    }

    doc_path = tmp_path / "valid.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


@pytest.fixture
def invalid_doc(tmp_path):
    """Create an invalid document (missing required fields)."""
    doc = {
        "orp_version": "0.1",
        "document_id": "test-002",
        "title": "Invalid Document",
        # Missing many required fields
    }

    doc_path = tmp_path / "invalid.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


def test_validate_valid_document(runner, valid_basic_doc):
    """Test validating a valid document."""
    result = runner.invoke(cli, ["validate", str(valid_basic_doc)])

    assert result.exit_code == 0
    assert "✓ Valid" in result.output
    assert "ORP-Basic" in result.output
    assert "Validation Report" in result.output


def test_validate_invalid_document(runner, invalid_doc):
    """Test validating an invalid document."""
    result = runner.invoke(cli, ["validate", str(invalid_doc)])

    assert result.exit_code == 1
    assert "✗ Invalid" in result.output
    assert "Errors:" in result.output


def test_validate_json_output(runner, valid_basic_doc):
    """Test JSON output mode."""
    result = runner.invoke(cli, ["validate", str(valid_basic_doc), "--json"])

    assert result.exit_code == 0

    output = json.loads(result.output)
    assert output["valid"] is True
    assert output["compliance_level"] == "ORP-Basic"
    assert "layers_present" in output


def test_validate_json_output_invalid(runner, invalid_doc):
    """Test JSON output for invalid document."""
    result = runner.invoke(cli, ["validate", str(invalid_doc), "--json"])

    assert result.exit_code == 1

    output = json.loads(result.output)
    assert output["valid"] is False
    assert len(output["errors"]) > 0


def test_validate_verbose_mode(runner, valid_basic_doc):
    """Test verbose output mode."""
    result = runner.invoke(cli, ["validate", str(valid_basic_doc), "--verbose"])

    assert result.exit_code == 0
    assert "Layers Present:" in result.output
    assert "l1_data_provenance" in result.output


def test_validate_verbose_invalid(runner, invalid_doc):
    """Test verbose mode with invalid document."""
    result = runner.invoke(cli, ["validate", str(invalid_doc), "--verbose"])

    assert result.exit_code == 1
    assert "Layers Present:" in result.output


def test_validate_nonexistent_file(runner):
    """Test validating non-existent file."""
    result = runner.invoke(cli, ["validate", "nonexistent.yaml"])

    assert result.exit_code == 2


def test_validate_shows_warnings(runner, tmp_path):
    """Test that warnings are shown for documents that could achieve higher compliance."""
    # Create ORP-Basic doc (will get warning about upgrading to Standard)
    doc = {
        "orp_version": "0.1",
        "document_id": "test-003",
        "title": "Basic Doc",
        "domain": "policy",
        "authors": [{"name": "Author", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-25",
        "status": "draft",
        "compliance_level": "ORP-Basic",
        "summary": "Basic document",
        "l1_data_provenance": [
            {
                "dataset_id": "ds1",
                "name": "Dataset",
                "description": "Desc",
                "source": "government",
                "collection_method": "Method",
                "date_range": "2024",
                "geographic_scope": "Global",
                "inclusion_criteria": {"description": "All"},
                "exclusion_criteria": [],
                "cleaning_decisions": [],
                "synthetic_elements": {"present": False},
                "known_limitations": ["None"],
                "access": {"public": True},
                "attested_by": [
                    {"name": "A", "role": "author", "date": "2026-02-25", "statement": "OK"}
                ],
            }
        ],
    }

    doc_path = tmp_path / "basic_with_warning.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    result = runner.invoke(cli, ["validate", str(doc_path)])

    assert result.exit_code == 0
    assert "Warnings:" in result.output


def test_validate_full_compliance(runner, tmp_path):
    """Test validating ORP-Full document shows correct compliance."""
    doc = {
        "orp_version": "0.1",
        "document_id": "test-full",
        "title": "Full Doc",
        "domain": "policy",
        "authors": [{"name": "Author", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-25",
        "status": "draft",
        "compliance_level": "ORP-Full",
        "summary": "Full compliance document",
        "l1_data_provenance": [
            {
                "dataset_id": "ds1",
                "name": "Dataset",
                "description": "Desc",
                "source": "government",
                "collection_method": "Method",
                "date_range": "2024",
                "geographic_scope": "Global",
                "inclusion_criteria": {"description": "All"},
                "exclusion_criteria": [],
                "cleaning_decisions": [],
                "synthetic_elements": {"present": False},
                "known_limitations": ["None"],
                "access": {"public": True},
                "attested_by": [
                    {"name": "A", "role": "author", "date": "2026-02-25", "statement": "OK"}
                ],
            }
        ],
        "l2_consequence_simulation": {
            "affected_population": {"description": "Pop", "size_estimate": "100"},
            "variables": {
                "independent": [
                    {"variable": "x", "description": "X", "range": "0-1", "default_value": "0"}
                ],
                "dependent": [{"variable": "y", "description": "Y", "unit": "units"}],
            },
            "model": {
                "type": "Model",
                "assumptions": [{"assumption": "A", "basis": "B", "sensitivity": "S"}],
            },
            "scenarios": [
                {
                    "scenario_id": "s1",
                    "name": "Scenario",
                    "description": "D",
                    "variable_values": {"x": "0"},
                    "outcomes": {"y": "1"},
                }
            ],
            "primary_scenario": "s1",
        },
        "l3_empathy_mapping": {
            "stakeholder_map": [
                {
                    "stakeholder": "S",
                    "description": "D",
                    "estimated_population": "100",
                    "relationship_to_proposal": "R",
                    "impacts_by_scenario": [{"scenario_id": "s1", "direction": "neutral"}],
                }
            ],
            "minority_stress_test": {
                "description": "Test",
                "groups_tested": [
                    {"group": "G", "scenario_tested": "T", "outcome": "O", "mitigation": "M"}
                ],
            },
            "unresolved_impacts": [],
            "net_welfare_assessment": {
                "methodology": "M",
                "conclusion": "C",
                "confidence": "medium",
                "confidence_basis": "B",
            },
        },
        "l4_accountability_ledger": {
            "entries": [
                {
                    "entry_id": "L4-001",
                    "timestamp": "2026-02-25T10:00:00Z",
                    "decision_type": "framing",
                    "description": "Test decision",
                    "decided_by": [{"name": "Decision Maker"}],
                    "basis": "Test basis",
                }
            ],
            "review_history": []
        },
        "l5_fork_registry": {
            "this_document": {
                "document_id": "test-full",
                "forked_from": None,
                "fork_reason": "Original",
                "key_differences": "N/A"
            },
            "known_forks": [],
            "responses": []
        },
    }

    doc_path = tmp_path / "full.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    result = runner.invoke(cli, ["validate", str(doc_path)])

    assert result.exit_code == 0
    assert "ORP-Full" in result.output
    # Full compliance shouldn't suggest higher compliance
    assert "achieving higher compliance" not in result.output.lower()


def test_validate_error_handling(runner, tmp_path):
    """Test error handling for malformed YAML."""
    bad_yaml = tmp_path / "bad.yaml"
    bad_yaml.write_text("this is not: valid: yaml: [")

    result = runner.invoke(cli, ["validate", str(bad_yaml)])

    assert result.exit_code == 2
    assert "Error:" in result.output


def test_validate_verbose_error_handling(runner, tmp_path):
    """Test verbose mode shows traceback on errors."""
    bad_yaml = tmp_path / "bad.yaml"
    bad_yaml.write_text("this is not: valid: yaml: [")

    result = runner.invoke(cli, ["validate", str(bad_yaml), "--verbose"])

    assert result.exit_code == 2
    assert "Error:" in result.output
