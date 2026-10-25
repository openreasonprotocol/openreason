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

from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

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
    permission_id: str | None = None
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


def _assignee_matches(assignee: Any, who: str | None) -> bool:
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


# Transport-envelope fields a rail adds AFTER signing its receipt (verification, tracking, trace data). They are
# never part of the signed bytes. Rails may pass their own list to `strip_receipt_envelope`.
DEFAULT_RECEIPT_ENVELOPE: frozenset[str] = frozenset(
    {
        "signature",
        "tracking",
        "verify",
        "trace",
        "declared_winner_seat",
        "declared_winner_seat_note",
    }
)


def strip_receipt_envelope(
    receipt: dict[str, Any], envelope: Iterable[str] = DEFAULT_RECEIPT_ENVELOPE
) -> dict[str, Any]:
    """Return the exact object a rail signed: the receipt minus its signature and transport envelope."""
    drop = set(envelope)
    return {k: v for k, v in receipt.items() if k not in drop}


def _receipt_signatures(receipt: dict[str, Any]) -> list[dict[str, Any]] | None:
    """Normalise the rail's signature(s): `signatures: [...]`, a single `signature: {alg,kid,sig}` object
    (Railu `/v1/execute`), or flat `sig`/`kid`/`alg` fields."""
    sigs = receipt.get("signatures")
    if sigs:
        return list(sigs)
    single = receipt.get("signature")
    if isinstance(single, dict) and single.get("sig"):
        return [
            {
                "kid": single.get("kid"),
                "alg": single.get("alg", "Ed25519"),
                "sig": single["sig"],
                "role": single.get("role", "rail"),
            }
        ]
    if receipt.get("sig"):
        return [
            {
                "kid": receipt.get("kid"),
                "alg": receipt.get("alg", "Ed25519"),
                "sig": receipt["sig"],
                "role": "rail",
            }
        ]
    return None


def usage_record_from_receipt(
    receipt: dict[str, Any],
    *,
    dataset_id: str,
    dataset_hash: str,
    policy_hash: str,
    purpose: str,
    embed_receipt: bool = False,
    envelope: Iterable[str] = DEFAULT_RECEIPT_ENVELOPE,
) -> dict[str, Any]:
    """Build a usage record from a rail's signed clearing receipt (RFC §7.2: receipt equivalence).

    The receipt already proves *who cleared what, when, for how much, signed by the rail*. We graft the
    dataset + policy identity (which the activation knew) onto it. This is the concrete Railu ↔ ORP
    integration point.

    Field aliases (0.5.1): the buyer may arrive as `principal`, `counterparty`, `buyer` or `winner`; the time
    as `ts`, `timestamp` or `signed_at`; the id as `iid`, `id`, `record_id`, `execution_id` or `proof.iid`.

    `embed_receipt=True` (0.5.1, recommended): the record carries the rail's receipt verbatim under `receipt`
    (signed object + its signature, envelope stripped). `verify_usage_record` then verifies the rail's
    signature over the *receipt* bytes and binds the record to it — the rail never has to sign a second
    object. Without it, the rail's signature is copied into `signatures`, which only verifies if the rail
    signed the record itself (legacy behaviour).
    """
    proof_raw = receipt.get("proof")
    proof: dict[str, Any] = proof_raw if isinstance(proof_raw, dict) else {}
    exec_id = (
        receipt.get("iid")
        or receipt.get("execution_id")
        or proof.get("iid")
        or receipt.get("id")
        or receipt.get("record_id")
    )
    rec: dict[str, Any] = {
        "record_id": receipt.get("iid")
        or receipt.get("id")
        or receipt.get("record_id")
        or receipt.get("execution_id")
        or proof.get("iid"),
        "timestamp": receipt.get("ts") or receipt.get("timestamp") or receipt.get("signed_at"),
        "dataset_id": dataset_id,
        "dataset_hash": dataset_hash,
        "policy_hash": policy_hash,
        "counterparty": receipt.get("principal")
        or receipt.get("counterparty")
        or receipt.get("buyer")
        or receipt.get("winner"),
        "purpose": purpose,
        "context": {
            "geo": receipt.get("geo"),
            "media": receipt.get("media"),
            "execution_id": exec_id,
            "volume": receipt.get("volume") or receipt.get("qty"),
        },
    }
    amount = receipt.get("fee_micro", receipt.get("amount"))
    if amount is not None:
        rec["fee"] = {"amount": amount, "currency": receipt.get("currency", "USD_micro")}
    sigs = _receipt_signatures(receipt)
    if embed_receipt:
        signed = strip_receipt_envelope(receipt, envelope)
        embedded = dict(signed)
        if sigs:
            embedded["signatures"] = sigs
        rec["receipt"] = embedded
    elif sigs:
        # legacy: carry the rail's signature(s) through as the record's own attestation
        rec["signatures"] = sigs
    return rec


