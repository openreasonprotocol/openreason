# ORP_META: The OpenReason Protocol's Own Provenance
## Documented under ORP v0.1

> A transparency protocol that is not transparent about its own origins would contradict its founding principles. This document applies ORP to itself.

---

```yaml
orp_version: "0.1"
document_id: "orp-meta-001"
title: "OpenReason Protocol — Self-Documentation of Provenance and Reasoning"
domain: "governance"
authors:
  - name: "Asbjørn"
    role: "author"
created: "2026-02-25"
last_modified: "2026-02-25"
status: "open-for-comment"
forked_from: null
compliance_level: "ORP-Full"
summary: |
  This document applies the OpenReason Protocol to itself — documenting the 
  origins, reasoning, assumptions, and known limitations of ORP v0.1. It exists 
  because a protocol demanding transparency in the reasoning of others must 
  demonstrate the same transparency about its own reasoning. The protocol 
  originated from a conversation about Danish property taxation that expanded 
  into a broader framework for transparent democratic reasoning, grounded in 
  the Rational, Empathy-Informed Ethics (REE) philosophical framework.
```

---

## L1: Data Provenance

### Source 1 — The originating conversation

```yaml
dataset_id: "orp-origin-conversation-2026-02"
name: "Founding conversation — Danish property tax to OpenReason"
description: >
  The OpenReason Protocol emerged from a single extended conversation beginning 
  with an analysis of competing Danish property tax proposals and expanding 
  through a series of logical steps into a general framework for transparent, 
  simulatable reasoning in policy and AI. The conversation was not planned as 
  a protocol design exercise. The protocol emerged from applying consistent 
  logical principles to a concrete problem and following where they led.
source: "Original reasoning — human-AI collaborative conversation"
collection_method: >
  Organic reasoning conversation. No prior literature review conducted before 
  the protocol structure emerged. Existing frameworks (LVT, CPF, OpenRTB, 
  model cards, IETF standards) were introduced as analogies and reference 
  points during the conversation rather than as inputs to a structured design process.
date_range: "2026-02-25"
geographic_scope: "Denmark as starting context; universal scope intended"

inclusion_criteria:
  description: >
    The protocol structure was derived from the following chain of reasoning:
    (1) Good policy requires transparent assumptions
    (2) Transparent assumptions require structured documentation
    (3) Structured documentation should be simulatable and forkable
    (4) Simulatable documentation requires standardised schemas
    (5) Standardised schemas should be open and governed as public infrastructure
    Each step follows from the previous through logical consistency rather 
    than literature review or prior art survey.

exclusion_criteria:
  - excluded: "Systematic survey of existing transparency frameworks before design"
    reason: >
      The protocol was designed from first principles before existing frameworks 
      were researched. This is a limitation — ORP may duplicate or conflict with 
      existing work in ways not yet identified.
    potential_impact: >
      High — post-hoc research identified model cards, Data Provenance Initiative, 
      Stanford Transparency Index, and EU AI Act documentation requirements as 
      adjacent work. ORP may need to align with or explicitly differentiate from 
      these in v0.2.
  - excluded: "Formal academic review of REE philosophical framework"
    reason: >
      REE was developed independently by the author through reasoning about AI 
      cognition and ethics. It has not been peer reviewed or tested against the 
      academic ethics literature.
    potential_impact: >
      Medium — REE's core principles are broadly consistent with evidence-based 
      ethics literature but this has not been formally verified. Philosophical 
      challenges to REE foundations could affect the protocol's theoretical grounding.

cleaning_decisions:
  - decision: >
      Protocol layers named L1–L5 rather than using existing terminology from 
      adjacent frameworks (e.g. model card sections, EU AI Act Annex IV fields)
    reason: >
      Naming from first principles avoids inheriting assumptions from existing 
      frameworks. However it also creates a translation burden for practitioners 
      already familiar with model cards or EU AI Act documentation.
    alternatives_considered: >
      Aligning with EU AI Act Annex IV field names would aid regulatory adoption 
      but would constrain the protocol's scope beyond AI to policy and governance.

synthetic_elements:
  present: false
  description: "All content derived from actual reasoning — no synthetic or hypothetical provenance"

known_limitations:
  - >
    ORP v0.1 was designed by a single author in a single day. It has not been 
    stress-tested by diverse practitioners across different domains and contexts.
  - >
    The protocol's own provenance (this document) was produced by the same author 
    who designed the protocol — creating an inherent conflict of interest in 
    self-assessment that independent review should address.
  - >
    No formal engagement with governments, standards bodies, or existing 
    transparency initiatives occurred before publication. ORP may be solving 
    problems that existing bodies are already addressing in ways not yet known.
  - >
    The REE philosophical foundation has not been independently reviewed. 
    The protocol's ethical grounding should be validated separately from 
    the technical specification.
  - >
    ORP v0.1 is heavily influenced by the Danish policy context in which it 
    originated. Its applicability to non-Western governance contexts, different 
    legal systems, and non-democratic political environments requires explicit testing.

access:
  public: true
  url: "https://gitlab.com/publicreason/orp"
  license: "Creative Commons CC-BY — open for reuse with attribution"

attested_by:
  - name: "Asbjørn"
    role: "author"
    date: "2026-02-25"
    statement: >
      I confirm the above documentation is accurate to the best of my knowledge. 
      I acknowledge the inherent limitation that self-documentation of one's own 
      protocol cannot be fully objective and that independent review of this 
      document is both invited and necessary.
```

