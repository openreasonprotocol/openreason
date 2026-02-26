# Claude Code Context for OpenReason

This document provides context and guidelines for Claude Code (or other AI assistants) working on the OpenReason project.

---

## Important: Git Commit Policy

**DO NOT include Claude Code attribution in git commits.**

- ❌ Do NOT add: `🤖 Generated with [Claude Code](https://claude.com/claude-code)`
- ❌ Do NOT add: `Co-Authored-By: Claude <noreply@anthropic.com>`

Git commits should be clean and professional without AI attribution footers. The user will handle attribution separately if needed.

---

## Project Overview

**OpenReason (ORP)** is an open-source protocol that standardizes how reasoning is documented, shared, and challenged in consequential decisions — particularly in public policy and AI systems.

**Current Status:** Phase 0 (Foundation) — v0.1 draft
**Goal:** Build transparency infrastructure for democratic decision-making and AI development

---

## Core Philosophy

OpenReason is grounded in **Rational, Empathy-Informed Ethics (REE)** with five principles:

1. **Measured Compassion** — claims of compassion must be testable with evidence
2. **Rational Inquiry** — assumptions are hypotheses, not settled facts
3. **Simulated Consequences** — model outcomes before committing to decisions
4. **Universal Sentience** — no affected stakeholder should be invisible
5. **Transparent Accountability** — decisions must be logged, attributable, and auditable

See `docs/specs/REE_PHILOSOPHY.md` for full philosophical foundation.

---

## Protocol Structure

ORP documents consist of five layers plus a header:

| Layer | Name | Purpose |
|-------|------|---------|
| **Header** | Metadata | Document ID, authors, status, summary |
| **L1** | Data Provenance | Where data came from, what was excluded, how it was cleaned |
| **L2** | Consequence Simulation | Affected population, variables, scenarios, outcomes |
| **L3** | Empathy Mapping | Stakeholder impacts, minority stress-testing |
| **L4** | Accountability Ledger | Immutable log of decisions and who made them |
| **L5** | Fork Registry | Track document lineage, forks, and responses |

See `docs/specs/ORP_SPEC.md` for full technical specification.

---

## Repository Structure

```
open-reason/
├── README.md                          # Project overview
├── CLAUDE.md                          # This file (YOU ARE HERE)
├── CHANGELOG.md                       # Version history and releases
├── pyproject.toml                     # Python package configuration
├── orp_validator/                     # CLI and validator library
│   ├── cli.py                        # Main CLI entry point
│   ├── validator.py                  # Core validation logic
│   ├── commands/                     # CLI command implementations
│   ├── schemas/                      # JSON Schema for ORP v0.1
│   └── templates/                    # Document templates (basic/standard/full)
├── tests/                            # CLI/validator test suite
├── examples/
│   └── danish_property_tax_reform.yaml # First ORP-Full worked example
├── api/                              # REST API (PRODUCTION at api.publicreasonproject.org)
│   ├── main.py                       # FastAPI application
│   ├── routes.py                     # API route handlers
│   ├── models.py                     # Pydantic request/response models
│   ├── requirements.txt              # API dependencies
│   ├── Dockerfile                    # Container configuration
│   ├── docker-compose.yml            # Local development setup
│   ├── pytest.ini                    # Test configuration
│   ├── TESTING.md                    # Manual testing documentation
│   ├── README.md                     # API documentation
│   └── tests/                        # 39 automated tests (96% coverage)
│       ├── conftest.py               # Shared test fixtures
│       ├── test_validate_endpoint.py # /api/v1/validate tests
│       ├── test_check_endpoint.py    # /api/v1/check tests
│       ├── test_diff_endpoint.py     # /api/v1/diff tests
│       ├── test_security.py          # CORS, headers, security tests
│       └── README.md                 # Testing guide
├── docs/
│   ├── CONTRIBUTING.md               # How to contribute
│   ├── ROADMAP.md                    # Development phases and priorities
│   ├── specs/
│   │   ├── ORP_SPEC.md              # Protocol specification v0.1
│   │   └── REE_PHILOSOPHY.md        # Philosophical foundation
│   └── governance/
│       ├── GOVERNANCE.md            # Governance model
│       └── ORP_META.md              # Protocol's own provenance
└── .gitlab-ci.yml                    # CI/CD pipeline configuration
```

---

## Development Phases

**Phase 0 (Current)** — Foundation
- ✅ Core specification documents
- ✅ Worked example (Danish Property Tax Reform)
- ✅ Governance model
- ⏳ 60-day public comment period (not yet started)

**Phase 1 (Next)** — Core Tooling
- ORP CLI (`orp new`, `orp validate`, `orp diff`, `orp check`, `orp summarise`)
- ORP Validator (Python/JS libraries + REST API)
- ORP Schema (JSON/YAML schema definitions)
- Reference implementation validation

**Phase 2** — Developer Experience (GitHub integration, VS Code extension)
**Phase 3** — Agent Layer (AI-assisted document creation)
**Phase 4** — Side Protocols (ORP-AI, ORP-Econ, ORP-Env, etc.)
**Phase 5** — Platform and API (Hosted infrastructure)

