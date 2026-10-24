"""Main CLI entry point for ORP commands."""

import click

from orp_validator import __version__
from orp_validator.commands import check, conform, diff, new, validate


@click.group()
@click.version_option(version=__version__, prog_name="orp")
def cli() -> None:
    """OpenReason Protocol (ORP) command-line tools.

    Create, validate, and work with ORP-compliant documents.

    \b
    Common commands:
      orp new <file>           Create a new ORP document
      orp validate <file>      Validate an existing document
      orp check <file>         Quick compliance level check
      orp diff <file1> <file2> Compare two documents
      orp conform              Run the v0.3 conformance suite

    For help on a specific command:
      orp <command> --help
    """
    pass


# Register commands
cli.add_command(new.new)
cli.add_command(validate.validate)
cli.add_command(check.check)
cli.add_command(diff.diff)
cli.add_command(conform.conform)


def main() -> None:
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
