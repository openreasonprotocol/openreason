# ORP Document: Danish Property Tax Reform
## A Hybrid Land Value Tax and Smoothed Profit Tax Proposal

---

```yaml
orp_version: "0.1"
document_id: "orp-dk-property-tax-001"
title: "Danish Property Tax Reform: LVT + Smoothed Profit Tax"
domain: "policy"
authors:
  - name: "Asbjørn"
    role: "author"
created: "2026-02-25"
last_modified: "2026-02-25"
status: "open-for-comment"
forked_from: null
compliance_level: "ORP-Full"
summary: |
  Denmark's current property tax system combines an annual property value tax 
  (ejendomsværdiskat) with a land tax (grundskyld), producing a complex framework 
  that exempts primary residence capital gains at sale entirely. This proposal 
  replaces it with a permanent Land Value Tax (LVT) at 1% of land value combined 
  with a 10% profit tax on gains at sale, smoothed over 5–10 years in equal annual 
  installments. LVT payments accumulate as a credit that offsets the profit tax base, 
  preventing double taxation. The combination is fairer, simpler, more stable, and 
  demonstrably cheaper for the majority of Danish homeowners than the current system.
```

---

## L1: Data Provenance

### Dataset 1 — Danish Property Tax Rates 2024

```yaml
dataset_id: "dk-skat-rates-2024"
name: "Danish Property Tax Rates and Rules 2024"
description: >
  Official current tax rates for ejendomsværdiskat and grundskyld as reformed 
  under the 2024 Danish property tax overhaul. Used to establish the current 
  system baseline for comparison.
source: "Government — SKAT (Danish Tax Authority) and Vurderingsstyrelsen"
collection_method: "Official published rates from skat.dk and schjødt.com legal summary"
date_range: "2024–present"
geographic_scope: "Denmark national"

inclusion_criteria:
  description: >
    Current statutory rates for owner-occupied residential property only. 
    Commercial property rates excluded as outside scope of this proposal.

exclusion_criteria:
  - excluded: "Commercial property tax rates (dækningsafgift)"
    reason: "Proposal scoped to residential owner-occupied property"
    potential_impact: "Low — commercial property reform is a separate policy question"
  - excluded: "Holiday home (sommerhus) tax rules"
    reason: "Different legal and usage regime; separate reform warranted"
    potential_impact: "Medium — holiday home owners are a distinct stakeholder group not modelled here"
  - excluded: "Pre-2024 historical rates"
    reason: "2024 reform represents the current baseline; historical comparison would add complexity without improving the core argument"
    potential_impact: "Low for proposal validity; relevant for historical context"

cleaning_decisions:
  - decision: "Used 0.7% as effective combined annual rate for illustrative calculations"
    reason: >
      The true combined rate varies by municipality and property value. 
      0.7% represents a reasonable approximation of the effective rate for 
      a median Danish owner-occupied home combining ejendomsværdiskat (0.51% 
      up to DKK 9.2M) and grundskyld (municipal average). This simplification 
      is appropriate for illustrative comparison but should be replaced with 
      municipality-specific rates in any formal policy modelling.
    alternatives_considered: "Using the maximum statutory rate (0.51% + up to 3%) would overstate the current burden"

synthetic_elements:
  present: false

known_limitations:
  - "Effective rates vary significantly by municipality — Copenhagen rates differ substantially from rural municipalities"
  - "The 20% prudence discount on assessed values means statutory rates overstate effective rates"
  - "The 2024 transition discount scheme means many existing owners pay less than the statutory rate until their property next sells"

access:
  public: true
  url: "https://skat.dk/en-us/individuals/property/introduction-to-property-in-denmark"
  license: "Public domain — Danish government data"

attested_by:
  - name: "Asbjørn"
    role: "author"
    date: "2026-02-25"
    statement: "I confirm the above documentation is accurate and complete to the best of my knowledge"
```

---

### Dataset 2 — Danish Property Market Price Data