See `docs/ROADMAP.md` for full details.

---

## Working Principles

### 1. Protocol-First, Not Product-First
OpenReason is a protocol (like OpenRTB or IETF RFCs), not a commercial product. Anyone can implement it. No single entity owns it.

### 2. Transparency Applied to Itself
The protocol demands transparency from others, so it must be transparent about its own reasoning. Every significant decision is documented in `docs/governance/ORP_META.md` using the same ORP structure it requires of others.

### 3. Incomplete by Design
v0.1 is explicitly incomplete. We document what we don't know, not just what we do. Missing pieces are flagged as "known limitations" rather than hidden.

### 4. Fork-First, Not Vote-First
Disagreement is resolved through forking and showing alternative reasoning, not through voting or consensus building. The best argument wins through demonstration.

### 5. No Founder Dependency
The governance model (see `docs/governance/GOVERNANCE.md`) is designed so the project can function without its founder. Any code, documentation, or process that requires founder involvement is a design failure.

---

## Coding Guidelines (for Phase 1+)

### Language Preferences
- **CLI:** Python (widely used in policy/data science, good for rapid development)
- **Validator:** Python + JavaScript/TypeScript (to support both backend and frontend use)
- **Schema:** JSON Schema (language-agnostic, widely supported)

### Code Quality Standards
- **Type hints required** (Python: use `mypy`, JS: use TypeScript)
- **Tests required** for all validator logic (pytest for Python, jest for JS)
- **Documentation required** for all public APIs
- **No external dependencies** for core validation logic (keep it portable)

### Transparency in Code
- Document **why** decisions were made in comments, not just **what** the code does
- Log all validation decisions with clear, actionable error messages
- Make assumptions explicit — no magic numbers or undocumented heuristics

---

## Sprint Organization

We use `docs/sprints/` for planning and tracking work.

