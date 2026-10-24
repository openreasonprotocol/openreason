"""Core validation logic for ORP documents."""

import json
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Optional, Union

if sys.version_info >= (3, 10):
    from importlib.resources import files
else:
    # Python 3.9: use importlib_resources backport
    try:
        from importlib_resources import files  # type: ignore
    except ImportError:
        # Fallback if backport not installed
        files = None

import yaml
from jsonschema import Draft7Validator
from jsonschema import ValidationError as JSONSchemaValidationError


class ComplianceLevel(Enum):
    """ORP compliance levels (v0.1/v0.2). v0.3 renames these to trust tiers; see TrustTier."""

    BASIC = "ORP-Basic"
    STANDARD = "ORP-Standard"
    FULL = "ORP-Full"
    POSTHOC = "ORP-PostHoc"  # v0.2: Post-hoc reconstruction
    NONE = "Non-compliant"


class TrustTier(Enum):
    """ORP v0.3 trust tiers (RFC change C7). How much a reader can rely on a passport, and how it is verified.

    self_declared  Core fields present, platform/self signature  — verified by schema validation
    attested       Owner-key signature, named steward            — verified by signature verification
    verified       Independent accredited party signed the passport against the data — verifier signature
    full           verified + Layer-3 impact statement where the profile requires it
    posthoc        L1/L4 reconstructed, marked as such
    """

    SELF_DECLARED = "self_declared"
    ATTESTED = "attested"
    VERIFIED = "verified"
    FULL = "full"
    POSTHOC = "posthoc"
    NONE = "none"


# v0.3 profiles (RFC C6): declared `profile` value -> schema filename. ORP-Core is the default.
V03_PROFILE_SCHEMAS = {
    "ORP-Core": "orp-v0.3-core.schema.json",
    "ORP-Policy": "orp-v0.3-policy.schema.json",
    "ORP-Ads": "orp-v0.3-ads.schema.json",
    "ORP-AI": "orp-v0.3-ai.schema.json",
}

# Compliance-level -> trust-tier mapping (RFC C7 table), used for v0.1/v0.2 docs read under v0.3 vocabulary.
LEVEL_TO_TIER = {
    ComplianceLevel.BASIC: TrustTier.SELF_DECLARED,
    ComplianceLevel.STANDARD: TrustTier.ATTESTED,
    ComplianceLevel.FULL: TrustTier.FULL,
    ComplianceLevel.POSTHOC: TrustTier.POSTHOC,
    ComplianceLevel.NONE: TrustTier.NONE,
}


