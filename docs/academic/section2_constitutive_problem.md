# Section 2: The Constitutive Problem in Data

## Draft v0.1 — for review and iteration

---

The dominant discourse around data governance proceeds from a shared and largely unexamined assumption: that data, once collected, represents a more or less faithful encoding of reality, whose ethical problems emerge downstream — in how it is stored, accessed, processed, or acted upon. Privacy frameworks regulate who can see the data. Algorithmic accountability frameworks regulate what decisions the data informs. Fairness-aware machine learning intervenes in how models trained on data perform across demographic groups. Each of these interventions treats the data asset itself as an antecedent — a given — and focuses its ethical attention on what happens next.

This assumption is the fundamental error that the present paper seeks to correct.

Data is not a pre-ethical given. It is a social product, constituted through a series of decisions — about what to measure, how to measure it, which observations to retain and which to discard, how to label and classify what remains — each of which is made by agents operating inside institutional structures that carry specific interests, incentive profiles, and epistemic commitments. These decisions do not merely introduce noise into an otherwise faithful representation of reality. They determine, at the most fundamental level, what reality the data is capable of representing at all. The ethical character of a data asset is not a downstream property; it is present at the moment of constitution, and no subsequent intervention can fully recover what was never encoded.

We term this the **constitutive problem in data**: the systematic encoding of interests, exclusions, and assumptions into data assets prior to and independently of any downstream use, in ways that are structurally incentivized, epistemically invisible, and currently unaddressed by existing governance frameworks.

### 2.1 Incentive Structures and Scope Capture

The constitutive problem does not require dishonesty. It does not require conspiracy. It requires only that the agents who produce data operate within institutional structures that reward certain findings and penalize others — a condition that describes the overwhelming majority of data production in contemporary science, policy, and commercial research.

Consider the canonical case of privately funded scientific research. A pharmaceutical company commissions a clinical trial. The scope of the trial — which outcomes are measured, across which populations, over which timeframe — is determined before data collection begins, by agents whose institutional interests are served by particular configurations of findings. The scientist conducting the trial may be entirely honest within that scope. But the scope itself is not epistemically neutral. It is the product of what Ravetz (1971) called "finalization" — the closure of research agendas around commercially or politically useful questions before scientific inquiry can follow its own logic.

The consequences are well documented. Ioannidis (2005) demonstrated that a majority of published research findings in certain domains are false, driven not by fraud but by systematic publication bias in favor of confirmatory results. The "file drawer problem" (Rosenthal, 1979) describes the structural disappearance of null and anomalous findings — not suppressed through active concealment, but through the rational calculation of agents who correctly anticipate that inconvenient findings will not be funded, published, or institutionally rewarded. The anomaly that does not fit the research agenda does not merely go unreported; it disappears from the epistemic record entirely, leaving no trace of its absence.

This is not a failure of individual scientific integrity. It is a structural property of data production organized around private interest rather than public epistemic good. The result is that published datasets — the raw material from which models are built, policies are derived, and institutional knowledge is accumulated — systematically overrepresent findings that confirmed the interests of those who funded their production. The data asset that downstream governance frameworks take as their starting point is already distorted before those frameworks engage.

### 2.2 Exclusion by Design and the Absent Node

A second dimension of the constitutive problem concerns not what is distorted within a dataset, but what is absent from it entirely. Every dataset is defined as much by what it does not contain as by what it does. The choice of which populations to include in a study sample, which languages to represent in a training corpus, which geographic contexts to treat as default and which as edge cases, which historical periods to draw upon — each of these choices encodes assumptions about whose experience constitutes the relevant universe of inquiry.

Crawford and Paglen (2021) demonstrate this concretely in the domain of image classification: the taxonomies used to label training data carry inherited cultural assumptions that are invisible precisely because they are treated as neutral descriptions rather than interpretive acts. But the problem extends far beyond image classification. It describes the structural condition of any dataset assembled by agents with a particular social position, institutional context, and set of interests — which is to say, every dataset.

The epistemological significance of this extends to artificial intelligence systems trained on such data. When a system develops inferential capacity from a dataset, the absences in that dataset are not merely gaps in coverage; they shape the inferential structure itself. Patterns that exist only in the included population are generalized as universal. Relationships that would have appeared differently, or not appeared at all, in the excluded population become invisible assumptions built into the model's reasoning. The system does not know what it does not know — but more critically, it cannot flag the boundaries of its own competence, because those boundaries were constituted before the system existed.

We describe this as the **absent node problem**: the epistemically significant condition in which the experiential graph that grounds a system's inferential capacity was populated from a systematically non-representative sample, producing inferences that present as universal but are in fact particular — and that carry no internal signal of their own particularity.

### 2.3 The Compounding of Constitutive Distortion

Individually, each dimension of the constitutive problem is significant. In combination, their effects are not merely additive but compounding. Scope capture determines which phenomena are measured. Publication bias determines which measurements enter the record. Exclusion by design determines whose experience those measurements reflect. The resulting dataset is then treated as the evidential basis for downstream decisions — policy choices, model training, institutional knowledge — whose errors propagate forward in ways that are structurally disconnected from their constitutive origin.

There is no mechanism within existing governance frameworks for tracing a downstream error back to its constitutive source. GDPR does not require documentation of what was not collected. Algorithmic impact assessments evaluate model outputs without examining the incentive structures that shaped the training data. Fairness metrics detect disparate performance across groups represented in evaluation sets — but cannot detect the impact of groups excluded from both training and evaluation. Each framework takes the data asset as its starting point and asks legitimate questions about what happens next. None asks the prior question: under what conditions, by whose decisions, and in whose interests was this data constituted in the first place?

That is the question the present paper addresses.

---

*Next: Section 3 — Why Existing Frameworks Miss It*

---

**References cited in this section (to be compiled in full bibliography):**
- Crawford, K., & Paglen, T. (2021). Excavating AI: The politics of images in machine learning training sets. *AI & Society*, 36, 1105–1116.
- Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLOS Medicine*, 2(8), e124.
- Ravetz, J. R. (1971). *Scientific Knowledge and Its Social Problems*. Oxford: Clarendon Press.
- Rosenthal, R. (1979). The file drawer problem and tolerance for null results. *Psychological Bulletin*, 86(3), 638–641.
