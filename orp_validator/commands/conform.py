"""Conform command: run the ORP v0.3 conformance suite (RFC §9.2, R8).

An implementation claims conformance to the protocol by passing this suite. Exits 0 on full pass, 1 on
any failure, so it can gate CI or a release.
"""

from __future__ import annotations

import json as _json
import sys

import click

from orp_validator import conformance


@click.command()
@click.option("--json", "output_json", is_flag=True, help="Output the full report as JSON")
@click.option(
    "--profile",
    type=click.Choice(["ORP-Core", "ORP-Policy", "ORP-Ads", "ORP-AI"]),
    default=None,
    help="Filter the schema suite to one profile (policy + lineage suites always run)",
)
def conform(output_json: bool, profile: str | None) -> None:
    """Run the ORP v0.3 conformance suite (schema + usage-policy + lineage fixtures)."""
    report = conformance.run(profile=profile)

    if output_json:
        click.echo(_json.dumps(report, indent=2))
    else:
        click.echo(f"\nORP v0.3 conformance — {report['passed']}/{report['total']} passed")
        for r in report["results"]:
            mark = click.style("✓", fg="green") if r["passed"] else click.style("✗", fg="red")
            click.echo(f"  {mark} [{r['suite']}] {r['name']}")
            if not r["passed"] and r["detail"]:
                click.echo(f"      {r['detail']}")
        if report["conformant"]:
            click.secho("\nCONFORMANT", fg="green", bold=True)
        else:
            click.secho(f"\nNOT CONFORMANT — {report['failed']} failure(s)", fg="red", bold=True)

    sys.exit(0 if report["conformant"] else 1)
