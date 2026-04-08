"""Command-line interface for ORP validator."""

import json
import sys
from pathlib import Path

import click

from orp_validator import ORPValidator, ValidationResult, __version__, validate


@click.command()
@click.argument("document", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--json",
    "output_json",
    is_flag=True,
    help="Output results in JSON format",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Show detailed validation trace",
)
@click.option(
    "--orp-version",
    "orp_version",
    type=click.Choice(["0.1", "0.2"], case_sensitive=False),
    help="ORP version to validate against (default: auto-detect from document)",
)
@click.version_option(version=__version__, prog_name="orp-validate")
def main(document: Path, output_json: bool, verbose: bool, orp_version: str | None) -> None:
    """Validate an OpenReason Protocol (ORP) document.

    DOCUMENT: Path to the ORP document to validate (YAML, JSON, or Markdown with YAML frontmatter)

    Examples:

        orp-validate my-proposal.yaml

        orp-validate examples/danish_property_tax_reform.md --verbose

        orp-validate my-proposal.yaml --json > validation-results.json

        orp-validate my-proposal.yaml --orp-version 0.2
    """
    try:
        if orp_version:
            # Use explicit version
            validator = ORPValidator(version=orp_version)
            result = validator.validate(document)
        else:
            # Auto-detect version from document
            result = validate(document)

        if output_json:
            # Machine-readable JSON output
            click.echo(json.dumps(result.to_dict(), indent=2))
        else:
            # Human-readable output
            _print_human_readable(document, result, verbose)

        # Exit with appropriate code
        sys.exit(0 if result.valid else 1)

    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(2)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(2)


def _print_human_readable(document: Path, result: ValidationResult, verbose: bool) -> None:
    """Print validation results in human-readable format."""

    # Header
    click.echo(f"\n{'='*60}")
    click.echo(f"ORP Validation Report: {document.name}")
    click.echo(f"{'='*60}\n")

    # Validity status
    if result.valid:
        click.secho("✓ Valid", fg="green", bold=True)
    else:
        click.secho("✗ Invalid", fg="red", bold=True)

    # Compliance level
    compliance_color = _get_compliance_color(result.compliance_level.value)
    click.echo("\nCompliance Level: ", nl=False)
    click.secho(result.compliance_level.value, fg=compliance_color, bold=True)

    # Layers present
    if verbose or not result.valid:
        click.echo("\nLayers Present:")
        for layer, present in result.layers_present.items():
            status = "✓" if present else "✗"
            color = "green" if present else "white"
            click.secho(f"  {status} {layer}", fg=color, dim=not present)

    # Errors
    if result.errors:
        click.echo(f"\n{click.style('Errors:', fg='red', bold=True)}")
        for i, error in enumerate(result.errors, 1):
            click.echo(f"  {i}. {error}")

    # Warnings
    if result.warnings:
        click.echo(f"\n{click.style('Warnings:', fg='yellow', bold=True)}")
        for i, warning in enumerate(result.warnings, 1):
            click.echo(f"  {i}. {warning}")

    # Summary
    if result.valid:
        click.echo(f"\n{click.style('Summary:', bold=True)}")
        click.echo(f"  Document is valid and meets {result.compliance_level.value} requirements.")
        if result.compliance_level.value != "ORP-Full":
            click.echo("  See warnings above for guidance on achieving higher compliance.")
    else:
        click.echo(f"\n{click.style('Summary:', bold=True)}")
        click.echo(f"  Document has {len(result.errors)} validation error(s).")
        click.echo("  Fix the errors above to achieve ORP compliance.")

    click.echo(f"\n{'='*60}\n")


def _get_compliance_color(compliance_level: str) -> str:
    """Get color for compliance level display."""
    colors = {
        "ORP-Full": "green",
        "ORP-Standard": "cyan",
        "ORP-Basic": "yellow",
        "ORP-PostHoc": "magenta",  # v0.2: Post-hoc reconstruction
        "Non-compliant": "red",
    }
    return colors.get(compliance_level, "white")


if __name__ == "__main__":
    main()
