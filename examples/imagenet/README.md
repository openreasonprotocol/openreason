# ImageNet ILSVRC-2012: ORP-Full Example

## Overview

This directory contains an ORP-Full analysis of **ImageNet ILSVRC-2012** (ImageNet-1K), the most influential training dataset in AI history. Created 2009-2012 at Princeton and Stanford under Fei-Fei Li's leadership, this dataset enabled the deep learning revolution following AlexNet's 2012 breakthrough.

## Why ImageNet?

ImageNet was chosen as OpenReason's second worked example (after Danish Property Tax Reform) to demonstrate:

1. **Cross-domain applicability**: ORP works for AI training data, not just policy
2. **Constitutive problem in AI**: Dataset creation decisions in 2009 shaped AI systems for a decade
3. **Absent node visibility**: Multiple stakeholder groups (AMT workers, depicted individuals, non-Western communities) systematically excluded from governance
4. **Post-hoc remediation costs**: Removing 600,000 images in 2019 much harder than inclusive design in 2009

## What This Example Demonstrates

### Layer 1: Data Provenance
- **Funding sources**: NSF, Google, Intel, Microsoft, Yahoo!
- **Collection methodology**: Web scraping → WordNet taxonomy → AMT annotation
- **Documented exclusions**: Photos only (no art), NSFW filtered, resolution threshold
- **Structural exclusions**: 80%+ Western images, English-language bias, socioeconomic bias
- **Post-publication cleaning**: 1,593 offensive person categories removed (2019)

### Layer 2: Consequence Simulation
Four scenarios comparing actual ImageNet constitution with alternatives:
- **S1 (Actual)**: WordNet + Western web scraping → 10-20pp bias in non-Western contexts
- **S2 (Global Sampling)**: Hypothetical proportional geographic distribution
- **S3 (Worker Governance)**: AMT workers with consultative voice
- **S4 (Consent-Based)**: Opt-in only from depicted individuals

### Layer 3: Empathy Mapping
Eight stakeholder groups identified, four as **absent nodes**:
- ✅ Represented: Dataset creators, funders, AI researchers
- ❌ **Absent nodes**: AMT workers (49,000), depicted individuals (millions), non-Western communities (billions), demographic minorities

**Minority stress test**: Black women face 2-5x higher facial recognition error rates (Gender Shades study)

### Layer 4: Accountability Ledger
Six major constitutive decisions documented:
1. WordNet as taxonomy source (2007) → inherited derogatory terms
2. Amazon Mechanical Turk for annotation (2008) → labor exploitation critique
3. Multiple-annotator quality control (2009) → 99.7% precision but ~5-10% noise
4. ILSVRC 1,000-category subset (2010) → standard benchmark
5. Public release with registration (2009-2010) → tracking vs openness trade-off
6. Offensive label removal (2019) → post-hoc remediation after public exposure

### Layer 5: Fork Registry
Four existing forks documented:
- **ImageNet-V2** (2019): New test set → 11-14% accuracy drop (distribution shift)
- **ImageNet-R** (2021): Artistic renditions → poor performance (texture bias)
- **Cleaned Labels** (2021): Fixed 6% annotation errors in validation set
- **Removed Person Categories** (2019): Ethical content moderation

Three potential forks proposed:
- **Global Representative ImageNet**: Proportional geographic sampling
- **Consent-Based ImageNet**: Opt-in only from depicted individuals
- **Worker Co-Governed ImageNet**: AMT workers with governance voice

## Methodology

### Post-Hoc Reconstruction
**Critical limitation**: This is **retrospective analysis**, not real-time governance.

- ImageNet created 2007-2012, before ORP existed (v0.1 draft published 2026)
- Decisions reconstructed from published sources, not internal records
- Cannot verify unpublished deliberations
- Demonstrates what ORP *would* capture if applied prospectively

### Sources
Primary documentation from:
- Deng et al. (2009): Original ImageNet paper
- Russakovsky et al. (2015): ILSVRC Challenge paper
- Crawford & Paglen (2021): "Excavating AI" (constitutive critique)
- Prabhu & Birhane (2021): "Large image datasets: A pyrrhic win"
- Yang et al. (2020): Dataset bias mitigation (by ImageNet creators)

All claims cited in `research_notes.md`.

### Not Critique of Creators
**Important**: This analysis is **descriptive**, not accusatory.

- Fei-Fei Li and team made principled decisions within 2009 constraints
- Ethical standards evolved 2009-2026 (retroactive judgment unfair)
- ImageNet's transformative benefits are undeniable (deep learning revolution)
- Purpose: demonstrate *system-level* transparency needs, not individual failings

## How This Differs from Existing Documentation Standards

### vs. Datasheets for Datasets (Gebru et al., 2018)
- **Datasheets**: Templates for dataset documentation (motivation, composition, collection, preprocessing)
- **ORP adds**: Constitutive decisions (Layer 4), stakeholder impacts (Layer 3), fork registry (Layer 5)

### vs. Model Cards (Mitchell et al., 2019)
- **Model Cards**: Model-level documentation (performance, limitations, ethical considerations)
- **ORP scope**: Dataset-level (ImageNet), not model-level (ResNet, VGG)

### vs. FAIR Data Principles
- **FAIR**: Findability, Accessibility, Interoperability, Reusability (technical metadata)
- **ORP adds**: Governance transparency (who decided, why, alternatives considered)

## Key Findings

