# OpenReason Governance Model v0.1

> A transparency protocol that does not govern itself transparently would contradict its own principles. This document defines how OpenReason is governed — how decisions are made, who makes them, and how power is structured to prevent capture by any single actor including its founder.

---

## Founding principle

OpenReason exists as a public good. It is not owned by its creator, by any company, or by any government. The governance model is designed to ensure that remains true permanently — not as an aspiration but as a structural fact.

The single most important design constraint on governance is this: **the protocol must be able to function, evolve, and be maintained without its founder.** Any governance structure that depends on the founder's continued involvement has failed, regardless of how well it works while the founder is present.

---

## Phase 0 Governance: Founder stewardship
*Active from: launch — until first Stewardship Council is seated*

During Phase 0, the founder (Asbjørn) retains editorial control over the protocol specification for the sole purpose of incorporating community feedback and preparing v1.0 for ratification. This is a temporary and explicitly limited authority.

**What the founder can do during Phase 0:**
- Publish changes to the protocol specification
- Merge contributions to the core repository
- Represent the project publicly
- Invite contributors and working group members

**What the founder cannot do during Phase 0:**
- Commercialise the protocol or its name without explicit community consent
- Transfer governance rights to any private entity
- Make irrevocable decisions about the protocol's direction
- Extend Phase 0 beyond the conditions defined below

**Phase 0 ends when:**
1. The Stewardship Council (defined below) has been constituted with a minimum of five members from at least three different organisations or institutions
2. The Council has formally ratified this governance document with any amendments
3. The founder has formally transferred administrative rights to the Council

There is no time limit on Phase 0 — it ends when governance is genuinely ready, not on a calendar date. However the founder commits to actively working toward Council formation within six months of the first public release.

---

## Permanent Governance Structure

### The Stewardship Council

The Stewardship Council is the governing body of OpenReason. It is responsible for ratifying protocol versions, managing the domain and trademarks, and ensuring the project remains a public good.

**Composition:**
- Minimum 5 members, maximum 11
- No single organisation may hold more than 2 seats
- At least one seat reserved for an academic or research institution
- At least one seat reserved for a civil society or public interest organisation
- At least one seat reserved for a government or public sector body
- The founder may hold a seat but has no special authority beyond one vote

**How Council members are selected:**
- Initial Council: founder nominates candidates from active contributors; nominees accepted by consensus of the initial group
- Subsequent members: nominated by existing Council members or by the contributor community; approved by two-thirds Council vote
- Term: three years, renewable once
- Removal: two-thirds Council vote, with documented reasons published under ORP

**What the Council decides:**
- Protocol version ratification (requires two-thirds majority)
- Governance document amendments (requires two-thirds majority)
- Trademark and name usage policy
- Formal partnerships with external organisations
- Dissolution of the project (requires unanimous vote)

**What the Council does not decide:**
- Day-to-day repository management (delegated to Working Groups)
- Technical implementation details (delegated to Working Groups)
- Individual contribution acceptance (delegated to Working Groups)

---

### Working Groups

Working Groups handle the ongoing technical and community work of the protocol. They operate autonomously within their defined scope and report to the Council only when decisions exceed their delegated authority.

**Standing Working Groups:**

| Working Group | Scope | Minimum Members |
|---------------|-------|-----------------|
| Core Specification | ORP spec versions, schema, validation | 3 |
| Tooling | CLI, validator, SDK, API | 3 |
| Extensions | Side protocols (ORP-AI, ORP-Econ, etc.) | 2 per extension |
| Education | ORP-Edu, classroom tools, documentation | 2 |
| Community | Contributor experience, events, communications | 2 |

**Working Group principles:**
- Any contributor with two or more accepted contributions may join a Working Group
- Working Groups elect their own leads by simple majority
- Decisions within Working Group scope are made by rough consensus (no formal vote required)
- Any Working Group member may escalate a decision to the full group or to the Council

---

### Contributors

Anyone who submits an accepted pull request, published critique, or formal fork becomes a contributor. Contributors have:
- Voice in Working Group discussions
- The right to be nominated for Working Group membership
- Recognition in the contributor record

There are no tiers of contributor beyond Working Group membership and Council membership.

---

## Decision-making process

### For protocol changes (spec amendments)