Each sprint should have:
- **Sprint goal** (1-2 sentences)
- **Scope** (what's in, what's out)
- **Tasks** (broken down, estimable)
- **Success criteria** (how we know it's done)
- **Retrospective notes** (what we learned)

Sprint docs should be ORP-inspired but not ORP-compliant (too heavyweight for internal planning).

---

## Key Files Reference

| File | Purpose |
|------|---------|
| `README.md` | Project introduction for newcomers |
| `docs/specs/ORP_SPEC.md` | Technical specification — the source of truth |
| `docs/specs/REE_PHILOSOPHY.md` | Why the protocol exists and what principles guide it |
| `docs/ROADMAP.md` | What we're building and in what order |
| `docs/CONTRIBUTING.md` | How to propose changes, critique, or fork |
| `docs/governance/GOVERNANCE.md` | How decisions about the protocol are made |
| `docs/governance/ORP_META.md` | The protocol's own provenance documented under ORP |
| `examples/danish_property_tax_reform.md` | First complete ORP-Full example |

---

## When Working on OpenReason

### Always consider:
1. **Is this decision transparent?** Could someone else understand why we made this choice?
2. **Is this forkable?** If someone disagreed, could they take this and modify it?
3. **Are we documenting our assumptions?** What are we taking for granted that should be explicit?
4. **Who does this affect?** Are we considering all stakeholders, including edge cases?
5. **Can this work without the founder?** Is there institutional knowledge that needs to be written down?

### Red flags:
- ❌ "This is how we've always done it" (violates Rational Inquiry)
- ❌ Undocumented exclusions from datasets or scope
- ❌ Decisions made without recorded reasoning
- ❌ Processes that only one person understands
- ❌ Complexity without clear justification

### Green lights:
- ✅ "Here's the assumption and here's why we made it"
- ✅ "This is incomplete and here's what we don't know yet"
- ✅ "If you disagree with X, fork and show us your alternative"
- ✅ Clear error messages that teach, not just reject
- ✅ Documentation that explains the "why" not just the "what"

---

## Common Pitfalls to Avoid

### 1. Over-engineering Phase 1
The first tooling should be simple, correct, and usable — not feature-complete. Build the minimum that proves the protocol works.

### 2. Breaking backward compatibility casually
Once v1.0 is ratified, breaking changes require major version bumps. Treat the schema as a contract.

### 3. Hiding complexity in defaults
Default values are assumptions. Document them explicitly. A bad default silently applied is worse than requiring the user to make a choice.

### 4. Building tools before the spec is stable
Phase 0 must complete before Phase 1 begins. Skipping layers produces fragile ecosystems (see ROADMAP philosophy).

### 5. Treating AI agent output as attestable
Agents assist, they do not attest. Anything produced by an AI must be reviewed and signed off by a human before it's considered valid (L4 enforcement).

---

## Testing Philosophy

### For the validator:
- **Test the spec, not the implementation** — if the spec says a field is required, test that the validator catches it
- **Test error messages** — they should be actionable, not cryptic
- **Test edge cases explicitly** — empty strings, very long strings, Unicode, nested structures
- **Test compliance levels** — Basic, Standard, Full should validate correctly

### For the CLI:
- **Test the happy path** — does `orp new` produce a valid document?
- **Test the error path** — does `orp validate` give useful errors?
- **Test idempotency** — running `orp check` twice should produce the same result

### For the REST API (CRITICAL - api.publicreasonproject.org):
- **ALL tests must pass before ANY deployment** — The API is public-facing at https://api.publicreasonproject.org
- **Minimum 80% code coverage required** — Enforced by CI/CD pipeline
- **Run tests before committing:** `cd api && pytest tests/ -v --cov=. --cov-report=term-missing`
- **39 automated tests covering:**
  - All three endpoints (/api/v1/validate, /api/v1/check, /api/v1/diff)
  - Security features (CORS, headers, rate limiting, injection attempts)
  - Error handling (invalid YAML, missing fields, wrong types, size limits)
  - Edge cases (large documents, nested changes, fork detection, metadata filtering)
- **Test files location:** `api/tests/` (see `api/tests/README.md` for details)
- **CI/CD integration:** Tests run automatically on all merge requests and main branch commits
- **Coverage reports:** Generated in `api/htmlcov/` and uploaded to GitLab artifacts

**Before adding new API features:**
1. Write tests first (TDD approach)
2. Add to appropriate file in `api/tests/` (follow existing patterns)
3. Run full test suite locally
4. Ensure coverage stays above 80%
5. All tests must pass before merge

**Before deploying to production:**
1. Verify all tests pass in CI/CD
2. Check coverage report (must be ≥80%)
3. Manually test critical paths if major changes
4. Review test failures carefully - they catch real issues

---

## Communication Style

OpenReason is serious about transparency but not pompous about it. The tone should be:

- **Direct** — say what you mean
- **Honest** — admit uncertainty rather than hiding it
- **Accessible** — avoid jargon where plain language works
- **Respectful** — challenge ideas, not people

Examples:
- ✅ "This assumption may be wrong — here's how to test it"
- ❌ "Trust us, we know best"

- ✅ "We don't have data for this yet — it's flagged as a gap"
- ❌ "This is the complete analysis" (when it isn't)

---

## Questions Claude Should Ask

If you're uncertain about:

1. **Does this belong in the core spec or in an extension?**
   - Core = applies to all domains (policy, AI, governance)
   - Extension = domain-specific (ORP-AI, ORP-Econ)

2. **Is this a breaking change?**
   - If existing ORP documents would fail validation after this change, it's breaking
   - Breaking changes must wait for a major version

3. **Should this be configurable or fixed?**
   - Prefer fixed when it enforces transparency (required fields)
   - Prefer configurable when it reflects legitimate choice (compliance level)

4. **Is this documented well enough for someone else to maintain?**
   - If the founder disappeared tomorrow, could someone else understand this?

---

## Contribution Workflow (when implemented)

1. **Read** `docs/CONTRIBUTING.md`
2. **Discuss** in an issue before writing code
3. **Fork** the repository (once we're on GitHub)
4. **Write tests** before writing code
5. **Document** your reasoning in commit messages
6. **Submit PR** with clear description of what changed and why
7. **Respond** to review feedback transparently

---

## Success Metrics (Aspirational)

We'll know OpenReason is working if:

- **Adoption** — governments and AI developers publish ORP documents voluntarily
- **Forks** — people fork documents to propose better assumptions
- **Critiques** — documents are challenged on substance, not on politics
- **Education** — students learn to reason about policy using ORP
- **Independence** — the protocol evolves without requiring founder involvement

We'll know it's failing if:
- Documents are technically compliant but substantively empty
- No one forks because the tooling is too hard
- The protocol becomes a bureaucratic checkbox
- Community doesn't form or can't govern itself

---

## Current Production Services

**🚀 Live and operational:**

### REST API
- **URL:** https://api.publicreasonproject.org
- **Endpoints:**
  - `POST /api/v1/validate` - Full schema validation
  - `POST /api/v1/check` - Quick compliance check
  - `POST /api/v1/diff` - Document comparison
- **Documentation:** https://api.publicreasonproject.org/docs (Swagger UI)
- **Status:** Production-ready with 39 automated tests (96% coverage)
- **Deployment:** DigitalOcean (134.209.250.174), Docker, nginx, SSL via Let's Encrypt
- **CI/CD:** Automated testing on all commits via GitLab CI

### Python Package
- **PyPI:** https://pypi.org/project/orp-validator/
- **Install:** `pip install orp-validator`
- **Version:** 0.3.0
- **Commands:** `orp new`, `orp validate`, `orp check`, `orp diff`

---

## Contact and Governance

- **Founder:** Asbjørn (current steward during Phase 1)
- **Governance:** See `docs/governance/GOVERNANCE.md`
- **Repository:** https://gitlab.com/publicreason/orp
- **License:** Creative Commons CC-BY (documentation), MIT (code)

---

*This document should evolve as the project grows. If you find yourself repeatedly explaining the same thing to Claude, add it here.*

*Last updated: 2026-02-26 (Phase 1 - Sprint 1.6 complete)*
