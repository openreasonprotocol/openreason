"""API route handlers."""

import tempfile
from pathlib import Path
from typing import Dict

import yaml
from fastapi import APIRouter, HTTPException, status
from orp_validator import validate as validate_document

from models import (
    CheckRequest,
    CheckResponse,
    DiffRequest,
    DiffResponse,
    ValidateRequest,
    ValidateResponse,
)

router = APIRouter(prefix="/api/v1", tags=["validation"])


@router.post(
    "/validate",
    response_model=ValidateResponse,
    summary="Validate ORP document",
    description=(
        "Performs full JSON Schema validation of an ORP document. "
        "Returns detailed errors, warnings, and compliance level information."
    ),
    responses={
        200: {"description": "Validation completed (check 'valid' field for result)"},
        400: {"description": "Invalid request (malformed YAML/JSON)"},
        413: {"description": "Request too large (>1MB)"},
    },
)
async def validate(request: ValidateRequest) -> ValidateResponse:
    """Validate an ORP document with full schema validation.

    Args:
        request: Validation request containing document text

    Returns:
        Validation result with errors, warnings, and compliance level

    Raises:
        HTTPException: If document cannot be parsed
    """
    try:
        # Parse document to check if it's valid YAML/JSON
        try:
            doc_data = yaml.safe_load(request.document)
        except yaml.YAMLError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid YAML/JSON: {str(e)}",
            ) from e

        if not isinstance(doc_data, dict):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Document must be a YAML/JSON object (not array or scalar)",
            )

        # Write to temp file for validation
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
            yaml.dump(doc_data, f)
            temp_path = Path(f.name)

        try:
            # Validate using orp_validator
            result = validate_document(temp_path)

            # Extract metadata if valid
            metadata = None
            if result.valid and doc_data:
                metadata = {
                    "orp_version": doc_data.get("orp_version", "unknown"),
                    "document_id": doc_data.get("document_id", "unknown"),
                    "title": doc_data.get("title", "untitled"),
                    "domain": doc_data.get("domain", "unknown"),
                }

            return ValidateResponse(
                valid=result.valid,
                compliance_level=result.compliance_level.value,
                layers_present=result.layers_present,
                errors=result.errors,
                warnings=result.warnings,
                metadata=metadata,
            )
        finally:
            # Clean up temp file
            temp_path.unlink(missing_ok=True)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Validation error: {str(e)}",
        ) from e


@router.post(
    "/check",
    response_model=CheckResponse,
    summary="Quick compliance check",
    description=(
        "Quickly checks which ORP layers are present without full schema validation. "
        "Faster than /validate but doesn't check field validity."
    ),
    responses={
        200: {"description": "Compliance check completed"},
        400: {"description": "Invalid request (malformed YAML/JSON)"},
    },
)
async def check(request: CheckRequest) -> CheckResponse:
    """Quick compliance level check without full validation.

    Args:
        request: Check request containing document text

    Returns:
        Compliance level and next steps

    Raises:
        HTTPException: If document cannot be parsed
    """
    try:
        # Parse document
        try:
            doc_data = yaml.safe_load(request.document)
        except yaml.YAMLError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid YAML/JSON: {str(e)}",
            ) from e

        if not isinstance(doc_data, dict):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Document must be a YAML/JSON object",
            )

        # Detect layers
        layers_present = {
            "l1_data_provenance": "l1_data_provenance" in doc_data,
            "l2_consequence_simulation": "l2_consequence_simulation" in doc_data,
            "l3_empathy_mapping": "l3_empathy_mapping" in doc_data,
            "l4_accountability_ledger": "l4_accountability_ledger" in doc_data,
            "l5_fork_registry": "l5_fork_registry" in doc_data,
        }

        # Determine compliance level
        compliance_level = _determine_compliance(doc_data, layers_present)

        # Generate next steps guidance
        next_steps = _get_next_steps(compliance_level)

        return CheckResponse(
            compliance_level=compliance_level,
            layers_present=layers_present,
            next_steps=next_steps,
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Check error: {str(e)}",
        ) from e


def _determine_compliance(doc_data: Dict, layers_present: Dict[str, bool]) -> str:
    """Determine compliance level based on layers present."""
    # Check header
    required_header = [
        "orp_version",
        "document_id",
        "title",
        "domain",
        "authors",
        "created",
        "last_modified",
        "status",
        "summary",
    ]
    has_header = all(field in doc_data for field in required_header)

    if not has_header:
        return "Non-compliant"

    # Check compliance levels
    if all(
        [
            layers_present["l1_data_provenance"],
            layers_present["l2_consequence_simulation"],
            layers_present["l3_empathy_mapping"],
            layers_present["l4_accountability_ledger"],
            layers_present["l5_fork_registry"],
        ]
    ):
        return "ORP-Full"

    if all(
        [
            layers_present["l1_data_provenance"],
            layers_present["l2_consequence_simulation"],
            layers_present["l3_empathy_mapping"],
        ]
    ):
        return "ORP-Standard"

    if layers_present["l1_data_provenance"]:
        return "ORP-Basic"

    return "Non-compliant"


def _get_next_steps(compliance_level: str) -> str:
    """Get guidance for achieving higher compliance."""
    if compliance_level == "ORP-Basic":
        return "To reach ORP-Standard, add L2 (Consequence Simulation) and L3 (Empathy Mapping)"
    elif compliance_level == "ORP-Standard":
        return "To reach ORP-Full, add L4 (Accountability Ledger) and L5 (Fork Registry)"
    elif compliance_level == "ORP-Full":
        return "Full compliance achieved!"
    else:
        return "Add L1 (Data Provenance) to achieve ORP-Basic compliance"
