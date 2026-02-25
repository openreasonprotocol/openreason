# Changelog

All notable changes to the OpenReason Protocol (ORP) project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned (Phase 1 Completion)
- **Sprint 1.3.0** (v0.2.1): Danish Property Tax reference implementation as pure YAML
- **Sprint 1.4.0** (v0.3.0): PyPI publication and automated releases
- **Sprint 1.5.0** (v0.4.0): REST API validator service at api.publicreasonproject.org
- **Sprint 1.6.0** (v0.5.0): Documentation website at publicreasonproject.org with interactive validator

See `docs/sprints/PHASE1_PLAN.md` for complete sequencing rationale and sprint details.

### Deferred to Phase 2
- JavaScript/TypeScript validator (REST API provides browser validation)
- GitLab CI/CD integration examples
- VS Code extension
- ORP Registry

---

## [0.2.0] - 2026-02-25

### Added
- **CLI Command Groups** - New `orp` command with subcommands
  - `orp new` - Interactive scaffolding for new ORP documents
  - `orp check` - Quick compliance level assessment without full validation
  - `orp diff` - Compare two ORP documents and highlight differences
  - `orp validate` - Full validation (replaces `orp-validate`)
  - Backward compatibility maintained with `orp-validate` command

- **Document Templates**
  - `templates/orp-basic.yaml` - ORP-Basic template with helpful comments
  - `templates/orp-standard.yaml` - ORP-Standard template
  - `templates/orp-full.yaml` - ORP-Full template with all 5 layers
  - Templates included in package distribution

- **`orp new` Command Features**
  - Interactive prompts for header fields
  - Non-interactive mode with flags (`--title`, `--domain`, `--author`, `--non-interactive`)
  - Compliance level selection (`--compliance basic|standard|full`)
  - Output format selection (`--format yaml|json`)
  - Auto-validation of generated documents
  - Document ID auto-generation from filename

- **`orp check` Command Features**
  - Fast layer detection without schema validation
  - Compliance level determination (Basic/Standard/Full/None)
  - Guidance on achieving higher compliance
  - Quiet mode (`--quiet`) for automation
  - JSON output mode (`--json`)
  - Exit codes: 0=Full, 1=Standard, 2=Basic, 3=None, 4=Error

- **`orp diff` Command Features**
  - Side-by-side comparison of two documents
  - Fork relationship detection
  - Colored diff output (added/removed/changed)
  - Metadata filtering (exclude `last_modified` by default)
  - Layer-specific diffs (`--layer l2`)
  - JSON output for automation

- **Test Suite**
  - 49 tests total (up from 20)
  - New command tests: 11 tests for `orp new`, 9 tests for `orp check`, 12 tests for `orp diff`
  - Maintained 81% code coverage
  - Integration tests for CLI workflows

- **Infrastructure**
  - GitLab CI/CD pipeline configuration (`.gitlab-ci.yml`)
  - Automated testing across Python 3.9-3.12
  - Code quality checks (black, ruff, mypy)
  - Coverage reporting

### Changed
- CLI architecture refactored to use Click command groups
- Main entry point changed from `orp-validate` to `orp` with subcommands
- Updated README with new CLI commands and examples
- Package now includes templates directory

### Sprint
- Completed: sprint-1.2.0 (CLI Scaffolding Commands)
- Code version: v0.2.0
- Protocol version: ORP v0.1

---

## [0.1.0] - 2026-02-25

### Added
- **JSON Schema for ORP v0.1** - Complete schema definition for all 5 layers (Header + L1-L5)
  - Conditional validation based on declared compliance level (Basic/Standard/Full)
  - Detailed field descriptions serving as inline documentation
  - Support for all domain types: policy, ai-training, governance, other

- **Python Validator Library** (`orp_validator`)
  - Core validation logic with type hints throughout
  - Compliance level detection (ORP-Basic, ORP-Standard, ORP-Full)
  - Structured error reporting with actionable messages
  - Support for YAML, JSON, and Markdown with YAML frontmatter
  - Warnings for documents that could achieve higher compliance