### Transformative Benefits, Unequal Distribution
ImageNet enabled:
- ✅ Deep learning revolution (AlexNet 2012 → <5% error by 2017)
- ✅ Medical imaging, accessibility tools, scientific research
- ✅ Most-cited dataset in computer vision

But benefits distributed unequally:
- ❌ AMT workers: Low wages (~$0.01-$0.10/task), no credit, no governance voice
- ❌ Depicted individuals: No consent, some offensive labels pre-2019
- ❌ Non-Western populations: 10-20pp higher error rates in deployed systems
- ❌ Demographic minorities: Biased facial recognition → civil rights harms

### Absent Nodes Bear Disproportionate Costs
Groups excluded from dataset governance experienced systematic harms:
- **49,000 AMT workers**: Invisible labor, cultural backgrounds shaped annotations but no voice
- **Millions depicted**: Privacy violations, offensive labels (54% of person categories problematic)
- **Billions in Global South**: Western visual culture generalized as "universal"

### Post-Hoc Remediation Insufficient
2019 offensive label removal addressed symptoms, not root cause:
- Millions of models trained 2012-2019 retain offensive associations
- Retraining all downstream models infeasible
- Proactive inclusion (2009) would have caught issues before 7 years of deployment

## Files in This Directory

### `imagenet_training_data.yaml` (1,513 lines)
The complete ORP-Full document with all five layers.

**Status**: Substantively complete but schema alignment in progress (v0.1 draft schema evolved during writing).

### `research_notes.md` (744 lines)
Background research with:
- Primary source citations (papers, reports)
- Funding documentation
- Timeline of controversy (2009-2021)
- Stakeholder analysis
- Decision history

All claims in the ORP document sourced here.

## How to Use This Example

### For AI Dataset Creators
Before building the next ImageNet:
1. **Layer 1**: Document exclusion criteria (implicit and explicit)
2. **Layer 3**: Identify absent nodes *before* publication (who has no voice?)
3. **Layer 4**: Log major decisions with alternatives considered (not just outcomes)
4. **Layer 5**: Enable forking (someone will disagree—give them infrastructure to show alternatives)

### For Policymakers
Regulating AI training data (EU AI Act, etc.):
- ORP makes dataset governance transparent and auditable
- Absent nodes (L3) reveal who bears risks without representation
- Decision ledger (L4) enables accountability for harms

### For Researchers
Studying dataset bias:
- ORP framework structures analysis (5 layers cover provenance → impacts → governance)
- Fork registry (L5) tracks how datasets evolve through critique

### For Students
Learning responsible AI:
- ImageNet as case study: transformative technology + systematic exclusions
- ORP demonstrates: technical decisions are *always* political decisions
- Absent nodes are not edge cases—they're *constitutive* of dataset limitations

## Comparison to Danish Property Tax Example

| Dimension | Danish Tax Reform | ImageNet Training Data |
|-----------|-------------------|------------------------|
| **Domain** | Policy (taxation) | AI (training data) |
| **Compliance** | ORP-Full | ORP-Full |
| **Geographic Scope** | National (Denmark) | Global (but 80% Western) |
| **Stakeholder Scale** | ~3M Danish homeowners | Billions (downstream AI users) |
| **Primary Absent Node** | Low-income homeowners | AMT workers, non-Western communities |
| **Temporal Scope** | Prospective (proposed reform) | Retrospective (2009-2012 dataset) |
| **Key Insight** | Tax policy = wealth redistribution → simulate impacts | Dataset constitution → decade of AI bias |
| **Fork Type** | Policy alternatives (different tax rates) | Data alternatives (different exclusions) |

Both examples demonstrate: **constitutive decisions shape outcomes for years** → transparency at decision-making layer crucial.

## Known Limitations

1. **Post-hoc analysis**: Cannot verify internal deliberations, only published sources
2. **Attester not creator**: Document written by analyst, not ImageNet team (acknowledged in L1 attestation)
3. **Incomplete outcome data**: Some L2 scenarios hypothetical (counterfactual never tested)
4. **Schema evolution**: v0.1 draft schema finalized during document writing; some structural adjustments pending

## Contributing

If you believe:
- Different taxonomy source would reduce bias (not WordNet)
- Geographic sampling should be proportional (not 80% Western)
- AMT workers should have governance voice
- Consent from depicted individuals should be required
- Alternative dataset constitution would better balance ethics and AI progress

**Fork this document.** Change L1 exclusion criteria, L2 scenarios, L3 stakeholder analysis, L4 decisions. The diff between your fork and this document makes your proposal explicit and debatable.

## Citation

If referencing this example:

```
Asbjørn (2026). ImageNet ILSVRC-2012: Constitution of a Foundation AI Training Dataset (ORP-Full).
OpenReason Project. https://github.com/publicreason/open-reason/examples/imagenet/
```

For ImageNet itself:
```
Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., & Fei-Fei, L. (2009).
ImageNet: A Large-Scale Hierarchical Image Database.
2009 IEEE Conference on Computer Vision and Pattern Recognition, 248-255.
```

## License

This ORP documentation: **CC-BY 4.0** (Creative Commons Attribution)

ImageNet dataset: Separate license (non-commercial research use, registration required). See https://www.image-net.org/

---

**Questions or feedback?** Open an issue at https://github.com/publicreason/open-reason/issues

**Want to apply ORP to your dataset?** See docs/CONTRIBUTING.md
