# Changelog

All notable changes to the OpenReason Protocol (ORP) project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned (Phase 2)
- GitLab CI/CD integration examples
- VS Code extension
- ORP Registry (public searchable document index)

See `docs/sprints/PHASE1_PLAN.md` for complete Phase 1 details.

---

## [0.6.0] - 2026-04-08

### Added

**ORP v0.2 Protocol Support** - orp-validator v0.4.0 released to PyPI

**Core Features**:
- **Post-hoc reconstruction support**: `post_hoc` flag and `analyst`/`reconstructor` author roles
- **Domain-specific extensions**: orp-ai-training-v1, orp-safety-v1, orp-license-v1
- **Flexible schema validation**: `additionalProperties: true` throughout for natural document evolution
- **Granular confidence levels**: 7-point scale (very-high to very-low) for uncertainty quantification
- **Accountability gap documentation**: Explicit WHO/WHY/WHAT unknowns in Layer 4
- **Auto-detection**: Validator automatically detects document version (v0.1 vs v0.2)

**Enhanced Fields**:
- New author roles: `analyst`, `reconstructor` for post-hoc analysis
- `critical_undocumented_exclusions` (L1): Document post-hoc discovered gaps
- `comparison_to_actual` (L2): Counterfactual analysis capabilities
- `highest_severity_harm` (L3): Harm tier classification (Tier 0-3)
- Rich object formats: benefits/harms can be simple strings or detailed objects with severity/affected_groups

**New Compliance Level**:
- **ORP-PostHoc**: For retrospective analysis when decision-making history unavailable
- Recognized alongside ORP-Basic, ORP-Standard, ORP-Full

**Examples** - 4 comprehensive AI training dataset analyses (8,328 lines total):
- **ImageNet Training Data** (1,513 lines): ILSVRC-2012 post-hoc reconstruction
- **LAION-5B Training Data** (2,162 lines): 5.85B image-text pairs analysis
- **Common Crawl Training Data** (2,232 lines): 250B+ page web corpus analysis
- **GitHub Copilot Training Data** (2,421 lines): Code training data with license compliance

**Documentation**:
- ORP v0.2 Specification (`docs/specs/ORP_V0.2_SPEC.md`) - 16 comprehensive sections
- Migration Guide (`docs/specs/MIGRATION_V0.1_TO_V0.2.md`) - Automated migration script included
- Updated README with v0.2 release notes and 5 examples
- Design rationale document (`docs/specs/ORP_V0.2_DESIGN.md`)

### Changed

**Validator**:
- Schema location: Added `orp_validator/schemas/orp-v0.2.schema.json` (714 lines + 311 lines extensions)
- Validator loads schema based on `orp_version` field in document
- CLI `--orp-version` parameter for explicit version selection (optional)
- Package version: 0.3.0 → 0.4.0

**Extension System**:
- Three domain-specific extensions defined:
  - `orp-ai-training-v1`: AI training dataset fields (training_run, model_details, etc.)
  - `orp-safety-v1`: Safety validation fields (red_teaming, deployment_gates)
  - `orp-license-v1`: License compliance tracking (license_analysis, compliance_status)

### Fixed

**Empirical Validation Results**:
- **311 validation errors** discovered when validating real-world AI dataset examples against v0.1 schema
- **0 errors** with v0.2 flexible schema → **100% validation success rate**
- All 5 examples (Danish Property Tax + 4 AI datasets) validate successfully
- Backward compatibility: All v0.1 documents still validate correctly

### Backward Compatibility

✅ **Fully backward compatible**: All ORP v0.1 documents validate successfully with orp-validator v0.4.0

**No Breaking Changes**:
- v0.1 core required fields unchanged
- v0.1 structure fully supported
- Minimal migration path: Update `orp_version: "0.2"` and `last_modified` date
- Enhanced migration paths available for leveraging new v0.2 features

**Migration Time**:
- Minimal (version bump only): 2 minutes per document
- Enhanced (add extensions): 15-30 minutes per document
- Full (post-hoc conversion): 2-8 hours for complex datasets

### Technical Details

**Schema Statistics**:
- JSON Schema v0.2: 714 lines (core) + 311 lines (extensions) = 1,025 lines total
- 9 flexibility patterns applied throughout
- Extension registry tracking (informational, non-blocking)
- oneOf patterns for gradual enrichment (string → object evolution)

**Validation Coverage**:
- 5 examples validated: 8,328 lines of ORP documentation
- Compliance levels tested: ORP-Basic, ORP-Standard, ORP-Full, ORP-PostHoc
- Cross-domain validation: policy, AI training, AI safety, license compliance

**Installation**:
```bash
pip install orp-validator==0.4.0
# or
pip install --upgrade orp-validator
```

**Verify Version**:
```bash
orp --version
# Expected: orp-validator 0.4.0 (ORP v0.2 support)
```

