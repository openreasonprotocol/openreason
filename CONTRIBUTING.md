# Contributing to OpenReason

OpenReason is an open protocol, not a product. Anyone can implement it; no single entity owns it. Disagreement is
resolved by forking and showing better reasoning, not by vote. Contributions that make the reasoning behind the
protocol more checkable are the ones we value most.

## Ways to contribute

- **Report a bug** in the validator, SDK, MCP server or API: open a bug report issue with a minimal document that reproduces it.
- **Propose a spec change**: open a spec-change issue first. Explain the problem, the proposed change, and who it affects. Spec text and schemas change together, with a conformance case.
- **Add or improve an example**: real documents are the best documentation. Examples must validate (`orp validate`) and should say what they deliberately leave out.
- **Improve the docs site** (`docs-site/`): typos and clarity fixes can go straight to a pull request.

## Development setup

```bash
git clone https://github.com/openreasonprotocol/openreason.git
cd openreason
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
orp conform
```

JavaScript packages:

```bash
cd sdk-js && npm install && npm run build
cd ../mcp && npm install && npm run build
```

## Before you open a pull request

CI runs the same gates on every PR; run them locally first:

```bash
black --check orp_validator/ tests/
ruff check orp_validator/ tests/
mypy orp_validator/
pytest tests/
orp conform
orp validate examples/danish_property_tax_reform.yaml --verbose
orp validate examples/data_product_ctv_segment.v0.3.yaml --profile ORP-Ads
```

- Keep pull requests focused on one change.
- Schema or spec changes need a conformance fixture under `orp_validator/schemas/conformance/` and a CHANGELOG entry under *Unreleased*.
- Tests must pass on Python 3.9 through 3.12, not only on your local version. `importlib.resources` and typing syntax are the usual traps.
- Write commit messages that say *why*, not just *what*.

## Principles that guide review

1. **Attest, never grade.** The protocol records who said what, when, citing which sources and assumptions. It never issues a verdict on whether a claim is good or correct. Changes that move the protocol toward grading content will be declined.
2. **Verifiable without trusting the author.** Anything a document asserts should be checkable by hand or by signature.
3. **Fail closed.** Unknown keys, unknown purposes and unresolved ancestors are errors, not warnings.
4. **No new crypto.** Attestation uses Ed25519, RFC 8785 canonicalisation and SHA-256. Proposals for new primitives need a very good reason.

## Licence

By contributing you agree that your contributions are licensed under the Apache License 2.0, the same licence as the project. See `LICENSE` and `NOTICE`.
