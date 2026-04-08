---
title: Danish Property Tax Reform
description: Complete ORP-Full example — LVT + Smoothed Profit Tax proposal
---

# Danish Property Tax Reform: LVT + Smoothed Profit Tax

**Document ID:** `orp-dk-property-tax-001`
**Compliance Level:** ORP-Full
**Status:** Open for comment
**Author:** Asbjørn
**Created:** 2026-02-25

## What This Example Demonstrates

This is a complete, validated ORP-Full document proposing a reform to Denmark's residential property tax system. It demonstrates:

- **All five ORP layers** working together
- **Real policy proposal** with substantive claims
- **Transparent data provenance** (Layer 1) — Two datasets with full documentation
- **Economic modeling** (Layer 2) — Four scenarios comparing current vs proposed systems
- **Stakeholder analysis** (Layer 3) — Seven stakeholder groups with impact assessment
- **Decision accountability** (Layer 4) — Six documented methodological choices
- **Fork invitation** (Layer 5) — Explicit invitation to challenge assumptions

This document is designed to be **debated, challenged, and forked**. If you disagree with the LVT rate, the land value assumptions, or the stakeholder analysis — fork it and publish your alternative.

---

## Executive Summary

### The Problem

Denmark's current property tax system:
- Combines annual property value tax (ejendomsværdiskat) with land tax (grundskyld)
- Creates complex, unpredictable tax burden
- Exempts all capital gains on primary residence at sale
- Generates lock-in effects (people afraid to sell and trigger reassessment)

### The Proposal

Replace with:
1. Annual **Land Value Tax (LVT) of 1%** on land value only (not buildings)
2. Profit tax **of 10% on gains at sale**, paid in annual installments over 5 to 10 years
3. **LVT credit system** — LVT paid accumulates as credit that offsets profit tax base (prevents double taxation)
4. Opt-in window **of 12 months** for existing owners to register cost basis

### The Claim

This system is:
- **Fairer** — Taxes windfall gains currently fully exempt
- **Simpler** — One base rate, clear rules
- **More stable** — Fixed LVT + smoothed profit tax = predictable costs
- **Cheaper for most** — 3 out of 4 scenarios show lower total tax burden

**The one group that pays more:** High-appreciation urban owners (e.g. Copenhagen apartments with DKK 3M gain). But they're being taxed on a gain currently fully exempt.

---

## Layer 1 — Data Provenance

This proposal uses two datasets. Both are fully documented below.

### Dataset 1: Danish Property Tax Rates 2024

**Source:** SKAT (Danish Tax Authority) and Vurderingsstyrelsen
**What it contains:** Official current tax rates for ejendomsværdiskat and grundskyld
**Why it matters:** Establishes the baseline for comparison

**Key Data Points:**
- Ejendomsværdiskat: 0.51% on property value up to DKK 9.2M
- Grundskyld: Municipal rate (average ~0.2-0.3%)
- Combined effective rate: ~0.7% for median property
- Capital gains on primary residence: **Fully exempt**

**Known Limitations:**
- Rates vary by municipality
- 20% prudence discount means statutory rates overstate actual burden
- Transition discount scheme means many existing owners pay less until next sale

**Data Quality:** <span style="color: #10b981;">✓</span> High — Official government data, publicly accessible

### Dataset 2: Illustrative Property Price Scenarios

**Source:** Author-constructed based on general market knowledge
**What it contains:** Purchase and sale prices for four illustrative scenarios
**Why it matters:** Demonstrates how the proposal affects different homeowner types

**Synthetic Data Warning:** <span style="color: #f59e0b;">⚠</span> These are **illustrative scenarios**, not statistical records. Formal policy modeling should use actual transaction data from Danmarks Statistik.

