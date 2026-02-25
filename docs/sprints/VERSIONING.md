# Sprint and Code Versioning for OpenReason

This document defines how we version sprints, code releases, and the relationship between them.

---

## Philosophy

OpenReason follows semantic versioning for the **protocol specification** (v0.1, v1.0, etc.). Our code and sprint versioning should align with this while remaining independent — code can evolve faster than the spec.

---

## Sprint Versioning

Sprints use a **phase.sprint.iteration** format:

```
sprint-1.1.0
sprint-1.2.0
sprint-2.1.0
```

### Format: `sprint-PHASE.SPRINT.ITERATION`

- **PHASE** — Maps to development phase (0 = Phase 0, 1 = Phase 1, etc.)
- **SPRINT** — Sequential sprint number within that phase
- **ITERATION** — Incremented if a sprint is revised or extended (usually 0)

### Examples:

- `sprint-0.1.0` — First sprint in Phase 0 (if we had tracked it)
- `sprint-1.1.0` — First sprint in Phase 1 (JSON Schema + Python Validator)
- `sprint-1.2.0` — Second sprint in Phase 1 (CLI scaffolding)
- `sprint-1.2.1` — Revision/extension of sprint 1.2

### Sprint Status Lifecycle

Each sprint file includes a version and status:

```yaml
version: "sprint-1.1.0"
status: "planned" | "in_progress" | "completed" | "revised"
```

---

## Code Versioning

Code follows semantic versioning: `MAJOR.MINOR.PATCH`

```
v0.1.0  — First validator release (sprint-1.1.0 deliverable)
v0.2.0  — CLI scaffolding added (sprint-1.2.0 deliverable)
v1.0.0  — First stable release (all Phase 1 complete)
```

### Version Components

- **MAJOR** — Breaking changes to public API or CLI interface
- **MINOR** — New features, backward-compatible additions
- **PATCH** — Bug fixes, documentation updates

### Relationship to Protocol Versions

Code versions are **independent** from protocol versions:

- Protocol at v0.1, code at v0.3.2 → Validator implements ORP v0.1 spec
- Protocol at v1.0, code at v1.5.0 → Validator implements ORP v1.0 spec
- Code may support multiple protocol versions simultaneously

---

## Git Tagging Strategy

### Sprint Tags

When a sprint completes, tag the final commit:

```bash
git tag sprint-1.1.0 -a -m "Sprint 1.1: JSON Schema + Python Validator - Completed"
git push origin sprint-1.1.0
```

### Release Tags

When code is released, tag with version:

```bash
git tag v0.1.0 -a -m "Release v0.1.0 - Python validator for ORP v0.1"
git push origin v0.1.0
```

### Tag Naming Convention

- Sprint completions: `sprint-X.Y.Z`
- Code releases: `vX.Y.Z`
- Protocol versions: `orp-vX.Y` (spec versions, not code)

---

## Commit Message Convention

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types:

- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation changes
- `test:` — Adding or updating tests
- `refactor:` — Code refactoring without behavior change
- `chore:` — Build, CI, dependencies
- `sprint:` — Sprint planning/retrospective updates

### Scopes:

- `validator` — Python validator
- `schema` — JSON Schema
- `cli` — Command-line interface
- `docs` — Documentation
- `sprint` — Sprint planning

### Examples:

```
feat(validator): add compliance level detection

Implements ORP-Basic/Standard/Full detection based on which
layers are present and complete.

Closes sprint-1.1.0 Task 2
```

```
docs(sprint): complete sprint-1.1.0 retrospective

Added learnings about JSON Schema limitations and error
message design patterns discovered during implementation.
```

```
sprint(1.1): start sprint-1.1.0 - JSON Schema + Validator

Beginning Phase 1 core tooling. Target completion: 2 weeks.
```

---

## Version Tracking in Code

### Python Package Version

In `pyproject.toml` or `setup.py`:

```toml
[project]
name = "orp-validator"
version = "0.1.0"  # Code version
description = "Validator for OpenReason Protocol v0.1"
```

### Protocol Version Constant

In `orp_validator/__init__.py`:

```python
__version__ = "0.1.0"  # Code version
SUPPORTED_ORP_VERSIONS = ["0.1"]  # Protocol versions we support
```

### Schema Files

In `schemas/orp-v0.1.schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://openreason.org/schemas/orp-v0.1.schema.json",
  "version": "0.1",
  "title": "OpenReason Protocol v0.1"
}
```

---

## Sprint-to-Release Mapping

| Sprint | Code Version | Deliverable |
|--------|--------------|-------------|
| sprint-1.1.0 | v0.1.0 | JSON Schema + Python validator |
| sprint-1.2.0 | v0.2.0 | CLI scaffolding commands |
| sprint-1.3.0 | v0.3.0 | JavaScript/TypeScript validator |
| sprint-1.4.0 | v0.4.0 | REST API validator endpoint |
| Phase 1 complete | v1.0.0 | First stable release |

**Note:** Minor patches (v0.1.1, v0.1.2) may be released between sprints for bug fixes.

---

## When to Bump Versions

### Sprint Versions

- **SPRINT** increments when starting a new sprint in the same phase
- **ITERATION** increments if a sprint is revised or extended
- **PHASE** increments when moving to a new development phase

### Code Versions

- **PATCH** increments for bug fixes, docs, minor tweaks (v0.1.0 → v0.1.1)
- **MINOR** increments for new features, backward-compatible changes (v0.1.5 → v0.2.0)
- **MAJOR** increments for breaking changes (v0.9.0 → v1.0.0)

### Protocol Versions

Defined in `docs/specs/ORP_SPEC.md` — follows MAJOR.MINOR:
- **MINOR** for backward-compatible additions (v0.1 → v0.2)
- **MAJOR** for breaking schema changes (v0.9 → v1.0)

---

## Changelog Management

Maintain `CHANGELOG.md` at repo root:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Thing being worked on

## [0.1.0] - 2026-03-15 (sprint-1.1.0)

### Added
- JSON Schema for ORP v0.1
- Python validator with compliance level detection
- CLI validation command

### Documentation
- Initial CLAUDE.md and sprint planning structure
```

---

## Versioning in Sprint Files

Sprint files include version metadata:

```yaml
version: "sprint-1.1.0"
phase: 1
sprint_number: 1
iteration: 0
code_target_version: "v0.1.0"
protocol_version_supported: "0.1"
```

This makes it explicit which sprint produces which code version implementing which protocol version.

---

## Transparency Principle

All version increments should be:
- **Documented** — Why did we bump the version?
- **Traceable** — Git tags link versions to specific commits
- **Justified** — Changes recorded in CHANGELOG.md with reasoning

Version numbers are commitments. A v1.0.0 release means we're confident the public API is stable.

---

## Future Considerations

### Multi-Protocol Version Support

When ORP v0.2 is released, code may support both:

```python
SUPPORTED_ORP_VERSIONS = ["0.1", "0.2"]
```

Validator should detect which version a document uses and validate accordingly.

### Deprecation Policy

When we drop support for an old protocol version:
- Announce 6 months in advance
- Document in CHANGELOG
- Bump MAJOR version (breaking change)

---

*This versioning system is itself open to revision. If it doesn't work in practice, we'll fork it.*
