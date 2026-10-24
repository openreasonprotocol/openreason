"""Tests for ORP v0.3 attestation (change C1). Covers the RFC §10 R1 checklist:
tampered document fails; unknown key fails; wrong-`use` key fails; expired key fails; offline
verification with a supplied unexpired key passes; hash recomputation; did:key round-trip.
"""

from datetime import datetime, timedelta, timezone

import pytest

from orp_validator import attestation as A

crypto = pytest.importorskip(
    "cryptography", reason="attestation tests need the [attestation] extra (cryptography)"
)
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey  # noqa: E402

NOW = datetime(2026, 9, 24, 12, 0, 0, tzinfo=timezone.utc)


def _keypair():
    sk = Ed25519PrivateKey.generate()
    raw_pub = sk.public_key().public_bytes_raw()
    return sk, raw_pub


def _attested_doc(
    sk, kid="did:web:example.org#key-1", *, use=A.ATTESTATION_USE, key_expires=None, tier="attested"
):
    """Build a minimal, correctly-attested ORP document signed by `sk`."""
    content = {
        "orp_version": "0.3",
        "document_id": "orp:example:1",
        "title": "Test dataset",
        "attested_by": {"name": "A. Steward", "role": "data_steward"},
    }
    signing_input = A.canonicalize(content)
    sig = A.b64u_encode(sk.sign(signing_input))
    doc = dict(content)
    doc["attestation"] = {
        "hash": A.content_hash(content),
        "version": 1,
        "previous_hash": None,
        "tier": tier,
        "signatures": [
            {
                "kid": kid,
                "alg": "Ed25519",
                "use": use,
                "sig": sig,
                "role": "data_steward",
                "signed_at": "2026-09-24T12:00:00Z",
                "key_expires": key_expires or "2026-10-24T12:00:00Z",
            }
        ],
    }
    return doc


# ---------------------------------------------------------------- canonicalisation / hash


def test_canonicalize_sorts_keys_and_omits_whitespace():
    assert A.canonicalize({"b": 1, "a": 2}) == b'{"a":2,"b":1}'
    assert A.canonicalize([1, "x", True, None]) == b'[1,"x",true,null]'


def test_canonicalize_is_order_independent():
    assert A.canonicalize({"a": 1, "b": {"d": 4, "c": 3}}) == A.canonicalize(
        {"b": {"c": 3, "d": 4}, "a": 1}
    )


def test_content_hash_stable_and_excludes_attestation_block():
    sk, _ = _keypair()
    doc = _attested_doc(sk)
    # hash is over the content WITHOUT the attestation block
    assert A.content_hash(A.attested_content(doc)) == doc["attestation"]["hash"]


def test_number_rejects_nan_and_infinity():
    with pytest.raises(ValueError):
        A.canonicalize({"x": float("nan")})
    with pytest.raises(ValueError):
        A.canonicalize({"x": float("inf")})


def test_bool_not_treated_as_number():
    # bools serialise as true/false, not 1/0
    assert A.canonicalize({"x": True}) == b'{"x":true}'


# ---------------------------------------------------------------- happy path (offline verify)


def test_valid_attestation_verifies_offline():
    sk, pub = _keypair()
    doc = _attested_doc(sk)
    res = A.verify_attestation(doc, resolve_key=lambda kid: pub, now=NOW)
    assert res.valid, res.errors
    assert res.tier == "attested"
    assert res.signatures[0].valid
    assert res.computed_hash == doc["attestation"]["hash"]


def test_did_key_resolution_round_trip():
    sk, pub = _keypair()
    # encode the raw pubkey as a did:key and resolve through the pure decoder
    did = "did:key:z" + _b58encode(b"\xed\x01" + pub)
    assert A.public_key_from_did_key(did) == pub
    doc = _attested_doc(sk, kid=did)
    res = A.verify_attestation(
        doc, resolve_key=lambda kid: kid, now=NOW
    )  # resolver hands the did back
    assert res.valid, res.errors


# ---------------------------------------------------------------- failure modes (all hard errors)


def test_tampered_document_fails():
    sk, pub = _keypair()
    doc = _attested_doc(sk)
    doc["title"] = "Tampered title"  # content changed, hash + signature no longer match
    res = A.verify_attestation(doc, resolve_key=lambda kid: pub, now=NOW)
    assert not res.valid
    assert any("hash_mismatch" in e for e in res.errors)
    assert not res.signatures[0].valid  # signature is over the original bytes


def test_unknown_key_fails():
    sk, _ = _keypair()
    doc = _attested_doc(sk)

    def resolve(kid):
        raise KeyError("no such key")

    res = A.verify_attestation(doc, resolve_key=resolve, now=NOW)
    assert not res.valid
    assert any("key_resolution_failed" in e for e in res.signatures[0].errors)


def test_wrong_use_key_fails():
    sk, pub = _keypair()
    doc = _attested_doc(sk, use="some-other-purpose")
    res = A.verify_attestation(doc, resolve_key=lambda kid: pub, now=NOW)
    assert not res.valid
    assert any("wrong_key_use" in e for e in res.signatures[0].errors)


def test_expired_key_fails():
    sk, pub = _keypair()
    doc = _attested_doc(sk, key_expires="2026-09-01T00:00:00Z")  # well before NOW
    res = A.verify_attestation(doc, resolve_key=lambda kid: pub, now=NOW)
    assert not res.valid
    assert any("key_expired" in e for e in res.signatures[0].errors)


def test_wrong_key_fails_signature():
    sk, _ = _keypair()
    _, other_pub = _keypair()
    doc = _attested_doc(sk)
    res = A.verify_attestation(doc, resolve_key=lambda kid: other_pub, now=NOW)
    assert not res.valid
    assert any("bad_signature" in e for e in res.signatures[0].errors)


def test_version_chain_shape():
    sk, pub = _keypair()
    doc = _attested_doc(sk)
    doc["attestation"]["version"] = 2  # v2 with null previous_hash is invalid
    # re-sign content is unaffected (attestation block excluded from hash), but hash still matches content...
    # the hash is over content, unchanged — so only the version-chain rule should trip:
    res = A.verify_attestation(doc, resolve_key=lambda kid: pub, now=NOW)
    assert not res.valid
    assert any("previous_hash" in e for e in res.errors)


def test_skew_tolerates_recent_expiry():
    sk, pub = _keypair()
    just_expired = (NOW - timedelta(seconds=60)).isoformat().replace("+00:00", "Z")
    doc = _attested_doc(sk, key_expires=just_expired)
    res = A.verify_attestation(doc, resolve_key=lambda kid: pub, now=NOW, skew_seconds=300)
    assert res.valid, res.errors  # within the 300s skew window


def test_no_attestation_block():
    res = A.verify_attestation({"orp_version": "0.3"}, resolve_key=lambda kid: b"")
    assert not res.valid
    assert "no_attestation_block" in res.errors


# ---------------------------------------------------------------- helper (base58btc encode, for did:key test)

_B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def _b58encode(b: bytes) -> str:
    num = int.from_bytes(b, "big")
    out = ""
    while num:
        num, rem = divmod(num, 58)
        out = _B58[rem] + out
    pad = len(b) - len(b.lstrip(b"\x00"))
    return "1" * pad + out