---

### Source 2 — Intellectual influences and adjacent work

```yaml
dataset_id: "orp-adjacent-frameworks"
name: "Adjacent frameworks and intellectual influences"
description: >
  Frameworks and prior work that informed, paralleled, or were discovered 
  as adjacent to ORP during and after its design. Documented here to give 
  proper context and enable comparison.
source: "Multiple — academic, industry, and standards bodies"
collection_method: "Post-hoc research following protocol design"
date_range: "2018–2026"
geographic_scope: "Global"

inclusion_criteria:
  description: "Frameworks with meaningful overlap with one or more ORP layers"

adjacent_frameworks:
  - name: "Model Cards for Model Reporting (Mitchell et al., 2019 / Google)"
    overlap: "L1 data provenance, L3 stakeholder impact"
    key_difference: >
      Model Cards are scoped to AI models. ORP applies the same logic to 
      policy reasoning, governance decisions, and any consequential public 
      decision-making. Model Cards also lack the fork mechanic and the 
      accountability ledger.
    known_weakness_they_share: >
      Training data documentation in model cards is routinely summarised as 
      'publicly available data' without meaningful provenance detail — 
      exactly the gap ORP L1 is designed to address.

  - name: "Data Provenance Initiative (MIT, 2023)"
    overlap: "L1 data provenance for AI training datasets"
    key_difference: >
      DPI focuses specifically on AI training data lineage and licensing. 
      ORP extends provenance documentation to policy datasets, economic 
      models, and any reasoning context. DPI is a tool; ORP is a protocol.
    alignment_opportunity: >
      ORP-AI extension (Phase 4) should align with DPI methodology for 
      AI training data documentation.

  - name: "EU AI Act Annex IV (2024)"
    overlap: "L1, L2, L4 — documentation requirements for high-risk AI systems"
    key_difference: >
      EU AI Act documentation is a compliance obligation imposed by regulation. 
      ORP is a voluntary protocol designed for proactive adoption. EU AI Act 
      is also AI-specific; ORP is domain-general.
    alignment_opportunity: >
      ORP-AI extension should be designed to satisfy EU AI Act Annex IV 
      requirements as a subset of full ORP compliance.

  - name: "Stanford Foundation Model Transparency Index (2024)"
    overlap: "L1, L4 — transparency scoring for AI models"
    key_difference: >
      FMTI is an external audit framework — it scores existing documentation. 
      ORP is a production framework — it defines how documentation should be 
      produced in the first place.
    alignment_opportunity: >
      ORP compliance should be designed to score well on FMTI by construction.

  - name: "OpenRTB (IAB Tech Lab)"
    overlap: "Governance model, open standards approach, industry adoption strategy"
    key_difference: >
      OpenRTB standardises commercial value exchange. ORP standardises 
      reasoning exchange. The governance and adoption model is the relevant 
      parallel, not the technical content.
    key_lesson: >
      OpenRTB succeeded because reference implementations and SDKs made 
      compliance trivially easy. ORP must prioritise tooling alongside 
      specification for the same reason.

  - name: "IETF RFC process"
    overlap: "Governance model — open comment, working groups, versioned ratification"
    key_difference: >
      IETF governs internet technical standards. ORP governs reasoning 
      documentation standards. The RFC process is the relevant model for 
      how ORP versions should be published and ratified.
    key_lesson: >
      The 'rough consensus and running code' principle of IETF governance 
      is directly applicable to ORP — a version should not be ratified 
      until there are working implementations.

  - name: "Datasheets for Datasets (Gebru et al., 2021)"
    overlap: "L1 — dataset documentation standards"
    key_difference: >
      Datasheets focus on dataset documentation for ML. ORP L1 applies 
      similar principles to any dataset used in consequential reasoning, 
      including policy datasets, economic models, and demographic data.
    alignment_opportunity: >
      ORP L1 field definitions should be compatible with Datasheet methodology.

known_limitations:
  - "This survey of adjacent frameworks is not comprehensive — conducted post-hoc in limited time"
  - "Deeper engagement with each adjacent framework may reveal conflicts or alignment opportunities not identified here"
  - "Non-English language frameworks and non-Western transparency initiatives are not represented"

access:
  public: true
  url: null
  license: "N/A — references to third-party frameworks; ORP content CC-BY"
```