**Sprint**: sprint-1.7.3 (Phases 0-7 complete)
**Protocol Version**: ORP v0.2.0
**Package Version**: orp-validator v0.4.0
**PyPI**: https://pypi.org/project/orp-validator/0.4.0/

---

## [0.5.0] - 2026-02-27

### Added
- **Documentation Website** - Live at https://docs.publicreasonproject.org
  - Complete documentation for ORP v0.1 specification
  - Interactive validator widget (uses REST API)
  - Getting Started guides (installation, quickstart, first document)
  - Protocol documentation (specification, philosophy, compliance levels)
  - Tool references (CLI, Python API, REST API)
  - Examples showcase (Danish Property Tax Reform)
  - Community section (contributing, governance, roadmap)

- **Interactive Validator Widget**
  - Browser-based YAML validator
  - Calls REST API at api.publicreasonproject.org
  - Shows compliance level, layers present, errors, warnings
  - Load example button, clear functionality
  - Mobile-responsive design

- **SEO & Social Media Optimization**
  - Open Graph meta tags for social sharing
  - Twitter Card support
  - Custom social media image (1200x630)
  - Keywords, canonical URLs, robots.txt
  - Sitemap auto-generated by Next.js

- **Branding**
  - Custom fork icon (represents ORP's branching/forking philosophy)
  - Favicon (SVG + PNG versions)
  - Apple touch icon
  - Two-tier logo: Public Reason Project / OpenReason Protocol

### Technical Details
- Built with Next.js 14 + Nextra (docs framework)
- Static site generation for fast loading
- Light theme only (as requested)
- Search functionality built-in
- Deployed to DigitalOcean at docs.publicreasonproject.org
- SSL via nginx + Let's Encrypt

### Phase 1 Status
**COMPLETE** - All core tooling deliverables achieved:
- ✅ JSON Schema + Python Validator (v0.1.0)
- ✅ CLI Commands (v0.2.0)
- ✅ Reference Implementation (v0.2.1)
- ✅ PyPI Publication (v0.3.0)
- ✅ REST API (v0.4.0)
- ✅ Documentation Website (v0.5.0)

OpenReason Protocol is now ready for external use and community contributions.

---

## [0.4.0] - 2026-02-26

### Added
- **REST API Validator Service** - Live at https://api.publicreasonproject.org
  - `POST /api/v1/validate` - Full schema validation
  - `POST /api/v1/check` - Quick compliance check
  - `POST /api/v1/diff` - Document comparison and fork detection
  - OpenAPI/Swagger documentation at /docs
  - CORS enabled for browser access

- **Comprehensive Test Suite** - 39 automated tests, 96% coverage
  - test_validate_endpoint.py - 12 tests
  - test_check_endpoint.py - 7 tests
  - test_diff_endpoint.py - 11 tests
  - test_security.py - 12 tests (CORS, headers, rate limiting)
  - All tests run in CI/CD pipeline

- **Production Infrastructure**
  - Docker containerization
  - Deployed to DigitalOcean (134.209.250.174)
  - nginx reverse proxy
  - SSL via Let's Encrypt
  - Rate limiting (60 requests/minute per IP)
  - Security headers (X-Content-Type-Options, X-Frame-Options, CSP)

### Technical Details
- Built with FastAPI
- Uses orp-validator PyPI package
- Health check endpoint at /health
- Root endpoint (/) shows API info and available endpoints

---

## [0.3.0] - 2026-02-26

### Added
- **PyPI Publication** - Package now available on PyPI
  - Install with: `pip install orp-validator`
  - Published to https://pypi.org/project/orp-validator/
  - Tested on TestPyPI before production release

### Changed
- **Package Structure** - Moved resources inside package for proper distribution
  - `schemas/` → `orp_validator/schemas/`
  - `templates/` → `orp_validator/templates/`
  - Uses `importlib.resources` for portable resource loading
  - Ensures schemas and templates are included in wheel distribution

- **Package Metadata** - Added contact information
  - Authors: OpenReason Contributors <hello@publicreasonproject.org>
  - Maintainer: Asbjørn Ras <asbjorn@publicreasonproject.org>
  - Homepage: https://publicreasonproject.org

### Fixed
- Schema and template files now properly included in pip installations
- Package version correctly reports 0.3.0

### Infrastructure
- MANIFEST.in created for package data inclusion
- PyPI accounts configured (production and test)
- API tokens set up for automated uploads

**Sprint**: sprint-1.4.0
**Install**: `pip install orp-validator`
**PyPI**: https://pypi.org/project/orp-validator/0.3.0/

---

## [0.2.1] - 2026-02-25

### Added
- **Danish Property Tax Reform** - First ORP-Full reference implementation
  - Complete YAML document with all 5 layers
  - Real-world policy proposal demonstrating protocol in practice
  - Validates as ORP-Full with zero errors
  - Available at `examples/danish_property_tax_reform.yaml`
  - Documentation in `examples/README.md`

**Sprint**: sprint-1.3.0
**Validation**: `orp validate examples/danish_property_tax_reform.yaml`

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
