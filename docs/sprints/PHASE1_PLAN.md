# Phase 1 Sprint Plan - Complete Sequencing

**Phase 1 Goal:** Core Tooling - The minimum viable toolkit that makes ORP documents easy to produce, validate, and compare.

**Status:** Sprints 1.1-1.2 Complete | Sprints 1.3-1.6 Planned

---

## Completed Sprints

### ✅ Sprint 1.1.0 - JSON Schema + Python Validator
**Code Version:** v0.1.0
**Completed:** 2026-02-25

**Delivered:**
- JSON Schema for ORP v0.1 (all 5 layers)
- Python validator library (`orp_validator`)
- CLI tool (`orp-validate`)
- 20 tests, 82% coverage

### ✅ Sprint 1.2.0 - CLI Scaffolding Commands
**Code Version:** v0.2.0
**Completed:** 2026-02-25

**Delivered:**
- Refactored CLI (`orp` command group)
- `orp new` - Interactive document creation
- `orp check` - Quick compliance checking
- `orp diff` - Document comparison
- Document templates (basic/standard/full)
- 69 tests, 95% coverage

---

## Planned Sprints - Dependency Order

### Sprint 1.3.0 - Danish Property Tax Reference Implementation
**Code Version:** v0.2.1
**Dependencies:** Requires 1.1, 1.2 (schema + CLI)
**Blocks:** None (parallel-safe)
**Estimated Effort:** 2-3 days

**Goal:** Create first ORP-Full compliant real-world example as pure YAML

**Why This Order:**
- Validates that the protocol actually works for complex real-world documents
- Identifies gaps in schema/tooling before we build more infrastructure
- Provides reference implementation for documentation
- Can be done in parallel with other work - doesn't block anything

**Deliverables:**
- `examples/danish_property_tax_reform.yaml` - Pure YAML (not markdown)
- Validates as ORP-Full with `orp validate`
- Well-commented as reference for other users
- Update example to demonstrate all 5 layers properly

---

### Sprint 1.4.0 - PyPI Publication + Packaging
**Code Version:** v0.3.0
**Dependencies:** Requires 1.1, 1.2 (working validator)
**Blocks:** 1.6 (website needs install instructions)
**Estimated Effort:** 1-2 days

**Goal:** Make `orp-validator` installable via `pip install orp-validator`

**Why This Order:**
- Enables external users to actually use the tool
- Required before we can build REST API (needs to pip install as dependency)
- Needed before publicreasonproject.org goes live (install instructions)
- Low risk, high value

**Deliverables:**
- Publish to PyPI
- CI/CD pipeline for automated releases
- Installation documentation
- Version badge in README

---

### Sprint 1.5.0 - REST API Validator
**Code Version:** v0.4.0
**Dependencies:** Requires 1.4 (PyPI package)
**Blocks:** 1.6 (website validator widget)
**Estimated Effort:** 3-4 days

**Goal:** Web service that validates ORP documents via HTTP

**Why This Order:**
- Requires stable PyPI package to install as dependency
- Enables browser-based validation (needed for website)
- Foundation for future integrations (GitLab CI, VS Code)
- Must come before website so we can embed validator

**Deliverables:**
- FastAPI service with endpoints:
  - `POST /validate` - Validate document
  - `POST /check` - Quick compliance check
  - `POST /diff` - Compare two documents
- Docker container
- API documentation (OpenAPI/Swagger)
- Deployed to api.publicreasonproject.org
- CORS configured for web embedding

---

### Sprint 1.6.0 - Documentation Website
**Code Version:** v0.5.0
**Dependencies:** Requires 1.4 (PyPI), 1.5 (REST API)
**Blocks:** Public launch
**Estimated Effort:** 4-5 days

**Goal:** publicreasonproject.org with docs, examples, and online validator

**Why This Order:**
- Needs PyPI package (for install instructions)
- Needs REST API (for embedded validator)
- Should have reference example (Danish tax)
- This is the public face - should come when tooling is solid

**Deliverables:**
- Static site (MkDocs Material or similar)
- Content:
  - Landing page (README content)
  - Protocol specification
  - Philosophy (REE_PHILOSOPHY)
  - Examples (Danish tax)
  - API reference
  - Contributing guide