---

## L2: Consequence Simulation

```yaml
affected_population:
  description: >
    Potential adopters of the OpenReason Protocol across three primary contexts: 
    policy and governance, AI development, and education.
  size_estimate: "Indeterminate at v0.1 — adoption is voluntary and unproven"
  segments:
    - segment: "Government policy departments"
      description: "Ministries, agencies, and legislative bodies producing policy proposals"
      estimated_size: "Thousands globally; pilot target is Danish and Nordic governments"
    - segment: "AI developers and researchers"
      description: "Teams developing AI systems who need to document training data and model decisions"
      estimated_size: "Hundreds of thousands globally"
    - segment: "Educators and students"
      description: "Secondary and tertiary institutions using ORP as a teaching tool for policy reasoning"
      estimated_size: "Millions globally if ORP-Edu gains traction"
    - segment: "Journalists and civil society"
      description: "Organisations investigating public decisions and demanding transparency"
      estimated_size: "Tens of thousands globally"
    - segment: "Citizens"
      description: "General public who would consume ORP-compliant documents through the Viewer interface"
      estimated_size: "Potentially very large — depends entirely on adoption by governments"

variables:
  independent:
    - variable: "protocol_complexity"
      description: "How difficult ORP-Full compliance is to achieve in practice"
      range: "Low to High"
      default_value: "Currently medium-high without tooling; target low with Phase 1 CLI"
    - variable: "institutional_adoption"
      description: "Whether major governments or standards bodies formally adopt ORP"
      range: "None to mandatory"
      default_value: "Voluntary at launch"
    - variable: "tooling_quality"
      description: "How good the Phase 1 CLI and validator are"
      range: "Poor to excellent"
      default_value: "Unknown — Phase 1 not yet built"

  dependent:
    - variable: "adoption_rate"
      description: "How widely ORP is used within 2 years of v1.0 release"
      unit: "Number of published ORP documents"
    - variable: "quality_improvement"
      description: "Whether policy and AI documentation quality improves in practice"
      unit: "Qualitative — measurable through fork activity and critique volume"
    - variable: "democratic_impact"
      description: "Whether public policy debate becomes more grounded in locatable reasoning"
      unit: "Qualitative — hard to measure directly"

scenarios:
  - scenario_id: "META-S1"
    name: "Slow adoption — niche academic use"
    description: "ORP remains a theoretical framework used by researchers and educators but not adopted by governments or major AI developers"
    outcomes:
      adoption_rate: "Low — dozens of documents"
      quality_improvement: "Minimal at scale"
      democratic_impact: "Limited"
      most_likely_cause: "Tooling insufficient; no institutional anchor; complexity barrier too high"

  - scenario_id: "META-S2"
    name: "Moderate adoption — Nordic governments and AI community"
    description: "One or more Nordic governments adopt ORP for policy proposals; AI community adopts ORP-AI for training data documentation"
    outcomes:
      adoption_rate: "Medium — hundreds to thousands of documents"
      quality_improvement: "Meaningful in adopting contexts"
      democratic_impact: "Visible in countries with adoption"
      most_likely_cause: "Strong Phase 1 tooling; credible worked examples; institutional champion"

  - scenario_id: "META-S3"
    name: "Strong adoption — international standard"
    description: "ORP or a derivative becomes a recognised international standard for policy and AI transparency documentation"
    outcomes:
      adoption_rate: "High — tens of thousands of documents"
      quality_improvement: "Significant"
      democratic_impact: "Substantial in adopting jurisdictions"
      most_likely_cause: "EU AI Act alignment; educational platform traction; fork community generates momentum"

primary_scenario: "META-S2"

model_code:
  available: false
  repository: null
  note: "Adoption modelling not formally conducted at v0.1"
```

