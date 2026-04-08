"""Tests for /api/v1/check endpoint."""

import pytest


class TestCheckEndpoint:
    """Test suite for compliance check endpoint."""

    def test_check_orp_basic(self, client, valid_orp_basic):
        """Test quick check of ORP-Basic document."""
        response = client.post(
            "/api/v1/check",
            json={"document": valid_orp_basic}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["compliance_level"] == "ORP-Basic"
        assert data["layers_present"]["l1_data_provenance"] is True
        assert data["layers_present"]["l2_consequence_simulation"] is False
        assert "next_steps" in data
        assert "ORP-Standard" in data["next_steps"]

    def test_check_orp_full(self, client, valid_orp_full):
        """Test quick check of ORP-Full document."""
        response = client.post(
            "/api/v1/check",
            json={"document": valid_orp_full}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["compliance_level"] == "ORP-Full"
        assert sum(data["layers_present"].values()) == 5
        assert "Full compliance achieved" in data["next_steps"]

    def test_check_non_compliant(self, client, minimal_document):
        """Test quick check of non-compliant document."""
        response = client.post(
            "/api/v1/check",
            json={"document": minimal_document}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["compliance_level"] == "Non-compliant"
        assert all(not v for v in data["layers_present"].values())
        assert "L1" in data["next_steps"]

    def test_check_invalid_yaml(self, client, invalid_yaml):
        """Test quick check with invalid YAML."""
        response = client.post(
            "/api/v1/check",
            json={"document": invalid_yaml}
        )
        assert response.status_code == 400
        assert "Invalid YAML/JSON" in response.json()["detail"]

    def test_check_yaml_array(self, client, yaml_array):
        """Test quick check with YAML array."""
        response = client.post(
            "/api/v1/check",
            json={"document": yaml_array}
        )
        assert response.status_code == 400
        assert "must be a YAML/JSON object" in response.json()["detail"]

    def test_check_performance(self, client, valid_orp_full):
        """Test that check is faster than full validation."""
        import time

        # Time check endpoint
        start = time.time()
        check_response = client.post(
            "/api/v1/check",
            json={"document": valid_orp_full}
        )
        check_time = time.time() - start

        # Time validate endpoint
        start = time.time()
        validate_response = client.post(
            "/api/v1/validate",
            json={"document": valid_orp_full}
        )
        validate_time = time.time() - start

        assert check_response.status_code == 200
        assert validate_response.status_code == 200
        # Check should be faster (or at least not slower)
        assert check_time <= validate_time + 0.1  # Allow 100ms tolerance

    def test_check_orp_standard(self, client):
        """Test check endpoint with ORP-Standard document."""
        orp_standard = """
orp_version: '0.1'
document_id: test-standard-001
title: Standard Test
domain: policy
authors:
  - name: Test
    role: author
created: '2026-01-01'
last_modified: '2026-01-01'
status: draft
summary: Test
l1_data_provenance:
  - dataset_id: ds1
    name: Test
    description: Test
    source: government
    collection_method: Survey
    date_range: '2024'
    geographic_scope: Global
    inclusion_criteria:
      description: All
    exclusion_criteria: []
    cleaning_decisions: []
    synthetic_elements:
      present: false
    known_limitations: []
    access:
      public: true
    attested_by:
      - name: Manager
        role: data_steward
        date: '2026-01-01'
        statement: OK
l2_consequence_simulation:
  affected_population:
    description: Pop
    size_estimate: '100'
  variables:
    independent:
      - variable: x
        description: X
        range: '0-1'
        default_value: '0'
    dependent:
      - variable: y
        description: Y
        unit: units
  model:
    type: Model
    assumptions:
      - assumption: A
        basis: B
        sensitivity: Low
  scenarios:
    - scenario_id: s1
      name: S
      description: D
      variable_values:
        x: '0'
      outcomes:
        y: '1'
  primary_scenario: s1
l3_empathy_mapping:
  stakeholder_map:
    - stakeholder: S
      description: D
      estimated_population: '100'
      relationship_to_proposal: R
      impacts_by_scenario:
        - scenario_id: s1
          direction: neutral
  minority_stress_test:
    description: Test
    groups_tested:
      - group: G
        scenario_tested: T
        outcome: O
        mitigation: M
  unresolved_impacts: []
  net_welfare_assessment:
    methodology: M
    conclusion: C
    confidence: medium
    confidence_basis: B
"""
        response = client.post(
            "/api/v1/check",
            json={"document": orp_standard}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["compliance_level"] == "ORP-Standard"
        assert data["layers_present"]["l1_data_provenance"] is True
        assert data["layers_present"]["l2_consequence_simulation"] is True
        assert data["layers_present"]["l3_empathy_mapping"] is True
        assert data["layers_present"]["l4_accountability_ledger"] is False
        assert data["layers_present"]["l5_fork_registry"] is False
        assert "ORP-Full" in data["next_steps"]

    def test_check_orp_v02_posthoc(self, client, valid_orp_v02_posthoc):
        """Test quick check of ORP v0.2 post-hoc document."""
        response = client.post(
            "/api/v1/check",
            json={"document": valid_orp_v02_posthoc}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["compliance_level"] == "ORP-PostHoc"
        assert data["layers_present"]["l1_data_provenance"] is True
        assert "Post-hoc reconstruction" in data["next_steps"]
