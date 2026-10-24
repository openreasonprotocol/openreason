"""Tests for ORP v0.3 usage_policy evaluation (R3, RFC §5.5) and usage records (R5, RFC §7)."""

import pytest

from orp_validator import attestation as A
from orp_validator import conformance, usage

# Single source of truth: the bundled conformance fixtures (RFC §9.2).
FIXTURES = conformance.load_fixture("policy_cases.json")["cases"]

crypto = pytest.importorskip("cryptography")
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey  # noqa: E402

# ------------------------------------------------------------------- R3: policy evaluation (fixtures)


@pytest.mark.parametrize("case", FIXTURES, ids=[c["name"] for c in FIXTURES])
def test_policy_evaluation_fixtures(case):
    d = usage.evaluate_policy(case["policy"], case["context"])
    exp = case["expect"]
    assert d.decision == exp["decision"], f"{case['name']}: {d.to_dict()}"
    if "permission_id" in exp:
        assert d.permission_id == exp["permission_id"], d.to_dict()
    if "duties" in exp:
        assert d.duties == exp["duties"]
    if "reason" in exp:
        assert d.reason == exp["reason"], d.to_dict()


def test_allow_exposes_duties_and_allowed_property():
    policy = {
        "policy_id": "p",
        "permissions": [{"permission_id": "x", "purpose": "measurement", "duties": ["pay"]}],
    }
    d = usage.evaluate_policy(policy, {"purpose": "measurement"})
    assert d.allowed and d.duties == ["pay"]


def test_prohibition_with_scope_only_matches_in_scope():
    policy = {
        "policy_id": "p",
        "permissions": [{"permission_id": "ok", "purpose": "advertising_targeting"}],
        "prohibitions": [{"purpose": "advertising_targeting", "scope": {"geo": ["US"]}}],
    }
    # prohibited only in US; DK falls through to the permission
    assert (
        usage.evaluate_policy(policy, {"purpose": "advertising_targeting", "geo": "US"}).decision
        == "deny"
    )
    assert (
        usage.evaluate_policy(policy, {"purpose": "advertising_targeting", "geo": "DK"}).decision
        == "allow"
    )


# ------------------------------------------------------------------- R5: usage records + receipt equivalence


def _receipt_and_key():
    sk = Ed25519PrivateKey.generate()
    pub = sk.public_key().public_bytes_raw()
    receipt = {
        "iid": "clr_123",
        "ts": "2026-10-24T12:00:00Z",
        "principal": "did:ex:buyer",
        "fee_micro": 2000,
        "currency": "USD_micro",
        "geo": "DK",
        "media": "ctv",
        "volume": 1,
    }
    return sk, pub, receipt


def test_usage_record_from_receipt_maps_fields():
    _sk, _pub, receipt = _receipt_and_key()
    rec = usage.usage_record_from_receipt(
        receipt,
        dataset_id="https://ds/1",
        dataset_hash="sha256:" + "a" * 64,
        policy_hash="sha256:" + "b" * 64,
        purpose="advertising_targeting",
    )
    ok, missing = usage.is_wellformed_usage_record(rec)
    assert ok, missing
    assert rec["record_id"] == "clr_123"
    assert rec["counterparty"] == "did:ex:buyer"
    assert rec["context"]["execution_id"] == "clr_123"
    assert rec["fee"] == {"amount": 2000, "currency": "USD_micro"}


def test_usage_record_missing_fields_flagged():
    ok, missing = usage.is_wellformed_usage_record({"record_id": "x"})
    assert not ok
    assert any("dataset_hash" in m for m in missing)


def test_usage_record_signature_verifies_and_tamper_fails():
    sk, pub, receipt = _receipt_and_key()
    rec = usage.usage_record_from_receipt(
        receipt,
        dataset_id="https://ds/1",
        dataset_hash="sha256:" + "a" * 64,
        policy_hash="sha256:" + "b" * 64,
        purpose="advertising_targeting",
    )
    # rail signs the canonical record (minus signatures)
    content = {k: v for k, v in rec.items() if k != "signatures"}
    sig = A.b64u_encode(sk.sign(A.canonicalize(content)))
    rec["signatures"] = [{"kid": "did:web:rail#k1", "alg": "Ed25519", "sig": sig, "role": "rail"}]

    good = usage.verify_usage_record(rec, resolve_key=lambda kid: pub)
    assert good["valid"], good

    rec["counterparty"] = "did:ex:attacker"  # tamper
    bad = usage.verify_usage_record(rec, resolve_key=lambda kid: pub)
    assert not bad["valid"]