---

## L3: Empathy Mapping

```yaml
stakeholder_map:

  - stakeholder: "Policy practitioners who would use ORP"
    description: "Civil servants, policy advisers, and analysts who would produce ORP-compliant documents"
    estimated_population: "Unknown"
    relationship_to_proposal: >
      Primary producers of ORP content. Their adoption is the critical path. 
      If ORP feels too burdensome relative to current practice they will not use it.
    impacts_by_scenario:
      - scenario_id: "META-S1"
        financial_impact: "Increased documentation burden with no visible benefit"
        quality_of_life_impact: "Negative — more work, no reward"
        direction: "harmed"
      - scenario_id: "META-S2"
        financial_impact: "Manageable with good tooling; offset by reduced challenge and rework"
        quality_of_life_impact: "Neutral to positive — clearer requirements, less ambiguity"
        direction: "neutral"
    vulnerability_flags:
      - "Time pressure and resource constraints in government make any additional documentation burden a significant adoption barrier"

  - stakeholder: "Citizens and non-technical stakeholders"
    description: "General public who should be able to read and challenge public reasoning"
    estimated_population: "Very large"
    relationship_to_proposal: >
      Ultimate intended beneficiaries. ORP only serves its democratic purpose 
      if its outputs are genuinely accessible to non-experts.
    impacts_by_scenario:
      - scenario_id: "META-S2"
        financial_impact: "None direct"
        quality_of_life_impact: >
          Improved ability to understand and challenge public decisions — 
          but only if the ORP Viewer makes documents genuinely readable
        direction: "benefits"
    vulnerability_flags:
      - >
        Risk that ORP produces technically compliant but practically impenetrable 
        documents — transparency in form but not in substance. The 'summarise' 
        command and ORP Viewer must address this directly.

  - stakeholder: "Governments and institutions resistant to transparency"
    description: "Political actors who benefit from opaque reasoning and would resist ORP adoption"
    estimated_population: "Significant — most political systems have actors who benefit from opacity"
    relationship_to_proposal: >
      Primary source of institutional resistance. ORP cannot be mandatory 
      without political will; voluntary adoption depends on whether transparency 
      is perceived as advantageous or threatening by those in power.
    impacts_by_scenario:
      - scenario_id: "all"
        financial_impact: "None direct"
        quality_of_life_impact: "Reduced ability to obscure reasoning behind public decisions"
        direction: "harmed"
    vulnerability_flags:
      - "This stakeholder group has significant power to block adoption and should be explicitly considered in the governance and launch strategy"

  - stakeholder: "AI developers"
    description: "Teams building AI systems who would adopt ORP-AI for training data documentation"
    estimated_population: "Hundreds of thousands"
    relationship_to_proposal: >
      Key early adopter target for credibility. AI community already has 
      model card norms; ORP-AI needs to offer clear improvement over 
      existing practice to gain adoption.
    impacts_by_scenario:
      - scenario_id: "META-S2"
        financial_impact: "Increased documentation cost offset by regulatory compliance value (EU AI Act)"
        quality_of_life_impact: "Positive if tooling makes compliance easy and regulatory risk decreases"
        direction: "neutral to benefits"
    vulnerability_flags:
      - "Competitive pressure makes full data provenance disclosure uncomfortable for some AI developers"
      - "ORP must be careful not to require disclosure that creates legitimate IP or security risks"

  - stakeholder: "The OpenReason founder (Asbjørn)"
    description: "The originating author who explicitly does not want to become a long-term administrator"
    estimated_population: "1"
    relationship_to_proposal: >
      Has designed the protocol and the governance model to enable clean 
      handover. Success means the protocol runs without him. Failure mode 
      is the protocol becoming dependent on his continued involvement.
    impacts_by_scenario:
      - scenario_id: "all"
        financial_impact: "None — project is open source and non-commercial"
        quality_of_life_impact: >
          Positive if the governance model works and the project runs itself. 
          Negative if governance fails and administrative burden falls back 
          to the founder by default.
        direction: "neutral — depends entirely on governance execution"
    vulnerability_flags:
      - >
        Founder-dependent open source projects frequently stall when the 
        founder steps back. The governance model (see GOVERNANCE.md) must 
        create genuine institutional independence before the founder steps down.

minority_stress_test:
  description: "Two specific failure modes tested for disproportionate harm"
  groups_tested:
    - group: "Non-English speaking policy practitioners"
      scenario_tested: "ORP adopted in contexts where English is not the working language"
      outcome: >
        ORP v0.1 is written entirely in English. Field names and documentation 
        are English-only. This creates a meaningful adoption barrier for the 
        majority of the world's governments.
      mitigation: >
        Internationalisation (i18n) should be a Phase 2 priority. Field names 
        should be language-agnostic identifiers; display labels should be 
        translatable. Community translations of core documentation should be 
        actively supported.

    - group: "Small organisations with limited documentation capacity"
      scenario_tested: "NGO or small government department tries to produce ORP-Full compliant document"
      outcome: >
        ORP-Full compliance is resource-intensive. Without tooling, producing 
        a high-quality document across all five layers could take days of work 
        that small organisations cannot afford.
      mitigation: >
        ORP-Basic (Header + L1 only) provides a meaningful entry point. 
        The agent layer in Phase 3 specifically targets reducing the cost 
        of compliance for under-resourced actors. This is a core design 
        principle, not an afterthought.

unresolved_impacts:
  - "Long-term impact on democratic quality is genuinely unknown and may be small if adoption remains limited"
  - "Whether ORP creates a new form of transparency theatre — technically compliant but substantively empty — is a real risk not fully mitigated by the current design"
  - "The interaction between ORP and freedom of information law in different jurisdictions is not addressed"

net_welfare_assessment:
  methodology: "Qualitative assessment across stakeholder groups"
  conclusion: >
    If adoption reaches META-S2 or beyond, net welfare impact is clearly 
    positive — better informed public debate, more accountable AI systems, 
    and a generation of students who reason about policy more rigorously. 
    If adoption stalls at META-S1, the welfare impact is negligible and 
    the opportunity cost of the effort is the main cost.
  confidence: "low"
  confidence_basis: >
    Adoption of open standards is notoriously difficult to predict. The 
    protocol's welfare impact is almost entirely adoption-dependent.
```

