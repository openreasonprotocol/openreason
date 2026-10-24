"""Drives the bundled ORP v0.3 conformance suite (R8). CI runs this, so a regression that breaks
conformance fails the pipeline."""

from pathlib import Path

from orp_validator import conformance, validate


def test_suite_is_conformant():
    report = conformance.run()
    assert report["conformant"], f"{report['failed']} failure(s): {report['failures']}"
    # sanity: all three suites contributed cases
    suites = {r["suite"] for r in report["results"]}
    assert suites == {"schema", "policy", "lineage"}
    assert report["total"] >= 20


def test_profile_filter_runs_policy_and_lineage_too():
    report = conformance.run(profile="ORP-Ads")
    suites = {r["suite"] for r in report["results"]}
    assert "policy" in suites and "lineage" in suites
    assert report["conformant"], report["failures"]


def test_shipped_v03_example_validates():
    example = (
        Path(__file__).resolve().parents[1] / "examples" / "data_product_ctv_segment.v0.3.yaml"
    )
    res = validate(str(example), profile="ORP-Ads")
    assert res.valid, res.errors
    assert res.profile == "ORP-Ads"
