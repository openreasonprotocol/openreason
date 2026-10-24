"""ORP v0.3 Layer 5 as a derivation graph (RFC change C4, R4).

v0.2's Layer 5 tracked *forks* of a document (alternative reasoning). Data products are also *derived*
from other data products (a subset, an overlap, a lookalike, a model trained on a corpus), and each
derivative must carry its ancestors' usage constraints. That is a different relationship, modelled here.

Enforcement (RFC §6.3): a derivative's effective policy is the INTERSECTION of its own usage_policy and
every ancestor's — an activation is allowed only if every policy in the whole ancestry allows it —
UNLESS an ancestor granted `derivation: licensed` with a `derivative_policy` that relaxes a named
constraint, in which case that ancestor is enforced via its derivative_policy. The walk descends every
`derivations` edge (a true DAG, not just a single parent), to the root or to the nearest ancestor whose
attestation tier is `verified`+ (that ancestor vouches for everything above it), whichever comes first.

Pure + offline. Fetching an ancestor document is the caller's job (`fetch(parent_id) -> doc | None`).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from .usage import evaluate_policy

VOUCHING_TIERS = frozenset({"verified", "full"})
DEFAULT_MAX_DEPTH = 32


@dataclass
class LineageResult:
    decision: str  # "allow" | "deny"
    reason: str = ""
    denied_by: str | None = None
    chain: list[str] = field(default_factory=list)  # node ids visited, DFS order
    truncated_at_verified: bool = False

    @property
    def allowed(self) -> bool:
        return self.decision == "allow"

    def to_dict(self) -> dict[str, Any]:
        return {
            "decision": self.decision,
            "reason": self.reason,
            "denied_by": self.denied_by,
            "chain": self.chain,
            "truncated_at_verified": self.truncated_at_verified,
        }


def _claimed_tier(doc: dict[str, Any]) -> str | None:
    att = doc.get("attestation")
    return att.get("tier") if isinstance(att, dict) else None


def _node_id(doc: dict[str, Any], fallback: str) -> str:
    return str(doc.get("document_id") or doc.get("dataset_id") or fallback)


def _derivations(doc: dict[str, Any]) -> list[dict[str, Any]]:
    lin = doc.get("lineage")
    return (lin.get("derivations") or []) if isinstance(lin, dict) else []


def _policy_for_node(
    node: dict[str, Any], inbound_edge: dict[str, Any] | None
) -> tuple[dict[str, Any] | None, str]:
    """Which policy enforces at this node: its usage_policy, or — when the inbound edge legitimately
    relaxed it under a licensed grant — its derivative_policy (RFC §5.4)."""
    if (
        inbound_edge
        and inbound_edge.get("inherits") == "relaxed"
        and _relaxation_is_legitimate(node, inbound_edge)
    ):
        dp = node.get("derivative_policy")
        if isinstance(dp, dict):
            return dp, "derivative_policy"
        # relaxed claimed but no derivative_policy to back it → fail safe to the full usage_policy
    up = node.get("usage_policy")
    return (up if isinstance(up, dict) else None), (
        "usage_policy" if isinstance(up, dict) else "none"
    )


def _relaxation_is_legitimate(ancestor: dict[str, Any], edge: dict[str, Any]) -> bool:
    basis = edge.get("relaxation_basis")
    up = ancestor.get("usage_policy")
    if not basis or not isinstance(up, dict):
        return False
    for perm in up.get("permissions", []) or []:
        if (perm.get("permission_id") or perm.get("id")) == basis and perm.get(
            "derivation"
        ) == "licensed":
            return True
    return False


def resolve_effective_decision(
    doc: dict[str, Any],
    context: dict[str, Any],
    fetch: Callable[[str], dict[str, Any] | None],
    max_depth: int = DEFAULT_MAX_DEPTH,
) -> LineageResult:
    """Evaluate `context` against `doc` AND its entire derivation ancestry (DAG intersection, RFC §6.3)."""
    visited: list[str] = []
    seen: set[str] = set()
    state = {"truncated": False}

    def walk(
        node: dict[str, Any], inbound_edge: dict[str, Any] | None, depth: int
    ) -> LineageResult | None:
        nid = _node_id(node, f"node{len(visited)}")
        if nid in seen:
            return None  # cycle / diamond: already constrained on another path
        if depth > max_depth:
            return LineageResult("deny", reason="max_depth_exceeded", denied_by=nid)
        seen.add(nid)
        visited.append(nid)

        policy, _src = _policy_for_node(node, inbound_edge)
        if not policy:
            return LineageResult("deny", reason="node_without_usage_policy", denied_by=nid)
        d = evaluate_policy(policy, context)
        if not d.allowed:
            return LineageResult("deny", reason=f"{d.reason}@{nid}", denied_by=nid)

        # Trust short-circuit: a verified/full ANCESTOR (not the leaf) vouches for everything above it.
        if inbound_edge is not None and _claimed_tier(node) in VOUCHING_TIERS:
            state["truncated"] = True
            return None

        for edge in _derivations(node):
            pid = edge.get("parent_id")
            if not pid:
                continue
            parent = fetch(pid)
            if parent is None:
                visited.append(str(pid))
                return LineageResult("deny", reason="unresolved_ancestor", denied_by=str(pid))
            denial = walk(parent, edge, depth + 1)
            if denial is not None:
                return denial
        return None

    denial = walk(doc, None, 0)
    if denial is not None:
        denial.chain = visited
        denial.truncated_at_verified = state["truncated"]
        return denial
    return LineageResult(
        "allow",
        reason="all_ancestors_allow",
        chain=visited,
        truncated_at_verified=state["truncated"],
    )
