# OpenReason Roadmap

This document outlines the planned development of the OpenReason ecosystem — from the core protocol through tooling, agents, side protocols, and integrations. It is a living document and is itself subject to the OpenReason principle of transparent, forkable reasoning. If you disagree with the sequencing or priorities, open a discussion or fork it.

---

## Philosophy of sequencing

Good open source infrastructure earns adoption in layers. The protocol must be implementable manually before tooling is built. Tooling must be stable before agents are layered on top. Agents must be trustworthy before integrations embed them in critical workflows.

Skipping layers produces fragile ecosystems. Each phase below must be genuinely complete before the next begins — not feature-complete, but stable enough that contributors can build on it without fear of breaking changes underneath them.

---

## Phase 0 — Foundation (current)
*Status: In progress*

The protocol specification and philosophical foundation. No tooling yet. The goal of Phase 0 is to produce documents that are coherent enough to invite rigorous challenge before any code is written.

- [x] ORP v0.1 specification (`ORP_SPEC.md`)
- [x] REE philosophical foundation (`REE_PHILOSOPHY.md`)
- [x] README and project overview
- [x] CONTRIBUTING guide
- [ ] First worked example — Danish Property Tax Reform formatted as ORP-compliant document
- [ ] ORP_META.md — the protocol's own provenance, documented under ORP
- [ ] Governance model v0.1 — how decisions about the protocol are made
- [ ] Public comment period — minimum 60 days open for community challenge before Phase 1 begins

---

## Phase 1 — Core Tooling
*Target: v0.2*

The minimum viable toolkit that makes ORP documents easy to produce, validate, and compare. No agents yet. No integrations. Just clean, reliable tools that prove the protocol works in practice.

### 1.1 ORP CLI (`orp`)

A command-line tool that scaffolds, validates, and diffs ORP documents.

```bash
# Scaffold a new ORP document
orp new --title "My Policy Proposal" --domain policy --compliance standard

# Validate an existing document
orp validate proposal.yaml

# Compare two documents and show where they diverge
orp diff original.yaml fork.yaml

# Check what compliance level a document meets
orp check proposal.yaml

# Generate a human-readable summary from an ORP document
orp summarise proposal.yaml --audience general
```

Core commands:
- `orp new` — interactive scaffolding wizard with field prompts and examples
- `orp validate` — schema validation with clear, actionable error messages
- `orp diff` — human-readable diff showing exactly where two documents diverge
- `orp check` — compliance level assessment (Basic / Standard / Full)
- `orp summarise` — plain-language summary generation for non-technical audiences

### 1.2 ORP Validator

A standalone validation library that can be embedded in other tools without requiring the full CLI. Available as:
- Python package (`pip install orp-validator`)
- JavaScript/Node package (`npm install orp-validator`)
- REST endpoint (hosted, for integrations that cannot run local tooling)

Validation produces structured output with:
- Compliance level achieved
- Missing required fields
- Fields present but flagged as thin or likely incomplete
- Suggestions for strengthening weak sections

### 1.3 ORP Schema

The formal JSON Schema and YAML Schema definitions for ORP documents. Versioned and published independently so validators, editors, and agents can reference them without depending on the full toolchain.

### 1.4 Reference implementation

A fully worked ORP-Full compliant document produced using only Phase 1 tooling, demonstrating that the protocol is implementable without agents or automation. The Danish Property Tax Reform is the planned reference implementation.

---

## Phase 2 — Developer Experience
*Target: v0.3*

Making ORP feel native to existing developer workflows. The goal is zero friction adoption — a developer who already uses GitLab and VS Code should be able to work with ORP documents without learning new tools.

### 2.1 GitLab integration

- ORP document templates for GitLab repositories
- GitLab CI pipeline that validates ORP compliance on merge requests
- Automatic fork registry updates when a document is forked via merge request
- Issue templates for critique and amendment proposals

### 2.2 VS Code extension

- Schema-aware autocomplete for ORP YAML documents
- Inline validation with error highlighting
- Field documentation on hover
- Compliance level indicator in status bar

### 2.3 ORP Registry

A public registry of ORP-compliant documents — searchable by domain, compliance level, author, and topic. Forks and responses are linked automatically. Think of it as the public ledger that makes the fork mechanic visible and navigable.

### 2.4 ORP Viewer

A clean web interface for reading ORP documents without requiring technical knowledge. Renders the five layers in plain language, shows the fork tree, and links to related documents. The interface for non-technical stakeholders — politicians, journalists, students, citizens.

---

## Phase 3 — Agent Layer
*Target: v1.0*

AI-assisted tooling that dramatically reduces the cost of producing high-quality ORP documents. The agents do the research and drafting. Humans review, challenge, and attest.

**Critical principle:** Agents assist, they do not attest. Every field produced by an agent must be reviewed and signed off by a human before a document reaches ORP-Standard or ORP-Full compliance. The attestation mechanism in L4 enforces this structurally.

### 3.1 Provenance Agent (L1)

Given a policy domain and a brief description of the proposal, the Provenance Agent:
- Identifies datasets commonly used in this domain
- Researches their known limitations and coverage gaps
- Flags likely exclusions based on domain knowledge
- Drafts L1 with sources cited for human review