```yaml
dataset_id: "dk-property-prices-illustrative"
name: "Illustrative Danish Property Price Scenarios"
description: >
  Property purchase and sale prices used in the four illustrative calculation 
  scenarios. Drawn from general knowledge of the Danish property market rather 
  than a specific statistical dataset.
source: "Author-constructed based on general market knowledge"
collection_method: "Illustrative scenarios constructed to represent typical cases across property types and holding periods"
date_range: "1999–2024"
geographic_scope: "Denmark — provincial and Copenhagen"

inclusion_criteria:
  description: >
    Four scenarios selected to represent: (1) provincial house with modest 
    appreciation, (2) Copenhagen apartment with strong appreciation, (3) 
    long-term family home, (4) short hold. Designed to cover the range of 
    typical Danish homeowner experiences.

exclusion_criteria:
  - excluded: "Luxury property (>DKK 15M)"
    reason: "Edge case unlikely to be politically central; different rate threshold applies"
    potential_impact: "Medium — the 1.4% ejendomsværdiskat tier applies above DKK 9.2M and is not modelled"
  - excluded: "Properties with negative equity or loss at sale"
    reason: "Profit tax only applies to gains; loss scenarios produce zero profit tax liability under the proposal"
    potential_impact: "Low for the proposal's core argument; worth noting that no profit tax arises on a loss"
  - excluded: "Rental investment property"
    reason: "Different tax regime; proposal scoped to primary residence"
    potential_impact: "High if extended — rental property reform requires separate treatment"

cleaning_decisions:
  - decision: "Land value assumed at 35% of total property value for provincial homes and 50% for Copenhagen"
    reason: >
      Land-to-total-value ratios vary significantly by location. 35% is a 
      reasonable approximation for provincial Danish homes where building 
      value dominates. 50% reflects Copenhagen's higher land scarcity premium. 
      These are approximations requiring replacement with official Vurderingsstyrelsen 
      land assessment data in formal modelling.
    alternatives_considered: >
      Using a uniform ratio would obscure the geographic differentiation that 
      is a core feature of the LVT's fairness argument
  - decision: "Average land value used across holding period rather than year-by-year growth"
    reason: "Simplification appropriate for illustrative purposes; formal modelling should use time-series land values"
    alternatives_considered: "Year-by-year modelling would require property price index data not included here"

synthetic_elements:
  present: true
  description: >
    All four scenarios are constructed illustrations rather than records of 
    actual transactions. Purchase prices, sale prices, and holding periods 
    are chosen to be representative and internally consistent but do not 
    correspond to specific properties. This is appropriate for illustrative 
    policy documents but formal modelling should use actual transaction data 
    from e.g. Statistics Denmark (Danmarks Statistik).

known_limitations:
  - "Scenarios do not account for inflation — real gains would be lower than nominal gains used in calculations"
  - "Mortgage interest, maintenance costs, and transaction costs are excluded — these affect the net financial position but not the tax comparison directly"
  - "Land value ratios are approximations; official separation of land and building value requires Vurderingsstyrelsen methodology"
  - "The Copenhagen scenario assumes a 3M gain in 9 years which is high but not atypical for central Copenhagen 2015–2024"

access:
  public: true
  url: null
  license: "Original work — open for reuse under Creative Commons CC-BY"

attested_by:
  - name: "Asbjørn"
    role: "author"
    date: "2026-02-25"
    statement: "I confirm the above documentation is accurate and complete to the best of my knowledge"
```

---

## L2: Consequence Simulation