**Scenarios Constructed:**
1. Provincial house, modest appreciation (DKK 2M → DKK 3M over 14 years)
2. Copenhagen apartment, strong appreciation (DKK 3M → DKK 6M over 9 years)
3. Long-term family home (DKK 1.5M → DKK 4M over 25 years)
4. Short hold (DKK 2.5M → DKK 2.8M over 3 years)

**Key Assumptions:**
- Land value = 35% of total value (provincial) or 50% (Copenhagen)
- Linear property value growth (simplification)
- No inflation adjustment (conservative — overstates taxable gains)

**What's Excluded:**
- Luxury properties over DKK 15M
- Holiday homes (sommerhus)
- Rental investment property
- Commercial property

---

## Layer 2 — Consequence Simulation

### Affected Population

**~1.4 million Danish owner-occupied households**

Segmented into:
- **Provincial homeowners** (~900K) — Lower land values, modest appreciation
- **Copenhagen/urban** (~500K) — Higher land values, stronger appreciation
- **Long-term holders 15+ years** (~400K) — Often asset-rich, cash-poor
- **Recent buyers <5 years** (~250K) — Bought expecting zero capital gains tax
- **Prospective first-time buyers** (~300K) — Affected by market fluidity

### The Model

**Type:** Static comparison model
**What it does:** Calculate total tax burden under current vs proposed system for each scenario

**Formula (Proposed System):**
```
Total Tax = (LVT × Land Value × Years) + (Profit Tax × (Gain - LVT Paid))
```

The **LVT credit** is the key mechanism — every year of LVT paid reduces the taxable gain at sale by that amount.

### Four Scenarios Compared

#### Scenario 1: Provincial House, Modest Appreciation

**Profile:** Typical provincial home, 14-year hold
**Purchase:** DKK 2,000,000 (land: 35% = DKK 700,000)
**Sale:** DKK 3,000,000
**Gain:** DKK 1,000,000

| System | Annual Cost | Total Tax | Tax on Gain | Details |
|--------|-------------|-----------|-------------|---------|
| **Current System** | ~DKK 17,500/year | **DKK 245,000** | DKK 0 (exempt) | 0.7% combined rate over 14 years |
| **Proposed System** | DKK 7,000/year (LVT) | **DKK 188,200** | DKK 90,200 (10%) | LVT: DKK 98K + Profit tax: DKK 90.2K<br/>Taxable gain after LVT credit: DKK 902K<br/>Smoothed: DKK 9,020/year over 10 years |

**Result:** <span style="color: #10b981;">↓</span> **DKK 56,800 cheaper** (23% savings)

---

#### Scenario 2: Copenhagen Apartment, Strong Appreciation

**Profile:** Central Copenhagen apartment, 9-year hold
**Purchase:** DKK 3,000,000 (land: 50% = DKK 1,500,000)
**Sale:** DKK 6,000,000
**Gain:** DKK 3,000,000

| System | Annual Cost | Total Tax | Tax on Gain | Details |
|--------|-------------|-----------|-------------|---------|
| **Current System** | ~DKK 27,000/year | **DKK 243,000** | DKK 0 (exempt) | 0.7% combined rate over 9 years |
| **Proposed System** | DKK 15,000/year (LVT) | **DKK 421,500** | DKK 286,500 (10%) | LVT: DKK 135K + Profit tax: DKK 286.5K<br/>Taxable gain after LVT credit: DKK 2,865K<br/>Smoothed: DKK 28,650/year over 10 years |

**Result:** <span style="color: #f59e0b;">⚠</span> **DKK 178,500 more expensive**

**But:** This is the **only scenario that's more expensive**. And it taxes a DKK 3M gain that's currently completely untaxed. The annual installment (DKK 28,650/year) is manageable in the context of a DKK 3M realized gain.

---

#### Scenario 3: Long-Term Family Home (25 Years)

**Profile:** Family home held for a generation
**Purchase:** DKK 1,500,000 (land: DKK 525,000)
**Sale:** DKK 4,000,000
**Gain:** DKK 2,500,000