1. **Proposal** — any contributor may open a proposal as a GitHub issue with a clear statement of the problem and proposed change
2. **Discussion** — minimum 30 days open for community comment
3. **Working Group review** — Core Specification Working Group produces a recommendation
4. **Council ratification** — two-thirds majority vote for acceptance into a new version
5. **Publication** — new version published with full changelog and reasoning documented in L4

### For tooling and implementation

1. **Proposal** — contributor opens issue or pull request
2. **Review** — Tooling Working Group reviews within 14 days
3. **Merge** — Working Group lead approves by rough consensus
4. **No Council involvement** required unless change affects the spec

### For governance amendments

1. **Proposal** — any Council member or 5 contributors acting together may propose an amendment
2. **Discussion** — minimum 60 days open for community comment
3. **Council vote** — two-thirds majority required
4. **Publication** — amendments published with full reasoning in a new version of this document

### For urgent decisions

If a security issue or other urgent matter requires a decision faster than the standard process allows, the Council may act by two-thirds vote without the standard discussion period. The decision and reasoning must be published within 48 hours.

---

## Versioning and ratification

OpenReason follows semantic versioning adapted for a protocol:

- **Major versions (1.0, 2.0)** — breaking changes to the core schema. Require Council ratification and a minimum 60-day community comment period.
- **Minor versions (0.1, 0.2, 1.1)** — backwards-compatible additions. Require Working Group approval and 30-day comment period.
- **Patches (0.1.1)** — corrections to errors or clarifications. Require Working Group approval, no minimum comment period.

A version is not ratified until there is at least one working implementation that demonstrates the changes are implementable. This is the IETF principle of "rough consensus and running code" applied to ORP.

---

## Funding and commercialisation

**Prohibited:**
- Selling the OpenReason name or protocol
- Granting exclusive implementation rights to any party
- Accepting funding that conditions the protocol's direction or decisions

**Permitted:**
- Accepting donations for infrastructure costs (hosting, CI, domain)
- Grants for specific development work, provided the output is public and open
- Working Group members and contributors being employed by organisations that build on ORP
- Commercial tools and services that implement ORP, provided they do not misrepresent compliance or claim exclusivity

**Transparency requirement:**
All funding received by the project — its source, amount, and intended use — must be published publicly. This is not optional.

---

## Founder handover

The founder commits to the following upon Council formation:

1. Transfer of all administrative rights to the Council within 30 days of Council formation
2. Transfer of the project domain and any registered trademarks to the Council or its designated legal entity
3. Publication of a formal handover document in the L4 accountability ledger of this governance document
4. Retention of contributor status with no special authority

The founder may subsequently participate as a Council member if nominated and elected by the community through the standard process. If elected, the founder holds one vote — the same as any other Council member.

**The founder explicitly waives:**
- Any right to veto Council decisions
- Any claim to ownership of the protocol or its name after handover
- Any right to unilateral changes to the protocol after handover

This waiver is published publicly and is intended to be permanent.

---

## Conflict of interest

Any Council member or Working Group lead must declare a conflict of interest when a decision could benefit their employer, their own work, or any organisation they are affiliated with. Declaration does not require recusal — it requires transparency. The community judges whether the conflict affected the decision.

Undisclosed conflicts of interest are grounds for removal from the Council or Working Group.

---

## Protocol dissolution

If the Stewardship Council determines that OpenReason should be dissolved:

1. A unanimous Council vote is required
2. A 90-day community comment period must precede any dissolution
3. All protocol documentation, tooling, and worked examples must be archived in a publicly accessible location in perpetuity
4. No private entity may acquire exclusive rights to the OpenReason name or protocol upon dissolution

A dissolved protocol is better than a captured one.

---

## Amendments to this document

This governance document is v0.1 and is explicitly provisional. It was written by the founder before any community exists. Its most important feature is that it can be amended by the community once that community forms.

The founder's expectation is that the Council's first substantive act will be to review and amend this document based on the community's actual needs and the lessons of early adoption. That expectation is not binding — the Council may find this document adequate or may rewrite it entirely. Both outcomes are acceptable.

What is not acceptable is a governance document that cannot be changed by the community it governs.

---

## Accountability

This governance document is itself an ORP document. Its provenance, assumptions, and known limitations are documented in ORP_META.md. Changes to this document are logged in its own L4 accountability ledger.

The governance of the protocol is subject to the same transparency standards the protocol demands of everything else.

---

*OpenReason Governance Model v0.1 — February 2026*
*Written by the founder. Intended to be amended by the community.*
*Fork it.*
