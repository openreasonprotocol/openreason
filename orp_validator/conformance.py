"""ORP v0.3 conformance suite runner (RFC change C7 §9.2, R8).

An implementation claims conformance to the protocol by passing this suite. Three fixture families,
all bundled with the package so a `pip install`ed copy can self-check:

  * schema_cases   — per-profile positive/negative documents (ORP-Core/Policy/Ads/AI)
  * policy_cases   — usage_policy reference-evaluator decisions (RFC §5.5)
  * lineage_cases  — derivation-graph inheritance decisions (RFC §6.3)

`run()` returns a structured report; `tests/test_conformance.py` asserts zero failures so CI enforces it,
and `orp conform` prints it for a human claiming conformance.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Optional

if sys.version_info >= (3, 10):
    from importlib.resources import files
else:  # pragma: no cover
    try:
        from importlib_resources import files  # type: ignore
    except ImportError:
        files = None  # type: ignore

from . import lineage as _lineage
from . import usage as _usage
from .validator import ORPValidator

FIXTURE_DIR = "conformance"
FIXTURE_FILES = ("schema_cases.json", "policy_cases.json", "lineage_cases.json")


def load_fixture(name: str) -> dict[str, Any]:
    """Load a bundled conformance fixture (importlib.resources, filesystem fallback)."""
    if files is not None:
        return json.loads(files("orp_validator.schemas").joinpath(FIXTURE_DIR, name).read_text())
    with open(Path(__file__).parent / "schemas" / FIXTURE_DIR / name, encoding="utf-8") as f:
        return json.load(f)


def _run_schema_cases(validator: ORPValidator) -> list[dict[str, Any]]:
    out = []
    for c in load_fixture("schema_cases.json")["cases"]:
        res = validator.validate(dict(c["doc"]), profile=c.get("profile"))
        ok = res.valid == c["expect_valid"]
        if ok and not c["expect_valid"] and c.get("error_contains"):
            ok = any(c["error_contains"] in e for e in res.errors)
        out.append(
            {
                "suite": "schema",
                "name": c["name"],
                "passed": ok,
                "detail": "" if ok else f"valid={res.valid} errors={res.errors[:3]}",
            }
        )
    return out


def _run_policy_cases() -> list[dict[str, Any]]:
    out = []
    for c in load_fixture("policy_cases.json")["cases"]:
        d = _usage.evaluate_policy(c["policy"], c["context"])
        exp = c["expect"]
        ok = d.decision == exp["decision"]
        if ok and "permission_id" in exp:
            ok = d.permission_id == exp["permission_id"]
        if ok and "reason" in exp:
            ok = d.reason == exp["reason"]
        out.append(
            {
                "suite": "policy",
                "name": c["name"],
                "passed": ok,
                "detail": "" if ok else json.dumps(d.to_dict()),
            }
        )
    return out


def _run_lineage_cases() -> list[dict[str, Any]]:
    out = []
    for c in load_fixture("lineage_cases.json")["cases"]:
        registry = c.get("registry", {})
        res = _lineage.resolve_effective_decision(c["doc"], c["context"], fetch=registry.get)
        ok = res.decision == c["expect_decision"]
        if ok and c.get("denied_by") is not None:
            ok = res.denied_by == c["denied_by"]
        out.append(
            {
                "suite": "lineage",
                "name": c["name"],
                "passed": ok,
                "detail": "" if ok else json.dumps(res.to_dict()),
            }
        )
    return out


def run(profile: Optional[str] = None) -> dict[str, Any]:
    """Run the full conformance suite. `profile` filters the schema cases to one profile (policy/lineage
    suites always run — they are profile-independent)."""
    validator = ORPValidator()
    results: list[dict[str, Any]] = []
    schema = _run_schema_cases(validator)
    if profile:
        schema = [r for r in schema if _case_profile(r["name"]) in (None, profile)]
    results.extend(schema)
    results.extend(_run_policy_cases())
    results.extend(_run_lineage_cases())

    passed = sum(1 for r in results if r["passed"])
    failures = [r for r in results if not r["passed"]]
    return {
        "total": len(results),
        "passed": passed,
        "failed": len(failures),
        "conformant": len(failures) == 0,
        "results": results,
        "failures": failures,
    }


def _case_profile(
    _name: str,
) -> Optional[str]:  # placeholder hook for future per-profile filtering by name
    return None
