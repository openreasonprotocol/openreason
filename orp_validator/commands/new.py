"""New command for creating ORP documents."""

import sys
from datetime import date
from pathlib import Path
from typing import Any, Optional

try:
    from importlib.resources import files  # Python 3.9+
except ImportError:
    from importlib_resources import files  # type: ignore

import click
import yaml

from orp_validator import validate as validate_document


@click.command()
@click.argument("filename", type=click.Path(path_type=Path))
@click.option(
    "--compliance",
    type=click.Choice(["basic", "standard", "full"], case_sensitive=False),
    default="basic",
    help="Compliance level (default: basic)",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["yaml", "json"], case_sensitive=False),
    default="yaml",
    help="Output format (default: yaml)",
)
@click.option(
    "--title",
    help="Document title (interactive if not provided)",
)
@click.option(
    "--domain",
    type=click.Choice(["policy", "ai-training", "governance", "other"], case_sensitive=False),
    help="Document domain (interactive if not provided)",
)
@click.option(
    "--author",
    help="Author name (interactive if not provided)",
)
@click.option(
    "--non-interactive",
    is_flag=True,
    help="Non-interactive mode (requires all fields via flags)",
)
@click.option(
    "--from-template",
    type=click.Path(exists=True, path_type=Path),
    help="Use custom template file",
)
def new(
    filename: Path,
    compliance: str,
    output_format: str,
    title: Optional[str],
    domain: Optional[str],
    author: Optional[str],
    non_interactive: bool,
    from_template: Optional[Path],
) -> None:
    """Create a new ORP document with interactive scaffolding.

    FILENAME: Path where the new document will be created

    \b
    Examples:
      orp new my-proposal.yaml
      orp new my-proposal.yaml --compliance standard
      orp new doc.json --format json --title "My Policy" --domain policy \\
          --author "John Doe" --non-interactive
    """
    # Check if file already exists
    if filename.exists():
        if not click.confirm(f"File {filename} already exists. Overwrite?"):
            click.echo("Aborted.")
            sys.exit(0)

    # Load template
    if from_template:
        template = _load_custom_template(from_template)
    else:
        template = _load_builtin_template(compliance)

    # Gather information (interactive or from flags)
    if non_interactive:
        if not all([title, domain, author]):
            click.echo(
                "Error: In non-interactive mode, --title, --domain, and --author are required.",
                err=True,
            )
            sys.exit(1)
        # Type narrowing: all() check ensures these are not None
        assert title is not None
        assert domain is not None
        assert author is not None
        doc_info = {
            "title": title,
            "domain": domain.lower(),
            "author": author,
        }
    else:
        doc_info = _gather_info_interactive(title, domain, author)

    # Populate template
    document = _populate_template(template, doc_info, filename)

    # Write to file
    _write_document(filename, document, output_format)

    # Validate
    click.echo(f"\n✓ Created {filename}")
    click.echo(f"  Compliance level: ORP-{compliance.capitalize()}")

    # Quick validation check
    try:
        result = validate_document(filename)
        if result.valid:
            click.secho("  Validation: ✓ Valid", fg="green")
        else:
            click.secho(f"  Validation: ✗ Invalid ({len(result.errors)} errors)", fg="yellow")
            click.echo(f"\n  Run 'orp validate {filename}' for details.")
    except Exception:
        click.echo(f"  Run 'orp validate {filename}' to check validity.")

    click.echo("\nNext steps:")
    click.echo(f"  1. Edit {filename} and fill in the placeholders")
    click.echo(f"  2. Run 'orp validate {filename}' to check for errors")
    click.echo(f"  3. Run 'orp check {filename}' for quick compliance check")


def _load_builtin_template(compliance: str) -> dict[str, Any]:
    """Load built-in template for specified compliance level."""
    try:
        template_content = (
            files("orp_validator.templates").joinpath(f"orp-{compliance}.yaml").read_text()
        )
        return yaml.safe_load(template_content)  # type: ignore[no-any-return]
    except FileNotFoundError:
        click.echo(f"Error: Template orp-{compliance}.yaml not found", err=True)
        sys.exit(1)


def _load_custom_template(template_path: Path) -> dict[str, Any]:
    """Load custom template from file."""
    with open(template_path, encoding="utf-8") as f:
        return yaml.safe_load(f)  # type: ignore[no-any-return]


def _gather_info_interactive(
    title: Optional[str], domain: Optional[str], author: Optional[str]
) -> dict[str, str]:
    """Gather document information interactively."""
    click.echo("\nCreating new ORP document. Please provide the following information:\n")

    # Title
    if not title:
        title = click.prompt("Document title", type=str)

    # Domain
    if not domain:
        domain = click.prompt(
            "Domain",
            type=click.Choice(
                ["policy", "ai-training", "governance", "other"], case_sensitive=False
            ),
            default="policy",
        )

    # Author
    if not author:
        author = click.prompt("Your name (author)", type=str)

    return {
        "title": title,
        "domain": domain.lower(),
        "author": author,
    }


def _populate_template(
    template: dict[str, Any], info: dict[str, str], filename: Path
) -> dict[str, Any]:
    """Populate template with user information."""
    # Generate document ID from filename
    doc_id = filename.stem.replace(" ", "-").replace("_", "-").lower()

    # Update header fields
    template["document_id"] = f"{doc_id}-001"
    template["title"] = info["title"]
    template["domain"] = info["domain"]
    template["created"] = str(date.today())
    template["last_modified"] = str(date.today())

    # Update author
    if "authors" in template and len(template["authors"]) > 0:
        template["authors"][0]["name"] = info["author"]

    # Update attestation if present (L1)
    if "l1_data_provenance" in template:
        for dataset in template["l1_data_provenance"]:
            if "attested_by" in dataset and len(dataset["attested_by"]) > 0:
                dataset["attested_by"][0]["name"] = info["author"]
                dataset["attested_by"][0]["date"] = str(date.today())

    return template


def _write_document(filename: Path, document: dict[str, Any], output_format: str) -> None:
    """Write document to file in specified format."""
    if output_format == "yaml":
        with open(filename, "w", encoding="utf-8") as f:
            yaml.dump(document, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    else:  # json
        import json

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(document, f, indent=2, ensure_ascii=False)
