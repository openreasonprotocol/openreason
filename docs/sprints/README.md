# Sprint Planning for OpenReason

This directory contains sprint planning documents for OpenReason development.

---

## Sprint Structure

Each sprint should include:

1. **Sprint Goal** — One clear objective (1-2 sentences)
2. **Scope** — What's in scope and what's explicitly out of scope
3. **Tasks** — Broken down into estimable work items
4. **Success Criteria** — How we know the sprint is complete
5. **Dependencies** — What needs to exist before this sprint can start
6. **Retrospective** — What we learned (added after sprint completes)

---

## Sprint Naming

Sprints are named by phase and number:
- `phase0-sprint1.md` — First sprint in Phase 0
- `phase1-sprint1.md` — First sprint in Phase 1 (Core Tooling)

---

## Current Sprint

See the most recent sprint file for current work.

---

## Sprint Philosophy

From the ROADMAP:

> Good open source infrastructure earns adoption in layers. The protocol must be implementable manually before tooling is built. Tooling must be stable before agents are layered on top. Agents must be trustworthy before integrations embed them in critical workflows.

This means:
- **Don't skip phases** — each phase must be stable before the next begins
- **Don't over-engineer** — build the minimum that proves the concept works
- **Don't build without testing** — every sprint should produce something we can validate

---

## Sprint Retrospectives

After each sprint, we document:
- What worked well
- What didn't work
- What assumptions were wrong
- What we learned about the protocol or the tooling
- What should change for the next sprint

These are **not ORP-compliant documents** (too heavyweight for internal planning), but they should be **ORP-inspired** — transparent about reasoning, honest about limitations, and open to challenge.

---

*Sprint planning docs live here. Start with `sprint-template.md` when creating a new sprint.*
