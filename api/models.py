"""Pydantic models for API request/response schemas."""

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class ValidateRequest(BaseModel):
    """Request model for document validation."""

    document: str = Field(
        ...,
        description="ORP document as YAML or JSON string",
        min_length=1,
        max_length=1048576,  # 1MB limit
        example=(
            "orp_version: '0.1'\n"
            "document_id: my-policy-001\n"
            "title: Example Policy Proposal\n"
            "domain: policy\n"
            "authors:\n"
            "  - name: Jane Doe\n"
            "    role: author\n"
            "created: '2026-01-01'\n"
            "last_modified: '2026-01-15'\n"
            "status: draft\n"
            "summary: An example ORP document\n"
            "l1_data_provenance:\n"
            "  - dataset_id: ds1\n"
            "    name: Example Dataset\n"
            "    # ... additional L1 fields"
        ),
    )

    model_config = {"json_schema_extra": {"example": {"document": "orp_version: '0.1'\n..."}}}


class ValidateResponse(BaseModel):
    """Response model for document validation."""

    valid: bool = Field(..., description="Whether the document is valid")
    compliance_level: str = Field(..., description="Compliance level achieved")
    layers_present: Dict[str, bool] = Field(..., description="Which layers are present")
    errors: List[str] = Field(default_factory=list, description="Validation errors")
    warnings: List[str] = Field(default_factory=list, description="Validation warnings")
    metadata: Optional[Dict[str, str]] = Field(
        None, description="Document metadata (if valid)"
    )


class CheckRequest(BaseModel):
    """Request model for compliance check."""

    document: str = Field(
        ...,
        description="ORP document as YAML or JSON string",
        min_length=1,
        max_length=1048576,
    )


class CheckResponse(BaseModel):
    """Response model for compliance check."""

    compliance_level: str = Field(..., description="Compliance level achieved")
    layers_present: Dict[str, bool] = Field(..., description="Which layers are present")
    next_steps: Optional[str] = Field(None, description="Guidance for higher compliance")


class DiffRequest(BaseModel):
    """Request model for document comparison."""

    document1: str = Field(
        ..., description="First ORP document as YAML or JSON string", max_length=1048576
    )
    document2: str = Field(
        ..., description="Second ORP document as YAML or JSON string", max_length=1048576
    )
    include_metadata: bool = Field(
        False, description="Include metadata fields in diff (last_modified, etc.)"
    )
    layer: Optional[str] = Field(
        None, description="Compare specific layer only (e.g., 'l1_data_provenance')"
    )


class DiffChange(BaseModel):
    """Model for a single difference between documents."""

    type: str = Field(..., description="Type of change: added, removed, changed")
    field: str = Field(..., description="Field path (e.g., 'l1.datasets[0].name')")
    old_value: Optional[str] = Field(None, description="Old value (if changed/removed)")
    new_value: Optional[str] = Field(None, description="New value (if changed/added)")


class DiffResponse(BaseModel):
    """Response model for document comparison."""

    identical: bool = Field(..., description="Whether documents are identical")
    is_fork: bool = Field(..., description="Whether document2 is a fork of document1")
    fork_direction: Optional[str] = Field(None, description="Fork relationship description")
    differences: List[DiffChange] = Field(
        default_factory=list, description="List of differences"
    )
    num_changes: int = Field(..., description="Total number of changes")


class ErrorResponse(BaseModel):
    """Standard error response."""

    detail: str = Field(..., description="Error message")
    error_type: Optional[str] = Field(None, description="Type of error")
