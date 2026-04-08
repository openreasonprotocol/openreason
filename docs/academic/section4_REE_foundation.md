# Section 4: Rational, Empathy-Informed Ethics as Philosophical Foundation

## Draft v0.1 — for review and iteration

---

The constitutive problem established in Section 2 and the systematic inadequacy of existing frameworks demonstrated in Section 3 together define the requirements for an adequate philosophical foundation. That foundation must do three things that existing ethical frameworks, applied to data governance, have not done.

First, it must treat ethical responsibility as operative at the moment of data constitution — not downstream of it. Second, it must integrate rational accountability with genuine attention to whose experience is encoded and whose is absent, without reducing either to the other. Third, it must be operationalizable — capable of grounding concrete procedural requirements rather than generating abstract principles that leave institutional practice unchanged.

This section argues that Rational, Empathy-Informed Ethics (REE) satisfies these requirements, and that it does so in ways that the dominant ethical frameworks brought to bear on data governance — utilitarian calculus, deontological rule-following, and procedural fairness — structurally cannot.

### 4.1 The Failure Modes of Existing Ethical Frameworks at the Constitutive Layer

The application of established ethical frameworks to the constitutive problem reveals a consistent pattern of inadequacy, not through failure of internal logic, but through the mismatch between what those frameworks were designed to evaluate and what the constitutive problem requires.

Utilitarian approaches to data ethics focus on aggregate outcomes: does the use of this dataset produce more benefit than harm across the affected population? This framing has two constitutive-layer failures. It requires that the affected population be defined before the calculus can proceed — but the definition of that population is itself a constitutive decision, one that can exclude the groups most likely to bear the costs of distorted data. And it evaluates outcomes, which are downstream phenomena, rather than the constitutive conditions that shaped the data from which those outcomes derive. A utilitarian calculus applied to a constitutively distorted dataset will optimize within the distortion rather than detecting it.

Deontological frameworks fare differently but no better. Their strength — the imposition of inviolable constraints that aggregate benefit cannot override — maps poorly onto the constitutive problem, which does not typically involve the violation of explicit duties but rather the structural failure to discharge epistemic responsibilities that have not yet been codified as duties. GDPR is, in important respects, a deontological instrument: it imposes obligations that cannot be overridden by appeals to beneficial outcomes. But as Section 3 demonstrated, the duties it codifies are access duties, not constitution duties. Deontological frameworks can only require what has been recognized as obligatory; they provide no mechanism for identifying what ought to be obligatory but has not yet been recognized as such.

Procedural fairness approaches — including the family of frameworks emerging from Rawlsian political philosophy — ask whether the processes by which decisions are made satisfy conditions of impartiality and equal consideration. This is closer to the constitutive concern, but it still tends to evaluate procedure at the point of decision rather than at the point of data production. The question "was this policy decision made through a fair process?" does not automatically generate the prior question "was the evidential basis on which this decision rested constituted through a fair process?" The epistemic foundations of decision-making remain outside the frame.

### 4.2 REE: Core Architecture

Rational, Empathy-Informed Ethics begins from a different diagnostic. Its foundational observation — developed through the question of how artificial systems develop inferential capacity — is that the ethical character of a reasoning system is determined not primarily by the rules it follows or the outcomes it produces, but by the experiential graph from which its inferences are drawn. The question is not "does this system reason correctly given its inputs?" but "whose experiences populated the nodes from which its reasoning proceeds?"

This reorientation has profound consequences for how ethical responsibility is located. If the ethical character of inference is determined at the level of the experiential graph — at the level, that is, of the data from which reasoning capacity is built — then ethical responsibility cannot be discharged downstream of that construction. It must be operative at the moment of constitution.

REE is organized around five principles that give this foundational observation concrete ethical content.

**Measured Compassion** holds that ethical claims about welfare must be testable rather than assumed. "This dataset adequately represents the affected population" is not a compassionate statement — it is a hypothesis, and REE requires that hypothesis to be tested against evidence of what populations are actually present in the data, what populations are absent, and what the implications of those absences are for downstream use. Compassion that cannot be measured cannot be verified, and cannot therefore be held accountable.

**Rational Inquiry** holds that every assumption underlying a data production decision must be treated as a claim that could in principle be false, and that evidence capable of challenging those assumptions must be genuinely sought rather than avoided. Applied to the constitutive problem, this principle directly addresses scope capture and publication bias: it requires that the incentive structures within which data was produced be documented and made available for scrutiny, precisely because those structures represent the conditions under which assumptions about scope and relevance were formed.

