"""Tests for /api/v1/diff endpoint."""

import pytest


class TestDiffEndpoint:
    """Test suite for document comparison endpoint."""

    def test_diff_identical_documents(self, client, valid_orp_basic):
        """Test diff with two identical documents."""
        response = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_basic,
                "document2": valid_orp_basic,
                "include_metadata": False
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["identical"] is True
        assert data["num_changes"] == 0
        assert len(data["differences"]) == 0

    def test_diff_different_documents(self, client, valid_orp_basic, valid_orp_full):
        """Test diff with significantly different documents."""
        response = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_basic,
                "document2": valid_orp_full,
                "include_metadata": False
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["identical"] is False
        assert data["num_changes"] > 0
        assert len(data["differences"]) > 0

    def test_diff_fork_detection(self, client, valid_orp_basic):
        """Test fork relationship detection."""
        # Create a forked document
        forked_doc = valid_orp_basic.replace(
            "document_id: test-basic-001",
            "document_id: test-fork-001\nforked_from: test-basic-001"
        ).replace(
            "title: Test Basic Document",
            "title: Forked Document"
        )

        response = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_basic,
                "document2": forked_doc,
                "include_metadata": False
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["is_fork"] is True
        assert data["fork_direction"] == "document2 forked from document1"
        assert data["num_changes"] > 0

    def test_diff_metadata_filtering(self, client, valid_orp_basic):
        """Test metadata field filtering."""
        doc2 = valid_orp_basic.replace(
            "last_modified: '2026-01-01'",
            "last_modified: '2026-12-31'"
        )

        # Without metadata
        response1 = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_basic,
                "document2": doc2,
                "include_metadata": False
            }
        )
        assert response1.status_code == 200
        data1 = response1.json()
        assert data1["identical"] is True

        # With metadata
        response2 = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_basic,
                "document2": doc2,
                "include_metadata": True
            }
        )
        assert response2.status_code == 200
        data2 = response2.json()
        assert data2["identical"] is False
        assert data2["num_changes"] == 1

    def test_diff_layer_filtering(self, client, valid_orp_full):
        """Test layer-specific comparison."""
        doc2 = valid_orp_full.replace(
            "title: Test Full Document",
            "title: Modified Document"
        )

        # Compare only L2 layer
        response = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_full,
                "document2": doc2,
                "layer": "l2_consequence_simulation"
            }
        )
        assert response.status_code == 200
        data = response.json()
        # Title change shouldn't appear in L2-only diff
        assert data["identical"] is True

    def test_diff_invalid_layer(self, client, valid_orp_basic):
        """Test diff with non-existent layer."""
        response = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_basic,
                "document2": valid_orp_basic,
                "layer": "l6_nonexistent"
            }
        )
        assert response.status_code == 400
        assert "not found" in response.json()["detail"]

    def test_diff_invalid_yaml_doc1(self, client, invalid_yaml, valid_orp_basic):
        """Test diff with invalid YAML in first document."""
        response = client.post(
            "/api/v1/diff",
            json={
                "document1": invalid_yaml,
                "document2": valid_orp_basic
            }
        )
        assert response.status_code == 400
        assert "Invalid YAML/JSON" in response.json()["detail"]

    def test_diff_invalid_yaml_doc2(self, client, valid_orp_basic, invalid_yaml):
        """Test diff with invalid YAML in second document."""
        response = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_basic,
                "document2": invalid_yaml
            }
        )
        assert response.status_code == 400
        assert "Invalid YAML/JSON" in response.json()["detail"]

    def test_diff_change_types(self, client):
        """Test that diff correctly identifies added, removed, and changed fields."""
        doc1 = """
orp_version: '0.1'
document_id: test-001
title: Original
domain: policy
field1: value1
field2: value2
"""
        doc2 = """
orp_version: '0.1'
document_id: test-001
title: Modified
domain: policy
field2: changed_value2
field3: value3
"""
        response = client.post(
            "/api/v1/diff",
            json={
                "document1": doc1,
                "document2": doc2
            }
        )
        assert response.status_code == 200
        data = response.json()

        # Find specific change types
        changes = {d["field"]: d for d in data["differences"]}
        assert "field1" in changes
        assert changes["field1"]["type"] == "removed"
        assert "field3" in changes
        assert changes["field3"]["type"] == "added"
        assert "title" in changes or "field2" in changes  # At least one changed

    def test_diff_nested_changes(self, client, valid_orp_full):
        """Test diff with nested field changes."""
        doc2 = valid_orp_full.replace(
            "revenue: '250000000'",
            "revenue: '300000000'"
        )

        response = client.post(
            "/api/v1/diff",
            json={
                "document1": valid_orp_full,
                "document2": doc2,
                "include_metadata": False
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["identical"] is False
        assert data["num_changes"] > 0

        # Check that field path includes nested structure
        field_paths = [d["field"] for d in data["differences"]]
        has_nested = any("." in path or "[" in path for path in field_paths)
        assert has_nested