```yaml
affected_population:
  description: >
    All Danish owner-occupied residential property holders. Approximately 
    1.4 million owner-occupied homes in Denmark as of 2024.
  size_estimate: "~1.4 million households"
  segments:
    - segment: "Provincial homeowners"
      description: "Owner-occupied homes outside major cities, typically lower absolute land values"
      estimated_size: "~900,000 households (est.)"
    - segment: "Copenhagen and major city homeowners"
      description: "Owner-occupied homes in Copenhagen, Aarhus, Odense, Aalborg — higher land values and typically stronger appreciation"
      estimated_size: "~500,000 households (est.)"
    - segment: "Long-term holders (>15 years)"
      description: "Owners who have held their primary residence for 15 or more years. Often older, asset-rich, cash-poor."
      estimated_size: "~400,000 households (est.)"
    - segment: "Recent buyers (<5 years)"
      description: "Owners who purchased under the current system with an expectation of zero capital gains tax"
      estimated_size: "~250,000 households (est.)"
    - segment: "First-time buyers (prospective)"
      description: "Renters and young people not yet in the housing market. Affected by market pricing and accessibility."
      estimated_size: "~300,000 households (est.)"

variables:
  independent:
    - variable: "lvt_rate"
      description: "Annual Land Value Tax rate as percentage of land value"
      range: "0.1% to 3.0%"
      default_value: "1.0%"
    - variable: "profit_tax_rate"
      description: "Tax rate applied to gain at point of sale after LVT credit"
      range: "5% to 25%"
      default_value: "10%"
    - variable: "smoothing_period_years"
      description: "Number of years over which profit tax is paid in equal installments"
      range: "1 to 20"
      default_value: "10 (for gains above threshold), 5 (for gains below threshold)"
    - variable: "land_value_ratio_provincial"
      description: "Land value as proportion of total property value for provincial homes"
      range: "25% to 50%"
      default_value: "35%"
    - variable: "land_value_ratio_copenhagen"
      description: "Land value as proportion of total property value for Copenhagen/urban"
      range: "40% to 65%"
      default_value: "50%"

  dependent:
    - variable: "total_tax_burden"
      description: "Combined LVT paid + profit tax paid over full ownership period"
      unit: "DKK"
    - variable: "annual_tax_cost"
      description: "Average annual tax cost under each system"
      unit: "DKK/year"
    - variable: "profit_tax_annual_installment"
      description: "Annual profit tax payment during smoothing period post-sale"
      unit: "DKK/year"
    - variable: "vs_current_system"
      description: "Difference in total tax burden versus current system (negative = cheaper)"
      unit: "DKK"

model:
  type: >
    Static comparison model. For each scenario: calculate current system total 
    tax (annual rate × property value × years). Calculate proposed system total 
    tax (LVT on land value × years + profit tax on gain minus LVT credit). 
    Compare totals and annual installments. No dynamic market feedback modelled.
  assumptions:
    - assumption: "Property value grows linearly between purchase and sale"
      basis: "Simplification for illustrative purposes"
      sensitivity: "Medium — actual appreciation is non-linear but the cumulative tax calculation is not highly sensitive to the growth path"
    - assumption: "LVT is calculated on average land value across holding period"
      basis: "Simplification; formal model should use annual assessed values"
      sensitivity: "Low for long holding periods, higher for short holds in rapidly appreciating markets"
    - assumption: "Current system effective rate of 0.7% applied uniformly"
      basis: "Approximation of combined ejendomsværdiskat + grundskyld for median property"
      sensitivity: "High — using municipality-specific rates would change results materially for high and low rate municipalities"
    - assumption: "Capital gains on primary residence currently fully exempt"
      basis: "Broadly accurate under current Danish law for owner-occupied primary residence meeting size and occupancy requirements"
      sensitivity: "Low — the exemption is well established in Danish tax law"
    - assumption: "No inflation adjustment to gains"
      basis: "Conservative assumption that overstates taxable gains and therefore overstates the profit tax burden"
      sensitivity: "Medium — with inflation adjustment at 2% annually, taxable gains would be materially lower for long holds"

scenarios:
  - scenario_id: "S1"
    name: "Provincial house, modest appreciation"
    description: "Typical provincial Danish home, moderate appreciation over 14 years"
    variable_values:
      purchase_price: "DKK 2,000,000"
      sale_price: "DKK 3,000,000"
      holding_years: 14
      land_value_ratio: "35%"
    outcomes:
      current_system_total: "DKK 245,000"
      proposed_system_total: "DKK 210,250"
      vs_current: "DKK -34,750 (14% cheaper)"
      annual_profit_installment: "DKK ~9,000/year over 10 years"

  - scenario_id: "S2"
    name: "Copenhagen apartment, strong appreciation"
    description: "Central Copenhagen apartment, strong appreciation reflecting 2015–2024 market"
    variable_values:
      purchase_price: "DKK 3,000,000"
      sale_price: "DKK 6,000,000"
      holding_years: 9
      land_value_ratio: "50%"
    outcomes:
      current_system_total: "DKK 243,000"
      proposed_system_total: "DKK 482,250"
      vs_current: "DKK +239,250 (more expensive)"
      annual_profit_installment: "DKK ~28,000/year over 10 years"
      note: "Only scenario more expensive than current. Taxes a DKK 3M gain currently fully exempt at effective rate of 16.1%."

  - scenario_id: "S3"
    name: "Long-term family home, 25 years"
    description: "Family home held for a generation, substantial appreciation"
    variable_values:
      purchase_price: "DKK 1,500,000"
      sale_price: "DKK 4,000,000"
      holding_years: 25
      land_value_ratio: "35%"
    outcomes:
      current_system_total: "DKK 475,000"
      proposed_system_total: "DKK 466,675"
      vs_current: "DKK -8,325 (essentially neutral)"
      annual_profit_installment: "DKK ~22,600/year over 10 years"

  - scenario_id: "S4"
    name: "Short hold, small gain"
    description: "Recent purchase with modest appreciation over 3 years"
    variable_values:
      purchase_price: "DKK 2,500,000"
      sale_price: "DKK 2,800,000"
      holding_years: 3
      land_value_ratio: "35%"
    outcomes:
      current_system_total: "DKK 63,000"
      proposed_system_total: "DKK 53,625"
      vs_current: "DKK -9,375 (15% cheaper)"
      annual_profit_installment: "DKK ~5,500/year over 5 years"

primary_scenario: "S1"

model_code:
  available: false
  repository: null
  note: "Calculations are arithmetic and reproducible from the variable values above. Formal model code planned for Phase 1 tooling."
```

