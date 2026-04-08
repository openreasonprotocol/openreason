# Section 5: The OpenReason Protocol as Operationalization of REE

## Draft v0.1 — for review and iteration

---

The argument developed across Sections 2 through 4 establishes a philosophical requirement: that data governance frameworks must address the constitutive conditions of data assets, grounded in an ethical framework that integrates rational accountability with genuine attention to whose experience is encoded and whose is absent. Section 4 concluded that REE satisfies this requirement philosophically, and that its operationalizability — its capacity to generate verifiable procedural requirements from ethical principles — is what distinguishes it from existing frameworks that generate principles without traction.

This section presents the OpenReason Protocol (ORP) as the concrete operationalization of that philosophical architecture. ORP is not a theoretical proposal. It is a working protocol, implemented in a publicly available specification with associated validation tooling, whose structural design follows directly from the REE principles established in Section 4. The relationship between REE and ORP is not one of inspiration but of implementation: each protocol layer is the procedural instantiation of a specific REE principle, designed to make that principle verifiable in practice.

We demonstrate the protocol's operation through its application to a concrete case — the 2024 Danish property tax reform — showing how ORP surfaces constitutive-layer information that existing governance frameworks leave unexamined.

### 5.1 Protocol Architecture: From Principle to Procedure

ORP is structured as five sequential layers of increasing comprehensiveness, defined by three compliance levels. The layered architecture reflects a deliberate design choice: rather than requiring full constitutive-layer accountability in a single step — a requirement that would face prohibitive implementation barriers in most institutional contexts — ORP provides a graduated pathway from minimum viable transparency to full epistemic accountability. Each layer corresponds to a specific REE principle and addresses a specific dimension of the constitutive problem.

**Layer 1: Data Provenance** operationalizes Rational Inquiry and Transparent Accountability at the most foundational level. It requires explicit documentation of every dataset used in a reasoning process: source, methodology, collection period, cleaning decisions, known limitations, and — critically — access conditions that would allow independent verification of the documented claims. Provenance documentation under ORP is not a summary description of data sources; it is a structured record of the decisions made in constituting the data asset, attributed to specific agents at specific points in time.

The constitutive significance of Layer 1 is in what it requires to be documented beyond what existing frameworks mandate. GDPR requires documentation of data processing activities; Layer 1 requires documentation of data production decisions — the scope choices, the exclusion criteria, the funding relationships, the methodological alternatives considered and rejected. This is the information that existing frameworks systematically fail to capture, and whose absence renders downstream scrutiny epistemically incomplete.

**Layer 2: Consequence Simulation** operationalizes Simulated Consequences. It requires that the reasoning process built on the documented data assets include explicit modeling of potential outcomes under multiple scenarios, with stated assumptions, identified uncertainties, and sensitivity analysis that tests the robustness of conclusions to variation in key parameters. Crucially, scenarios must include conditions under which the documented limitations of the data assets — the exclusions, the scope constraints, the funding relationships disclosed in Layer 1 — affect the conclusions. This is the layer at which constitutive distortions, once documented, are required to be followed through into their downstream implications.

**Layer 3: Empathy Mapping** operationalizes Measured Compassion and Universal Sentience. It requires explicit identification of all parties affected by the reasoning process and its outputs, including parties not represented in the underlying data assets. For each identified stakeholder group, ORP requires documentation of projected impacts under the scenarios modeled in Layer 2, with particular attention to minority stakeholders whose interests may be obscured by aggregate analysis. The absent node problem identified in Section 2 is directly addressed here: groups excluded from the data must be identified as stakeholders whose absence from the evidential base is itself a relevant fact about the reliability of conclusions that affect them.

**Layer 4: Accountability Ledger** operationalizes Transparent Accountability at the decision level. It requires that every significant methodological decision made in the reasoning process — every choice about scenario scope, every exclusion from stakeholder mapping, every assumption built into consequence simulations — be recorded with attribution (who made the decision), timestamp (when it was made), and rationale (why it was made and what alternatives were considered). The accountability ledger converts the reasoning process from an output into a traceable record, enabling scrutiny not just of conclusions but of the decision pathway that produced them.

**Layer 5: Fork Registry** operationalizes Rational Inquiry at the social level — extending the individual epistemic commitment to challenge assumptions into a structural mechanism for collective scrutiny. It provides a formal framework for proposing, documenting, and comparing alternative versions of an ORP document that adopt different assumptions, scope definitions, or methodological choices. A fork is not a competing claim that one version is correct and another is wrong; it is a structured acknowledgment that different starting assumptions produce different conclusions, and that the relationship between assumptions and conclusions should be transparent and contestable. The fork registry is ORP's institutional response to the absent node problem at the systemic level: it creates the conditions under which excluded perspectives can enter the reasoning process as documented alternatives rather than invisible absences.

### 5.2 Compliance Levels and Implementation Pathway

ORP defines three compliance levels that determine which layers are required:

