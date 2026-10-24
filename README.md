# OpenReason (ORP)

[![Website](https://img.shields.io/website?url=https%3A%2F%2Fdocs.publicreasonproject.org&label=docs)](https://docs.publicreasonproject.org)
[![PyPI version](https://badge.fury.io/py/orp-validator.svg)](https://badge.fury.io/py/orp-validator)
[![Python Support](https://img.shields.io/pypi/pyversions/orp-validator.svg)](https://pypi.org/project/orp-validator/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![GitLab Pipeline](https://gitlab.com/publicreason/orp/badges/main/pipeline.svg)](https://gitlab.com/publicreason/orp/-/pipelines)

**Repositories:** [GitHub](https://github.com/openreasonprotocol/openreason) (public mirror) · [GitLab](https://gitlab.com/publicreason/orp) (CI, merge requests) · **Site:** [openreasonprotocol.org](https://openreasonprotocol.org) · **Founded by** the [Public Reason Project](https://publicreasonproject.org)

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

ORP is structured in five layers. See [docs/specs/ORP_V0.2_SPEC.md](docs/specs/ORP_V0.2_SPEC.md) for the full v0.2 specification, or [docs/specs/ORP_SPEC.md](docs/specs/ORP_SPEC.md) for the original v0.1 spec.

| Layer | Name | Purpose |
|-------|------|---------|
| L1 | Data Provenance | Document data origin, cleaning, exclusions, and synthetic elements |
| L2 | Consequence Simulation | Define affected population, variables, outcome metrics, and weightings |
| L3 | Empathy Mapping | Identify all stakeholders, model differential impacts, stress-test minority interests |
| L4 | Accountability Ledger | Immutable log of who decided what, when, and on what basis |
| L5 | Fork and Propose | Standardised mechanism for proposing alternative assumptions and publishing diffs |

---

## Formats

ORP documents can be represented in multiple machine-readable formats:

### YAML/JSON (Primary)
Human-readable format validated against JSON Schema. All CLI tools and examples use YAML by default.

### JSON-LD (Semantic Web)
**NEW**: ORP documents can be represented as JSON-LD for semantic web integration:
- Maps to W3C standards (PROV-O, DCAT, Dublin Core, Schema.org)
- Enables knowledge graph integration and cross-document SPARQL querying
- Store in triple stores (Apache Jena Fuseki, GraphDB)
- Query stakeholders, datasets, and decisions across all ORP documents

**Example**: `examples/danish_property_tax_reform.jsonld`
**Guide**: `orp_validator/schemas/JSON_LD_GUIDE.md`

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

## Worked Examples

OpenReason includes **5 complete ORP-Full reference implementations** demonstrating cross-domain applicability:

### 1. Danish Property Tax Reform (Policy Domain, v0.1)
A comprehensive policy proposal replacing Denmark's property tax system with a Land Value Tax + smoothed profit tax. Demonstrates prospective policy analysis with simulated impacts on 3 million Danish homeowners.

**Validate it yourself:**
```bash
pip install orp-validator
orp validate examples/danish_property_tax_reform.yaml
# ✓ Valid - Compliance Level: ORP-Full
```

[View the proposal →](examples/danish_property_tax_reform.yaml) | [Read the explanation →](examples/danish_property_tax_reform.md)

### 2. ImageNet Training Data (AI Domain, v0.2, 1,513 lines)
A retrospective analysis of how ImageNet ILSVRC-2012—the most influential AI training dataset—was constituted. Documents funding sources, collection methodology, absent stakeholders (49,000 AMT workers, depicted individuals), and how 2009 decisions shaped a decade of AI bias.

**Key findings:**
- 80%+ Western images → 10-20pp accuracy drop on non-Western test sets
- 54% of person categories (1,593 labels) later found offensive, removed 2019
- Post-hoc remediation cannot undo millions of models trained 2012-2019

[View the analysis →](examples/imagenet_training_data.yaml) | [Read the methodology →](examples/imagenet/README.md)

### 3. LAION-5B Training Data (AI Domain, v0.2, 2,162 lines)
Post-hoc analysis of the 5.85 billion image-text pair dataset that trained Stable Diffusion. Documents critical undocumented exclusions: 3,226 CSAM URLs discovered post-publication (Stanford 2023), medical privacy violations, non-consensual intimate imagery.

**Key findings:**
- No CSAM filtering applied pre-publication (PhotoDNA not integrated)
- Federated URL structure prevents remediation (cached images remain despite URL removal)
- Post-hoc reconstruction demonstrates accountability gaps in real-world datasets

[View the analysis →](examples/laion5b_training_data.yaml)

### 4. Common Crawl Training Data (AI Domain, v0.2, 2,232 lines)
Analysis of the 250+ billion page web corpus underlying GPT, Claude, Gemini, and other LLMs. Documents linguistic extinction cascade: 70%+ English content despite 20% world population, <0.1% representation for 6,900+ languages.

**Key findings:**
- Digital absence accelerates language extinction (Kornai 2013 "digital language death")
- Tier 1 existential harm: 3,500-6,300 languages at risk by 2100
- Counterfactual scenarios show global sampling would reduce harm at 2.5x cost

[View the analysis →](examples/common_crawl_training_data.yaml)

### 5. GitHub Copilot Training Data (AI Domain, v0.2, 2,421 lines)
Post-hoc analysis of code training data including GPL-licensed code. Documents license violations, economic harm to open source developers, deontological vs utilitarian welfare assessment.

**Key findings:**
- GPL code used in proprietary model (copyleft violation debate)
- $8.6B economic displacement (Stack Overflow revenue decline)
- Extension demonstrates `orp-license-v1` compliance tracking

[View the analysis →](examples/github_copilot_training_data.yaml)

**Total**: 8,328 lines of validated ORP v0.2 documentation across 5 domains

---

## How ORP Relates to Existing Standards

ORP doesn't replace existing data governance frameworks like GDPR, EU AI Act, W3C PROV, ISO 19115, Model Cards, or Datasheets. **It complements them** by addressing the constitutive layer — the decisions made during data production that determine what the data represents, whose interests shaped it, and what was excluded.

**Read the full analysis:** [ORP vs Existing Standards (docs/analysis/ORP_vs_existing_standards.md)](docs/analysis/ORP_vs_existing_standards.md)

This comprehensive comparison document shows:
- What each existing standard does well (genuine achievements)
- What constitutive-layer gaps each standard doesn't address
- How ORP fills those gaps without duplicating existing requirements
- **5 integration pathways** showing how organizations already compliant with existing standards can adopt ORP incrementally (2-6 weeks pilot effort)

**Key finding:** All existing standards focus downstream of data constitution. ORP is the first framework to systematically address how data came to exist, whose interests shaped it, what was excluded, and how to contest those decisions.

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

OpenReason is currently at **v0.2 draft** status. The protocol now supports post-hoc reconstruction, domain-specific extensions, and flexible schema validation while maintaining full backward compatibility with v0.1.

This is intentional. A transparency protocol that is not itself transparent about its own incompleteness would contradict its founding principles.

---

## Version History

### v0.2.0 (2026-04-08) — Post-Hoc Reconstruction & Extensions

**New Features:**
- **Post-hoc reconstruction support**: `post_hoc` flag allows retrospective analysis when decision-making history is unavailable
- **Extension system**: Domain-specific fields (orp-ai-training-v1, orp-safety-v1, orp-license-v1)
- **Granular confidence levels**: 7-point scale (very-high to very-low) for uncertainty quantification
- **Accountability gap documentation**: Explicit WHO/WHY/WHAT unknowns in Layer 4
- **Flexible schema**: `additionalProperties: true` throughout—documents evolve richer structures naturally

**Enhanced Fields:**
- New author roles: `analyst`, `reconstructor` for post-hoc analysis
- `critical_undocumented_exclusions` (L1): Document post-hoc discovered gaps
- `comparison_to_actual` (L2): Counterfactual analysis
- `highest_severity_harm` (L3): Harm tier classification
- Rich object formats: benefits/harms can be simple strings or detailed objects

**Empirical Validation:**
- Validated against 4 comprehensive AI training dataset examples (8,328 lines total)
- ImageNet, LAION-5B, Common Crawl, GitHub Copilot all validate successfully
- 311 validation errors discovered in v0.1 → 0 errors in v0.2 (100% success rate)

**Breaking Changes**: None—v0.2 is fully backward compatible with v0.1

**Documentation:**
- [ORP v0.2 Specification](docs/specs/ORP_V0.2_SPEC.md) (comprehensive 16-section spec)
- [Migration Guide](docs/specs/MIGRATION_V0.1_TO_V0.2.md) (v0.1 → v0.2 upgrade path)
- [Design Document](docs/specs/ORP_V0.2_DESIGN.md) (design philosophy and rationale)

### v0.1.0 (2026-01-15) — Initial Release

**Core Features:**
- 5-layer transparency framework (Data Provenance, Consequence Simulation, Empathy Mapping, Accountability Ledger, Fork Registry)
- JSON Schema validation (Draft-07)
- CLI validator with `new`, `validate`, `check`, `diff` commands
- Compliance levels: ORP-Basic, ORP-Standard, ORP-Full
- Danish Property Tax Reform example (ORP-Full)

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
  - `docs/analysis/` — Comparative analysis (ORP vs existing standards)
  - `docs/academic/` — Academic papers and theoretical foundations
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
git clone https://github.com/openreasonprotocol/openreason.git   # or git@gitlab.com:publicreason/orp.git
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
orp validate examples/danish_property_tax_reform.yaml
```

### Run Linting

```bash
black orp_validator/ tests/
ruff check orp_validator/ tests/
mypy orp_validator/
```

### Continuous Integration

The project uses GitLab CI/CD for automated testing, linting, and releases:
- **Tests**: Run on Python 3.9, 3.10, 3.11, 3.12
- **Coverage**: Reports generated for each commit
- **Releases**: Automated package building on tags
- **PyPI**: Manual deployment trigger for tagged releases

See `.gitlab-ci.yml` for pipeline configuration.

---

*OpenReason is grounded in Rational, Empathy-Informed Ethics (REE). The philosophical foundation is documented separately in docs/specs/REE_PHILOSOPHY.md and is itself open to scrutiny and challenge under the same principles.*
