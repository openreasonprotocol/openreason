"""Tests for ORP validator CLI."""

import json

import pytest
import yaml
from click.testing import CliRunner

from orp_validator.cli import main


@pytest.fixture
def runner():
    """Click CLI test runner."""
    return CliRunner()


@pytest.fixture
def valid_basic_document(tmp_path):
    """Create a temporary valid ORP-Basic document."""
    doc = {
        "orp_version": "0.1",
        "document_id": "test-001",
        "title": "Test Document",
        "domain": "policy",
        "authors": [{"name": "Test", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-25",
        "status": "draft",
        "forked_from": None,
        "compliance_level": "ORP-Basic",
        "summary": "Test document summary.",
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
                    {
                        "name": "Test",
                        "role": "author",
                        "date": "2026-02-25",
                        "statement": "Accurate",
                    }
                ],
            }
        ],
    }

    doc_path = tmp_path / "test_valid.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


@pytest.fixture
def invalid_document(tmp_path):
    """Create a temporary invalid document."""
    doc = {
        "orp_version": "0.1",
        "document_id": "test-002",
        # Missing required fields
    }

    doc_path = tmp_path / "test_invalid.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


def test_cli_valid_document(runner, valid_basic_document):
    """Test CLI with valid document."""
    result = runner.invoke(main, [str(valid_basic_document)])

    assert result.exit_code == 0
    assert "✓ Valid" in result.output
    assert "ORP-Basic" in result.output


def test_cli_invalid_document(runner, invalid_document):
    """Test CLI with invalid document."""
    result = runner.invoke(main, [str(invalid_document)])

    assert result.exit_code == 1
    assert "✗ Invalid" in result.output
    assert "Errors:" in result.output


def test_cli_json_output(runner, valid_basic_document):
    """Test CLI with JSON output format."""
    result = runner.invoke(main, [str(valid_basic_document), "--json"])

    assert result.exit_code == 0

    # Parse JSON output
    output_data = json.loads(result.output)
    assert output_data["valid"] is True
    assert output_data["compliance_level"] == "ORP-Basic"
    assert "errors" in output_data
    assert "warnings" in output_data
    assert "layers_present" in output_data


def test_cli_verbose_output(runner, valid_basic_document):
    """Test CLI with verbose flag."""
    result = runner.invoke(main, [str(valid_basic_document), "--verbose"])

    assert result.exit_code == 0
    assert "Layers Present:" in result.output


def test_cli_nonexistent_file(runner):
    """Test CLI with nonexistent file."""
    result = runner.invoke(main, ["nonexistent.yaml"])

    assert result.exit_code == 2
    assert "Error:" in result.output


def test_cli_version(runner):
    """Test CLI version flag."""
    result = runner.invoke(main, ["--version"])

    assert result.exit_code == 0
    assert "version" in result.output.lower()
