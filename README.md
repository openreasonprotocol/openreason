# OpenReason (ORP)

> A public protocol for transparent, simulatable reasoning in policy, AI, and democratic decision-making.

---

## What is OpenReason?

OpenReason is an open-source protocol that standardises how reasoning is documented, shared, and challenged in consequential decisions — particularly in public policy and AI systems.

Just as OpenRTB standardised how value is exchanged in advertising markets, OpenReason standardises how **reasoning is exchanged** in democratic and policy markets. It makes the invisible visible: the data assumptions, the cleaning decisions, the stakeholder weightings, and the simulated consequences that currently sit buried inside government departments, consultancies, and AI training pipelines.

A policy proposal, an AI training methodology, or any significant public decision documented under ORP is not just a document. It is a **simulatable object** — something any party can take, inspect, fork, and run with their own assumptions to see whether they reach the same conclusions.

---

## Why does this matter?

Most democratic disagreement is not about values. It is about **assumptions** — about which data was used, how it was cleaned, whose experiences it reflects, and what consequences were modelled before a decision was made.

Currently those assumptions are largely invisible. The modelling behind major policy decisions is typically proprietary, produced behind closed doors, and impossible for outside parties to interrogate meaningfully. The result is that political debate generates enormous heat while rarely locating the actual point of disagreement.

OpenReason changes that. When reasoning is standardised and public, disagreement becomes **locatable**. You can find the exact assumption where two parties diverge and debate that specific thing — rather than talking past each other at the level of conclusions.

---

## The deeper problem: data, not algorithms

Public discourse around AI bias focuses almost entirely on algorithms. This is misdirected.

An algorithm is an execution layer. It does exactly what it is told with the inputs it receives. Bias lives upstream — in the **selection** of data, the **cleaning** of data, and the **creation** of synthetic data used to fill gaps. These decisions are made by humans, often under time pressure, rarely documented, and almost never subject to public scrutiny.

OpenReason addresses this directly. Data provenance — where data came from, what was excluded and why, how it was cleaned, what was synthesised and with what assumptions — is the foundation of the protocol, not an afterthought.

---

## Core principles

OpenReason is grounded in Rational, Empathy-Informed Ethics (REE). See [docs/specs/REE_PHILOSOPHY.md](docs/specs/REE_PHILOSOPHY.md) for the full framework. The five principles that shape the protocol are:

1. **Measured Compassion** — decisions must demonstrably account for impact on all affected parties, measured rather than assumed
2. **Rational Inquiry** — assumptions are treated as testable hypotheses, not settled facts
3. **Simulated Consequences** — consequences are modelled before commitment, not rationalised after
4. **Universal Sentience** — all affected stakeholders are mapped explicitly, including minorities and marginalised groups
5. **Transparent Accountability** — every decision in the reasoning chain is logged, attributable, and auditable

---

## Protocol layers

ORP is structured in five layers. See [docs/specs/ORP_SPEC.md](docs/specs/ORP_SPEC.md) for the full technical specification.

| Layer | Name | Purpose |
|-------|------|---------|
| L1 | Data Provenance | Document data origin, cleaning, exclusions, and synthetic elements |
| L2 | Consequence Simulation | Define affected population, variables, outcome metrics, and weightings |
| L3 | Empathy Mapping | Identify all stakeholders, model differential impacts, stress-test minority interests |
| L4 | Accountability Ledger | Immutable log of who decided what, when, and on what basis |
| L5 | Fork and Propose | Standardised mechanism for proposing alternative assumptions and publishing diffs |

---

## Quick Start

### Installation

```bash
pip install orp-validator
```

### Create a New Document

```bash
orp new my-proposal.yaml
```

The CLI will interactively prompt you for basic information and generate a valid ORP-Basic template. Edit the file and fill in the placeholders.

### Validate a Document

```bash
orp validate my-proposal.yaml
```

### Check Compliance Level

```bash
orp check my-proposal.yaml
```

Quick check showing which layers are present and what compliance level you've achieved.

### Compare Documents

```bash
orp diff original.yaml fork.yaml
```

See exactly what changed between two documents or forks.

### All Commands

```bash
orp --help                    # Show all available commands
orp new <file>               # Create new ORP document
orp validate <file>          # Full validation with detailed errors
orp check <file>             # Quick compliance level check
orp diff <file1> <file2>     # Compare two documents
```

### Example Output

```
============================================================
ORP Validation Report: my-proposal.yaml
============================================================

✓ Valid

Compliance Level: ORP-Basic

Warnings:
  1. Document is ORP-Basic. Add L2 (Consequence Simulation) and
     L3 (Empathy Mapping) for ORP-Standard.

Summary:
  Document is valid and meets ORP-Basic requirements.
============================================================
```

### Python API

```python
from orp_validator import validate

result = validate("my-proposal.yaml")

if result.valid:
    print(f"✓ Valid! Compliance: {result.compliance_level.value}")
else:
    for error in result.errors:
        print(f"Error: {error}")
```

---

## Worked example

The Danish Property Tax Reform proposal published alongside this repository is the first worked example of an ORP-compliant policy document. It demonstrates all five layers in practice and shows how a complex policy debate can be made transparent, simulatable, and forkable.

[Read the Danish Property Tax Reform →](examples/danish_property_tax_reform.md)

---

## Who is this for?

- **Governments and policymakers** who want to publish proposals in a way that builds public trust and invites rigorous scrutiny
- **Researchers and academics** who want a standardised way to document and share policy analysis
- **Journalists and civil society** who want to interrogate the assumptions behind public decisions
- **AI developers** who want to document training data provenance transparently
- **Educators** who want to teach students how reasoning actually works in complex systems
- **Citizens** who want to understand not just what was decided but why and on what basis

---

## Status

OpenReason is currently at **v0.1 draft** status. The core specification is coherent and implementable but explicitly incomplete. We are seeking critique, challenge, and contribution before ratifying v1.0.

This is intentional. A transparency protocol that is not itself transparent about its own incompleteness would contradict its founding principles.

---

## Get involved

Read [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) to understand how to propose changes, challenge assumptions, or fork the protocol in a new direction.

---

## Governance

OpenReason is not owned by any individual, company, or government. It is stewarded as a public good. See [docs/governance/GOVERNANCE.md](docs/governance/GOVERNANCE.md) for the full governance model.

---

## Project Structure

- `README.md` — This file
- `CLAUDE.md` — Context for AI assistants working on the project
- `docs/` — All documentation
  - `docs/specs/` — Protocol specification and philosophy
  - `docs/governance/` — Governance model and protocol provenance
  - `docs/sprints/` — Sprint planning and retrospectives
  - `docs/CONTRIBUTING.md` — How to contribute
  - `docs/ROADMAP.md` — Development phases and timeline
- `examples/` — Worked examples of ORP-compliant documents
- `schemas/` — JSON Schema for ORP documents
- `orp_validator/` — Python validator package
- `tests/` — Test suite

---

## Development

### Setup

```bash
# Clone the repository
git clone git@gitlab.com:publicreason/orp.git
cd orp

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest tests/ -v --cov=orp_validator
```

### Validate an ORP Document

```bash
orp-validate examples/danish_property_tax_reform.md --verbose
```

---

*OpenReason is grounded in Rational, Empathy-Informed Ethics (REE). The philosophical foundation is documented separately in docs/specs/REE_PHILOSOPHY.md and is itself open to scrutiny and challenge under the same principles.*
