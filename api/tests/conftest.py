"""Pytest configuration and shared fixtures."""

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture
def valid_orp_basic():
    """Minimal valid ORP-Basic document."""
    return """
orp_version: '0.1'
document_id: test-basic-001
title: Test Basic Document
domain: policy
authors:
  - name: Test Author
    role: author
created: '2026-01-01'
last_modified: '2026-01-01'
status: draft
summary: A basic test document
l1_data_provenance:
  - dataset_id: ds1
    name: Test Dataset
    description: Test data
    source: government
    collection_method: Survey
    date_range: '2024-2025'
    geographic_scope: Global
    inclusion_criteria:
      description: All participants
    exclusion_criteria: []
    cleaning_decisions: []
    synthetic_elements:
      present: false
    known_limitations:
      - Small sample
    access:
      public: true
    attested_by:
      - name: Data Manager
        role: data_steward
        date: '2026-01-01'
        statement: Data is accurate
"""


@pytest.fixture
def valid_orp_full():
    """Complete valid ORP-Full document."""
    return """
orp_version: '0.1'
document_id: test-full-001
title: Test Full Document
domain: policy
authors:
  - name: Test Author
    role: author
created: '2026-01-01'
last_modified: '2026-01-01'
status: draft
summary: A full test document
l1_data_provenance:
  - dataset_id: ds1
    name: Test Dataset
    description: Test data
    source: government
    collection_method: Survey
    date_range: '2024-2025'
    geographic_scope: Global
    inclusion_criteria:
      description: All participants
    exclusion_criteria: []
    cleaning_decisions: []
    synthetic_elements:
      present: false
    known_limitations:
      - Small sample
    access:
      public: true
    attested_by:
      - name: Data Manager
        role: data_steward
        date: '2026-01-01'
        statement: Data is accurate
l2_consequence_simulation:
  affected_population:
    description: General population
    size_estimate: '1000000'
  variables:
    independent:
      - variable: tax_rate
        description: Tax rate
        range: '0-50'
        default_value: '25'
    dependent:
      - variable: revenue
        description: Revenue
        unit: USD
  model:
    type: Linear
    assumptions:
      - assumption: Linear relationship
        basis: Historical data
        sensitivity: Low
  scenarios:
    - scenario_id: s1
      name: Baseline
      description: Current policy
      variable_values:
        tax_rate: '25'
      outcomes:
        revenue: '250000000'
  primary_scenario: s1
l3_empathy_mapping:
  stakeholder_map:
    - stakeholder: Taxpayers
      description: General taxpayers
      estimated_population: '1000000'
      relationship_to_proposal: Directly affected
      impacts_by_scenario:
        - scenario_id: s1
          direction: neutral
  minority_stress_test:
    description: Testing minorities
    groups_tested:
      - group: Low income
        scenario_tested: Baseline
        outcome: Neutral
        mitigation: None
  unresolved_impacts: []
  net_welfare_assessment:
    methodology: Cost-benefit
    conclusion: Net positive
    confidence: medium
    confidence_basis: Limited data
l4_accountability_ledger:
  entries:
    - entry_id: e1
      timestamp: '2026-01-01T10:00:00Z'
      decision_type: methodology
      description: Initial draft
      decided_by:
        - name: Author
          role: author
      basis: Research
l5_fork_registry:
  this_document:
    document_id: test-full-001
    fork_reason: original
    key_differences: []
  known_forks: []
  responses: []
"""


@pytest.fixture
def invalid_yaml():
    """Invalid YAML syntax."""
    return "invalid: yaml: [missing bracket"


@pytest.fixture
def yaml_array():
    """Valid YAML but not an object."""
    return """
- item1
- item2
- item3
"""


@pytest.fixture
def minimal_document():
    """Document with only orp_version."""
    return "orp_version: '0.1'"
