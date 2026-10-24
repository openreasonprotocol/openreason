"""Tests for ORP v0.3 lineage / derivation-graph enforcement (R4, RFC §6)."""

from orp_validator import lineage


def _allow(purpose, pid="p"):
    return {"policy_id": "pol:" + pid, "permissions": [{"permission_id": pid, "purpose": purpose}]}


def _node(doc_id, policy=None, parent=None, inherits="full", tier=None, **extra):
    d = {"document_id": doc_id}
    if policy is not None:
        d["usage_policy"] = policy
    if parent:
        d["lineage"] = {
            "derivations": [
                {"parent_id": parent, "transformation": "subset", "inherits": inherits, **extra}
            ]
        }
    if tier:
        d["attestation"] = {"tier": tier}
    return d


def test_intersection_denies_when_ancestor_denies():
    # leaf allows analytics; parent only allows measurement -> intersection denies analytics
    parent = _node("P", _allow("measurement"))
    leaf = _node("L", _allow("analytics"), parent="P")
    reg = {"P": parent}
    res = lineage.resolve_effective_decision(leaf, {"purpose": "analytics"}, fetch=reg.get)
    assert res.decision == "deny"
    assert res.denied_by == "P"


def test_intersection_allows_when_all_allow():
    parent = _node("P", _allow("analytics"))
    leaf = _node("L", _allow("analytics"), parent="P")
    reg = {"P": parent}
    res = lineage.resolve_effective_decision(leaf, {"purpose": "analytics"}, fetch=reg.get)
    assert res.allowed, res.to_dict()
    assert res.chain == ["L", "P"]


def test_trust_short_circuit_stops_at_verified_ancestor():
    # grandparent would deny, but parent is `verified` and vouches for everything above it
    grand = _node("G", _allow("measurement"))  # would deny analytics
    parent = _node("P", _allow("analytics"), parent="G", tier="verified")
    leaf = _node("L", _allow("analytics"), parent="P")
    reg = {"P": parent, "G": grand}
    res = lineage.resolve_effective_decision(leaf, {"purpose": "analytics"}, fetch=reg.get)
    assert res.allowed, res.to_dict()
    assert res.truncated_at_verified
    assert "G" not in res.chain  # grandparent never consulted


def test_licensed_relaxation_uses_derivative_policy():
    # parent prohibits model_training in its usage_policy, but grants a licensed permission p-lic and
    # publishes a derivative_policy that permits model_training; the relaxed edge honours it.
    parent = {
        "document_id": "P",
        "usage_policy": {
            "policy_id": "pol:P",
            "permissions": [
                {"permission_id": "p-lic", "purpose": "model_training", "derivation": "licensed"}
            ],
            "prohibitions": [{"purpose": "model_training"}],
        },
        "derivative_policy": {
            "policy_id": "pol:P:deriv",
            "permissions": [{"permission_id": "d1", "purpose": "model_training"}],
        },
    }
    leaf = _node(
        "L", _allow("model_training"), parent="P", inherits="relaxed", relaxation_basis="p-lic"
    )
    reg = {"P": parent}
    res = lineage.resolve_effective_decision(leaf, {"purpose": "model_training"}, fetch=reg.get)
    assert res.allowed, res.to_dict()


def test_relaxed_without_legitimate_basis_falls_back_to_usage_policy():
    # edge claims relaxed but the named permission does not grant licensed -> enforce the full usage_policy
    parent = {
        "document_id": "P",
        "usage_policy": {
            "policy_id": "pol:P",
            "permissions": [
                {"permission_id": "p-lic", "purpose": "model_training", "derivation": "internal"}
            ],
            "prohibitions": [{"purpose": "model_training"}],
        },
        "derivative_policy": {"policy_id": "d", "permissions": [{"purpose": "model_training"}]},
    }
    leaf = _node(
        "L", _allow("model_training"), parent="P", inherits="relaxed", relaxation_basis="p-lic"
    )
    reg = {"P": parent}
    res = lineage.resolve_effective_decision(leaf, {"purpose": "model_training"}, fetch=reg.get)
    assert res.decision == "deny"  # prohibition in the full usage_policy bites


def test_unresolved_ancestor_fails_closed():
    leaf = _node("L", _allow("analytics"), parent="MISSING")
    res = lineage.resolve_effective_decision(leaf, {"purpose": "analytics"}, fetch=lambda _id: None)
    assert res.decision == "deny"
    assert res.reason == "unresolved_ancestor"


def test_multi_parent_dag_denies_if_any_branch_denies():
    # L derives from BOTH P1 (allows analytics) and P2 (only allows measurement) -> intersection denies
    p1 = _node("P1", _allow("analytics"))
    p2 = _node("P2", _allow("measurement"))
    leaf = {
        "document_id": "L",
        "usage_policy": _allow("analytics"),
        "lineage": {
            "derivations": [
                {"parent_id": "P1", "transformation": "overlap", "inherits": "full"},
                {"parent_id": "P2", "transformation": "overlap", "inherits": "full"},
            ]
        },
    }
    reg = {"P1": p1, "P2": p2}
    res = lineage.resolve_effective_decision(leaf, {"purpose": "analytics"}, fetch=reg.get)
    assert res.decision == "deny"
    assert res.denied_by == "P2"


def test_multi_parent_dag_allows_if_all_branches_allow():
    reg = {"P1": _node("P1", _allow("analytics")), "P2": _node("P2", _allow("analytics"))}
    leaf = {
        "document_id": "L",
        "usage_policy": _allow("analytics"),
        "lineage": {
            "derivations": [
                {"parent_id": "P1", "transformation": "overlap", "inherits": "full"},
                {"parent_id": "P2", "transformation": "overlap", "inherits": "full"},
            ]
        },
    }
    res = lineage.resolve_effective_decision(leaf, {"purpose": "analytics"}, fetch=reg.get)
    assert res.allowed, res.to_dict()
    assert set(res.chain) == {"L", "P1", "P2"}


def test_cycle_is_bounded():
    a = _node("A", _allow("analytics"), parent="B")
    b = _node("B", _allow("analytics"), parent="A")
    reg = {"A": a, "B": b}
    res = lineage.resolve_effective_decision(a, {"purpose": "analytics"}, fetch=reg.get)
    # cycle guard halts the walk; both allow -> allow, and A appears once
    assert res.allowed
    assert res.chain.count("A") == 1