| System | Annual Cost | Total Tax | Tax on Gain | Details |
|--------|-------------|-----------|-------------|---------|
| **Current System** | ~DKK 19,000/year | **DKK 475,000** | DKK 0 (exempt) | 0.7% combined rate over 25 years |
| **Proposed System** | DKK 5,250/year (LVT) | **DKK 368,150** | DKK 236,900 (10%) | LVT: DKK 131.25K + Profit tax: DKK 236.9K<br/>Taxable gain after LVT credit: DKK 2,369K<br/>Smoothed: DKK 23,690/year over 10 years |

**Result:** <span style="color: #10b981;">↓</span> **DKK 106,850 cheaper** (22% savings)

---

#### Scenario 4: Short Hold, Small Gain

**Profile:** Recent purchase, 3-year hold
**Purchase:** DKK 2,500,000 (land: DKK 875,000)
**Sale:** DKK 2,800,000
**Gain:** DKK 300,000

| System | Annual Cost | Total Tax | Tax on Gain | Details |
|--------|-------------|-----------|-------------|---------|
| **Current System** | ~DKK 21,000/year | **DKK 63,000** | DKK 0 (exempt) | 0.7% combined rate over 3 years |
| **Proposed System** | DKK 8,750/year (LVT) | **DKK 53,650** | DKK 27,400 (10%) | LVT: DKK 26.25K + Profit tax: DKK 27.4K<br/>Taxable gain after LVT credit: DKK 274K<br/>Smoothed: DKK 5,480/year over 5 years |

**Result:** <span style="color: #10b981;">↓</span> **DKK 9,350 cheaper** (15% savings)

---

### Summary: Who Benefits?

| Scenario | Current System | Proposed System | Difference |
|----------|----------------|-----------------|------------|
| S1: Provincial house | DKK 245,000 | DKK 188,200 | **-DKK 56,800** <span style="color: #10b981;">✓</span> |
| S2: Copenhagen apt | DKK 243,000 | DKK 421,500 | **+DKK 178,500** <span style="color: #f59e0b;">⚠</span> |
| S3: Long-term family | DKK 475,000 | DKK 368,150 | **-DKK 106,850** <span style="color: #10b981;">✓</span> |
| S4: Short hold | DKK 63,000 | DKK 53,650 | **-DKK 9,350** <span style="color: #10b981;">✓</span> |

**Three out of four scenarios are cheaper under the proposed system.**

The one exception (S2) pays more because they realized a DKK 3M gain that's currently fully tax-free. The profit tax brings their effective tax rate on that gain to 16% — which is hard to characterize as unfair.

---

## Layer 3 — Empathy Mapping

### Stakeholder Analysis

Who's affected? How do they feel about it? What are their vulnerabilities?

#### Median Provincial Homeowner (~700K households)

**Relationship:** Core beneficiary
**Financial Impact:** DKK 35K-110K better off over typical hold period
**Quality of Life:** Lower annual cost throughout ownership; no lump-sum shock at sale

**Vulnerabilities:** None — this group clearly benefits

---

#### Copenhagen High-Appreciation Owner (~200K households)

**Relationship:** The one group paying more
**Financial Impact:** Up to DKK 180K more on a DKK 3M gain
**Quality of Life:** Annual installment of ~DKK 28K for 10 years post-sale

**Vulnerabilities:**
- Some in this group are asset-rich but not income-rich (e.g. long-term owners on pension)
- Retirees on fixed income face highest burden

**Mitigation:** Extend existing tax freeze mechanism to allow LVT deferral for cash-poor owners

---

#### Asset-Rich, Cash-Poor Long-Term Owner (~150K households)

**Profile:** Older homeowner in appreciated property, pension-level income

**Relationship:** Mixed — Lower annual LVT than current system *for most*, but urban owners may face higher burden