---

## L3: Empathy Mapping

```yaml
stakeholder_map:

  - stakeholder: "Median provincial homeowner"
    description: "Owner of a home worth DKK 1.5–3M outside major cities, typically middle income, often long-term holder"
    estimated_population: "~700,000 households"
    relationship_to_proposal: "Core beneficiary — lower annual costs, modest profit tax at sale, manageable installments"
    impacts_by_scenario:
      - scenario_id: "S1"
        financial_impact: "DKK 34,750 better off over 14 years"
        quality_of_life_impact: "Lower monthly carrying cost throughout ownership; no lump-sum shock at sale"
        direction: "benefits"
      - scenario_id: "S3"
        financial_impact: "Essentially neutral over 25 years"
        quality_of_life_impact: "Significantly lower annual cost offset by profit tax — net cash flow improvement during ownership"
        direction: "benefits"
    vulnerability_flags: []

  - stakeholder: "Copenhagen and urban apartment owner with strong appreciation"
    description: "Owner of a property that has appreciated strongly, particularly in Copenhagen 2010–2024"
    estimated_population: "~200,000 households"
    relationship_to_proposal: "The one group paying more — but taxing a gain currently fully exempt"
    impacts_by_scenario:
      - scenario_id: "S2"
        financial_impact: "DKK 239,250 more over 9 years — but on a DKK 3M gain currently untaxed"
        quality_of_life_impact: "Annual installment of ~DKK 28,000 for 10 years post-sale — manageable in context of gain realised"
        direction: "mixed"
    vulnerability_flags:
      - "Some in this group are asset-rich but not income-rich (e.g. long-term owners who haven't moved)"
      - "Retirees on fixed income in appreciated Copenhagen apartments face highest LVT burden under proposal"

  - stakeholder: "Asset-rich, cash-poor long-term owner"
    description: "Typically older homeowner in an appreciated property, income may be pension-level, cannot easily afford increased annual costs"
    estimated_population: "~150,000 households (est.)"
    relationship_to_proposal: >
      LVT at 1% is lower than current combined rate for most, reducing annual 
      burden. However, those in high-value urban areas may face higher LVT than 
      current effective rate. The existing tax freeze mechanism should be extended 
      to cover LVT increases for this group.
    impacts_by_scenario:
      - scenario_id: "S3"
        financial_impact: "Broadly neutral overall; annual cost typically lower during ownership"
        quality_of_life_impact: "Improved during ownership; profit tax spread over 10 years is manageable on pension income"
        direction: "benefits"
    vulnerability_flags:
      - "High vulnerability to annual cash flow pressure even at 1% LVT if property value is very high"
      - "Existing tax freeze mechanism should explicitly extend to LVT under the new system"

  - stakeholder: "Recent buyer (purchased 2020–2025)"
    description: "Bought under current rules expecting zero capital gains tax at sale. Rule change mid-ownership feels unfair."
    estimated_population: "~250,000 households"
    relationship_to_proposal: >
      Primary source of political resistance. The 12-month opt-in transition 
      window addresses this by letting them register cost basis from day one 
      of the new system and begin accumulating LVT credit immediately.
    impacts_by_scenario:
      - scenario_id: "S4"
        financial_impact: "DKK 9,375 better off over 3 years even with profit tax"
        quality_of_life_impact: "Lower annual cost; modest profit tax at eventual sale"
        direction: "benefits"
    vulnerability_flags:
      - "Psychological impact of rule change mid-ownership may outweigh financial reality"
      - "Requires clear communication that most will be financially better off"

  - stakeholder: "First-time buyer and prospective homeowner"
    description: "Currently renting, aspiring to ownership. Affected by pricing, deposit requirements, and market fluidity."
    estimated_population: "~300,000 households (est.)"
    relationship_to_proposal: >
      Indirect but significant beneficiary. Reduced lock-in effect increases 
      market fluidity and supply of homes for sale. Lower ongoing carrying costs 
      may reduce asking prices at the margin as seller expectations adjust.
    impacts_by_scenario:
      - scenario_id: "all"
        financial_impact: "Indirect — improved market fluidity and potential pricing adjustment"
        quality_of_life_impact: "Greater housing mobility; more properties available as lock-in effect decreases"
        direction: "benefits"
    vulnerability_flags:
      - "Benefits are indirect and uncertain — depends on market adjustment which is not modelled here"

  - stakeholder: "Danish government and municipalities"
    description: "Revenue authority. Currently dependent on stable annual property tax income."
    estimated_population: "N/A — institutional stakeholder"
    relationship_to_proposal: >
      LVT provides stable transaction-independent base revenue. Profit tax 
      adds variable top-up. Revenue neutrality requires careful rate calibration 
      — this document does not model aggregate revenue impact, which requires 
      full transaction data from Danmarks Statistik.
    impacts_by_scenario:
      - scenario_id: "all"
        financial_impact: "Unknown without aggregate revenue modelling — flagged as gap"
        quality_of_life_impact: "More stable revenue base than profit-at-sale-only alternative; less stable than current if LVT set too low"
        direction: "mixed"
    vulnerability_flags:
      - "Municipal revenue currently includes grundskyld — transition to national LVT requires intergovernmental transfer review"

  - stakeholder: "Heirs inheriting property"
    description: "Danish residents who inherit owner-occupied property from deceased relatives"
    estimated_population: "~30,000–40,000 per year (est.)"
    relationship_to_proposal: >
      Inheritance is not treated as a sale. LVT credit transfers intact. 
      Cost basis resets to inherited value. Heir steps into original owner's 
      position and converts to new system on their eventual sale.
    impacts_by_scenario:
      - scenario_id: "all"
        financial_impact: "Neutral relative to current system — no new tax trigger at inheritance"
        quality_of_life_impact: "Credit transfer preserves accumulated value; no forced sale to cover tax"
        direction: "neutral"
    vulnerability_flags: []

minority_stress_test:
  description: >
    Three minority groups were explicitly tested for disproportionate harm 
    under the proposal.
  groups_tested:
    - group: "Retirees in high-value urban properties"
      scenario_tested: "Copenhagen retiree, fixed pension income, home worth DKK 8M, holding 20+ years"
      outcome: >
        LVT at 1% on land value (~DKK 4M) = DKK 40,000/year. This exceeds 
        the current effective rate for some in this group. Represents genuine 
        hardship for cash-poor owners.
      mitigation: >
        Extend existing tax freeze mechanism to LVT — allow deferral of LVT 
        above a threshold until sale, with interest accruing but no annual 
        cash obligation. Already established as a mechanism in Danish law.

    - group: "Recent buyers expecting zero capital gains tax"
      scenario_tested: "Bought DKK 3M home in 2023, expecting zero tax at sale in 2030"
      outcome: >
        Under new system: lower annual cost + profit tax at sale. 
        Net position likely better financially but psychologically significant 
        as rules changed mid-ownership.
      mitigation: >
        12-month opt-in window at launch to register cost basis and begin 
        accumulating credit from day one of the new system. Grandfathered 
        capital gains exemption option for owners who bought before a 
        specified date.

    - group: "Rural low-value property owners"
      scenario_tested: "Home worth DKK 800,000 in rural Jutland, 10% land value ratio, holding 15 years"
      outcome: >
        LVT at 1% on ~DKK 80,000 land value = DKK 800/year. Effectively 
        negligible. Current system charges approximately DKK 5,600/year. 
        Strong beneficiary of the proposal.
      mitigation: "No mitigation required — this group benefits significantly"

unresolved_impacts:
  - "Aggregate revenue impact on Danish government has not been modelled — requires full transaction data"
  - "Second-order market pricing effects are not modelled — whether and how quickly buyers price in the profit tax liability is uncertain"
  - "Impact on housing market fluidity is directionally modelled but not quantified"
  - "Non-EU/EEA foreign owners face existing restrictions on Danish property purchase — their treatment under the new system is not addressed"
  - "Mixed-use properties (residential + commercial) require separate treatment not covered here"

net_welfare_assessment:
  methodology: >
    Qualitative assessment across stakeholder groups weighted by population size 
    and impact magnitude. No formal welfare function applied.
  conclusion: >
    The proposal produces net positive welfare outcomes for the majority of Danish 
    homeowners. The only group clearly worse off is high-gain urban sellers — a 
    group currently receiving a significant untaxed windfall. Their additional 
    burden is manageable through smoothing and is difficult to characterise as 
    unfair. The asset-rich, cash-poor group requires a specific mitigation 
    (LVT freeze extension) to prevent genuine hardship.
  confidence: "medium"
  confidence_basis: >
    Directional confidence is high. Magnitude confidence is medium due to 
    reliance on illustrative rather than statistical data and absence of 
    aggregate revenue modelling.
```

