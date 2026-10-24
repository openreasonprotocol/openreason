"""Tests for ORP v0.3 profiles (RFC C6) and trust tiers (RFC C7).

Covers: ORP-Core/Policy/Ads/AI schema selection + required-field enforcement; profile auto-detection
from the `profile` field; and the trust-tier ladder (self_declared -> attested -> verified -> full,
plus posthoc and the no-resolver cap).
"""

import pytest

from orp_validator import attestation as A
from orp_validator.validator import ORPValidator, TrustTier

crypto = pytest.importorskip("cryptography")
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey  # noqa: E402


def _base(**over):
    doc = {
        "orp_version": "0.3",
        "document_id": "orp:test:1",
        "title": "Test",
        "domain": "policy",
        "authors": [{"name": "A", "role": "author"}],
        "created": "2026-10-24",
        "last_modified": "2026-10-24",
        "status": "draft",
        "summary": "A sufficiently long plain-language summary of the document.",
        "l1_data_provenance": [
            {"dataset_id": "ds1", "name": "DS", "source": "https://example.org"}
        ],
    }
    doc.update(over)
    return doc


def _l2():
    return {"affected_population": {"description": "everyone", "size": 100}}


def _l3():
    return {"stakeholder_map": {"group_a": {"benefits": "x"}}}


V = ORPValidator()


# --------------------------------------------------------------- profile selection + enforcement


def test_core_minimal_is_valid():
    res = V.validate(_base())
    assert res.valid, res.errors
    assert res.profile == "ORP-Core"
    assert res.trust_tier == TrustTier.SELF_DECLARED


def test_policy_requires_l2_and_l3():
    bad = V.validate(_base(profile="ORP-Policy"))
    assert not bad.valid
    assert bad.profile == "ORP-Policy"
    good = V.validate(
        _base(profile="ORP-Policy", l2_consequence_simulation=_l2(), l3_empathy_mapping=_l3())
    )
    assert good.valid, good.errors


def test_profile_autodetected_from_field():
    # No explicit profile arg — the document's own `profile` field drives schema selection.
    res = V.validate(_base(profile="ORP-Policy"))
    assert res.profile == "ORP-Policy"
    assert not res.valid  # missing L2/L3


def test_ads_requires_reach_and_freshness():
    bad = V.validate(_base(domain="ads", profile="ORP-Ads"))
    assert not bad.valid
    good_ds = {
        "dataset_id": "seg1",
        "name": "Segment",
        "source": "https://example.org",
        "reach": {"estimate": 1000000, "unit": "devices"},
        "freshness": {"refreshed_at": "2026-10-20"},
    }
    good = V.validate(_base(domain="ads", profile="ORP-Ads", l1_data_provenance=[good_ds]))
    assert good.valid, good.errors


def test_ai_requires_rights_holders_and_optout():
    bad = V.validate(_base(domain="ai-training", profile="ORP-AI"))
    assert not bad.valid
    good_ds = {
        "dataset_id": "corpus1",
        "name": "Corpus",
        "source": "https://example.org",
        "rights_holders": [{"name": "Author X", "role": "author", "licence": "CC-BY-4.0"}],
        "optout_signals_honoured": {"robots_txt": True, "tdm_reservation": "not_applicable"},
    }
    good = V.validate(_base(domain="ai-training", profile="ORP-AI", l1_data_provenance=[good_ds]))
    assert good.valid, good.errors


def test_unknown_profile_errors():
    res = V.validate(_base(), profile="ORP-Bogus")
    assert not res.valid
    assert any("Unknown profile" in e for e in res.errors)


# --------------------------------------------------------------- trust tiers


def _attested_doc(role="data_steward", tier="attested", with_l3=False):
    sk = Ed25519PrivateKey.generate()
    pub = sk.public_key().public_bytes_raw()
    extra = {"attested_by": {"name": "S", "role": "data_steward"}}
    if with_l3:
        extra["l3_empathy_mapping"] = _l3()
    content = _base(**extra)
    sig = A.b64u_encode(sk.sign(A.canonicalize(content)))
    doc = dict(content)
    doc["attestation"] = {
        "hash": A.content_hash(content),
        "version": 1,
        "previous_hash": None,
        "tier": tier,
        "signatures": [
            {
                "kid": "did:web:example.org#k1",
                "alg": "Ed25519",
                "use": A.ATTESTATION_USE,
                "sig": sig,
                "role": role,
                "key_expires": "2099-01-01T00:00:00Z",
            }
        ],
    }
    return doc, pub


def test_tier_self_declared_when_no_resolver():
    doc, _pub = _attested_doc()
    res = V.validate(doc)  # no resolver -> cannot verify -> capped
    assert res.trust_tier == TrustTier.SELF_DECLARED
    assert any("no key resolver" in w for w in res.warnings)


def test_tier_attested_with_verified_signature():
    doc, pub = _attested_doc(role="data_steward")
    res = V.validate(doc, resolve_key=lambda kid: pub)
    assert res.trust_tier == TrustTier.ATTESTED, res.warnings


ACCREDITED = {"did:web:example.org#k1"}  # the kid used by _attested_doc


def test_tier_verified_with_accredited_verifier():
    doc, pub = _attested_doc(role="verifier")
    res = V.validate(doc, resolve_key=lambda kid: pub, accredited_verifiers=ACCREDITED)
    assert res.trust_tier == TrustTier.VERIFIED, res.warnings


def test_tier_full_with_accredited_verifier_and_l3():
    doc, pub = _attested_doc(role="verifier", with_l3=True)
    res = V.validate(doc, resolve_key=lambda kid: pub, accredited_verifiers=ACCREDITED)
    assert res.trust_tier == TrustTier.FULL, res.warnings


def test_tier_unaccredited_verifier_caps_at_attested():
    doc, pub = _attested_doc(role="verifier")
    res = V.validate(doc, resolve_key=lambda kid: pub, accredited_verifiers=set())
    assert res.trust_tier == TrustTier.ATTESTED
    assert any("not on the accredited" in w for w in res.warnings)


def test_tier_posthoc():
    res = V.validate(_base(post_hoc=True))
    assert res.trust_tier == TrustTier.POSTHOC


def test_bad_attestation_drops_to_self_declared():
    doc, _pub = _attested_doc()
    _, other = Ed25519PrivateKey.generate().public_key().public_bytes_raw(), None  # noqa
    wrong = Ed25519PrivateKey.generate().public_key().public_bytes_raw()
    res = V.validate(doc, resolve_key=lambda kid: wrong)
    assert res.trust_tier == TrustTier.SELF_DECLARED
    assert any("did not verify" in w for w in res.warnings)


def test_to_dict_includes_v03_keys_only_for_v03():
    res = V.validate(_base())
    d = res.to_dict()
    assert d["profile"] == "ORP-Core"
    assert d["trust_tier"] == "self_declared"
