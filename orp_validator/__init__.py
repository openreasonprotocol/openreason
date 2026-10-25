"""OpenReason Protocol (ORP) Validator.

This package validates ORP v0.1, v0.2 and v0.3 documents, including profile selection,
trust-tier / compliance-level detection, cryptographic attestation (v0.3), and detailed errors.
"""

from orp_validator.validator import (
    ComplianceLevel,
    ORPValidator,
    TrustTier,
    ValidationResult,
    validate,
)

__version__ = "0.5.1"  # v0.3: attestation (R1) + profiles & trust tiers (R6/R7)
SUPPORTED_ORP_VERSIONS = ["0.1", "0.2", "0.3"]

__all__ = [
    "validate",
    "ORPValidator",
    "ValidationResult",
    "ComplianceLevel",
    "TrustTier",
    "__version__",
    "SUPPORTED_ORP_VERSIONS",
]
