# Contributing to OpenReason

OpenReason only works if it is genuinely open — to scrutiny, challenge, improvement, and disagreement. This document explains how to engage with the protocol, whether you want to propose a change, challenge an assumption, fork a document, or start something new.

---

## The spirit of contribution

OpenReason is not a finished product seeking validation. It is a working hypothesis seeking stress-testing. The most valuable contributions are not those that agree — they are those that find the weaknesses, the contradictions, and the edge cases the original authors missed.

If you think something is wrong, say so clearly and show your reasoning. If you think something is missing, propose it specifically. If you think the whole framing is off, fork it and show us what better looks like.

The only contribution that is not welcome is one that obscures rather than clarifies — that adds complexity without purpose, or asserts without reasoning.

---

## Ways to contribute

### 1. Critique an existing document

The most important contribution is rigorous challenge. If you find an assumption that is undocumented, an exclusion that is unjustified, a simulation that does not hold up, or a stakeholder that has been made invisible — document it clearly.

A good critique includes:

- **The specific claim or decision you are challenging** — reference the layer and field
- **Why you believe it is wrong or incomplete** — with reasoning and ideally evidence
- **What the impact of the error is** — how does it affect the conclusions
- **What you think should be there instead** — or at minimum, what questions need to be answered

Critiques can be submitted as issues in the repository or as formal response documents registered in the original document's L5 Fork Registry.

---

### 2. Fork a document

Forking is the core mechanic of OpenReason. If you disagree with assumptions in an existing document, the right response is not just to say so — it is to show what the document looks like with your assumptions instead.

A fork must:

- Reference the original document's `document_id` in the `forked_from` field
- Declare compliance with the same ORP level as the original or higher
- Document clearly in L5 what was changed and why
- Not misrepresent the original — the diff should be honest about what stayed the same

A fork does not require permission. It is an inherent right under the protocol.

---

### 3. Propose a protocol extension

ORP v0.1 defines a core schema. Domain-specific extensions are expected and welcome — for AI training data, environmental impact, healthcare policy, economic modelling, and other domains where the core schema needs additional structure.

An extension proposal should:

- Identify the domain it addresses
- Explain what the core schema cannot express that this extension adds
- Define new fields using the same YAML schema conventions as the core spec
- Show backwards compatibility — a document using the extension must still validate against the core schema
- Include at least one worked example

Extensions are reviewed by the working group before being accepted into the official spec. Rejected extensions can be published independently as community extensions.

---

### 4. Contribute a worked example

The protocol is only credible if it can be applied to real cases. Worked examples — ORP-compliant documents covering real policy proposals, AI training decisions, or governance choices — are as valuable as improvements to the spec itself.

The Danish Property Tax Reform included in this repository is the first worked example. We are looking for examples from:

- Different policy domains — healthcare, education, climate, housing, taxation
- Different geographic contexts — the spec should not be implicitly Euro-centric
- AI and data contexts — training data documentation, model cards, data provenance records
- Sub-national contexts — city-level and regional policy decisions

A worked example should be ORP-Basic compliant at minimum and ideally ORP-Standard or ORP-Full.

---

### 5. Improve the specification itself

If you believe a core field is missing, a definition is ambiguous, a required field is unnecessary, or the structure could be improved — propose it.

Specification changes require:

- A clear statement of the problem with the current spec
- A proposed change with revised field definitions
- An assessment of backwards compatibility
- At least one example showing the change in practice

Breaking changes to the core schema require broader consensus and will be reserved for major version increments.

---

## What makes a good contribution

Regardless of type, good contributions share these qualities:

**Specific** — "L1 does not adequately address the case where multiple datasets with conflicting coverage are merged" is actionable. "The data section could be better" is not.

**Reasoned** — explain why, not just what. The reasoning is more valuable than the conclusion because it can be challenged, improved, and generalised.

**Honest about uncertainty** — if you are not sure whether your critique is correct, say so. Tentative but specific is more valuable than confident but vague.

**Constructive** — the goal is to improve the protocol, not to win an argument. If you can propose a solution alongside a critique, do so.

---

## What we are specifically looking for in v0.1

The following are known gaps and open questions in the current specification. Contributions addressing these are particularly welcome:

- **Governance model** — how should decisions about the protocol itself be made? Who has authority to ratify changes? How are conflicts resolved?
- **Automated validation** — what does machine-readable validation of ORP compliance look like in practice?
- **Synthetic data standards** — L1 requires documentation of synthetic elements but does not specify what adequate documentation looks like. This needs to be more precise.
- **Empathy mapping methodology** — L3 defines what should be documented but not how to conduct the stakeholder analysis in the first place
- **Non-Western policy contexts** — the current worked example is Danish. The spec should be tested against governance contexts with different institutional structures
- **AI training data application** — a formal extension of ORP for documenting AI training data provenance, cleaning decisions, and synthetic data generation

---

## Code of conduct

OpenReason exists to improve the quality of public reasoning. Contributions should reflect that purpose.

Challenge ideas, not people. Disagree with reasoning, not with identity. Be specific, be honest, be direct — and be willing to be wrong.

---

## Getting started

1. Read [README.md](README.md) for project overview
2. Read [ORP_SPEC.md](ORP_SPEC.md) for the technical specification
3. Read [REE_PHILOSOPHY.md](REE_PHILOSOPHY.md) for the underlying principles
4. Look at the worked example in `examples/`
5. Identify where you want to contribute and follow the relevant guidance above

---

*If you are unsure whether your contribution is appropriate or how to frame it, open a discussion before investing significant time. The goal is useful engagement, not gatekeeping.*