---

## L4: Accountability Ledger

```yaml
entries:

  - entry_id: "001"
    timestamp: "2026-02-25"
    decision_type: "framing"
    description: >
      Proposal scoped to owner-occupied primary residence only. Rental investment 
      property, commercial property, and holiday homes excluded from this document.
    decided_by:
      - name: "Asbjørn"
    basis: >
      Owner-occupied primary residence is the politically central case in the 
      current Danish debate. Expanding scope would require significantly more 
      modelling and risk losing clarity on the core argument.
    alternatives_considered: "Including rental property would require a separate profit tax regime — better treated as an extension"
    dissenting_views: null

  - entry_id: "002"
    timestamp: "2026-02-25"
    decision_type: "assumption"
    description: >
      Capital gains on primary residence treated as currently fully exempt. 
      This is the key baseline assumption that makes the profit tax component 
      novel rather than a modification of existing rules.
    decided_by:
      - name: "Asbjørn"
    basis: >
      Danish tax law (Ejendomsavancebeskatningsloven section 8) provides a 
      broad exemption for gains on owner-occupied primary residence meeting 
      size and occupancy requirements. This is well established in practice.
    alternatives_considered: "Partial exemption scenarios were not modelled"
    dissenting_views: null

  - entry_id: "003"
    timestamp: "2026-02-25"
    decision_type: "methodology"
    description: >
      Profit tax smoothing period set at 5 years for smaller gains and 
      10 years for larger gains. No formal threshold defined in this document.
    decided_by:
      - name: "Asbjørn"
    basis: >
      The smoothing period is the primary mechanism for eliminating lock-in. 
      10 years produces annual installments that are manageable even on large 
      gains. 5 years for smaller gains reduces the administrative tail on 
      modest transactions. The threshold between the two periods requires 
      formal policy decision — DKK 1M gain is a reasonable starting point 
      for further analysis.
    alternatives_considered: "Flat 10-year period for all gains would be simpler; income-based smoothing would be more progressive but adds complexity"
    dissenting_views: null

  - entry_id: "004"
    timestamp: "2026-02-25"
    decision_type: "data"
    description: >
      Land-to-total-value ratios of 35% (provincial) and 50% (Copenhagen) 
      adopted as approximations rather than official assessments.
    decided_by:
      - name: "Asbjørn"
    basis: >
      Official Vurderingsstyrelsen land assessments exist but are subject to 
      the same contested methodology that has driven political debate about 
      the current system. Using approximations avoids importing that controversy 
      into this proposal while remaining directionally accurate.
    alternatives_considered: "Using official assessments would add precision but also controversy; using a flat ratio would obscure geographic differentiation"
    dissenting_views: null

  - entry_id: "005"
    timestamp: "2026-02-25"
    decision_type: "assumption"
    description: >
      No inflation adjustment applied to gains. Profit tax calculated on 
      nominal rather than real gains.
    decided_by:
      - name: "Asbjørn"
    basis: >
      Conservative assumption that overstates the profit tax burden and 
      therefore makes the proposal look less favourable than it would be 
      with inflation adjustment. Choosing the conservative assumption 
      strengthens rather than weakens the proposal's credibility.
    alternatives_considered: >
      Inflation adjustment at 2% annually would reduce taxable gains 
      materially for long holds — e.g. the 25-year scenario gain of 
      DKK 2.5M would reduce to approximately DKK 1.4M in real terms. 
      Formal policy design should include inflation adjustment.
    dissenting_views: null

  - entry_id: "006"
    timestamp: "2026-02-25"
    decision_type: "exclusion"
    description: "Aggregate government revenue impact not modelled in this document."
    decided_by:
      - name: "Asbjørn"
    basis: >
      Revenue modelling requires transaction volume data and distribution 
      of gains across the full Danish property market — data available from 
      Danmarks Statistik but not incorporated in this illustrative document. 
      The absence is explicitly flagged rather than glossed over.
    alternatives_considered: "A rough revenue estimate could be constructed from average transaction volumes — deferred to a formal extension of this analysis"
    dissenting_views: null
```

