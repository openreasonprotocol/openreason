"""API route handlers."""

import tempfile
from pathlib import Path
from typing import Any, Dict, List

import yaml
from fastapi import APIRouter, HTTPException, Request, status
from orp_validator import validate as validate_document
from slowapi import Limiter
from slowapi.util import get_remote_address

from models import (
    CheckRequest,
    CheckResponse,
    DiffChange,
    DiffRequest,
    DiffResponse,
    ValidateRequest,
    ValidateResponse,
)

# Rate limiter
limiter = Limiter(key_func=get_remote_address)

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
        429: {"description": "Too many requests - rate limit exceeded"},
    },
)
@limiter.limit("60/minute")
async def validate(body: ValidateRequest, request: Request) -> ValidateResponse:
    """Validate an ORP document with full schema validation.

    Args:
        body: Validation request containing document text

    Returns:
        Validation result with errors, warnings, and compliance level

    Raises:
        HTTPException: If document cannot be parsed
    """
    try:
        # Parse document to check if it's valid YAML/JSON
        try:
            doc_data = yaml.safe_load(body.document)
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
        429: {"description": "Too many requests - rate limit exceeded"},
    },
)
@limiter.limit("60/minute")
async def check(body: CheckRequest, request: Request) -> CheckResponse:
    """Quick compliance level check without full validation.

    Args:
        body: Check request containing document text

    Returns:
        Compliance level and next steps

    Raises:
        HTTPException: If document cannot be parsed
    """
    try:
        # Parse document
        try:
            doc_data = yaml.safe_load(body.document)
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


@router.post(
    "/diff",
    response_model=DiffResponse,
    summary="Compare two ORP documents",
    description=(
        "Compares two ORP documents and returns their differences. "
        "Can detect fork relationships and filter by specific layers."
    ),
    responses={
        200: {"description": "Comparison completed"},
        400: {"description": "Invalid request (malformed documents)"},
        429: {"description": "Too many requests - rate limit exceeded"},
    },
)
@limiter.limit("60/minute")
async def diff(body: DiffRequest, request: Request) -> DiffResponse:
    """Compare two ORP documents.

    Args:
        body: Diff request containing two documents

    Returns:
        Comparison result with differences and fork detection

    Raises:
        HTTPException: If documents cannot be parsed
    """
    try:
        # Parse both documents
        try:
            doc1 = yaml.safe_load(body.document1)
            doc2 = yaml.safe_load(body.document2)
        except yaml.YAMLError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid YAML/JSON: {str(e)}",
            ) from e

        if not isinstance(doc1, dict) or not isinstance(doc2, dict):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Both documents must be YAML/JSON objects",
            )

        # Filter out metadata fields if requested
        if not body.include_metadata:
            metadata_fields = ["last_modified", "created"]
            for field in metadata_fields:
                doc1.pop(field, None)
                doc2.pop(field, None)

        # Filter to specific layer if requested
        if body.layer:
            if body.layer not in doc1 and body.layer not in doc2:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Layer '{body.layer}' not found in either document",
                )
            doc1 = {body.layer: doc1.get(body.layer)}
            doc2 = {body.layer: doc2.get(body.layer)}

        # Detect fork relationship
        is_fork = False
        fork_direction = None
        if "forked_from" in doc2:
            forked_from_id = doc2.get("forked_from")
            if doc1.get("document_id") == forked_from_id:
                is_fork = True
                fork_direction = "document2 forked from document1"
        elif "forked_from" in doc1:
            forked_from_id = doc1.get("forked_from")
            if doc2.get("document_id") == forked_from_id:
                is_fork = True
                fork_direction = "document1 forked from document2"

        # Compare documents
        differences = _compare_dicts(doc1, doc2, prefix="")

        return DiffResponse(
            identical=len(differences) == 0,
            is_fork=is_fork,
            fork_direction=fork_direction,
            differences=differences,
            num_changes=len(differences),
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Diff error: {str(e)}",
        ) from e


def _compare_dicts(
    dict1: Dict[str, Any], dict2: Dict[str, Any], prefix: str = ""
) -> List[DiffChange]:
    """Recursively compare two dictionaries and return differences.

    Args:
        dict1: First dictionary
        dict2: Second dictionary
        prefix: Field path prefix for nested fields

    Returns:
        List of differences
    """
    differences: List[DiffChange] = []

    # Find keys in dict1 but not dict2 (removed)
    for key in dict1:
        if key not in dict2:
            field_path = f"{prefix}.{key}" if prefix else key
            differences.append(
                DiffChange(
                    type="removed",
                    field=field_path,
                    old_value=_serialize_value(dict1[key]),
                    new_value=None,
                )
            )

    # Find keys in dict2 but not dict1 (added)
    for key in dict2:
        if key not in dict1:
            field_path = f"{prefix}.{key}" if prefix else key
            differences.append(
                DiffChange(
                    type="added",
                    field=field_path,
                    old_value=None,
                    new_value=_serialize_value(dict2[key]),
                )
            )

    # Compare values for common keys
    for key in dict1:
        if key not in dict2:
            continue

        field_path = f"{prefix}.{key}" if prefix else key
        val1 = dict1[key]
        val2 = dict2[key]

        # If both are dicts, recurse
        if isinstance(val1, dict) and isinstance(val2, dict):
            differences.extend(_compare_dicts(val1, val2, field_path))
        # If both are lists, compare element by element
        elif isinstance(val1, list) and isinstance(val2, list):
            differences.extend(_compare_lists(val1, val2, field_path))
        # Otherwise compare values directly
        elif val1 != val2:
            differences.append(
                DiffChange(
                    type="changed",
                    field=field_path,
                    old_value=_serialize_value(val1),
                    new_value=_serialize_value(val2),
                )
            )

    return differences


def _compare_lists(
    list1: List[Any], list2: List[Any], prefix: str
) -> List[DiffChange]:
    """Compare two lists element by element.

    Args:
        list1: First list
        list2: Second list
        prefix: Field path prefix

    Returns:
        List of differences
    """
    differences: List[DiffChange] = []

    max_len = max(len(list1), len(list2))

    for i in range(max_len):
        field_path = f"{prefix}[{i}]"

        # Element only in list1 (removed)
        if i >= len(list2):
            differences.append(
                DiffChange(
                    type="removed",
                    field=field_path,
                    old_value=_serialize_value(list1[i]),
                    new_value=None,
                )
            )
        # Element only in list2 (added)
        elif i >= len(list1):
            differences.append(
                DiffChange(
                    type="added",
                    field=field_path,
                    old_value=None,
                    new_value=_serialize_value(list2[i]),
                )
            )
        # Both have element at index i
        else:
            val1 = list1[i]
            val2 = list2[i]

            # If both are dicts, recurse
            if isinstance(val1, dict) and isinstance(val2, dict):
                differences.extend(_compare_dicts(val1, val2, field_path))
            # If both are lists, recurse
            elif isinstance(val1, list) and isinstance(val2, list):
                differences.extend(_compare_lists(val1, val2, field_path))
            # Otherwise compare directly
            elif val1 != val2:
                differences.append(
                    DiffChange(
                        type="changed",
                        field=field_path,
                        old_value=_serialize_value(val1),
                        new_value=_serialize_value(val2),
                    )
                )

    return differences


def _serialize_value(value: Any) -> str:
    """Serialize a value to string for display.

    Args:
        value: Value to serialize

    Returns:
        String representation
    """
    if isinstance(value, (dict, list)):
        return yaml.dump(value, default_flow_style=True).strip()
    return str(value)
