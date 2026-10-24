"""Tests for ORP v0.3 Layer 1 extension fields (R2): legal provenance (C2) + identifier/access/freshness/reach (C8)."""

from orp_validator.validator import ORPValidator

V = ORPValidator()


def _base(dataset):
    return {
        "orp_version": "0.3",
        "document_id": "orp:test:r2",
        "title": "R2 fields",
        "domain": "data",
        "authors": [{"name": "A", "role": "author"}],
        "created": "2026-10-24",
        "last_modified": "2026-10-24",
        "status": "draft",
        "summary": "A sufficiently long summary for the R2 Layer-1 extension field tests.",
        "l1_data_provenance": [dataset],
    }


def test_full_legal_and_access_fields_validate():
    ds = {
        "dataset_id": "https://ds/1",
        "name": "DS",
        "source": "https://example.org",
        "legal_basis": "consent",
        "consent_scope": {
            "purposes": ["advertising_targeting"],
            "withdrawal_mechanism": "https://opt-out",
        },
        "sensitive_categories": [],
        "rights_holders": [{"name": "Pub X", "role": "publisher", "licence": "CC-BY-4.0"}],
        "optout_signals_honoured": {"robots_txt": True, "tdm_reservation": "not_applicable"},
        "data_subject_contact": "dpo@example.org",
        "access": {
            "visibility": "restricted",
            "endpoints": [{"kind": "sample", "url": "https://ds/1/sample", "auth": "none"}],
            "sample_hash": "sha256:" + "a" * 64,
        },
        "freshness": {"collected_to": "2026-09-01", "refreshed_at": "2026-10-20", "decay_days": 30},
        "reach": {
            "estimate": 1200000,
            "unit": "devices",
            "confidence": "medium",
            "as_of": "2026-10-20",
        },
    }
    res = V.validate(_base(ds))
    assert res.valid, res.errors


def test_bad_legal_basis_enum_fails():
    ds = {"dataset_id": "d", "name": "n", "source": "s", "legal_basis": "vibes"}
    res = V.validate(_base(ds))
    assert not res.valid


def test_bad_reach_unit_fails():
    ds = {
        "dataset_id": "d",
        "name": "n",
        "source": "s",
        "reach": {"estimate": 10, "unit": "furlongs"},
    }
    res = V.validate(_base(ds))
    assert not res.valid


def test_bad_access_visibility_fails():
    ds = {"dataset_id": "d", "name": "n", "source": "s", "access": {"visibility": "semi-public"}}
    res = V.validate(_base(ds))
    assert not res.valid


def test_v02_dataset_still_valid_under_v03_core():
    # the extension is additive — a plain v0.2-style dataset entry still validates
    ds = {"dataset_id": "d", "name": "n", "source": "s"}
    res = V.validate(_base(ds))
    assert res.valid, res.errors


def test_lineage_block_validates_and_relaxed_requires_basis():
    doc = _base({"dataset_id": "d", "name": "n", "source": "s"})
    doc["lineage"] = {
        "derivations": [
            {"parent_id": "https://ds/parent", "transformation": "subset", "inherits": "full"}
        ],
        "this_document": {"forking_permitted": True, "derivation_permitted": "internal"},
    }
    assert V.validate(doc).valid, V.validate(doc).errors

    # relaxed edge without relaxation_basis must fail (schema if/then)
    doc["lineage"]["derivations"][0] = {
        "parent_id": "p",
        "transformation": "subset",
        "inherits": "relaxed",
    }
    assert not V.validate(doc).valid