This is the most valuable agent because L1 is where most documents are currently weakest and where the most important bias lives.

### 3.2 Simulation Agent (L2)

Given a policy proposal and variable definitions, the Simulation Agent:
- Identifies standard modelling approaches for this domain
- Suggests affected population segments and sizing estimates
- Runs basic scenario analysis where data is available
- Flags assumptions that require explicit human decision

### 3.3 Empathy Mapping Agent (L3)

Given a proposal and an affected population definition, the Empathy Mapping Agent:
- Identifies stakeholder groups including non-obvious minorities
- Estimates differential impacts across scenarios
- Flags groups whose impacts could not be adequately modelled
- Prompts for explicit minority stress-testing

### 3.4 ORP Assistant

A conversational interface for producing ORP documents — an AI that asks the right questions in the right order, explains why each field matters, and helps users think through the implications of their choices. The assistant mode for users who find the CLI intimidating.

Designed specifically for:
- Politicians and policy staff without technical backgrounds
- Students using ORP in educational contexts
- Journalists investigating the reasoning behind public decisions

### 3.5 Fork Analyser

Given two ORP documents (original and fork), the Fork Analyser:
- Identifies the specific assumptions that differ
- Explains in plain language why those differences matter
- Estimates how different the outcomes would be if the fork's assumptions were correct
- Generates a structured debate brief for each position

This is the tool that makes public policy disagreement locatable and productive rather than rhetorical.

---

## Phase 4 — Side Protocols
*Target: v1.x extensions*

Domain-specific extensions that add fields and methodology standards for contexts where the core schema needs more structure. All extensions are backwards compatible with the core ORP spec.

### ORP-AI (AI Training Data)

Extends L1 with fields specific to AI and machine learning:
- Dataset lineage and chain of custody
- Demographic coverage analysis and known gaps
- Synthetic data generation methodology and assumptions
- Model training decisions and their data implications
- Fine-tuning data documentation

This is the extension that directly addresses the core REE insight: bias lives in data selection and cleaning, not in algorithms. ORP-AI makes that layer auditable.

### ORP-Econ (Economic Modelling)

Extends L2 with standard econometric fields:
- Model specification and identification strategy
- Causal vs correlational claims
- Confidence intervals and sensitivity analysis
- Peer review status of underlying methodology

### ORP-Env (Environmental Impact)

Extends L2 and L3 for environmental and climate policy:
- Carbon accounting methodology
- Intergenerational impact modelling
- Ecosystem stakeholder mapping (non-human sentient beings)
- Uncertainty ranges for long-horizon projections

### ORP-Health (Healthcare Policy)

Extends L3 with healthcare-specific stakeholder fields:
- Clinical outcome measures
- Health equity analysis across demographic groups
- Access and affordability modelling

### ORP-Edu (Educational Use)

A simplified implementation profile designed for classroom use — the same five layers but with age-appropriate language, guided examples, and a scoring rubric for educational assessment. The interface between OpenReason and the policy simulation game.

---

## Phase 5 — Platform and API
*Target: v2.0*

The hosted infrastructure that makes OpenReason accessible without local tooling.

### ORP API

A REST API that accepts a policy proposal in plain text and returns a partially populated ORP document — an AI-assisted first draft across all five layers. Not authoritative, but a serious starting point in minutes rather than weeks.

```
POST /api/v1/draft
{
  "title": "Danish Property Tax Reform",
  "domain": "policy",
  "description": "A proposal combining 1% Land Value Tax with 10% smoothed profit tax...",
  "compliance_target": "standard"
}

→ Returns: Partially populated ORP document with agent-drafted fields flagged for review
```

### ORP Registry API

Programmatic access to the public document registry — search, retrieve, compare, and track forks. The infrastructure for third-party tools to build on top of.

### OpenReason for Education

A hosted platform specifically for schools and universities — classroom management, student submissions, peer review workflows, and teacher assessment tools, all built on ORP-Edu. The entry point for the next generation of policy thinkers.

### OpenReason for Government

A hosted enterprise implementation for government departments — audit trails, multi-party attestation, integration with existing document management systems, and compliance reporting for emerging regulatory requirements like the EU AI Act.

---

## What we are explicitly not building

To stay focused, the following are out of scope for the core OpenReason project:

- **A policy recommendation engine** — OpenReason exposes reasoning, it does not produce conclusions. Recommendations remain with humans.
- **A fact-checking service** — ORP documents attest to their reasoning, not to the truth of their data. External fact-checking is a separate function.
- **A voting or consensus mechanism** — OpenReason surfaces disagreement, it does not resolve it. Democratic resolution happens through existing political processes.
- **Proprietary data hosting** — the Registry indexes documents and metadata, not the underlying datasets. Data remains with its originators.

---

## How to influence the roadmap

This roadmap is an ORP document. It has assumptions, it has priorities, and it will be wrong about some things. The right response to disagreement is not a comment — it is a fork.

If you believe Phase 3 should come before Phase 2, fork this document and show your reasoning. If you think ORP-AI should be in Phase 1 rather than Phase 4, make the case. The roadmap evolves through the same transparent, forkable reasoning that OpenReason is designed to enable everywhere else.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes.

---

*OpenReason Roadmap v0.1 — February 2026*
*This document is itself subject to ORP principles. Fork it.*