**ORP-Basic** (Layer 1 only) establishes minimum viable transparency: any reasoning process built on documented data provenance is more epistemically accountable than one built on undocumented data, regardless of whether subsequent layers are implemented. This level is designed to be achievable by any institution willing to document its data sources with the specificity Layer 1 requires — a low barrier to entry that nonetheless captures the most fundamental constitutive-layer information currently absent from governance practice.

**ORP-Standard** (Layers 1–3) adds consequence simulation and stakeholder mapping to data provenance, producing a reasoning document that addresses the constitutive problem, its downstream implications, and its distributional effects on affected parties. This level is appropriate for policy decisions with significant public impact.

**ORP-Full** (All 5 layers) adds the accountability ledger and fork registry, producing a fully traceable and contestable reasoning record. This level is appropriate for decisions of major public significance, AI system development involving training data constitution, and scientific research operating under conditions of known funding conflict.

The compliance levels serve an additional function beyond graduated implementation: they create a publicly legible standard against which the epistemic accountability of any ORP document can be assessed. A document's compliance level is a claim about what scrutiny its reasoning has been subjected to — a claim that is itself verifiable against the protocol specification.

### 5.3 Demonstration: Danish Property Tax Reform

The 2024 Danish property tax reform provides a concrete demonstration of ORP's operation at full compliance. The reform involved the reassessment of property valuations across Danish municipalities, with significant distributional implications for homeowners, renters, and local authorities. It was selected as the demonstration case precisely because it represents a domain — public policy built on data-intensive administrative processes — where the constitutive conditions of the underlying data are rarely examined but significantly consequential.

Under ORP-Full, the reasoning process supporting the reform produces a document structured across all five layers. Layer 1 documentation reveals the provenance of property valuation datasets: their collection methodology, the historical periods from which valuation benchmarks are drawn, the known limitations of assessment models in specific property categories, and the administrative decisions that shaped which properties were assessed through which processes. This information exists in administrative records but is not currently required to appear in any public-facing governance document related to the reform.

Layer 2 consequence simulation models reform outcomes under multiple scenarios — including scenarios in which the documented limitations of valuation data affect distributional outcomes differently across property types and geographic areas. This surfaces the sensitivity of reform conclusions to constitutive assumptions that ORP-Basic documentation has made explicit.

Layer 3 empathy mapping identifies affected stakeholder groups including categories systematically underrepresented in the administrative data underlying the reform — including renters whose welfare is indirectly affected by valuations they have no direct relationship to, and property owners in geographic areas where valuation methodology is least reliable. These groups are present in the affected population but absent from the evidential base in ways that Layer 1 documentation makes explicit and Layer 3 requires to be carried forward into impact analysis.

Layer 4 records the methodological decisions made at each stage, attributed and timestamped, enabling retrospective scrutiny of the reasoning pathway rather than merely its conclusion. Layer 5 documents alternative reform scenarios proposed by researchers and advocacy organizations operating from different assumptions about property market dynamics and distributional priorities, enabling systematic comparison of how different starting assumptions produce different reform recommendations.

The ORP-Full document for the Danish property tax reform does not resolve the political and distributional questions the reform raises. It does something more epistemically fundamental: it makes the constitutive conditions of the reasoning process visible, traceable, and contestable in ways that no existing governance framework requires. The false confidence described in Section 3 — the institutional impression that adequate scrutiny has been applied — is replaced by documented transparency about what is known, what is assumed, what is excluded, and who decided.

### 5.4 ORP as Infrastructure, Not Prescription

A final clarification is necessary to prevent a significant misreading of ORP's purpose. The protocol does not prescribe conclusions. It does not determine what a correct property valuation is, what a sound pharmaceutical dataset looks like, or what a fair AI training corpus contains. These are substantive questions that require domain expertise, political deliberation, and empirical investigation that ORP does not and cannot replace.

What ORP provides is epistemic infrastructure: a structured framework within which the constitutive conditions of data-driven reasoning are made visible, and within which the gap between those conditions and the conclusions they support is subject to scrutiny. It is, in Floridi's terms, a contribution to the governance of the infosphere — not through content prescription but through procedural transparency that enables the self-correction mechanisms of rational inquiry to operate at the layer where they are currently most needed and most absent.

The protocol's value is therefore not contingent on any particular set of conclusions being reached. It is contingent on the epistemic conditions under which conclusions are reached being made accountable. That accountability is what the constitutive problem demands, what REE grounds philosophically, and what ORP implements procedurally.

---

*Next: Section 6 — Implications and Limits*

---

**References cited in this section (to be compiled in full bibliography):**
- OpenReason Protocol Specification v0.1. (2025). Public Reason Project. https://docs.publicreasonproject.org/protocol/specification
- OpenReason Protocol: Danish Property Tax Reform Example. (2025). Public Reason Project. https://docs.publicreasonproject.org/examples/danish-property-tax
- Floridi, L. (2013). *The Ethics of Information*. Oxford: Oxford University Press.
