# Sprint 1-2: CLI Scaffolding Commands

**Version:** `sprint-1.2.0`
**Status:** Planned
**Start Date:** TBD
**Target End Date:** TBD
**Actual End Date:** N/A

**Code Target Version:** `v0.2.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Build CLI commands that make creating and working with ORP documents easy: `orp new` for scaffolding new documents, `orp check` for quick compliance assessment, and `orp diff` for comparing documents or forks.

---

## Scope

### In Scope
- `orp new` command - Interactive scaffolding for new ORP documents
- `orp check` command - Quick compliance level check without full validation
- `orp diff` command - Compare two ORP documents and highlight differences
- Templates for ORP-Basic, ORP-Standard, and ORP-Full documents
- Updated CLI with new subcommands
- Tests for new commands

### Explicitly Out of Scope
- AI-assisted document creation (Phase 3)
- Web-based document editor (Phase 2)
- Document merging or conflict resolution
- `orp fork` command (deferred to later sprint)
- `orp summarise` command (deferred to later sprint)

---

## Tasks

### Task 1: Implement `orp new` Command
**Owner:** TBD
**Estimate:** 2-3 days
**Status:** Not Started

**Description:**
Create an interactive command that scaffolds new ORP documents with proper structure.

Features:
- Interactive prompts for header fields (title, domain, authors, etc.)
- Choice of compliance level (Basic/Standard/Full)
- Template generation with placeholder content
- Support for both YAML and JSON output formats
- Validation of generated document before writing

**Acceptance Criteria:**
- [ ] Command: `orp new <filename>` creates new ORP document
- [ ] Interactive prompts for all required header fields
- [ ] `--compliance` flag to specify Basic/Standard/Full (default: Basic)
- [ ] `--format` flag for yaml/json output (default: yaml)
- [ ] `--non-interactive` mode with all values via flags
- [ ] Generated documents pass validation immediately
- [ ] Helpful placeholder text in templates guides users
- [ ] Support for `--from-template` to use custom templates

**Dependencies:**
- Validator from sprint-1.1.0

---

### Task 2: Implement `orp check` Command
**Owner:** TBD
**Estimate:** 1 day
**Status:** Not Started

**Description:**
Create a lightweight command that quickly checks which compliance level a document achieves without full validation.

Features:
- Fast compliance level detection
- Layer presence summary
- Minimal output (just compliance level and missing layers)
- Exit code indicates compliance level (0=Full, 1=Standard, 2=Basic, 3=None)

**Acceptance Criteria:**
- [ ] Command: `orp check <file>` outputs compliance level
- [ ] Output shows which layers are present vs missing
- [ ] `--quiet` flag outputs only compliance level string
- [ ] `--json` flag for machine-readable output
- [ ] Runs faster than full validation (no schema validation)
- [ ] Exit codes: 0=Full, 1=Standard, 2=Basic, 3=None, 4=Error

**Dependencies:**
- Validator from sprint-1.1.0

---

### Task 3: Implement `orp diff` Command
**Owner:** TBD
**Estimate:** 2-3 days
**Status:** Not Started

**Description:**
Create a command that compares two ORP documents and highlights differences, with special handling for forks.

Features:
- Side-by-side comparison of field values
- Highlight changed assumptions in L2, L3, L4
- Detect if one document is a fork of another
- Human-readable diff output
- Optional JSON output for automation

**Acceptance Criteria:**
- [ ] Command: `orp diff <file1> <file2>` shows differences
- [ ] Detects fork relationships via `forked_from` field
- [ ] Highlights key differences: assumptions, exclusions, scenarios
- [ ] Ignores metadata changes (last_modified, etc.) by default
- [ ] `--include-metadata` flag to show all differences
- [ ] `--json` flag for structured diff output
- [ ] `--layer` flag to diff specific layer only (e.g., `--layer l2`)
- [ ] Colored output with red (removed), green (added), yellow (changed)

**Dependencies:**
- Validator from sprint-1.1.0

---

### Task 4: Create Document Templates
**Owner:** TBD
**Estimate:** 1 day
**Status:** Not Started

**Description:**
Create well-documented YAML templates for each compliance level.

**Acceptance Criteria:**
- [ ] `templates/orp-basic.yaml` with helpful comments
- [ ] `templates/orp-standard.yaml` with helpful comments
- [ ] `templates/orp-full.yaml` with helpful comments
- [ ] Templates include example values that pass validation
- [ ] Comments explain what each field requires
- [ ] Templates referenced in `orp new` command

**Dependencies:**
- None

---

### Task 5: Update CLI Architecture
**Owner:** TBD
**Estimate:** 1 day
**Status:** Not Started

**Description:**
Refactor CLI to use Click's command groups for better organization.

Current:
```
orp-validate <file>
```

New:
```
orp validate <file>
orp new <file>
orp check <file>
orp diff <file1> <file2>
```

**Acceptance Criteria:**
- [ ] Main CLI entry point with subcommands
- [ ] `orp --version` shows version
- [ ] `orp --help` lists all commands
- [ ] Each subcommand has its own `--help`
- [ ] Backward compatibility: `orp-validate` still works (deprecated)
- [ ] Updated pyproject.toml with new entry points

**Dependencies:**
- Tasks 1-3 (all new commands)

---

### Task 6: Write Tests
**Owner:** TBD
**Estimate:** 2 days
**Status:** Not Started

**Description:**
Comprehensive test suite for all new commands.

**Acceptance Criteria:**
- [ ] Test `orp new` in interactive and non-interactive modes
- [ ] Test `orp new` with different compliance levels
- [ ] Test `orp check` on valid and invalid documents
- [ ] Test `orp diff` on identical, different, and forked documents
- [ ] Test CLI argument parsing and error handling
- [ ] Test template generation and validation
- [ ] Maintain >80% coverage
- [ ] Integration tests for full workflows

**Dependencies:**
- Tasks 1-5

---

## Success Criteria

This sprint is complete when:
1. `orp new` can create valid ORP documents interactively
2. `orp check` can quickly assess compliance level
3. `orp diff` can compare two documents meaningfully
4. All commands have tests with >80% coverage
5. Documentation explains how to use each command
6. A user can go from zero to a valid ORP-Basic document in <5 minutes

---

## Dependencies

**Requires from previous work:**
- sprint-1.1.0 validator must be complete (it is)
- JSON Schema for validation (exists)

**Blocks future work:**
- `orp fork` command (Sprint 1.4) depends on `orp diff`
- `orp summarise` command (Sprint 1.5) depends on document structure
- User adoption - these commands make ORP accessible to non-technical users

---

## Risks and Unknowns

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Interactive CLI may be hard to test | Medium | Low | Use Click's testing utilities; test both interactive and non-interactive modes |
| Diff algorithm may be complex for nested structures | Medium | Medium | Start with simple field-by-field comparison; iterate if needed |
| Template quality matters more than expected | High | High | Get user feedback early; iterate on placeholder text |
| Backward compatibility with `orp-validate` may confuse users | Low | Low | Deprecation warning + documentation |

---

## Decisions Made

### Decision 1: Use Click command groups instead of argparse subparsers
**When:** Planning phase
**Who:** TBD
**Reasoning:** Click provides better developer experience, built-in testing support, and cleaner subcommand organization. We're already using Click for the validator.
**Alternatives Considered:** Argparse subparsers - more stdlib but less ergonomic.

### Decision 2: `orp new` generates YAML by default, not JSON
**When:** Planning phase
**Who:** TBD
**Reasoning:** YAML is more human-readable and allows comments. JSON can be generated with `--format json` flag.
**Alternatives Considered:** Defaulting to JSON for strict parsing - rejected because YAML is more forgiving for manual editing.

### Decision 3: `orp check` doesn't run full schema validation
**When:** Planning phase
**Who:** TBD
**Reasoning:** Performance. Users want quick feedback on "which compliance level am I at?" without waiting for full validation. If they want validation, they use `orp validate`.
**Alternatives Considered:** Always run full validation - rejected as too slow for the use case.

### Decision 4: `orp diff` focuses on semantic changes, not textual diffs
**When:** Planning phase
**Who:** TBD
**Reasoning:** Users care about changed assumptions and stakeholder impacts, not whitespace or comment changes. Semantic diff is more valuable than `git diff`.
**Alternatives Considered:** Just use `git diff` - rejected because it doesn't understand ORP structure.

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

### User Experience Priority
The `orp new` command is the most important. If a user can't easily create their first document, they won't adopt the protocol. Template quality and helpful prompts matter more than technical sophistication.

### Inspiration Sources
- `cargo new` (Rust) - great interactive scaffolding
- `npm init` - good prompts and sensible defaults
- `git diff` - familiar diff UX

### Questions to Answer During Sprint
1. Should `orp new` create files with `.yaml`, `.yml`, or `.orp.yaml` extension?
2. Should templates be embedded in code or loaded from files?
3. How verbose should diff output be by default?
4. Should `orp check` output warnings like `orp validate` does?

### Tools We'll Need
- `click` (already dependency)
- `pytest` (already dependency)
- Possibly `rich` for prettier CLI output (deferred to later sprint)
- Possibly `prompt_toolkit` for advanced interactive prompts (deferred to later sprint)
