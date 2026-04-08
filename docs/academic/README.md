# Academic Papers and Theoretical Foundations

This directory contains academic papers and theoretical work that articulate the philosophical and conceptual foundations of the OpenReason Protocol.

## Contents

### The Manifesto
- **manifesto_openreason.md** - Public-facing manifesto: "The Data Is Lying to You — And Nobody Is Responsible For It"

### Research Paper: "Data Before Models"

A comprehensive academic paper presenting the theoretical case for provenance-grounded data governance.

**Proposed title:** *Data Before Models: Epistemic Transparency, Incentive Distortion, and the Case for Provenance-Grounded Governance*

**Alternative title:** *Whose Experiences Populate the Nodes: A Foundational Critique of Data Governance and a Protocol for Epistemic Accountability*

**Target word count:** 4,500–5,000 words (excluding abstract and bibliography)

**Paper structure:**
- **abstract_and_bibliography.md** - Abstract, bibliography, and submission metadata
- **section1_introduction.md** - The Premature Critique
- **section2_constitutive_problem.md** - The Constitutive Problem in Data
- **section3_existing_frameworks.md** - Why Existing Frameworks Miss It — and Why That Matters
- **section4_REE_foundation.md** - Rational, Empathy-Informed Ethics as Philosophical Foundation
- **section5_ORP_operationalization.md** - The OpenReason Protocol as Operationalization of REE
- **section6_implications_limits.md** - Implications, Limits, and Open Questions

## Core Arguments

### The Constitutive Problem in Data

The paper argues that contemporary data governance frameworks (GDPR, algorithmic accountability, open data, fairness-aware ML) share a fundamental flaw: they treat data as a pre-ethical given and focus ethical attention downstream of data production.

The **constitutive problem** is the systematic encoding of interests, exclusions, and assumptions into data assets through:
- **Scope capture** - funding interests shaping what gets measured
- **Publication bias** - inconvenient findings disappearing from the record
- **Exclusion by design** - systematic omission of certain populations/perspectives
- **The absent node problem** - inferential structures built on non-representative samples

### REE as Philosophical Foundation

**Rational, Empathy-Informed Ethics (REE)** provides the philosophical framework for addressing the constitutive problem through five principles:

1. **Measured Compassion** - claims about welfare must be testable with evidence
2. **Rational Inquiry** - assumptions are hypotheses subject to challenge
3. **Simulated Consequences** - model downstream effects before finalizing decisions
4. **Universal Sentience** - no affected stakeholder should be invisible
5. **Transparent Accountability** - decisions must be documented, attributed, auditable

See `docs/specs/REE_PHILOSOPHY.md` for the full philosophical specification.

### ORP as Operationalization

The **OpenReason Protocol** implements REE's philosophical architecture as a five-layer procedural framework:

- **Layer 1: Data Provenance** → operationalizes Rational Inquiry & Transparent Accountability
- **Layer 2: Consequence Simulation** → operationalizes Simulated Consequences
- **Layer 3: Empathy Mapping** → operationalizes Measured Compassion & Universal Sentience
- **Layer 4: Accountability Ledger** → operationalizes Transparent Accountability (decision level)
- **Layer 5: Fork Registry** → operationalizes Rational Inquiry (social level)

See `docs/specs/ORP_SPEC.md` for the full protocol specification.

## Target Venues

**Primary (journals):**
- *AI & Society* (Springer) - interdisciplinary, receptive to philosophical-technical integration
- *Big Data & Society* (SAGE) - explicit focus on social and ethical dimensions of data
- *Philosophy & Technology* (Springer) - appropriate for REE philosophical positioning

**Secondary (conferences):**
- FAccT (ACM Conference on Fairness, Accountability, and Transparency)
- CPDP (Computers, Privacy and Data Protection), Brussels

## Relationship to Project Documentation

The academic papers provide the theoretical justification for the protocol specifications:

```
Academic Foundation          →    Technical Implementation
├── manifesto_openreason.md  →    Public communication
├── REE philosophy (paper)   →    docs/specs/REE_PHILOSOPHY.md
├── ORP architecture (paper) →    docs/specs/ORP_SPEC.md
└── Case study (paper)       →    examples/danish_property_tax_reform.yaml
```

## Version History

- **v0.1** - Initial full draft, all sections (April 2026)

## Status

**Draft v0.1** - All sections complete and ready for review. Not yet submitted for publication.

## Contact

For questions about the academic work or potential collaborations:
- Email: hello@publicreasonproject.org
- Documentation: https://docs.publicreasonproject.org