**Financial Impact:** Broadly neutral to positive
**Quality of Life:** Improved cash flow during ownership; profit tax spread over 10 years manageable

**Vulnerabilities:**
- High vulnerability to annual cash flow pressure if in high-value urban property
- **Solution:** Extend existing Danish tax freeze mechanism to LVT — allow deferral until sale with interest

---

#### Recent Buyer 2020-2025 (~250K households)

**Relationship:** Psychological resistance — bought expecting zero capital gains tax

**Financial Impact:** Actually better off financially (see S4)
**Quality of Life:** Lower annual cost + modest profit tax at sale

**Vulnerabilities:**
- Feels like rule change mid-game even though they benefit
- **Solution:** 12-month opt-in window to register cost basis from day one of new system

---

#### First-Time Buyer / Prospective Homeowner (~300K households)

**Relationship:** Indirect beneficiary

**Financial Impact:** Indirect — improved market fluidity may increase supply
**Quality of Life:** More properties available as lock-in effect decreases

**Vulnerabilities:**
- Benefits are uncertain and depend on market adjustment (not modeled)

---

#### Danish Government and Municipalities

**Relationship:** Revenue authority

**Financial Impact:** Unknown — aggregate revenue modeling not included here (flagged as gap)
**Quality of Life:** More stable revenue base than profit-at-sale-only system

**Vulnerabilities:**
- Municipal grundskyld is currently local — transition to national LVT requires intergovernmental transfer review

---

#### Heirs Inheriting Property (~30-40K per year)

**Relationship:** Neutral

**Financial Impact:** Inheritance not treated as sale; LVT credit transfers intact
**Quality of Life:** No forced sale to cover tax; cost basis resets to inherited value

**Vulnerabilities:** None — proposal preserves inheritance-friendly treatment

---

### Minority Stress Test

Three vulnerable groups explicitly tested:

#### Test 1: Retirees in High-Value Urban Properties

**Scenario:** Copenhagen retiree, fixed pension, home worth DKK 8M, held 20+ years

**Outcome:** LVT at 1% on ~DKK 4M land value = **DKK 40,000/year**. This exceeds current rate for some in this group.

**Mitigation:** <span style="color: #10b981;">✓</span> **Extend existing tax freeze mechanism** to LVT — allow deferral until sale with interest accrual. Already established in Danish law.

---

#### Test 2: Recent Buyers Expecting Zero Capital Gains Tax

**Scenario:** Bought DKK 3M home in 2023, expecting zero tax at sale in 2030

**Outcome:** Actually better off financially — lower annual cost + profit tax at sale nets positive

**Mitigation:** <span style="color: #10b981;">✓</span> Opt-in window **of 12 months** to register cost basis and begin accumulating credit from day one. Optional grandfathering for pre-reform buyers.

---

#### Test 3: Rural Low-Value Property Owners

**Scenario:** Home worth DKK 800K in rural Jutland, 10% land value ratio, held 15 years

**Outcome:** LVT at 1% on DKK 80K = **DKK 800/year**. Current system: ~DKK 5,600/year.

**Mitigation:** None required — **this group benefits massively**.

---

### Net Welfare Assessment

**Conclusion:** The proposal produces **net positive welfare outcomes** for the majority of Danish homeowners.

**The only group clearly worse off:** High-gain urban sellers — currently receiving a significant untaxed windfall. Their additional burden is manageable through smoothing and difficult to characterize as unfair.

**Confidence:** Medium

**Confidence Basis:** Directional confidence is high. Magnitude confidence is medium due to reliance on illustrative data and absence of aggregate revenue modeling.

---

## Layer 4 — Accountability Ledger

