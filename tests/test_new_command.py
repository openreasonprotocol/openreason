"""Tests for orp new command."""

import yaml
from pathlib import Path

import pytest
from click.testing import CliRunner

from orp_validator.main import cli


@pytest.fixture
def runner():
    """Click CLI test runner."""
    return CliRunner()


def test_new_basic_interactive(runner, tmp_path):
    """Test creating ORP-Basic document interactively."""
    output_file = tmp_path / "test.yaml"

    # Simulate interactive input
    result = runner.invoke(
        cli,
        ["new", str(output_file)],
        input="Test Document\npolicy\nTest Author\n",
    )

    assert result.exit_code == 0
    assert output_file.exists()
    assert "✓ Created" in result.output

    # Verify document structure
    with open(output_file) as f:
        doc = yaml.safe_load(f)

    assert doc["title"] == "Test Document"
    assert doc["domain"] == "policy"
    assert doc["authors"][0]["name"] == "Test Author"
    assert doc["compliance_level"] == "ORP-Basic"
    assert "l1_data_provenance" in doc


def test_new_non_interactive(runner, tmp_path):
    """Test creating document in non-interactive mode."""
    output_file = tmp_path / "test.yaml"

    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--title", "My Policy",
            "--domain", "policy",
            "--author", "John Doe",
            "--non-interactive",
        ],
    )

    assert result.exit_code == 0
    assert output_file.exists()

    with open(output_file) as f:
        doc = yaml.safe_load(f)

    assert doc["title"] == "My Policy"
    assert doc["domain"] == "policy"
    assert doc["authors"][0]["name"] == "John Doe"


def test_new_standard_compliance(runner, tmp_path):
    """Test creating ORP-Standard document."""
    output_file = tmp_path / "test.yaml"

    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--compliance", "standard",
            "--title", "Test",
            "--domain", "policy",
            "--author", "Author",
            "--non-interactive",
        ],
    )

    assert result.exit_code == 0

    with open(output_file) as f:
        doc = yaml.safe_load(f)

    assert doc["compliance_level"] == "ORP-Standard"
    assert "l1_data_provenance" in doc
    assert "l2_consequence_simulation" in doc
    assert "l3_empathy_mapping" in doc


def test_new_full_compliance(runner, tmp_path):
    """Test creating ORP-Full document."""
    output_file = tmp_path / "test.yaml"

    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--compliance", "full",
            "--title", "Test",
            "--domain", "policy",
            "--author", "Author",
            "--non-interactive",
        ],
    )

    assert result.exit_code == 0

    with open(output_file) as f:
        doc = yaml.safe_load(f)

    assert doc["compliance_level"] == "ORP-Full"
    assert "l1_data_provenance" in doc
    assert "l2_consequence_simulation" in doc
    assert "l3_empathy_mapping" in doc
    assert "l4_accountability_ledger" in doc
    assert "l5_fork_registry" in doc


def test_new_json_format(runner, tmp_path):
    """Test creating document in JSON format."""
    output_file = tmp_path / "test.json"

    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--format", "json",
            "--title", "Test",
            "--domain", "policy",
            "--author", "Author",
            "--non-interactive",
        ],
    )

    assert result.exit_code == 0
    assert output_file.exists()

    import json
    with open(output_file) as f:
        doc = json.load(f)

    assert doc["title"] == "Test"


def test_new_file_exists_abort(runner, tmp_path):
    """Test aborting when file exists."""
    output_file = tmp_path / "test.yaml"
    output_file.write_text("existing content")

    # Simulate user declining to overwrite
    result = runner.invoke(
        cli,
        ["new", str(output_file)],
        input="n\n",
    )

    assert result.exit_code == 0
    assert "Aborted" in result.output
    assert output_file.read_text() == "existing content"


def test_new_file_exists_overwrite(runner, tmp_path):
    """Test overwriting existing file."""
    output_file = tmp_path / "test.yaml"
    output_file.write_text("existing content")

    # Simulate user confirming overwrite
    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--title", "Test",
            "--domain", "policy",
            "--author", "Author",
            "--non-interactive",
        ],
        input="y\n",
    )

    assert result.exit_code == 0
    assert output_file.read_text() != "existing content"


def test_new_non_interactive_missing_fields(runner, tmp_path):
    """Test error when required fields missing in non-interactive mode."""
    output_file = tmp_path / "test.yaml"

    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--non-interactive",
        ],
    )

    assert result.exit_code == 1
    assert "required" in result.output.lower()


def test_new_document_id_generation(runner, tmp_path):
    """Test that document ID is generated from filename."""
    output_file = tmp_path / "my-policy-proposal.yaml"

    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--title", "Test",
            "--domain", "policy",
            "--author", "Author",
            "--non-interactive",
        ],
    )

    assert result.exit_code == 0

    with open(output_file) as f:
        doc = yaml.safe_load(f)

    assert doc["document_id"] == "my-policy-proposal-001"


def test_new_dates_populated(runner, tmp_path):
    """Test that created and last_modified dates are set."""
    output_file = tmp_path / "test.yaml"

    result = runner.invoke(
        cli,
        [
            "new",
            str(output_file),
            "--title", "Test",
            "--domain", "policy",
            "--author", "Author",
            "--non-interactive",
        ],
    )

    assert result.exit_code == 0

    with open(output_file) as f:
        doc = yaml.safe_load(f)

    assert "created" in doc
    assert "last_modified" in doc
    assert doc["created"] == doc["last_modified"]
