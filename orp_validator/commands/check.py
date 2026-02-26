"""Check command for quick compliance level assessment."""

import json
import sys
from pathlib import Path
from typing import Any

import click
import yaml

from orp_validator import ComplianceLevel


@click.command()
@click.argument("document", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--quiet",
    "-q",
    is_flag=True,
    help="Output only compliance level (no details)",
)
@click.option(
    "--json",
    "output_json",
    is_flag=True,
    help="Output in JSON format",
)
def check(document: Path, quiet: bool, output_json: bool) -> None:
    """Quick compliance level check without full validation.

    DOCUMENT: Path to the ORP document to check

    \b
    Exit codes:
      0 = ORP-Full
      1 = ORP-Standard
      2 = ORP-Basic
      3 = Non-compliant
      4 = Error

    \b
    Examples:
      orp check my-proposal.yaml
      orp check my-proposal.yaml --quiet
      orp check my-proposal.yaml --json
    """
    try:
        # Load document
        with open(document, encoding="utf-8") as f:
            if document.suffix in [".yaml", ".yml"]:
                doc_data = yaml.safe_load(f)
            else:
                doc_data = json.load(f)

        # Detect layers present
        layers_present = _detect_layers(doc_data)

        # Determine compliance level
        compliance_level = _determine_compliance(doc_data, layers_present)

        # Output
        if output_json:
            _output_json(compliance_level, layers_present)
        elif quiet:
            click.echo(compliance_level.value)
        else:
            _output_human_readable(document, compliance_level, layers_present)

        # Exit with appropriate code
        exit_codes = {
            ComplianceLevel.FULL: 0,
            ComplianceLevel.STANDARD: 1,
            ComplianceLevel.BASIC: 2,
            ComplianceLevel.NONE: 3,
        }
        sys.exit(exit_codes[compliance_level])

    except Exception as e:
        if not quiet:
            click.echo(f"Error: {e}", err=True)
        sys.exit(4)


def _detect_layers(doc_data: dict[str, Any]) -> dict[str, bool]:
    """Detect which ORP layers are present in the document."""
    return {
        "l1_data_provenance": "l1_data_provenance" in doc_data,
        "l2_consequence_simulation": "l2_consequence_simulation" in doc_data,
        "l3_empathy_mapping": "l3_empathy_mapping" in doc_data,
        "l4_accountability_ledger": "l4_accountability_ledger" in doc_data,
        "l5_fork_registry": "l5_fork_registry" in doc_data,
    }


def _determine_compliance(
    doc_data: dict[str, Any], layers_present: dict[str, bool]
) -> ComplianceLevel:
    """Determine compliance level based on layers present."""
    # Check required header fields
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


def _output_json(compliance_level: ComplianceLevel, layers_present: dict[str, bool]) -> None:
    """Output results in JSON format."""
    result = {
        "compliance_level": compliance_level.value,
        "layers_present": layers_present,
    }
    click.echo(json.dumps(result, indent=2))


def _output_human_readable(
    document: Path, compliance_level: ComplianceLevel, layers_present: dict[str, bool]
) -> None:
    """Output results in human-readable format."""
    # Compliance level with color
    colors = {
        ComplianceLevel.FULL: "green",
        ComplianceLevel.STANDARD: "cyan",
        ComplianceLevel.BASIC: "yellow",
        ComplianceLevel.NONE: "red",
    }
    color = colors.get(compliance_level, "white")

    click.echo(f"\nCompliance Check: {document.name}")
    click.echo("=" * 50)
    click.echo("\nCompliance Level: ", nl=False)
    click.secho(compliance_level.value, fg=color, bold=True)

    # Layer status
    click.echo("\nLayers:")
    layer_names = {
        "l1_data_provenance": "L1: Data Provenance",
        "l2_consequence_simulation": "L2: Consequence Simulation",
        "l3_empathy_mapping": "L3: Empathy Mapping",
        "l4_accountability_ledger": "L4: Accountability Ledger",
        "l5_fork_registry": "L5: Fork Registry",
    }

    for key, name in layer_names.items():
        present = layers_present[key]
        status = "✓" if present else "✗"
        status_color = "green" if present else "white"
        click.secho(f"  {status} {name}", fg=status_color, dim=not present)

    # Next steps
    if compliance_level == ComplianceLevel.BASIC:
        click.echo("\nTo reach ORP-Standard, add:")
        click.echo("  • L2: Consequence Simulation")
        click.echo("  • L3: Empathy Mapping")
    elif compliance_level == ComplianceLevel.STANDARD:
        click.echo("\nTo reach ORP-Full, add:")
        click.echo("  • L4: Accountability Ledger")
        click.echo("  • L5: Fork Registry")
    elif compliance_level == ComplianceLevel.FULL:
        click.secho("\n✓ Full compliance achieved!", fg="green")

    click.echo()
