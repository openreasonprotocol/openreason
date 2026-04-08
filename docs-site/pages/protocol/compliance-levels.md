# Compliance Levels

OpenReason Protocol defines three compliance levels, each building on the previous one. Choose based on your resource constraints, stakes, and audience.

## Overview

| Level | Layers | Use Case | Typical Time Investment |
|-------|--------|----------|------------------------|
| **ORP-Basic** | Layer 1 only | Initial documentation, low-stakes decisions | 2–4 hours |
| **ORP-Standard** | Layers 1–3 | Policy proposals, contested decisions | 1–2 days |
| **ORP-Full** | Layers 1–5 | High-stakes, long-term, or highly contested | 3–5 days |

## ORP-Basic (Layer 1 Only)

**What it requires:**  
- Header metadata
- Data provenance for all datasets used

**What it provides:**  
- Transparency about data sources
- Explicit documentation of exclusions and limitations
- Foundation for others to build on

**Best for:**
- Initial documentation before full analysis
- Low-stakes internal decisions
- Resource-constrained contexts
- Establishing data transparency as a baseline

**Not sufficient for:**
- Public policy proposals affecting >1000 people
- Decisions with distributional impacts across groups
- Contested proposals where stakeholders disagree

### Example Use Cases

- Internal team decision on which dataset to use for analysis
- Blog post documenting data sources for public consumption
- Preliminary documentation before full proposal
- Academic research data provenance tracking

### Creating an ORP-Basic Document

```bash
orp new my-doc.yaml --compliance basic
```

The tool will prompt you for:
- Document title and ID
- Author information
- Data provenance details (source, methodology, limitations)

**Time investment:** 2-4 hours, mostly spent documenting datasets accurately.

## ORP-Standard (Layers 1-3)

**What it requires:**  
- Everything from ORP-Basic
- Consequence simulation (L2): Model outcomes with scenarios
- Empathy mapping (L3): Identify stakeholders, test minority impacts

**What it provides:**  
- Transparent reasoning about expected outcomes
- Explicit acknowledgment of who is affected and how
- Systematic comparison of alternative scenarios
- Minority stress testing

**Best for:**
- Policy proposals affecting significant populations
- Decisions with distributional impacts
- Resource allocation with trade-offs
- AI training dataset documentation
- Proposals that will face public scrutiny

**Not sufficient for:**
- Highly contested proposals with multiple competing versions
- Long-term decisions requiring accountability tracking
- Cases where systematic forking and comparison is needed

### Example Use Cases

- Municipal budget allocation
- Healthcare policy affecting multiple stakeholder groups
- Education funding reform
- Infrastructure projects with environmental impacts
- AI model training dataset selection and documentation

### Creating an ORP-Standard Document

```bash
orp new my-doc.yaml --compliance standard
```

Additional prompts will include:
- Affected population description
- Variables to model (independent and dependent)
- Scenarios to compare
- Stakeholder identification
- Minority groups to stress-test

**Time investment:** 1-2 days, with most time spent on modeling consequences and identifying stakeholders.

## ORP-Full (All 5 Layers)

**What it requires:**  
- Everything from ORP-Standard
- Accountability ledger (L4): Track all methodological decisions
- Fork registry (L5): Document lineage, invite alternatives

**What it provides:**  
- Complete transparency and accountability
- Systematic comparison with alternative proposals
- Clear attribution of decisions to individuals
- Forkable proposal that others can modify and improve
- Full audit trail of reasoning evolution

**Best for:**
- High-stakes policy decisions (national/regional impact)
- Highly contested proposals with multiple alternatives
- Long-term decisions affecting future generations
- Cases requiring systematic comparison of competing approaches
- Decisions that will be revisited and refined over time

**Required for:**
- Government policy proposals (recommended)
- Major infrastructure investments
- Climate policy with intergenerational impacts
- Contested resource allocation decisions

### Example Use Cases

- National tax reform
- Climate policy with 20+ year horizons
- Healthcare system restructuring
- Major infrastructure projects (>$100M)
- AI governance frameworks
- Constitutional amendments or major legal reforms

### Creating an ORP-Full Document

```bash
orp new my-doc.yaml --compliance full
```

All prompts from Standard, plus:
- Decision tracking setup (who will maintain ledger)
- Forking invitation (license, contact)
- Known alternatives to document

**Time investment:** 3-5 days initially, with ongoing maintenance as decisions evolve.

## Choosing the Right Level

Ask yourself:

### Question 1: What are the stakes?

- **Low** (internal, <100 people affected) → **Basic** is sufficient
- **Medium** (public, 100-10,000 affected) → **Standard** recommended
- **High** (policy, >10,000 affected or long-term) → **Full** recommended

### Question 2: How contested is this?

- **Consensus** (general agreement) → Lower level may suffice
- **Debated** (significant disagreement) → **Standard** minimum
- **Highly contested** (multiple competing proposals) → **Full** enables systematic comparison

### Question 3: How long will this matter?

- **Short-term** (<1 year impact) → Lower level may suffice
- **Medium-term** (1-5 years) → **Standard** recommended
- **Long-term** (>5 years or intergenerational) → **Full** recommended

### Question 4: What resources do you have?

- **Limited** (hours, not days) → **Basic** to establish baseline
- **Moderate** (1-2 days available) → **Standard**
- **Adequate** (3+ days available) → **Full**

## Upgrading Between Levels

Documents can be upgraded incrementally:

```bash
# Start with Basic
orp new policy.yaml --compliance basic
# ... fill in data provenance ...

# Later upgrade to Standard
# (edit the file, add L2 and L3, change compliance_level)
orp validate policy.yaml

# Later upgrade to Full
# (add L4 and L5, change compliance_level)
orp validate policy.yaml
```

**Tip:** Start with Basic to establish data transparency, then upgrade as the proposal matures.

## Compliance Checking

Check your document's current compliance level:

```bash
orp check policy.yaml
```

Output will show:
- Which layers are present
- Current compliance level
- Guidance on reaching next level

## Common Questions

### "Must I use ORP-Full for all government decisions?"

No. Use the level appropriate to the stakes and contestation. But as a principle: **the more people affected and the longer the impact, the higher the compliance level should be.**

### "Can I mix compliance levels?"

Yes. A proposal might use ORP-Full for the main analysis but ORP-Basic for minor supporting datasets. Declare the highest level used in the `compliance_level` field.

### "What if I don't have resources for Full but the decision warrants it?"

Document what you can with Standard, explicitly note in the summary that Full would be better, and invite others to fork and extend. **Incomplete transparency is better than no transparency.**

### "Can I validate without full compliance?"

Yes. The validator will show warnings if you could achieve a higher compliance level, but it won't fail validation if you're correctly claiming Basic when you only have L1.

## Next Steps

- **[Get started](/getting-started/installation)** - Install the validator
- **[Create your first document](/getting-started/first-document)** - Step-by-step ORP-Standard example
- **[See examples](/examples)** - Real ORP-Full document (Danish Property Tax)
- **[Read the specification](/protocol/specification)** - Full technical details