---

## L4: Accountability Ledger

```yaml
entries:

  - entry_id: "META-001"
    timestamp: "2026-02-25"
    decision_type: "framing"
    description: >
      Protocol designed from first principles rather than as an extension 
      of existing frameworks.
    decided_by:
      - name: "Asbjørn"
    basis: >
      The conversation that produced ORP began with a concrete policy problem 
      and derived a protocol structure through logical consistency. This 
      produced a coherent design but at the cost of potentially reinventing 
      existing work.
    alternatives_considered: >
      Building ORP as an extension of model cards or EU AI Act documentation 
      would have ensured better alignment with existing practice but would 
      have constrained scope to AI rather than enabling a domain-general protocol.
    dissenting_views: null

  - entry_id: "META-002"
    timestamp: "2026-02-25"
    decision_type: "framing"
    description: >
      REE chosen as philosophical foundation rather than utilitarianism, 
      deontological ethics, or other established frameworks.
    decided_by:
      - name: "Asbjørn"
    basis: >
      REE was developed independently by the author through reasoning about 
      AI cognition. It is genuinely believed to be the right foundation. 
      However the choice is not neutral — different philosophical foundations 
      would produce different protocol design choices, particularly in how 
      L3 empathy mapping weights different stakeholder interests.
    alternatives_considered: >
      Utilitarian framing would emphasise aggregate welfare maximisation. 
      Rights-based framing would emphasise individual protections regardless 
      of aggregate outcomes. REE attempts to integrate both but the integration 
      should be explicitly challenged.
    dissenting_views: null

  - entry_id: "META-003"
    timestamp: "2026-02-25"
    decision_type: "methodology"
    description: >
      Five-layer structure chosen for ORP rather than flat schema or 
      different number of layers.
    decided_by:
      - name: "Asbjørn"
    basis: >
      Each layer addresses a distinct failure mode in current transparency 
      practice: missing data provenance (L1), missing simulation (L2), 
      missing stakeholder mapping (L3), missing accountability (L4), 
      missing forkability (L5). Five layers emerged from the five failure 
      modes rather than from a target number.
    alternatives_considered: >
      Three layers (data, model, accountability) would be simpler but 
      would collapse the empathy mapping and fork registry into other layers 
      where they might be deprioritised.
    dissenting_views: null

  - entry_id: "META-004"
    timestamp: "2026-02-25"
    decision_type: "framing"
    description: >
      OpenReason designed as a protocol rather than a platform or product.
    decided_by:
      - name: "Asbjørn"
    basis: >
      The author explicitly does not want to become a long-term administrator. 
      A protocol can be governed as a public good and implemented by anyone. 
      A product requires ongoing ownership. The choice of protocol-first 
      is both philosophically consistent and personally motivated.
    alternatives_considered: >
      A commercial platform would have faster initial adoption but would 
      create dependency on a single organisation and contradict the 
      transparency principles at the core of ORP.
    dissenting_views: null

  - entry_id: "META-005"
    timestamp: "2026-02-25"
    decision_type: "exclusion"
    description: >
      ORP v0.1 does not include a formal conflict resolution mechanism 
      for disputes about what constitutes valid ORP compliance.
    decided_by:
      - name: "Asbjørn"
    basis: >
      Governance model is deferred to GOVERNANCE.md and to the community 
      process. Premature codification of conflict resolution risks encoding 
      the founder's assumptions before the community has had input.
    alternatives_considered: "Explicit arbitration process — deferred to governance working group"
    dissenting_views: null
```

---

## L5: Fork Registry

```yaml
this_document:
  document_id: "orp-meta-001"
  forked_from: null
  fork_reason: "Original self-documentation"
  key_differences: "N/A"

known_forks: []

responses: []

invitation: >
  This document is explicitly the most important one to fork and challenge. 
  If you believe the protocol's own reasoning is flawed, its philosophical 
  foundation is wrong, its adjacent framework analysis is incomplete, or 
  its self-assessment is self-serving — this is where to say so.
  
  Specific challenges invited:
  - Is REE the right philosophical foundation? What would a different foundation produce?
  - Is the five-layer structure the right decomposition?
  - What adjacent frameworks are missing from Source 2?
  - Is the founder's stated intent (step back after launch) credible and structurally supported?
  - What failure modes does this document not acknowledge?
```

---

*This document is ORP-Full compliant under OpenReason Protocol v0.1.*
*It is the protocol looking at itself. Treat it with appropriate scepticism.*
