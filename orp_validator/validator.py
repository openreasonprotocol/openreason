"""Core validation logic for ORP documents."""

import json
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

try:
    from importlib.resources import files  # Python 3.9+
except ImportError:
    from importlib_resources import files  # type: ignore

import yaml
from jsonschema import Draft7Validator, ValidationError as JSONSchemaValidationError


class ComplianceLevel(Enum):
    """ORP compliance levels."""

    BASIC = "ORP-Basic"
    STANDARD = "ORP-Standard"
    FULL = "ORP-Full"
    NONE = "Non-compliant"


@dataclass
class ValidationResult:
    """Result of ORP document validation.

    Attributes:
        valid: Whether the document is valid according to the schema
        compliance_level: Highest compliance level achieved
        errors: List of validation error messages
        warnings: List of validation warnings
        layers_present: Which layers (L1-L5) are present in the document
    """

    valid: bool
    compliance_level: ComplianceLevel
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    layers_present: Dict[str, bool] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "valid": self.valid,
            "compliance_level": self.compliance_level.value,
            "errors": self.errors,
            "warnings": self.warnings,
            "layers_present": self.layers_present,
        }


class ORPValidator:
    """Validator for OpenReason Protocol documents."""

    def __init__(self, schema_path: Optional[Path] = None) -> None:
        """Initialize validator with JSON Schema.

        Args:
            schema_path: Path to ORP JSON Schema file.
                        If None, uses bundled schema for ORP v0.1.
        """
        if schema_path is None:
            # Use bundled schema via importlib.resources
            schema_content = files("orp_validator.schemas").joinpath("orp-v0.1.schema.json").read_text()
            self.schema = json.loads(schema_content)
        else:
            with open(schema_path, "r", encoding="utf-8") as f:
                self.schema = json.load(f)

        self.validator = Draft7Validator(self.schema)

    def validate(self, document: Union[str, Path, Dict[str, Any]]) -> ValidationResult:
        """Validate an ORP document.

        Args:
            document: Either a file path (str/Path), or a dict containing the parsed document

        Returns:
            ValidationResult with validity status, compliance level, and errors

        Raises:
            FileNotFoundError: If document path doesn't exist
            yaml.YAMLError: If document is not valid YAML/JSON
        """
        # Load document if it's a file path
        if isinstance(document, (str, Path)):
            doc_data = self._load_document(Path(document))
        else:
            doc_data = document

        # Detect which layers are present
        layers_present = self._detect_layers(doc_data)

        # Validate against schema
        errors: List[str] = []
        warnings: List[str] = []

        # Run JSON Schema validation
        for error in self.validator.iter_errors(doc_data):
            errors.append(self._format_error(error))

        # Check compliance level
        compliance_level = self._determine_compliance(doc_data, layers_present)

        # Generate warnings
        warnings.extend(self._generate_warnings(doc_data, layers_present, compliance_level))

        return ValidationResult(
            valid=len(errors) == 0,
            compliance_level=compliance_level,
            errors=errors,
            warnings=warnings,
            layers_present=layers_present,
        )

    def _load_document(self, path: Path) -> Dict[str, Any]:
        """Load document from file path.

        Supports both YAML and JSON formats.
        For markdown files with YAML frontmatter, extracts the frontmatter.
        """
        if not path.exists():
            raise FileNotFoundError(f"Document not found: {path}")

        content = path.read_text(encoding="utf-8")

        # Handle markdown files with YAML frontmatter
        if path.suffix == ".md":
            content = self._extract_yaml_frontmatter(content)

        # Try YAML first (superset of JSON)
        try:
            return yaml.safe_load(content)
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Failed to parse document: {e}") from e

    def _extract_yaml_frontmatter(self, content: str) -> str:
        """Extract YAML frontmatter from markdown.

        Looks for content between ```yaml and ``` markers.
        """
        lines = content.split("\n")
        yaml_content: List[str] = []
        in_yaml = False

        for line in lines:
            if line.strip().startswith("```yaml"):
                in_yaml = True
                continue
            elif line.strip().startswith("```") and in_yaml:
                # Found closing marker, combine all YAML blocks
                if yaml_content:
                    break
            elif in_yaml:
                yaml_content.append(line)

        if not yaml_content:
            # No frontmatter found, return original content
            return content

        return "\n".join(yaml_content)

    def _detect_layers(self, doc_data: Dict[str, Any]) -> Dict[str, bool]:
        """Detect which ORP layers are present in the document."""
        return {
            "l1_data_provenance": "l1_data_provenance" in doc_data,
            "l2_consequence_simulation": "l2_consequence_simulation" in doc_data,
            "l3_empathy_mapping": "l3_empathy_mapping" in doc_data,
            "l4_accountability_ledger": "l4_accountability_ledger" in doc_data,
            "l5_fork_registry": "l5_fork_registry" in doc_data,
        }

    def _determine_compliance(
        self, doc_data: Dict[str, Any], layers_present: Dict[str, bool]
    ) -> ComplianceLevel:
        """Determine the highest compliance level achieved.

        ORP-Basic: Header + L1
        ORP-Standard: Header + L1 + L2 + L3
        ORP-Full: Header + L1 + L2 + L3 + L4 + L5
        """
        # Check required header fields
        required_header_fields = [
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
        has_header = all(field in doc_data for field in required_header_fields)

        if not has_header:
            return ComplianceLevel.NONE

        # Check compliance levels from highest to lowest
        if all(
            [
                layers_present["l1_data_provenance"],
                layers_present["l2_consequence_simulation"],
                layers_present["l3_empathy_mapping"],
                layers_present["l4_accountability_ledger"],
                layers_present["l5_fork_registry"],
            ]
        ):
            return ComplianceLevel.FULL

        if all(
            [
                layers_present["l1_data_provenance"],
                layers_present["l2_consequence_simulation"],
                layers_present["l3_empathy_mapping"],
            ]
        ):
            return ComplianceLevel.STANDARD

        if layers_present["l1_data_provenance"]:
            return ComplianceLevel.BASIC

        return ComplianceLevel.NONE

    def _generate_warnings(
        self,
        doc_data: Dict[str, Any],
        layers_present: Dict[str, bool],
        compliance_level: ComplianceLevel,
    ) -> List[str]:
        """Generate helpful warnings for document authors."""
        warnings: List[str] = []

        # Warn if declared compliance level doesn't match actual
        if "compliance_level" in doc_data:
            declared = doc_data["compliance_level"]
            if declared != compliance_level.value and compliance_level != ComplianceLevel.NONE:
                warnings.append(
                    f"Declared compliance level '{declared}' does not match "
                    f"detected level '{compliance_level.value}'"
                )

        # Warn about missing layers for higher compliance
        if compliance_level == ComplianceLevel.BASIC:
            warnings.append(
                "Document is ORP-Basic. Add L2 (Consequence Simulation) and "
                "L3 (Empathy Mapping) for ORP-Standard."
            )
        elif compliance_level == ComplianceLevel.STANDARD:
            warnings.append(
                "Document is ORP-Standard. Add L4 (Accountability Ledger) and "
                "L5 (Fork Registry) for ORP-Full."
            )

        return warnings

    def _format_error(self, error: JSONSchemaValidationError) -> str:
        """Format a JSON Schema validation error into a helpful message."""
        path = ".".join(str(p) for p in error.absolute_path) if error.absolute_path else "root"

        # Extract the most helpful error message
        if error.validator == "required":
            missing_field = error.message.split("'")[1]
            return f"Missing required field '{missing_field}' at {path}"
        elif error.validator == "type":
            expected_type = error.validator_value
            return f"Field '{path}' has wrong type (expected {expected_type})"
        elif error.validator == "enum":
            allowed = error.validator_value
            return f"Field '{path}' must be one of: {allowed}"
        elif error.validator == "minLength":
            return f"Field '{path}' is too short or empty"
        elif error.validator == "minItems":
            return f"Array '{path}' must have at least {error.validator_value} items"
        else:
            return f"Validation error at '{path}': {error.message}"


def validate(document: Union[str, Path, Dict[str, Any]]) -> ValidationResult:
    """Validate an ORP document.

    Convenience function that creates a validator and validates the document.

    Args:
        document: Either a file path (str/Path), or a dict containing the parsed document

    Returns:
        ValidationResult with validity status, compliance level, and errors

    Example:
        >>> result = validate("my-proposal.yaml")
        >>> if result.valid:
        ...     print(f"Valid! Compliance: {result.compliance_level.value}")
        ... else:
        ...     for error in result.errors:
        ...         print(f"Error: {error}")
    """
    validator = ORPValidator()
    return validator.validate(document)
