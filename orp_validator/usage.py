"""ORP v0.3 usage policy (RFC change C3, R3) and usage records (RFC change C5, R5).

This is the enforce/prove pair a rail actually consumes:
  * `evaluate_policy(policy, context)` — the pure reference ODRL-profile evaluator (RFC §5.5). A rail
    (e.g. Railu/Yumipop) calls this at activation time to decide allow/deny for a concrete use.
  * usage records (RFC §7) — the append-only record of *use*. A rail's signed clearing receipt that
    carries the dataset + policy hashes IS a usage record by construction; `usage_record_from_receipt`
    makes that mapping explicit and `verify_usage_record` checks its signatures with the R1 machinery.

Pure + total + offline. Signing/resolution is the caller's job (same convention as attestation.py).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Optional

# RFC §5.3 — normative purpose taxonomy. Profiles MAY restrict but MUST NOT extend; extension goes via the spec.
PURPOSES = frozenset(
    {
        "advertising_targeting",
        "suppression",
        "measurement",
        "analytics",
        "model_training",
        "fine_tuning",
        "evaluation",
        "retrieval",
        "inference",
        "resale",
        "research",
    }
)

# RFC §5.4 — derivation grants, ordered by how much they permit (a grant permits itself and anything below it).
DERIVATION_ORDER = {"none": 0, "internal": 1, "licensed": 2}

# Scope dimensions the evaluator understands. A scope key outside this set fails closed (RFC §5.5).
KNOWN_SCOPE_KEYS = frozenset({"geo", "media", "time"})


@dataclass
class PolicyDecision:
    decision: str  # "allow" | "deny"
    permission_id: Optional[str] = None
    duties: list[str] = field(default_factory=list)
    reason: str = ""

    @property
    def allowed(self) -> bool:
        return self.decision == "allow"

    def to_dict(self) -> dict[str, Any]:
        return {
            "decision": self.decision,
            "permission_id": self.permission_id,
            "duties": self.duties,
            "reason": self.reason,
        }


def _parse_iso(ts: str) -> datetime:
    dt = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def _in_scope(scope: dict[str, Any], context: dict[str, Any]) -> tuple[bool, str]:
    """Does the context fall inside a permission's scope? Unknown scope keys fail closed (deny)."""
    if not isinstance(scope, dict):
        return True, ""
    for key in scope:
        if key not in KNOWN_SCOPE_KEYS:
            return False, f"unknown_scope_key:{key}"
    # geo / media: context value (if given) must be in the permitted list
    for dim in ("geo", "media"):
        allowed = scope.get(dim)
        if allowed is None:
            continue
        want = context.get(dim)
        if want is None:
            continue  # context does not constrain this dimension
        allowed_set = {str(x) for x in (allowed if isinstance(allowed, list) else [allowed])}
        wants = want if isinstance(want, list) else [want]
        if not all(str(w) in allowed_set for w in wants):
            return False, f"{dim}_out_of_scope"
    # time window
    tw = scope.get("time")
    if isinstance(tw, dict) and context.get("time"):
        try:
            t = _parse_iso(context["time"])
            if tw.get("from") and t < _parse_iso(tw["from"]):
                return False, "time_before_window"
            if tw.get("to") and t > _parse_iso(tw["to"]):
                return False, "time_after_window"
        except Exception:
            return False, "bad_time"
    return True, ""


def _assignee_matches(assignee: Any, who: Optional[str]) -> bool:
    if assignee in (None, "any"):
        return True
    ids = assignee if isinstance(assignee, list) else [assignee]
    return who is not None and who in {str(x) for x in ids}


def _derivation_allowed(granted: Any, requested: Any) -> bool:
    g = DERIVATION_ORDER.get(str(granted or "none"))
    r = DERIVATION_ORDER.get(str(requested or "none"))
    if g is None or r is None:
        return False  # unknown derivation value → fail closed
    return r <= g


def evaluate_policy(policy: dict[str, Any], context: dict[str, Any]) -> PolicyDecision:
    """Reference evaluator (RFC §5.5). Returns deny if any prohibition matches, deny if no permission
    matches, otherwise allow with the matching permission id. Unknown purpose or unknown scope keys → deny.

    context = {purpose, assignee?, geo?, media?, time?, derivation_requested?}
    """
    purpose = context.get("purpose")
    if purpose not in PURPOSES:
        return PolicyDecision("deny", reason=f"unknown_or_missing_purpose:{purpose!r}")

    # expiry on the whole policy
    if policy.get("expiry"):
        try:
            if context.get("time") and _parse_iso(context["time"]) > _parse_iso(policy["expiry"]):
                return PolicyDecision("deny", reason="policy_expired")
        except Exception:
            return PolicyDecision("deny", reason="bad_policy_expiry")

    # 1. prohibitions first — a match denies regardless of permissions
    for pro in policy.get("prohibitions", []) or []:
        if pro.get("purpose") == purpose:
            ok, _why = _in_scope(pro.get("scope", {}), context)
            # a prohibition with no scope matches on purpose alone; with scope, matches inside that scope
            if "scope" not in pro or ok:
                return PolicyDecision("deny", reason=f"prohibited:{purpose}")

    # 2. permissions — need one that matches purpose + assignee + scope + derivation
    who = context.get("assignee")
    requested_deriv = context.get("derivation_requested", "none")
    for i, perm in enumerate(policy.get("permissions", []) or []):
        if perm.get("purpose") != purpose:
            continue
        if not _assignee_matches(perm.get("assignee"), who):
            continue
        in_scope, _why = _in_scope(perm.get("scope", {}), context)
        if not in_scope:
            continue
        if not _derivation_allowed(perm.get("derivation", "none"), requested_deriv):
            continue
        pid = perm.get("permission_id") or perm.get("id") or f"permission[{i}]"
        return PolicyDecision(
            "allow", permission_id=pid, duties=list(perm.get("duties", []) or []), reason="matched"
        )

    return PolicyDecision("deny", reason="no_matching_permission")