Six key decisions are documented with rationale and alternatives considered.

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| **1. Scope Limited to Owner-Occupied Primary Residence** | Owner-occupied primary residence is the politically central case. Including rental property would require separate modeling. | Including rental investment property — better treated as extension |
| **2. Current System Baseline Assumes Full Capital Gains Exemption** | Danish law (Ejendomsavancebeskatningsloven §8) provides broad exemption for primary residence. Well established. | Partial exemption scenarios not modeled |
| **3. Smoothing Period 5 to 10 Years** | 10 years produces manageable annual installments even on large gains. 5 years for small gains reduces administrative tail. | Flat 10-year period simpler; income-based smoothing more progressive but complex |
| **4. Land-to-Value Ratios are Approximations** | Using 35% (provincial) and 50% (Copenhagen) avoids importing controversial Vurderingsstyrelsen methodology while remaining directionally accurate. | Official assessments add precision but also controversy |
| **5. No Inflation Adjustment** | Conservative assumption that **overstates** profit tax burden. Strengthens proposal's credibility. | Inflation adjustment at 2% would reduce taxable gains materially for long holds (e.g. 25-year gain of DKK 2.5M nominal → DKK 1.4M real) |
| **6. Aggregate Revenue Not Modeled** | Requires transaction volume data from Danmarks Statistik not incorporated here. Absence explicitly flagged. | Rough estimate possible from average transaction volumes — deferred to formal extension |

---

## Layer 5 — Fork Registry

### This Document

**Document ID:** orp-dk-property-tax-001
**Forked From:** None (original proposal)
**Known Forks:** None yet
**Responses:** None yet

### Invitation to Fork

**This document is explicitly open for forking.**

If you believe:
- The LVT rate should be different (0.5%? 1.5%?)
- The profit tax rate should be higher or lower
- The land value ratios are wrong
- The stakeholder analysis missed an important group
- The smoothing period should be different
- Inflation adjustment should be included

→ **Fork this document, change the relevant fields, and publish your version.**

The diff between your fork and this document will make the actual point of disagreement explicit and debatable.

### Suggested Fork Starting Points

1. **Alternative rate combinations** — e.g. 0.5% LVT + 15% profit tax
2. **Revenue neutrality analysis** — Use Danmarks Statistik transaction data
3. **Extension to rental property** — Separate profit tax regime
4. **Inflation-adjusted gains** — Reduces taxable gains for long holds
5. **Municipality-specific rates** — Model Copenhagen vs rural differences
6. **ATP integration** — Allow pension savings to fund property purchases

---

## Download and Validate

The complete validated YAML document is available:

```bash
# Download
curl -O https://gitlab.com/publicreason/orp/-/raw/main/examples/danish_property_tax_reform.yaml

# Validate
orp validate danish_property_tax_reform.yaml

# Expected output:
# ✓ Valid ORP document
# Compliance Level: ORP-Full
# Layers Present: 5/5 (Header + L1-L5)
```

---

## What This Example Teaches

### About ORP Protocol

1. **All 5 layers work together** — Each layer builds on the previous
2. **Data honesty matters** — L1 explicitly flags synthetic data and approximations
3. **Stakeholders aren't abstract** — L3 names real groups with real vulnerabilities
4. **Decisions are documented** — L4 shows *why* choices were made
5. **Disagreement is invited** — L5 explicitly encourages forking

### About This Proposal

1. **Most homeowners benefit** — 3 out of 4 scenarios show lower tax burden
2. **High gains get taxed** — The one group that pays more realized a DKK 3M untaxed windfall
3. **Cash-poor owners are protected** — Tax freeze mechanism extended to LVT
4. **Recent buyers still benefit** — Despite rule change mid-ownership
5. **The system is simpler** — One LVT rate + one profit tax rate vs complex current system

---

## Next Steps

- **Challenge this proposal** — Fork it with your own assumptions
- **Extend the analysis** — Add aggregate revenue modeling
- **Apply to your context** — Use this structure for your own policy domain
- **Contribute** — Submit your ORP document as an example

**Questions or feedback?** Open an issue on [GitLab](https://gitlab.com/publicreason/orp/-/issues).
