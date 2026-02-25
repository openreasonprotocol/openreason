# Sprint 1-1: JSON Schema and Basic Validation

**Version:** `sprint-1.1.0`
**Status:** Completed
**Start Date:** 2026-02-25
**Target End Date:** 2026-02-25
**Actual End Date:** 2026-02-25

**Code Target Version:** `v0.1.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Create a formal JSON Schema definition for ORP v0.1 documents and a basic Python validator that proves the specification is implementable and can catch common errors.

---

## Scope

### In Scope
- JSON Schema definition for all ORP v0.1 fields (Header + L1-L5)
- Compliance level variants (Basic, Standard, Full)
- Python validator library that validates against the schema
- Command-line validation tool (`python -m orp_validator validate <file>`)
- Test suite covering all required fields and compliance levels
- Documentation for validator usage

### Explicitly Out of Scope
- CLI with multiple commands (`orp new`, `orp diff`, etc.) — deferred to Sprint 2
- JavaScript/TypeScript validator — deferred to Sprint 3
- REST API endpoint — deferred to Phase 1 Sprint 4
- Advanced validation (semantic validation, cross-field validation) — v0.2+
- VS Code extension or IDE integration — Phase 2
- Agent-assisted document creation — Phase 3

---

## Tasks

### Task 1: Define JSON Schema for ORP v0.1
**Owner:** TBD
**Estimate:** 2-3 days
**Status:** Not Started

**Description:**
Create a formal JSON Schema (draft-07 or later) that defines:
- Header block with all required and optional fields
- L1 (Data Provenance) with dataset array structure
- L2 (Consequence Simulation) with variables, scenarios, model fields
- L3 (Empathy Mapping) with stakeholder mapping and minority stress test
- L4 (Accountability Ledger) with entries and review history
- L5 (Fork Registry) with fork and response tracking

**Acceptance Criteria:**
- [ ] Schema validates the Danish Property Tax Reform example as ORP-Full compliant
- [ ] Schema correctly rejects documents missing required fields
- [ ] Schema includes descriptions for all fields (serves as inline documentation)
- [ ] Schema defines compliance level variants (Basic = Header + L1, Standard = +L2+L3, Full = all layers)
- [ ] Schema is published as `schemas/orp-v0.1.schema.json`

**Dependencies:**
- ORP_SPEC.md is stable (it is)

---

### Task 2: Build Python Validator Library
**Owner:** TBD
**Estimate:** 3-4 days
**Status:** Not Started

**Description:**
Create a Python package `orp_validator` that:
- Loads and parses ORP documents (YAML or JSON)
- Validates against the JSON Schema
- Determines compliance level achieved (Basic/Standard/Full)
- Produces structured validation results with clear error messages
- Can be imported as a library (`from orp_validator import validate`)

**Acceptance Criteria:**
- [ ] Validator accepts both YAML and JSON inputs
- [ ] Validator returns structured results: `{valid: bool, compliance_level: str, errors: [...]}`
- [ ] Error messages include field path, what's wrong, and what's expected
- [ ] Validator handles edge cases (empty files, malformed YAML, missing top-level keys)
- [ ] Code includes type hints and passes `mypy` strict mode
- [ ] Documentation includes API reference

**Dependencies:**
- Task 1 (JSON Schema) must be complete

---

### Task 3: Create CLI Validation Tool
**Owner:** TBD
**Estimate:** 1-2 days
**Status:** Not Started

**Description:**
Make the validator runnable from command line:
```bash
python -m orp_validator validate examples/danish_property_tax_reform.md
```

Output should show:
- Validity (✓ Valid / ✗ Invalid)
- Compliance level achieved
- List of errors if invalid
- Summary of what's present (which layers are complete)

**Acceptance Criteria:**
- [ ] CLI accepts file path as argument
- [ ] CLI outputs human-readable validation results
- [ ] CLI exits with code 0 for valid, 1 for invalid
- [ ] CLI supports `--json` flag for machine-readable output
- [ ] CLI supports `--verbose` flag for detailed validation trace

**Dependencies:**
- Task 2 (Python validator library) must be complete

---

### Task 4: Write Test Suite
**Owner:** TBD
**Estimate:** 2-3 days
**Status:** Not Started

**Description:**
Create comprehensive test suite using pytest:
- Unit tests for schema validation
- Integration tests for full document validation
- Test fixtures for valid and invalid documents
- Edge case testing (empty fields, very long strings, Unicode, nested structures)
- Compliance level testing (does Basic correctly reject missing L2?)

**Acceptance Criteria:**
- [ ] Test coverage >90% for validator logic
- [ ] Tests include valid ORP-Basic, ORP-Standard, ORP-Full examples
- [ ] Tests include common error cases (missing required fields, wrong types)
- [ ] Tests validate error message quality (are they actionable?)
- [ ] Tests run via `pytest` with clear output
- [ ] CI/CD ready (can run in GitLab CI when we add it)

**Dependencies:**
- Task 2 (Python validator library) must be complete

---

### Task 5: Documentation
**Owner:** TBD
**Estimate:** 1 day
**Status:** Not Started

**Description:**
Write documentation for:
- JSON Schema usage (how to validate against it directly)
- Python validator library API
- CLI usage and examples
- Common validation errors and how to fix them
- Contributing guide for validator improvements

**Acceptance Criteria:**
- [ ] README in `validator/` directory explains installation and usage
- [ ] API documentation generated (Sphinx or similar)
- [ ] Examples show both library and CLI usage
- [ ] Error message reference documents common issues
- [ ] Documentation published in `docs/validator/`

**Dependencies:**
- Tasks 1-3 must be complete

---

## Success Criteria

This sprint is complete when:
1. JSON Schema exists and validates the Danish Property Tax Reform example
2. Python validator library can validate ORP documents and determine compliance level
3. CLI tool can be run from command line and produces clear output
4. Test suite exists with >90% coverage and all tests pass
5. Documentation exists and explains how to use the validator
6. Another person could validate their ORP document using only the published tools and docs

---

## Dependencies

**Requires from previous work:**
- ORP_SPEC.md v0.1 must be stable (it is)
- Danish Property Tax Reform example must be complete (it is)

**Blocks future work:**
- Sprint 2 (CLI scaffolding commands) requires the validator
- ORP Registry (Phase 2) requires validation infrastructure
- AI agents (Phase 3) require validation to ensure output quality

---

## Risks and Unknowns

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| JSON Schema may not express all validation rules cleanly | Medium | Medium | Start simple; accept that some validation may need custom code |
| Compliance level detection may be ambiguous for partial documents | Medium | Low | Define clear rules: all required fields present = that level |
| Error messages may be hard to make truly helpful | High | Medium | Iterate on message quality; test with real users |
| YAML frontmatter in .md files may be tricky to parse | Low | Low | Use standard YAML parser; test with the actual example file |

---

## Decisions Made

### Decision 1: Use JSON Schema over custom validation DSL
**When:** TBD (planning phase)
**Who:** TBD
**Reasoning:** JSON Schema is a standard, widely supported, and has good tooling across languages. Creating a custom DSL would be reinventing the wheel and create a maintenance burden.
**Alternatives Considered:** Custom Python validation logic — would be more flexible but less portable and harder for the community to contribute to.

### Decision 2: Start with Python validator before JavaScript
**When:** TBD (planning phase)
**Who:** TBD
**Reasoning:** Python is the language of policy analysis and data science. Getting the validator working in Python first proves the spec is implementable and serves the likely early adopter community. JavaScript validator follows in Sprint 3.
**Alternatives Considered:** Building both simultaneously — would slow down initial delivery and split focus.

### Decision 3: CLI is a thin wrapper over library, not a standalone tool
**When:** TBD (planning phase)
**Who:** TBD
**Reasoning:** The validator should be usable as a library (imported into other Python code) and as a CLI. Making the library the primary artifact ensures it's reusable.
**Alternatives Considered:** CLI-first approach — would work but would make library integration harder later.

---

## Retrospective

*(Added after sprint completes)*

### What Worked Well
- TBD

### What Didn't Work
- TBD

### What We Learned
- TBD

### What Assumptions Were Wrong
- TBD

### Changes for Next Sprint
- TBD

---

## Notes

### Reference Implementations to Study
- **JSON Schema validation:** Look at how `ajv` (JavaScript) and `jsonschema` (Python) handle validation
- **Model card validation:** Study Google's model card schema for inspiration
- **OpenAPI validators:** See how they handle multi-version schema validation

### Questions to Answer During Sprint
1. Should the schema be strict (additionalProperties: false) or permissive?
2. How do we handle extensions (ORP-AI fields) that aren't in the core schema?
3. Should we validate that `forked_from` document_id actually exists somewhere?
4. How do we validate that L4 entries reference decisions actually made in other layers?

### Tools We'll Need
- `jsonschema` (Python library)
- `pyyaml` (YAML parsing)
- `pytest` (testing)
- `mypy` (type checking)
- `black` (code formatting)