# --------------------------------------------------------------------------- usage records (R5, RFC §7)

REQUIRED_USAGE_RECORD_FIELDS = (
    "record_id",
    "timestamp",
    "dataset_id",
    "dataset_hash",
    "policy_hash",
    "counterparty",
    "purpose",
)


def usage_record_from_receipt(
    receipt: dict[str, Any],
    *,
    dataset_id: str,
    dataset_hash: str,
    policy_hash: str,
    purpose: str,
) -> dict[str, Any]:
    """Build a usage record from a rail's signed clearing receipt (RFC §7.2: receipt equivalence).

    The receipt already proves *who cleared what, when, for how much, signed by the rail*. We graft the
    dataset + policy identity (which the activation knew) onto it; the receipt's own signature carries over
    as the rail's attestation of the use. This is the concrete Railu ↔ ORP integration point.
    """
    rec: dict[str, Any] = {
        "record_id": receipt.get("iid") or receipt.get("id") or receipt.get("record_id"),
        "timestamp": receipt.get("ts") or receipt.get("timestamp") or receipt.get("signed_at"),
        "dataset_id": dataset_id,
        "dataset_hash": dataset_hash,
        "policy_hash": policy_hash,
        "counterparty": receipt.get("principal")
        or receipt.get("counterparty")
        or receipt.get("buyer"),
        "purpose": purpose,
        "context": {
            "geo": receipt.get("geo"),
            "media": receipt.get("media"),
            "execution_id": receipt.get("iid") or receipt.get("execution_id"),
            "volume": receipt.get("volume") or receipt.get("qty"),
        },
    }
    amount = receipt.get("fee_micro", receipt.get("amount"))
    if amount is not None:
        rec["fee"] = {"amount": amount, "currency": receipt.get("currency", "USD_micro")}
    # carry the rail's signature(s) through as the record's attestation
    sigs = receipt.get("signatures")
    if sigs is None and receipt.get("sig"):
        sigs = [
            {
                "kid": receipt.get("kid"),
                "alg": receipt.get("alg", "Ed25519"),
                "sig": receipt["sig"],
                "role": "rail",
            }
        ]
    if sigs:
        rec["signatures"] = sigs
    return rec


def is_wellformed_usage_record(record: dict[str, Any]) -> tuple[bool, list[str]]:
    """Shape check (append-only semantics are a storage property, not verifiable in a pure function)."""
    missing = [f for f in REQUIRED_USAGE_RECORD_FIELDS if not record.get(f)]
    return (not missing), ([f"missing:{f}" for f in missing])


def verify_usage_record(
    record: dict[str, Any],
    resolve_key: Callable[[str], Any],
    now: Optional[datetime] = None,
) -> dict[str, Any]:
    """Verify a usage record's signatures with the R1 attestation machinery. The signing input is the
    canonical form of the record minus its `signatures` array (same construction as attestation)."""
    from . import attestation as A

    wf, missing = is_wellformed_usage_record(record)
    if not wf:
        return {"valid": False, "errors": missing, "signatures": []}

    content = {k: v for k, v in record.items() if k != "signatures"}
    signing_input = A.canonicalize(content)
    now = now or datetime.now(timezone.utc)
    verdicts = []
    any_valid = False
    for s in record.get("signatures", []) or []:
        v = {"kid": s.get("kid"), "role": s.get("role"), "valid": False, "errors": []}
        if not A.CRYPTO_AVAILABLE:
            v["errors"].append("crypto_unavailable")
        else:
            try:
                pub = A.load_ed25519_public_key(resolve_key(s.get("kid")))
                pub.verify(A.b64u_decode(str(s.get("sig", ""))), signing_input)
                v["valid"] = True
                any_valid = True
            except Exception as e:  # noqa: BLE001
                v["errors"].append(f"bad_signature:{e}")
        verdicts.append(v)
    return {
        "valid": any_valid,
        "errors": [] if any_valid else ["no_valid_signature"],
        "signatures": verdicts,
    }
