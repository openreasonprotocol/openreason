"""Tests for orp diff command."""

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
def doc1(tmp_path):
    """Create first test document."""
    doc = {
        "orp_version": "0.1",
        "document_id": "original-001",
        "title": "Original Document",
        "domain": "policy",
        "authors": [{"name": "Author", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-25",
        "status": "draft",
        "summary": "Original summary",
        "l1_data_provenance": [{"dataset_id": "ds1"}],
    }

    doc_path = tmp_path / "doc1.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


@pytest.fixture
def doc2(tmp_path):
    """Create second test document (modified)."""
    doc = {
        "orp_version": "0.1",
        "document_id": "modified-001",
        "title": "Modified Document",
        "domain": "policy",
        "authors": [{"name": "Author", "role": "author"}],
        "created": "2026-02-25",
        "last_modified": "2026-02-26",
        "status": "open-for-comment",
        "summary": "Modified summary",
        "l1_data_provenance": [{"dataset_id": "ds2"}],
    }

    doc_path = tmp_path / "doc2.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


@pytest.fixture
def fork_doc(tmp_path):
    """Create a fork of doc1."""
    doc = {
        "orp_version": "0.1",
        "document_id": "fork-001",
        "title": "Forked Document",
        "domain": "policy",
        "authors": [{"name": "Forker", "role": "author"}],
        "created": "2026-02-26",
        "last_modified": "2026-02-26",
        "status": "draft",
        "forked_from": "original-001",
        "summary": "Fork summary",
        "l1_data_provenance": [{"dataset_id": "ds1"}],
    }

    doc_path = tmp_path / "fork.yaml"
    with open(doc_path, "w") as f:
        yaml.dump(doc, f)

    return doc_path


def test_diff_identical_documents(runner, doc1, tmp_path):
    """Test diffing identical documents."""
    # Create identical copy
    doc1_copy = tmp_path / "doc1_copy.yaml"
    with open(doc1) as f:
        content = f.read()
    doc1_copy.write_text(content)

    result = runner.invoke(cli, ["diff", str(doc1), str(doc1_copy)])

    assert result.exit_code == 0  # Exit 0 for identical
    assert "identical" in result.output.lower()


def test_diff_different_documents(runner, doc1, doc2):
    """Test diffing different documents."""
    result = runner.invoke(cli, ["diff", str(doc1), str(doc2)])

    assert result.exit_code == 1  # Exit 1 for different
    assert "difference" in result.output.lower()
    assert "document_id" in result.output
    assert "title" in result.output


def test_diff_fork_detection(runner, doc1, fork_doc):
    """Test that fork relationships are detected."""
    result = runner.invoke(cli, ["diff", str(doc1), str(fork_doc)])

    assert result.exit_code == 1
    assert "fork" in result.output.lower()


def test_diff_exclude_metadata(runner, doc1, doc2):
    """Test that metadata changes are excluded by default."""
    result = runner.invoke(cli, ["diff", str(doc1), str(doc2)])

    # last_modified should not appear in diff by default
    assert "last_modified" not in result.output


def test_diff_include_metadata(runner, doc1, doc2):
    """Test including metadata changes."""
    result = runner.invoke(cli, ["diff", str(doc1), str(doc2), "--include-metadata"])

    # last_modified should appear when explicitly included
    assert "last_modified" in result.output


def test_diff_json_output(runner, doc1, doc2):
    """Test JSON output mode."""
    result = runner.invoke(cli, ["diff", str(doc1), str(doc2), "--json"])

    assert result.exit_code == 1

    output = json.loads(result.output)
    assert "file1" in output
    assert "file2" in output
    assert "differences" in output
    assert "num_changes" in output
    assert output["num_changes"] > 0


def test_diff_specific_layer(runner, tmp_path):
    """Test diffing specific layer only."""
    doc1_data = {
        "title": "Doc 1",
        "l1_data_provenance": [{"dataset_id": "ds1"}],
        "l2_consequence_simulation": {"field": "value1"},
    }
    doc2_data = {
        "title": "Doc 2",
        "l1_data_provenance": [{"dataset_id": "ds1"}],  # Same L1
        "l2_consequence_simulation": {"field": "value2"},  # Different L2
    }

    doc1 = tmp_path / "doc1.yaml"
    doc2 = tmp_path / "doc2.yaml"

    with open(doc1, "w") as f:
        yaml.dump(doc1_data, f)
    with open(doc2, "w") as f:
        yaml.dump(doc2_data, f)

    # Diff only L1 - should be identical
    result = runner.invoke(cli, ["diff", str(doc1), str(doc2), "--layer", "l1_data_provenance"])

    assert result.exit_code == 0
    assert "identical" in result.output.lower()


def test_diff_shows_added_fields(runner, tmp_path):
    """Test that added fields are shown."""
    doc1_data = {"field1": "value1"}
    doc2_data = {"field1": "value1", "field2": "value2"}

    doc1 = tmp_path / "doc1.yaml"
    doc2 = tmp_path / "doc2.yaml"

    with open(doc1, "w") as f:
        yaml.dump(doc1_data, f)
    with open(doc2, "w") as f:
        yaml.dump(doc2_data, f)

    result = runner.invoke(cli, ["diff", str(doc1), str(doc2)])

    assert result.exit_code == 1
    assert "Added" in result.output
    assert "field2" in result.output


def test_diff_shows_removed_fields(runner, tmp_path):
    """Test that removed fields are shown."""
    doc1_data = {"field1": "value1", "field2": "value2"}
    doc2_data = {"field1": "value1"}

    doc1 = tmp_path / "doc1.yaml"
    doc2 = tmp_path / "doc2.yaml"

    with open(doc1, "w") as f:
        yaml.dump(doc1_data, f)
    with open(doc2, "w") as f:
        yaml.dump(doc2_data, f)

    result = runner.invoke(cli, ["diff", str(doc1), str(doc2)])

    assert result.exit_code == 1
    assert "Removed" in result.output
    assert "field2" in result.output


def test_diff_nonexistent_file(runner, doc1):
    """Test diffing with non-existent file."""
    result = runner.invoke(cli, ["diff", str(doc1), "nonexistent.yaml"])

    assert result.exit_code == 2


def test_diff_json_format_documents(runner, tmp_path):
    """Test diffing JSON format documents."""
    doc1_data = {"field": "value1"}
    doc2_data = {"field": "value2"}

    doc1 = tmp_path / "doc1.json"
    doc2 = tmp_path / "doc2.json"

    with open(doc1, "w") as f:
        json.dump(doc1_data, f)
    with open(doc2, "w") as f:
        json.dump(doc2_data, f)

    result = runner.invoke(cli, ["diff", str(doc1), str(doc2)])

    assert result.exit_code == 1
    assert "difference" in result.output.lower()