def load_accredited_verifiers() -> set:
    """Accredited-verifier key ids for the `verified`/`full` tier (RFC C7 §9.1). Maintained as a list in
    the repo (`schemas/accredited_verifiers.json`). Empty by default — until a verifier is accredited,
    no document reaches `verified`, which fails safe. Callers may override via `accredited_verifiers`.
    """
    try:
        if files is not None:
            data = json.loads(
                files("orp_validator.schemas").joinpath("accredited_verifiers.json").read_text()
            )
        else:
            with open(
                Path(__file__).parent / "schemas" / "accredited_verifiers.json", encoding="utf-8"
            ) as f:
                data = json.load(f)
        return {v["kid"] for v in data.get("verifiers", []) if v.get("kid")}
    except Exception:
        return set()


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
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    layers_present: dict[str, bool] = field(default_factory=dict)
    profile: Optional[str] = (
        None  # v0.3: the ORP profile validated against (ORP-Core/Policy/Ads/AI)
    )
    trust_tier: Optional["TrustTier"] = (
        None  # v0.3: trust tier (RFC C7); None for v0.1/v0.2-only callers
    )

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization. v0.3 keys are included only when set,
        so v0.1/v0.2 output is unchanged."""
        base = {
            "valid": self.valid,
            "compliance_level": self.compliance_level.value,
            "errors": self.errors,
            "warnings": self.warnings,
            "layers_present": self.layers_present,
        }
        if self.profile is not None:
            base["profile"] = self.profile
        if self.trust_tier is not None:
            base["trust_tier"] = self.trust_tier.value
        return base


class ORPValidator:
    """Validator for OpenReason Protocol documents."""

    def __init__(self, schema_path: Optional[Path] = None, version: str = "0.1") -> None:
        """Initialize validator with JSON Schema.

        Args:
            schema_path: Path to ORP JSON Schema file.
                        If None, uses bundled schema for specified version.
            version: ORP version to validate against ("0.1" or "0.2"). Default "0.1".
        """
        self.version = version
        self.extensions_loaded: list[str] = []

        if schema_path is None:
            # Use bundled schema via importlib.resources
            schema_filename = f"orp-v{version}.schema.json"
            if files is not None:
                schema_content = (
                    files("orp_validator.schemas").joinpath(schema_filename).read_text()
                )
                self.schema = json.loads(schema_content)
            else:
                # Fallback for when importlib.resources is not available
                schema_path = Path(__file__).parent / "schemas" / schema_filename
                with open(schema_path, encoding="utf-8") as f:
                    self.schema = json.load(f)
        else:
            with open(schema_path, encoding="utf-8") as f:
                self.schema = json.load(f)

        self.validator = Draft7Validator(self.schema)

    def _load_extensions(self, extension_names: list[str]) -> None:
        """Load extension schemas and note which extensions are declared.

        Args:
            extension_names: List of extension names (e.g., ["orp-ai-training-v1"])

        Note:
            For v0.2, extensions are primarily documentation
            (additionalProperties: true allows them).
            Future versions may enforce extension schema validation.
        """
        self.extensions_loaded = extension_names
        # TODO: In future, merge extension schemas into validator for strict validation
        # For now, just track which extensions are declared

    def validate(
        self,
        document: Union[str, Path, dict[str, Any]],
        profile: Optional[str] = None,
        resolve_key: Optional[Callable[[str], Any]] = None,
        accredited_verifiers: Optional[set] = None,
    ) -> ValidationResult:
        """Validate an ORP document.

        Args:
            document: Either a file path (str/Path), or a dict containing the parsed document
            profile: v0.3 only — force a profile (ORP-Core/ORP-Policy/ORP-Ads/ORP-AI). If None, the
                document's own `profile` field is used, defaulting to ORP-Core.
            resolve_key: v0.3 only — optional `kid -> key material` callable. When supplied and the
                document carries an `attestation` block, the signature is verified and the trust tier
                is raised accordingly. Without it, a v0.3 document tops out at `self_declared`.

        Returns:
            ValidationResult with validity, compliance level, and (for v0.3) profile + trust_tier.

        Raises:
            FileNotFoundError: If document path doesn't exist
            yaml.YAMLError: If document is not valid YAML/JSON
        """
        # Load document if it's a file path
        if isinstance(document, (str, Path)):
            doc_data = self._load_document(Path(document))
        else:
            doc_data = document

        doc_version = doc_data.get("orp_version", "0.1")

        # v0.3 takes the profile path (core + profile overlay, trust tiers). v0.1/v0.2 are unchanged.
        if doc_version == "0.3":
            return self._validate_v03(
                doc_data,
                profile=profile,
                resolve_key=resolve_key,
                accredited_verifiers=accredited_verifiers,
            )

        # Auto-detect document version if not explicitly set during validator init
        if doc_version != self.version:
            # Reload schema for correct version
            schema_filename = f"orp-v{doc_version}.schema.json"
            if files is not None:
                schema_content = (
                    files("orp_validator.schemas").joinpath(schema_filename).read_text()
                )
                self.schema = json.loads(schema_content)
            else:
                schema_path = Path(__file__).parent / "schemas" / schema_filename
                with open(schema_path, encoding="utf-8") as f:
                    self.schema = json.load(f)
            self.validator = Draft7Validator(self.schema)
            self.version = doc_version

        # Load extensions if declared (v0.2+)
        if "extensions" in doc_data:
            self._load_extensions(doc_data["extensions"])

        # Detect which layers are present
        layers_present = self._detect_layers(doc_data)

        # Validate against schema
        errors: list[str] = []
        warnings: list[str] = []

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

    # ------------------------------------------------------------------ v0.3 (profiles + trust tiers)

    def _schema_dict(self, filename: str) -> dict[str, Any]:
        """Load a bundled schema file as a dict (importlib.resources, with a filesystem fallback)."""
        if files is not None:
            return json.loads(files("orp_validator.schemas").joinpath(filename).read_text())
        with open(Path(__file__).parent / "schemas" / filename, encoding="utf-8") as f:
            return json.load(f)

    def _build_v03_validator(self, profile: str) -> Draft7Validator:
        """Build a Draft7 validator for a v0.3 profile, resolving cross-file $refs (core, v0.2 layer
        definitions, the attestation block) from an in-memory store so no network fetch happens."""
        import warnings as _warnings

        with _warnings.catch_warnings():
            # RefResolver is deprecated (jsonschema 4.18+) but still the simplest in-memory multi-schema
            # resolver and present in our pinned range. Isolated + silenced here; swap to `referencing` later.
            _warnings.simplefilter("ignore", DeprecationWarning)
            from jsonschema import RefResolver

        profile_schema = self._schema_dict(V03_PROFILE_SCHEMAS[profile])
        store = {}
        for fname in (
            "orp-v0.3-core.schema.json",
            "orp-v0.2.schema.json",
            "attestation.schema.json",
            "usage-policy.schema.json",
            "orp-v0.3-lineage.schema.json",
            "orp-v0.3-l1-ext.schema.json",
            V03_PROFILE_SCHEMAS[profile],
        ):
            s = self._schema_dict(fname)
            store[s["$id"]] = s
        resolver = RefResolver(base_uri=profile_schema["$id"], referrer=profile_schema, store=store)
        return Draft7Validator(profile_schema, resolver=resolver)

    def _validate_v03(
        self,
        doc_data: dict[str, Any],
        profile: Optional[str],
        resolve_key: Optional[Callable[[str], Any]],
        accredited_verifiers: Optional[set] = None,
    ) -> ValidationResult:
        self.version = "0.3"
        if "extensions" in doc_data:
            self._load_extensions(doc_data["extensions"])

        # Resolve the profile: explicit arg > document's own `profile` field > ORP-Core default.
        resolved_profile = profile or doc_data.get("profile") or "ORP-Core"
        errors: list[str] = []
        warnings: list[str] = []
        if resolved_profile not in V03_PROFILE_SCHEMAS:
            errors.append(
                f"Unknown profile '{resolved_profile}'. Known: {', '.join(V03_PROFILE_SCHEMAS)}"
            )
            resolved_profile = "ORP-Core"
        if profile and doc_data.get("profile") and doc_data["profile"] != profile:
            warnings.append(
                f"Validating as '{profile}' but document declares profile '{doc_data['profile']}'."
            )

        validator = self._build_v03_validator(resolved_profile)
        for error in validator.iter_errors(doc_data):
            errors.append(self._format_error(error))

        layers_present = self._detect_layers(doc_data)
        schema_valid = len(errors) == 0

        # Attestation / trust tier (RFC C7)
        tier, tier_warnings = self._determine_tier(
            doc_data, schema_valid, resolve_key, accredited_verifiers
        )
        warnings.extend(tier_warnings)

        # A compliance_level is still reported for backward-compatible output, derived from the tier.
        compliance_level = self._tier_to_level(tier)

        return ValidationResult(
            valid=schema_valid,
            compliance_level=compliance_level,
            errors=errors,
            warnings=warnings,
            layers_present=layers_present,
            profile=resolved_profile,
            trust_tier=tier,
        )

    def _determine_tier(
        self,
        doc_data: dict[str, Any],
        schema_valid: bool,
        resolve_key: Optional[Callable[[str], Any]],
        accredited_verifiers: Optional[set] = None,
    ) -> tuple[TrustTier, list[str]]:
        """Determine the v0.3 trust tier. Starts at self_declared; a verified attestation signature
        raises it to attested; a signature whose role is `verifier` AND whose `kid` is on the accredited
        list (and who is not the dataset's own owner) raises it to verified/full (RFC C7 §9.1)."""
        warnings: list[str] = []
        if not schema_valid:
            return TrustTier.NONE, warnings
        if doc_data.get("post_hoc"):
            return TrustTier.POSTHOC, warnings

        att = doc_data.get("attestation")
        if not isinstance(att, dict):
            return TrustTier.SELF_DECLARED, warnings

        # Claimed tier can never exceed what the signatures prove. Verify if we can.
        if resolve_key is None:
            warnings.append(
                "Document carries an attestation but no key resolver was supplied; "
                "tier capped at self_declared (signatures unverified)."
            )
            return TrustTier.SELF_DECLARED, warnings

        from . import attestation as att_mod

        if not att_mod.CRYPTO_AVAILABLE:
            warnings.append(
                "crypto_unavailable: install orp-validator[attestation] to verify signatures."
            )
            return TrustTier.SELF_DECLARED, warnings

        res = att_mod.verify_attestation(doc_data, resolve_key=resolve_key)
        if not res.valid:
            warnings.append(f"Attestation did not verify: {'; '.join(res.errors) or 'invalid'}")
            return TrustTier.SELF_DECLARED, warnings

        # At least one valid signature exists (res.valid) → attested floor.
        accredited = (
            accredited_verifiers
            if accredited_verifiers is not None
            else load_accredited_verifiers()
        )
        valid = [s for s in res.signatures if s.valid]
        owner_kids = {s.kid for s in valid if (s.role or "") != "verifier"}
        verifier = next((s for s in valid if (s.role or "") == "verifier"), None)

        if verifier:
            if verifier.kid not in accredited:
                warnings.append(
                    f"verifier signature {verifier.kid!r} is not on the accredited-verifier list; "
                    "tier capped at attested."
                )
            elif verifier.kid in owner_kids:
                warnings.append(
                    "a verifier cannot verify its own dataset (verifier key is also an owner signer); "
                    "tier capped at attested."
                )
            else:
                # full = verified + L3 present where the profile requires it (policy/impact statements)
                return (
                    TrustTier.FULL if "l3_empathy_mapping" in doc_data else TrustTier.VERIFIED
                ), warnings
        return TrustTier.ATTESTED, warnings

    @staticmethod
    def _tier_to_level(tier: TrustTier) -> ComplianceLevel:
        reverse = {
            TrustTier.SELF_DECLARED: ComplianceLevel.BASIC,
            TrustTier.ATTESTED: ComplianceLevel.STANDARD,
            TrustTier.VERIFIED: ComplianceLevel.FULL,
            TrustTier.FULL: ComplianceLevel.FULL,
            TrustTier.POSTHOC: ComplianceLevel.POSTHOC,
            TrustTier.NONE: ComplianceLevel.NONE,
        }
        return reverse.get(tier, ComplianceLevel.NONE)

    def _load_document(self, path: Path) -> dict[str, Any]:
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
            data = yaml.safe_load(content)

            # Ensure the loaded data is a dict (not a string, list, etc.)
            if not isinstance(data, dict):
                raise yaml.YAMLError(
                    f"Document must be a YAML/JSON object (dict), got {type(data).__name__}. "
                    "Markdown files must contain YAML frontmatter."
                )

            return data
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Failed to parse document: {e}") from e

    def _extract_yaml_frontmatter(self, content: str) -> str:
        """Extract YAML frontmatter from markdown.

        Looks for content between ```yaml and ``` markers.
        """
        lines = content.split("\n")
        yaml_content: list[str] = []
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

    def _detect_layers(self, doc_data: dict[str, Any]) -> dict[str, bool]:
        """Detect which ORP layers are present in the document."""
        return {
            "l1_data_provenance": "l1_data_provenance" in doc_data,
            "l2_consequence_simulation": "l2_consequence_simulation" in doc_data,
            "l3_empathy_mapping": "l3_empathy_mapping" in doc_data,
            "l4_accountability_ledger": "l4_accountability_ledger" in doc_data,
            "l5_fork_registry": "l5_fork_registry" in doc_data,
        }

    def _determine_compliance(
        self, doc_data: dict[str, Any], layers_present: dict[str, bool]
    ) -> ComplianceLevel:
        """Determine the highest compliance level achieved.

        ORP-Basic: Header + L1
        ORP-Standard: Header + L1 + L2 + L3
        ORP-Full: Header + L1 + L2 + L3 + L4 + L5
        ORP-PostHoc (v0.2+): Post-hoc reconstruction (any compliance level with post_hoc flag)
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

        # v0.2+: Check for post-hoc reconstruction flag
        is_post_hoc = doc_data.get("post_hoc", False)

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
            # v0.2+: If post-hoc flagged, return POSTHOC compliance level
            return ComplianceLevel.POSTHOC if is_post_hoc else ComplianceLevel.FULL

        if all(
            [
                layers_present["l1_data_provenance"],
                layers_present["l2_consequence_simulation"],
                layers_present["l3_empathy_mapping"],
            ]
        ):
            return ComplianceLevel.POSTHOC if is_post_hoc else ComplianceLevel.STANDARD

        if layers_present["l1_data_provenance"]:
            return ComplianceLevel.POSTHOC if is_post_hoc else ComplianceLevel.BASIC

        return ComplianceLevel.NONE

    def _generate_warnings(
        self,
        doc_data: dict[str, Any],
        layers_present: dict[str, bool],
        compliance_level: ComplianceLevel,
    ) -> list[str]:
        """Generate helpful warnings for document authors."""
        warnings: list[str] = []

        # Warn if declared compliance level doesn't match actual
        if "compliance_level" in doc_data:
            declared = doc_data["compliance_level"]
            if declared != compliance_level.value and compliance_level != ComplianceLevel.NONE:
                warnings.append(
                    f"Declared compliance level '{declared}' does not match "
                    f"detected level '{compliance_level.value}'"
                )

        # v0.2+: Warn if extensions declared but not used
        if self.version >= "0.2" and self.extensions_loaded:
            warnings.append(
                f"Extensions declared: {', '.join(self.extensions_loaded)}. "
                "Note: Extension validation is informational only in current version."
            )

        # v0.2+: Warn if post-hoc reconstruction lacks accountability_gap
        is_post_hoc = doc_data.get("post_hoc", False)
        if is_post_hoc and layers_present.get("l4_accountability_ledger"):
            l4_data = doc_data.get("l4_accountability_ledger", [])
            if isinstance(l4_data, list):
                has_accountability_gap = any(
                    "accountability_gap" in decision for decision in l4_data
                )
            else:
                has_accountability_gap = "accountability_gap" in l4_data

            if not has_accountability_gap:
                warnings.append(
                    "Post-hoc reconstruction should document 'accountability_gap' in L4 "
                    "to explain what decision-making history is unknowable."
                )

        # Warn about missing layers for higher compliance
        if compliance_level == ComplianceLevel.BASIC or compliance_level == ComplianceLevel.POSTHOC:
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


def validate(
    document: Union[str, Path, dict[str, Any]],
    profile: Optional[str] = None,
    resolve_key: Optional[Callable[[str], Any]] = None,
    accredited_verifiers: Optional[set] = None,
) -> ValidationResult:
    """Validate an ORP document.

    Convenience function that creates a validator and validates the document.

    Args:
        document: Either a file path (str/Path), or a dict containing the parsed document
        profile: v0.3 only — force a profile (ORP-Core/ORP-Policy/ORP-Ads/ORP-AI)
        resolve_key: v0.3 only — `kid -> key material` callable to verify attestations and raise the tier
        accredited_verifiers: v0.3 only — set of verifier kids accepted for the `verified`/`full` tier
            (defaults to the bundled accredited-verifier list)

    Returns:
        ValidationResult with validity status, compliance level, and (for v0.3) profile + trust_tier

    Example:
        >>> result = validate("my-proposal.yaml")
        >>> if result.valid:
        ...     print(f"Valid! Compliance: {result.compliance_level.value}")
        ... else:
        ...     for error in result.errors:
        ...         print(f"Error: {error}")
    """
    validator = ORPValidator()
    return validator.validate(
        document,
        profile=profile,
        resolve_key=resolve_key,
        accredited_verifiers=accredited_verifiers,
    )