def is_wellformed_usage_record(record: dict[str, Any]) -> tuple[bool, list[str]]:
    """Shape check (append-only semantics are a storage property, not verifiable in a pure function)."""
    missing = [f for f in REQUIRED_USAGE_RECORD_FIELDS if not record.get(f)]
    return (not missing), ([f"missing:{f}" for f in missing])


def verify_usage_record(
    record: dict[str, Any],
    resolve_key: Callable[[str], Any],
    now: datetime | None = None,
) -> dict[str, Any]:
    """Verify a usage record's signatures with the R1 attestation machinery. The signing input is the
    canonical form of the record minus its `signatures` array (same construction as attestation)."""
    from . import attestation as A

    wf, missing = is_wellformed_usage_record(record)
    if not wf:
        return {"valid": False, "errors": missing, "signatures": []}

    now = now or datetime.now(timezone.utc)
    embedded = record.get("receipt")
    if isinstance(embedded, dict):
        # Receipt mode (RFC §7.2 as clarified in 0.5.1): the rail signed the RECEIPT, so that is what we verify;
        # the record is bound to it by id. The rail never signs the record itself.
        errors: list[str] = []
        proof_raw = embedded.get("proof")
        proof: dict[str, Any] = proof_raw if isinstance(proof_raw, dict) else {}
        ids = {
            embedded.get("iid"),
            embedded.get("execution_id"),
            embedded.get("id"),
            embedded.get("record_id"),
            proof.get("iid"),
        } - {None}
        if record.get("record_id") not in ids:
            errors.append("record_not_bound_to_receipt")
        sig_list = embedded.get("signatures") or []
        signing_input = A.canonicalize({k: v for k, v in embedded.items() if k != "signatures"})
        mode_sigs: list[dict[str, Any]] = sig_list
    else:
        errors = []
        signing_input = A.canonicalize({k: v for k, v in record.items() if k != "signatures"})
        mode_sigs = record.get("signatures", []) or []
    verdicts = []
    any_valid = False
    for s in mode_sigs:
        v: dict[str, Any] = {
            "kid": s.get("kid"),
            "role": s.get("role"),
            "valid": False,
            "errors": [],
        }
        if not A.CRYPTO_AVAILABLE:
            v["errors"].append("crypto_unavailable")
        else:
            try:
                pub = A.load_ed25519_public_key(resolve_key(str(s.get("kid") or "")))
                pub.verify(A.b64u_decode(str(s.get("sig", ""))), signing_input)
                v["valid"] = True
                any_valid = True
            except Exception as e:  # noqa: BLE001
                v["errors"].append(f"bad_signature:{e}")
        verdicts.append(v)
    if not any_valid:
        errors.append("no_valid_signature")
    return {
        "valid": any_valid and not errors,
        "errors": errors,
        "signatures": verdicts,
        "mode": "receipt" if isinstance(embedded, dict) else "record",
    }
