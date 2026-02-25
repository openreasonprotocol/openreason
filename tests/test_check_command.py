"""Tests for orp check command."""

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
def basic_doc(tmp_path):
    """Create a minimal ORP-Basic document."""
    doc = {
        "orp_version": "0.1",
        "document_id": "test-001",
        "title": "Test",
        "domain": "policy",
        "authors": [{"name": "Author", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-25",
        "status": "draft",
        "compliance_level": "ORP-Basic",
        "summary": "Test summary",
        "l1_data_provenance": [
            {
                "dataset_id": "test",
                "name": "Test",
                "description": "Test",
                "source": "government",
                "collection_method": "Test",
                "date_range": "2024",
                "geographic_scope": "Global",
                "inclusion_criteria": {"description": "All"},
                "exclusion_criteria": [],
                "cleaning_decisions": [],
                "synthetic_elements": {"present": False},
                "known_limitations": ["Test"],
                "access": {"public": True},
                "attested_by": [
                    {"name": "Test", "role": "author", "date": "2026-02-25", "statement": "Accurate"}
                ],
            }
        ],
    }

    doc_path = tmp_path / "basic.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


@pytest.fixture
def standard_doc(basic_doc, tmp_path):
    """Create an ORP-Standard document."""
    with open(basic_doc) as f:
        doc = yaml.safe_load(f)

    doc["compliance_level"] = "ORP-Standard"
    doc["l2_consequence_simulation"] = {
        "affected_population": {"description": "Test", "size_estimate": "100"},
        "variables": {
            "independent": [{"variable": "v", "description": "V", "range": "0-1", "default_value": "0"}],
            "dependent": [{"variable": "o", "description": "O", "unit": "units"}],
        },
        "model": {"type": "Test", "assumptions": [{"assumption": "A", "basis": "B", "sensitivity": "S"}]},
        "scenarios": [{"scenario_id": "S1", "name": "S", "description": "D", "variable_values": {"v": "0"}, "outcomes": {"o": "1"}}],
        "primary_scenario": "S1",
    }
    doc["l3_empathy_mapping"] = {
        "stakeholder_map": [
            {
                "stakeholder": "S",
                "description": "D",
                "estimated_population": "100",
                "relationship_to_proposal": "R",
                "impacts_by_scenario": [{"scenario_id": "S1", "direction": "neutral"}],
            }
        ],
        "minority_stress_test": {
            "description": "Test",
            "groups_tested": [{"group": "G", "scenario_tested": "T", "outcome": "O", "mitigation": "M"}],
        },
        "unresolved_impacts": [],
        "net_welfare_assessment": {
            "methodology": "M",
            "conclusion": "C",
            "confidence": "medium",
            "confidence_basis": "B",
        },
    }

    doc_path = tmp_path / "standard.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


def test_check_basic_compliance(runner, basic_doc):
    """Test checking ORP-Basic document."""
    result = runner.invoke(cli, ["check", str(basic_doc)])

    assert result.exit_code == 2  # Exit code 2 for Basic
    assert "ORP-Basic" in result.output
    assert "L1: Data Provenance" in result.output
    assert "✓" in result.output


def test_check_standard_compliance(runner, standard_doc):
    """Test checking ORP-Standard document."""
    result = runner.invoke(cli, ["check", str(standard_doc)])

    assert result.exit_code == 1  # Exit code 1 for Standard
    assert "ORP-Standard" in result.output
    assert "L2: Consequence Simulation" in result.output
    assert "L3: Empathy Mapping" in result.output


def test_check_quiet_mode(runner, basic_doc):
    """Test quiet mode outputs only compliance level."""
    result = runner.invoke(cli, ["check", str(basic_doc), "--quiet"])

    assert result.exit_code == 2
    assert result.output.strip() == "ORP-Basic"


def test_check_json_output(runner, basic_doc):
    """Test JSON output mode."""
    result = runner.invoke(cli, ["check", str(basic_doc), "--json"])

    assert result.exit_code == 2

    output = json.loads(result.output)
    assert output["compliance_level"] == "ORP-Basic"
    assert "layers_present" in output
    assert output["layers_present"]["l1_data_provenance"] is True
    assert output["layers_present"]["l2_consequence_simulation"] is False


def test_check_missing_header(runner, tmp_path):
    """Test checking document with missing header fields."""
    doc = {"orp_version": "0.1", "document_id": "test"}

    doc_path = tmp_path / "invalid.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    result = runner.invoke(cli, ["check", str(doc_path)])

    assert result.exit_code == 3  # Exit code 3 for Non-compliant
    assert "Non-compliant" in result.output


def test_check_nonexistent_file(runner):
    """Test checking non-existent file."""
    result = runner.invoke(cli, ["check", "nonexistent.yaml"])

    # FileNotFoundError from Click's Path validator exits with 2
    assert result.exit_code == 2


def test_check_shows_next_steps_basic(runner, basic_doc):
    """Test that check shows guidance for upgrading from Basic."""
    result = runner.invoke(cli, ["check", str(basic_doc)])

    assert "To reach ORP-Standard, add:" in result.output
    assert "L2: Consequence Simulation" in result.output
    assert "L3: Empathy Mapping" in result.output


def test_check_shows_next_steps_standard(runner, standard_doc):
    """Test that check shows guidance for upgrading from Standard."""
    result = runner.invoke(cli, ["check", str(standard_doc)])

    assert "To reach ORP-Full, add:" in result.output
    assert "L4: Accountability Ledger" in result.output
    assert "L5: Fork Registry" in result.output