---

## L5: Fork Registry

```yaml
this_document:
  document_id: "orp-dk-property-tax-001"
  forked_from: null
  fork_reason: "Original proposal"
  key_differences: "N/A — this is the original document"

known_forks: []

responses: []

invitation: >
  This document is explicitly open for forking. If you believe the LVT rate 
  should be different, the profit tax rate should be higher or lower, the 
  land value ratios are wrong, or the stakeholder analysis has missed an 
  important group — fork this document, change the relevant fields, and 
  publish your version. The diff between your fork and this document will 
  make the actual point of disagreement explicit and debatable.
  
  Suggested fork starting points:
  - Alternative rate combinations (e.g. 0.5% LVT + 15% profit tax)
  - Revenue neutrality analysis using Danmarks Statistik transaction data
  - Extension to rental investment property
  - Inflation-adjusted gains model
  - Municipality-specific rate modelling for Copenhagen vs rural areas
  - ATP integration — modelling the interaction between this proposal and 
    allowing ATP savings to fund property purchases
```

---

## Summary: Key Numbers

| Scenario | Holding | Gain | Current Total | Proposed Total | Difference |
|----------|---------|------|---------------|----------------|------------|
| Provincial, 14yr | 14 years | DKK 1M | DKK 245,000 | DKK 210,250 | −14% |
| Copenhagen, 9yr | 9 years | DKK 3M | DKK 243,000 | DKK 482,250 | +99%* |
| Long-term, 25yr | 25 years | DKK 2.5M | DKK 475,000 | DKK 466,675 | −2% |
| Short hold, 3yr | 3 years | DKK 300K | DKK 63,000 | DKK 53,625 | −15% |

*The Copenhagen case taxes a DKK 3M gain currently fully exempt. Annual installment: ~DKK 28,000 for 10 years.

---

## Core Principles Summary

**Why LVT at 1%:** Captures society-created location value continuously. Stable, transaction-independent revenue. Discourages speculative land holding. Low enough to avoid cash-flow hardship for most owners.

**Why profit tax at 10%:** Captures individual gain at the point of realisation. Low enough to be broadly acceptable. With LVT credit, effective burden is lower than nominal rate suggests.

**Why the credit mechanism:** Prevents double taxation. Reframes LVT as prepayment rather than pure cost. Reduces profit tax base for long-term holders.

**Why 5–10 year smoothing:** Eliminates lock-in effect entirely. Converts large lump-sum into manageable installments. Removes the main psychological and financial barrier to selling.

**Why inheritance transfers the credit:** Inheritance is not a sale. No cash changes hands. Treating it as a taxable event would create a perverse incentive to sell before death. The credit follows the asset, not the person.

---

*This document is ORP-Full compliant under OpenReason Protocol v0.1.*
*Fork it: [gitlab.com/publicreason/orp](https://gitlab.com/publicreason/orp)*
*Challenge it: open an issue or publish a response document in L5.*