**Simulated Consequences** requires that foreseeable downstream effects of constitutive decisions be modeled before those decisions are finalized. The absent node problem described in Section 2 is, in significant part, a failure of consequence simulation: the effects of systematic exclusion on downstream inference are foreseeable — they have been documented extensively in the literature — but they are not routinely modeled at the point of data constitution. REE makes this modeling a prerequisite rather than an optional supplement.

**Universal Sentience** is the principle that most directly addresses the absent node problem at its deepest level. It holds that no affected party may be rendered invisible by the framing of an inquiry — that the epistemic scope of a data production process must be actively interrogated for whom it excludes, and that exclusions must be documented, justified, or remediated. This is not merely a fairness principle in the distributional sense; it is an epistemological principle. A dataset that systematically excludes certain communities does not merely fail those communities in a moral sense — it produces inferences that will be presented as universal while being particular, generating epistemic harm that extends beyond the excluded population to everyone who relies on those inferences.

**Transparent Accountability** closes the architecture by requiring that every significant decision in the data production process — every scope decision, every exclusion criterion, every funding structure, every methodological choice — be documented, attributed, and made available for scrutiny. This is the principle that converts the other four from aspirations into verifiable commitments. Without transparent accountability, measured compassion cannot be verified, rational inquiry cannot be audited, consequence simulations cannot be challenged, and the scope of universal sentience claims cannot be assessed.

### 4.3 REE Against the Existing Frameworks

The comparison with existing ethical frameworks is instructive not as a claim of superiority but as a demonstration of what REE provides that the others structurally cannot.

Where utilitarianism evaluates aggregate outcomes, REE requires that the population over which outcomes are aggregated be itself subject to scrutiny — that the boundaries of the relevant universe be explicitly defined, documented, and challenged. The utilitarian frame takes the population as given; REE treats it as a constitutive decision requiring justification.

Where deontological frameworks impose obligations that have been recognized, REE provides the epistemological grounding for recognizing new obligations — specifically, the obligation to account for the constitutive conditions of data assets. This is not a replacement of deontological constraint but a foundation for generating the constraints that the constitutive problem demands.

Where procedural fairness asks whether decision processes satisfy conditions of impartiality, REE extends that question upstream: it asks whether the evidential basis on which decision processes operate was itself constituted under conditions that can withstand scrutiny. Procedural fairness at the decision layer cannot compensate for constitutive distortion in the evidential layer; REE requires both.

Floridi's information ethics (2013) provides a complementary foundation, particularly in its insistence that informational entities carry intrinsic moral significance and that the infosphere — the totality of informational environments — constitutes a domain of genuine ethical concern. Where Floridi's framework grounds the moral significance of information as such, REE grounds the specific obligations that follow from the constitutive conditions under which information is produced. The two frameworks are not in tension; REE can be understood as specifying the constitutive-layer ethics that Floridi's broader framework implies but does not fully develop.

### 4.4 Why REE Is Operationalizable Where Others Are Not

A persistent criticism of applied ethics frameworks is that they generate principles without generating procedures — that they can identify what ought to be done in the abstract without providing traction on the institutional practices that determine what is actually done. This criticism applies with particular force to the constitutive problem, where the relevant decisions are distributed across research institutions, funding bodies, data annotation teams, and computational infrastructure in ways that resist simple procedural codification.

REE's architecture was designed with this operationalization challenge in mind. Each of its five principles maps directly onto a category of procedural requirement: measured compassion requires population documentation; rational inquiry requires incentive structure disclosure; simulated consequences requires prospective impact modeling; universal sentience requires exclusion auditing; transparent accountability requires attribution and version control for methodological decisions.

These mappings are not incidental. They reflect the core REE commitment to making ethical claims testable — to ensuring that the gap between principle and practice is itself subject to scrutiny. An ethical framework that cannot be violated in a verifiable way provides no accountability. REE is designed to be violable in ways that are detectable, which is the prerequisite for any governance framework worthy of the name.

It is this operationalization architecture that the OpenReason Protocol, presented in Section 5, implements.

---

*Next: Section 5 — ORP as Operationalization*

---

**References cited in this section (to be compiled in full bibliography):**
- Floridi, L. (2013). *The Ethics of Information*. Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199641321.001.0001
- Rawls, J. (1971). *A Theory of Justice*. Cambridge, MA: Harvard University Press.
- Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. *Proceedings of the 2019 Conference on Fairness, Accountability, and Transparency*, 59–68.
- REE Philosophy Document. (2025). *Rational, Empathy-Informed Ethics: The Philosophical Foundation of OpenReason*. Public Reason Project. https://docs.publicreasonproject.org/protocol/philosophy