- **Interactive validator widget** (paste YAML, validate via REST API)
- GitLab Pages deployment to publicreasonproject.org
- Search functionality
- Mobile responsive

---

### Sprint 1.7.0 (Optional) - JavaScript/TypeScript Validator
**Code Version:** v0.6.0
**Dependencies:** Requires 1.1 (schema)
**Blocks:** Nothing (nice-to-have)
**Estimated Effort:** 5-7 days

**Goal:** `npm install orp-validator` for browser/Node.js validation

**Why This Order (DEFERRED):**
- **NOT NEEDED for Phase 1 completion**
- REST API already enables browser validation
- Significant effort to port + maintain two implementations
- Better to wait until users actually request it
- Could be community contribution later

**Recommendation:** SKIP for now, defer to Phase 2

**If we do build it:**
- Port Python validator to TypeScript
- Published to npm
- Browser bundle (for CDN usage)
- 100% feature parity with Python version
- Comprehensive test suite

---

## Phase 1 Completion Criteria

Phase 1 is **COMPLETE** when:

1. ✅ Users can scaffold new ORP documents (`orp new`)
2. ✅ Users can validate documents locally (`orp validate`)
3. ✅ Users can install via PyPI (`pip install orp-validator`)
4. ✅ Users can validate documents via web (REST API)
5. ✅ publicreasonproject.org is live with docs + online validator
6. ✅ At least one ORP-Full compliant reference implementation exists
7. ✅ Test coverage >90% for all core functionality

**After Phase 1:** Protocol is usable by external parties without our assistance

---

## Sequencing Rationale

### Why NOT start with website?
- Website needs working install instructions (requires PyPI)
- Website should have online validator (requires REST API)
- Website should showcase real examples (requires Danish example)
- Building website first = documenting things that don't exist yet

### Why Danish example early?
- **Validates the protocol works** for real complexity
- Often reveals schema gaps that are hard to see in abstract
- Provides reference for docs/website
- Can be done quickly and independently

### Why PyPI before REST API?
- REST API will `pip install orp-validator` as dependency
- Enables users to self-host if they want
- Low-hanging fruit - should just work

### Why REST API before website?
- Website wants to embed interactive validation
- API needs to be stable before public site links to it
- Gives us time to test API before high traffic

### Why defer JavaScript validator?
- REST API already enables browser validation
- Maintaining two implementations = 2x work
- Nobody has requested it yet
- Can be community contribution if there's demand

---

## Sprint Naming Convention

Following `docs/sprints/VERSIONING.md`:
- Sprint format: `sprint-PHASE.SPRINT.ITERATION`
- Sprint 1.3.0 = Phase 1, Sprint 3, Iteration 0
- Code target: `vMAJOR.MINOR.PATCH` (semver)

**Sprint to Code Version Mapping:**
- sprint-1.1.0 → v0.1.0
- sprint-1.2.0 → v0.2.0
- sprint-1.3.0 → v0.2.1 (patch - example only)
- sprint-1.4.0 → v0.3.0 (minor - new distribution)
- sprint-1.5.0 → v0.4.0 (minor - new API)
- sprint-1.6.0 → v0.5.0 (minor - website)

---

## Next Steps

1. Create detailed sprint plan for 1.3.0 (Danish example)
2. Execute 1.3.0
3. Create detailed sprint plan for 1.4.0 (PyPI)
4. Execute 1.4.0
5. Create detailed sprint plan for 1.5.0 (REST API)
6. Execute 1.5.0
7. Create detailed sprint plan for 1.6.0 (Website)
8. Execute 1.6.0
9. **Declare Phase 1 complete**
10. Begin Phase 2 planning (GitLab integration, VS Code extension)

---

## Open Questions

1. **Hosting for REST API:** Where to deploy? (Heroku, Railway, fly.io, GitLab Registry?)
2. **Domain setup:** api.publicreasonproject.org vs publicreasonproject.org/api/
3. **Analytics:** Do we want usage tracking on the website/API?
4. **Monitoring:** How do we monitor API uptime/errors?

---

*This is a living document. Fork it if you disagree with the sequencing.*
