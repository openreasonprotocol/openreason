"""Diff command for comparing ORP documents."""

import json
import sys
from pathlib import Path
from typing import Any

import click
import yaml


@click.command()
@click.argument("file1", type=click.Path(exists=True, path_type=Path))
@click.argument("file2", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--layer",
    help="Compare specific layer only (e.g., l2, l3)",
)
@click.option(
    "--include-metadata",
    is_flag=True,
    help="Include metadata changes (last_modified, etc.)",
)
@click.option(
    "--json",
    "output_json",
    is_flag=True,
    help="Output in JSON format",
)
def diff(
    file1: Path,
    file2: Path,
    layer: str,
    include_metadata: bool,
    output_json: bool,
) -> None:
    """Compare two ORP documents and highlight differences.

    FILE1: First document (original)

    FILE2: Second document (comparison)

    \b
    Examples:
      orp diff original.yaml fork.yaml
      orp diff doc1.yaml doc2.yaml --layer l2
      orp diff old.yaml new.yaml --include-metadata
      orp diff doc1.yaml doc2.yaml --json
    """
    try:
        # Load documents
        doc1 = _load_document(file1)
        doc2 = _load_document(file2)

        # Check if it's a fork relationship
        is_fork = _is_fork(doc1, doc2)

        # Filter to specific layer if requested
        if layer:
            doc1 = {layer: doc1.get(layer, {})}
            doc2 = {layer: doc2.get(layer, {})}

        # Compute differences
        differences = _compute_diff(doc1, doc2, include_metadata)

        # Output
        if output_json:
            _output_json(file1, file2, is_fork, differences)
        else:
            _output_human_readable(file1, file2, is_fork, differences)

        # Exit code: 0 if identical, 1 if different
        sys.exit(0 if not differences else 1)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(2)


def _load_document(path: Path) -> dict[str, Any]:
    """Load document from file."""
    with open(path, encoding="utf-8") as f:
        if path.suffix in [".yaml", ".yml"]:
            return yaml.safe_load(f)  # type: ignore[no-any-return]
        else:
            return json.load(f)  # type: ignore[no-any-return]


def _is_fork(doc1: dict[str, Any], doc2: dict[str, Any]) -> bool:
    """Check if doc2 is a fork of doc1."""
    doc1_id = doc1.get("document_id")
    doc2_forked_from = doc2.get("forked_from")

    return doc2_forked_from == doc1_id


def _compute_diff(
    doc1: dict[str, Any], doc2: dict[str, Any], include_metadata: bool
) -> list[dict[str, Any]]:
    """Compute differences between two documents."""
    differences = []

    # Metadata fields to skip unless explicitly included
    metadata_fields = {"last_modified", "created"}

    # Compare all keys
    all_keys = set(doc1.keys()) | set(doc2.keys())

    for key in sorted(all_keys):
        if not include_metadata and key in metadata_fields:
            continue

        if key not in doc1:
            differences.append(
                {
                    "type": "added",
                    "field": key,
                    "value": doc2[key],
                }
            )
        elif key not in doc2:
            differences.append(
                {
                    "type": "removed",
                    "field": key,
                    "value": doc1[key],
                }
            )
        elif doc1[key] != doc2[key]:
            differences.append(
                {
                    "type": "changed",
                    "field": key,
                    "old_value": doc1[key],
                    "new_value": doc2[key],
                }
            )

    return differences


def _output_json(
    file1: Path, file2: Path, is_fork: bool, differences: list[dict[str, Any]]
) -> None:
    """Output diff in JSON format."""
    result = {
        "file1": str(file1),
        "file2": str(file2),
        "is_fork": is_fork,
        "differences": differences,
        "num_changes": len(differences),
    }
    click.echo(json.dumps(result, indent=2))


def _output_human_readable(
    file1: Path,
    file2: Path,
    is_fork: bool,
    differences: list[dict[str, Any]],
) -> None:
    """Output diff in human-readable format."""
    click.echo("\nComparing ORP Documents")
    click.echo("=" * 60)
    click.echo(f"\nFile 1: {file1}")
    click.echo(f"File 2: {file2}")

    if is_fork:
        click.secho("\n✓ File 2 is a fork of File 1", fg="cyan")

    if not differences:
        click.secho("\n✓ Documents are identical", fg="green")
        click.echo()
        return

    click.echo(f"\n{len(differences)} difference(s) found:\n")

    for diff in differences:
        if diff["type"] == "added":
            click.secho(f"+ Added: {diff['field']}", fg="green")
            _print_value("  ", diff["value"])

        elif diff["type"] == "removed":
            click.secho(f"- Removed: {diff['field']}", fg="red")
            _print_value("  ", diff["value"])

        elif diff["type"] == "changed":
            click.secho(f"~ Changed: {diff['field']}", fg="yellow")
            click.echo("  Old: ", nl=False)
            _print_value("  ", diff["old_value"], inline=True)
            click.echo("  New: ", nl=False)
            _print_value("  ", diff["new_value"], inline=True)

        click.echo()


def _print_value(indent: str, value: Any, inline: bool = False) -> None:
    """Print a value with appropriate formatting."""
    if isinstance(value, (dict, list)):
        # Complex value - print YAML representation
        yaml_str = yaml.dump(value, default_flow_style=False, sort_keys=False)
        if inline:
            # First line inline, rest indented
            lines = yaml_str.strip().split("\n")
            if len(lines) == 1:
                click.echo(lines[0])
            else:
                click.echo(lines[0])
                for line in lines[1:]:
                    click.echo(f"{indent}  {line}")
        else:
            for line in yaml_str.strip().split("\n"):
                click.echo(f"{indent}{line}")
    else:
        # Simple value
        if inline:
            click.echo(str(value))
        else:
            click.echo(f"{indent}{value}")
