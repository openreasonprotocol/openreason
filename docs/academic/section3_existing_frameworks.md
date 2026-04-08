# Section 3: Why Existing Frameworks Miss It — and Why That Matters

## Draft v0.1 — for review and iteration

---

The constitutive problem described in Section 2 is not unknown to the fields that study data governance, algorithmic accountability, and information ethics. Elements of it appear in scattered form across the literature — in critiques of training data bias, in science and technology studies accounts of knowledge production, in political economy analyses of research funding. What is absent is a systematic engagement with the constitutive problem as a foundational challenge that precedes and conditions every other data governance concern.

Instead, the dominant frameworks address a different set of problems — real problems, addressed with genuine sophistication — while leaving the constitutive layer structurally untouched. This section argues that this omission is not merely a gap to be filled by incremental extension. It is a structural feature of how these frameworks are designed, rooted in the shared assumption identified in Section 2: that the data asset is a pre-ethical given, and that ethical work begins downstream of its production.

The consequence is not simply incomplete governance. It is the active generation of false confidence — the institutional impression that data-driven decisions have been subjected to adequate ethical scrutiny, when the most fundamental layer of that scrutiny has never been applied. This false confidence is, we argue, more epistemically dangerous than acknowledged ignorance. It forecloses the questions that most need asking.

### 3.1 Data Protection Frameworks: Governing Access, Not Constitution

The General Data Protection Regulation (GDPR) and its analogues represent the most comprehensive regulatory response to data ethics yet produced. Their core concerns — consent, purpose limitation, data minimization, the right to erasure — address the relationship between data subjects and the institutional actors who collect and process their data. This is genuinely important work. But it is work organized entirely around the question of access: who may hold data, for what declared purposes, under what conditions of subject consent.

The GDPR does not ask how a dataset was constituted. It does not require documentation of what was excluded from collection, or why. It does not mandate disclosure of the funding structures that shaped the scope of data gathering. It does not address the incentive environments within which data production decisions were made. A dataset assembled under conditions of severe scope capture and systematic exclusion — fully compliant with GDPR in every particular — receives no additional scrutiny under the regulation than a dataset assembled with rigorous attention to representational completeness and documented provenance.

This is not a criticism of data protection frameworks per se. Consent and access are legitimate governance concerns. The point is more precise: data protection frameworks were designed to solve a different problem than the constitutive problem, and they solve that problem reasonably well. The error is in treating compliance with data protection frameworks as evidence that data assets are epistemically sound — a conflation that the frameworks themselves do not claim but that institutional practice routinely produces.

### 3.2 Algorithmic Accountability: Auditing Outputs, Not Origins

The algorithmic accountability movement — represented by impact assessment requirements, audit frameworks, and transparency obligations emerging in jurisdictions including the EU AI Act — addresses the behavior of systems built on data: their accuracy, their fairness across groups, their explainability, their susceptibility to discrimination. These are substantive concerns, and the technical sophistication brought to bear on them has advanced considerably in recent years.

But algorithmic accountability, as currently constituted, audits outputs. It asks: given this system, trained on this data, operating in this context, does it perform equitably? It does not ask: under what conditions was the training data constituted, and do those conditions render the system's outputs epistemically unreliable in ways that output-level auditing cannot detect?

This limitation is precisely what Selbst et al. (2019) identify in their account of the "traps" that fairness-aware machine learning falls into. The Framing Trap — treating the technical system as the appropriate unit of analysis while the relevant causal factors lie in the social context surrounding it — and the Solutionism Trap — assuming that a technical intervention can resolve what is fundamentally a structural problem — both describe the condition in which algorithmic accountability operates. Selbst et al. propose extending the abstraction boundary to include social actors and institutional contexts. The present paper argues that extension must reach further still: to the constitutive conditions of the data assets themselves.

A system trained on data shaped by pharmaceutical funding incentives may perform with apparent consistency and technical fairness across the demographic groups represented in its evaluation set, while producing outputs that systematically reflect the interests of its data's funders. No output-level audit will detect this. The distortion is not in the model's behavior given the data; it is in the data's relationship to the reality it purports to represent. These are different problems requiring different interventions.

### 3.3 Open Data Initiatives: Democratizing Access to Constitutively Distorted Assets

Open data initiatives — mandating or encouraging the public release of government, scientific, and institutional data — proceed from the sound intuition that restricted access to data concentrates epistemic power inappropriately. If data is made openly available, the argument runs, a broader community of researchers and analysts can scrutinize it, replicate findings, and correct errors. Transparency of access, on this view, is a corrective mechanism for the distortions that closed data enables.

This intuition has merit, but it rests on an assumption that open data initiatives do not themselves examine: that access to a dataset is equivalent to access to the knowledge it purports to encode. If a dataset was constituted under conditions of scope capture, publication bias, and systematic exclusion, making it openly available does not correct those constitutive distortions — it democratizes them. A broader community of researchers now builds on a common distorted foundation, potentially with greater collective confidence in its validity than a smaller community would have had.

The open data movement has produced important gains in scientific reproducibility and public accountability. The point is not to dismiss those gains but to identify their limits precisely. Open access to a dataset does not provide access to the institutional conditions of its production — the funding structures, the scope decisions, the exclusion criteria, the incentive environments — without which the dataset cannot be adequately interpreted. Provenance, in this sense, is not a supplementary nicety; it is a prerequisite for epistemically responsible use.

### 3.4 The Shared Architecture of Failure

Surveyed together, these frameworks reveal a consistent structural pattern. Each addresses a genuine governance concern — access rights, output fairness, public availability — with genuine competence. Each takes the data asset as its starting point and directs its ethical attention to what happens downstream of production. None provides a mechanism for examining the constitutive conditions of data assets themselves, and none treats those conditions as within its scope.

This shared architecture is not accidental. It reflects the institutional and political conditions under which data governance has developed: regulatory frameworks responding to visible harms, technical communities optimizing within given problem definitions, open access movements challenging access asymmetries without challenging production asymmetries. Each intervention was shaped by the problems it could see — which were, in each case, the problems that existed downstream of constitution.

The result is a governance landscape that is simultaneously sophisticated and systematically incomplete. Within its own terms, it functions. Against the standard of epistemic accountability for data-driven decisions — the standard that the constitutive problem demands — it fails. And it fails in the particular way that is hardest to remedy: not through acknowledged ignorance, but through the active production of false confidence that forecloses the questions most in need of asking.

A pharmaceutical dataset compliant with GDPR, audited for algorithmic fairness, and publicly available under an open license may be all of these things simultaneously while encoding decades of funded distortion in its constitutive structure. Current frameworks have no instrument for this. The absence of such an instrument is not a minor gap in an otherwise adequate architecture. It is the missing foundation.

---

*Next: Section 4 — REE as the Philosophical Foundation*

---

**References cited in this section (to be compiled in full bibliography):**
- Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. *Proceedings of the 2019 Conference on Fairness, Accountability, and Transparency*, 59–68. https://doi.org/10.1145/3287560.3287598
- European Parliament and Council. (2016). *General Data Protection Regulation (EU) 2016/679*. Official Journal of the European Union.
- European Parliament and Council. (2024). *Artificial Intelligence Act (EU) 2024/1689*. Official Journal of the European Union.
