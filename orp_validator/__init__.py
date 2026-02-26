"""OpenReason Protocol (ORP) Validator.

This package provides validation for ORP v0.1 documents,
including compliance level detection and detailed error reporting.
"""

__version__ = "0.3.0"
SUPPORTED_ORP_VERSIONS = ["0.1"]

from orp_validator.validator import validate, ValidationResult, ComplianceLevel

__all__ = ["validate", "ValidationResult", "ComplianceLevel", "__version__", "SUPPORTED_ORP_VERSIONS"]