- **CLI Tool** (`orp-validate`)
  - Human-readable colored output with compliance level indication
  - JSON output mode (`--json`) for automation and CI/CD integration
  - Verbose mode (`--verbose`) for detailed validation traces
  - Proper exit codes (0 for valid, 1 for invalid, 2 for errors)

- **Test Suite**
  - 20 tests with 82% code coverage
  - Core validator logic tests (14 tests)
  - CLI integration tests (6 tests)
  - Edge case coverage (empty documents, missing fields, invalid values)
  - pytest-based with fixtures and parametrization

- **Documentation**
  - Complete README with Quick Start guide
  - Installation and usage examples
  - Development setup instructions
  - CLAUDE.md for AI assistant context
  - Sprint planning infrastructure with versioning system

- **Project Infrastructure**
  - Git repository initialized with proper `.gitignore`
  - MIT License
  - pyproject.toml with full dependency management
  - GitLab CI/CD pipeline for automated testing
  - Sprint versioning system (sprint-PHASE.SPRINT.ITERATION)

### Documentation
- OpenReason Protocol v0.1 specification (ORP_SPEC.md)
- Rational, Empathy-Informed Ethics philosophy (REE_PHILOSOPHY.md)
- Governance model v0.1 (GOVERNANCE.md)
- Protocol self-documentation (ORP_META.md)
- Contribution guidelines (CONTRIBUTING.md)
- Development roadmap through Phase 5 (ROADMAP.md)
- Danish Property Tax Reform example (ORP-Full compliant)

### Technical Details
- Python 3.9+ support with type safety (mypy strict mode)
- Minimal dependencies: jsonschema, pyyaml, click
- Black formatting, Ruff linting
- Modular design - validator library separate from CLI
- JSON Schema Draft 7 specification

### Sprint
- Completed: sprint-1.1.0 (JSON Schema + Python Validator)
- Code version: v0.1.0
- Protocol version: ORP v0.1

---

## [0.0.0] - 2026-02-25

### Added
- Initial repository structure
- Phase 0 foundation documentation complete
- Project ready for Phase 1 tooling development

---

## Version Mapping

| Code Version | Sprint | Protocol Version | Release Date |
|--------------|--------|------------------|--------------|
| v0.1.0 | sprint-1.1.0 | ORP v0.1 | 2026-02-25 |
| (unreleased) | sprint-1.2.0 | ORP v0.1 | TBD |
| (unreleased) | sprint-1.3.0 | ORP v0.1 | TBD |

---

## Protocol Versions

### ORP v0.1 (Current)
- **Status**: Draft - open for public comment
- **Release**: 2026-02-25
- **Compliance Levels**: ORP-Basic, ORP-Standard, ORP-Full
- **Layers**: Header + L1 (Data Provenance) + L2 (Consequence Simulation) + L3 (Empathy Mapping) + L4 (Accountability Ledger) + L5 (Fork Registry)
- **Breaking Changes from v0.0**: N/A (initial release)

### Future: ORP v1.0 (Planned)
- **Status**: Not yet defined
- **Target**: After 60-day public comment period on v0.1
- **Changes**: TBD based on community feedback

---

## Governance

All changes to the protocol specification (ORP_SPEC.md) follow the governance process defined in docs/governance/GOVERNANCE.md:
- Proposal period: minimum 30 days for spec changes, 60 days for governance changes
- Working Group review required
- Stewardship Council ratification (two-thirds majority) for major versions

Code changes follow conventional commits and semantic versioning:
- **MAJOR** (x.0.0): Breaking changes to public API or CLI
- **MINOR** (0.x.0): New features, backward-compatible additions
- **PATCH** (0.0.x): Bug fixes, documentation updates

---

## Links

- **Repository**: https://gitlab.com/publicreason/orp
- **Issues**: https://gitlab.com/publicreason/orp/-/issues
- **Documentation**: docs/
- **Roadmap**: docs/ROADMAP.md
- **Contributing**: docs/CONTRIBUTING.md

---

[Unreleased]: https://gitlab.com/publicreason/orp/-/compare/v0.1.0...main
[0.1.0]: https://gitlab.com/publicreason/orp/-/tags/v0.1.0
[0.0.0]: https://gitlab.com/publicreason/orp/-/commits/fefd565
