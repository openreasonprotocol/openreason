"""OpenReason Protocol (ORP) Validator.

This package provides validation for ORP v0.1 and v0.2 documents,
including compliance level detection and detailed error reporting.
"""

from orp_validator.validator import (
    ComplianceLevel,
    ORPValidator,
    ValidationResult,
    validate,
)

__version__ = "0.4.0"  # v0.2 support
SUPPORTED_ORP_VERSIONS = ["0.1", "0.2"]

__all__ = [
    "validate",
    "ORPValidator",
    "ValidationResult",
    "ComplianceLevel",
    "__version__",
    "SUPPORTED_ORP_VERSIONS",
]
