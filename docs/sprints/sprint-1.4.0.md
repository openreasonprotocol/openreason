# Sprint 1.4.0: PyPI Publication + Packaging

**Version:** `sprint-1.4.0`
**Status:** Completed
**Start Date:** 2026-02-25
**Target End Date:** 2026-02-26
**Actual End Date:** 2026-02-26

**Code Target Version:** `v0.3.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Publish `orp-validator` to PyPI and establish automated release infrastructure so external users can install the tool via `pip install orp-validator`.

---

## Scope

### In Scope
- Publish package to PyPI
- GitLab CI/CD pipeline for automated releases
- Version badge and install instructions in README
- Package metadata (description, keywords, classifiers)
- Test installation from PyPI works on clean system
- Documentation for contributors on release process

### Explicitly Out of Scope
- Building Docker images (defer to Sprint 1.5 REST API)
- Publishing to conda-forge (maybe later if requested)
- Creating brew formula (low priority)
- Windows installer (pip should be sufficient)

---

## Tasks

### Task 1: Prepare Package Metadata
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Ensure `pyproject.toml` has all required PyPI metadata.

**Acceptance Criteria:**
- [ ] `pyproject.toml` includes:
  - Project description (already present)
  - Keywords: `["orp", "openreason", "transparency", "policy", "validator", "governance"]`
  - Classifiers:
    - Development Status :: 4 - Beta
    - Intended Audience :: Developers
    - Intended Audience :: Science/Research
    - Topic :: Scientific/Engineering
    - Topic :: Software Development :: Quality Assurance
    - License :: OSI Approved :: MIT License
    - Programming Language :: Python :: 3.9
    - Programming Language :: Python :: 3.10
    - Programming Language :: Python :: 3.11
    - Programming Language :: Python :: 3.12
  - Project URLs:
    - Homepage: https://publicreasonproject.org
    - Repository: https://gitlab.com/publicreason/orp
    - Documentation: https://publicreasonproject.org/docs
    - Issues: https://gitlab.com/publicreason/orp/-/issues
  - `long_description` from README.md
  - `long_description_content_type = "text/markdown"`
- [ ] LICENSE file is MIT and included in package

**Dependencies:**
- None

---

### Task 2: Configure Build System
**Owner:** TBD
**Estimate:** 30 minutes
**Status:** Not Started

**Description:**
Ensure package builds correctly with modern Python packaging tools.

**Acceptance Criteria:**
- [ ] `pyproject.toml` uses `build-system` (already configured with setuptools)
- [ ] `python -m build` creates wheel and sdist successfully
- [ ] Generated package includes:
  - All Python modules
  - Templates directory
  - JSON schema file
  - LICENSE, README
- [ ] Package size is reasonable (<500KB)
- [ ] Test locally: `pip install dist/orp_validator-*.whl` works

**Dependencies:**
- Task 1 complete

---

### Task 3: Create PyPI Account and Project
**Owner:** TBD
**Estimate:** 30 minutes
**Status:** Not Started

**Description:**
Set up PyPI project and credentials.

**Acceptance Criteria:**
- [ ] Create account on https://pypi.org (if not exists)
- [ ] Reserve project name `orp-validator`
- [ ] Generate API token for automated uploads
- [ ] Store API token securely in GitLab CI/CD variables
  - Variable name: `PYPI_TOKEN`
  - Protected: Yes
  - Masked: Yes
- [ ] Test upload to TestPyPI first: https://test.pypi.org

**Dependencies:**
- Task 2 complete

---

### Task 4: First Manual Release
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Perform first release manually to validate process.

**Acceptance Criteria:**
- [ ] Update version to `0.3.0` in `pyproject.toml`
- [ ] Update `CHANGELOG.md` with v0.3.0 release notes
- [ ] Build package: `python -m build`
- [ ] Upload to TestPyPI: `python -m twine upload --repository testpypi dist/*`
- [ ] Test install from TestPyPI: `pip install --index-url https://test.pypi.org/simple/ orp-validator`
- [ ] Verify all commands work: `orp --help`, `orp validate`, etc.
- [ ] If successful, upload to real PyPI: `python -m twine upload dist/*`
- [ ] Test install from PyPI: `pip install orp-validator`
- [ ] Tag release: `git tag v0.3.0`
- [ ] Push tag: `git push origin v0.3.0`

**Dependencies:**
- Task 3 complete

---

### Task 5: Automate Releases with GitLab CI
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Set up CI/CD pipeline to automatically publish to PyPI when tags are pushed.

**Acceptance Criteria:**
- [ ] Update `.gitlab-ci.yml` with new `release` stage:
  ```yaml
  release:
    stage: release
    image: python:3.11
    only:
      - tags
    script:
      - pip install build twine
      - python -m build
      - python -m twine upload -u __token__ -p $PYPI_TOKEN dist/*
  ```
- [ ] Test by creating a test tag (e.g., `v0.3.0-rc1`)
- [ ] Verify package appears on PyPI
- [ ] Document release process in `CONTRIBUTING.md`:
  - How to create a release
  - Versioning convention
  - What triggers automated publish
- [ ] Delete test release/tag after validation

**Dependencies:**
- Task 4 complete

---

### Task 6: Update Documentation
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Update all documentation to reference PyPI installation.

**Acceptance Criteria:**
- [ ] Update README.md:
  - Change installation from `pip install -e .` to `pip install orp-validator`
  - Add PyPI badge: `![PyPI](https://img.shields.io/pypi/v/orp-validator)`
  - Add Python version badge: `![Python](https://img.shields.io/pypi/pyversions/orp-validator)`
  - Keep development install instructions in separate section
- [ ] Update `docs/CONTRIBUTING.md`:
  - Development setup still uses `pip install -e ".[dev]"`
  - Document release process
- [ ] Update `CHANGELOG.md`:
  - Add v0.3.0 section with:
    - "Published to PyPI"
    - "Install via: pip install orp-validator"
    - Automated release pipeline

**Dependencies:**
- Task 5 complete

---

### Task 7: Verify Installation on Clean Systems
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Test installation works on fresh systems across different platforms.

**Acceptance Criteria:**
- [ ] Test on Linux (Ubuntu/Debian):
  - Fresh Docker container
  - `pip install orp-validator`
  - All commands work
- [ ] Test on macOS:
  - Clean venv
  - `pip install orp-validator`
  - All commands work
- [ ] Test on Windows (if possible):
  - Clean venv
  - `pip install orp-validator`
  - All commands work
- [ ] Test Python 3.9, 3.10, 3.11, 3.12
- [ ] Document any platform-specific issues

**Dependencies:**
- Task 4 complete (package on PyPI)

---

## Success Criteria

This sprint is complete when:

1. `pip install orp-validator` installs the latest version from PyPI
2. All CLI commands (`orp new`, `orp validate`, `orp check`, `orp diff`) work after installation
3. GitLab CI automatically publishes new versions when tags are pushed
4. README shows PyPI badge with correct version
5. Installation works on Linux, macOS, and ideally Windows
6. CHANGELOG documents v0.3.0 release
7. Contributors know how to cut new releases

---

## Dependencies

**Requires from previous work:**
- Sprint 1.1.0: Working validator package
- Sprint 1.2.0: Complete CLI with all commands

**Blocks future work:**
- Sprint 1.5.0: REST API will `pip install orp-validator` as dependency
- Sprint 1.6.0: Website needs install instructions
- External adoption: Nobody can use it until it's on PyPI

---

## Risks and Unknowns

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Package name `orp-validator` already taken | Low | High | Check PyPI first, have backup name ready (`openreason-validator`) |
| Build fails on PyPI infrastructure | Low | Medium | Test on TestPyPI first |
| Missing dependencies in package | Medium | High | Test fresh install thoroughly before v0.3.0 tag |
| GitLab CI credentials leak | Low | Critical | Use masked CI variables, never commit tokens |
| Version conflicts with existing packages | Low | Medium | Pin dependency versions conservatively |

---

## Decisions Made

### Decision 1: Use PyPI, not conda-forge
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- PyPI is standard for Python packages
- conda-forge has complex approval process
- Can add conda later if users request it
**Alternatives Considered:**
- Conda-forge (more complex, defer)
- Both (maintain both, too much work initially)

### Decision 2: Automated releases via GitLab CI
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- Reduces human error
- Ensures consistency
- Standard practice for open source
**Alternatives Considered:**
- Manual releases every time (error-prone, doesn't scale)
- GitHub Actions (we're using GitLab)

### Decision 3: Semantic versioning (semver)
**When:** Sprint planning (already decided in v0.1.0)
**Who:** Project founders
**Reasoning:**
- Industry standard
- Clear upgrade expectations
- Works with pip dependency resolution
**Alternatives Considered:**
- Calendar versioning (less clear for API stability)

---

## Retrospective

### What Worked Well
- PyPI publication process went smoothly after initial package restructuring
- TestPyPI testing caught packaging issues before production release
- GitLab CI/CD pipeline configuration was straightforward
- Badge integration improved README visibility

### What Didn't Work
- Python 3.9 compatibility issues not caught until CI ran
- Initial package structure had schemas/templates outside package directory
- Resource loading with `importlib.resources` required version-specific handling
- Force push to protected branch caused git divergence (resolved with rebase)

### What We Learned

**Critical lesson: Python 3.9 resource loading**

The package initially failed all tests on Python 3.9 (40 failures) due to `importlib.resources.files()` not existing before Python 3.10.

**Solution implemented:**
```python
import sys

if sys.version_info >= (3, 10):
    from importlib.resources import files
else:
    # Python 3.9: use importlib_resources backport
    try:
        from importlib_resources import files  # type: ignore
    except ImportError:
        # Fallback if backport not installed
        files = None

# Then use fallback to direct paths if files is None
if files is not None:
    content = files("orp_validator.schemas").joinpath("file.json").read_text()
else:
    path = Path(__file__).parent / "schemas" / "file.json"
    with open(path, encoding="utf-8") as f:
        content = f.read()
```

**Why this matters:**
- Python 3.9 still widely used in production environments
- PyPI packages must work across all declared Python versions
- Resource loading is non-trivial when supporting multiple Python versions
- GitLab CI multi-version testing caught this early

**Files affected:**
- `orp_validator/validator.py:66-87` - Schema loading
- `orp_validator/commands/new.py:142-157` - Template loading
- `pyproject.toml:39` - Added `importlib-resources>=5.0; python_version < '3.10'`

**Testing approach:**
- Added comprehensive documentation to CONTRIBUTING.md
- Local testing with Python 3.9 recommended before pushing
- CI tests across Python 3.9, 3.10, 3.11, 3.12
- Fallback paths ensure it works even without backport package

### What Assumptions Were Wrong

**Assumption:** Package resources "just work" when bundled in a wheel
**Reality:** Resource loading APIs changed between Python versions, requiring explicit compatibility handling

**Assumption:** Linting fixes could be amended to previous commit
**Reality:** Protected branches prevent force push, requiring git rebase workflow instead

**Assumption:** importlib_resources backport would always be installed
**Reality:** Need fallback to direct file paths for robustness

### Changes for Next Sprint

1. **Test multi-version compatibility earlier** - Don't wait for CI to catch Python version issues
2. **Document version-specific patterns** - Added to CONTRIBUTING.md for future contributors
3. **Run full linting suite before pushing** - Especially after compatibility fixes
4. **Use git rebase workflow** - For protected branches, never attempt force push

### Technical Debt Created

None - all issues resolved during sprint.

### Technical Debt Resolved

- Package structure now correct (schemas/templates inside package)
- Python 3.9 fully supported with robust fallback mechanism
- All linting issues resolved (Black, Ruff, Mypy strict mode)
- Git history clean after rebase resolution

---

## Notes

- First publish to TestPyPI, then real PyPI
- Keep version numbers in sync: git tag = PyPI version = pyproject.toml version
- Once published, versions cannot be deleted (only "yanked")
- Be conservative with v0.3.0 - make sure it's solid before pushing
- README on PyPI uses the long_description from pyproject.toml

**Resources:**
- PyPI packaging guide: https://packaging.python.org/
- Twine docs: https://twine.readthedocs.io/
- GitLab CI PyPI example: https://docs.gitlab.com/ee/user/packages/pypi_repository/

---

**Reference:**
- See PHASE1_PLAN.md for sprint sequencing rationale
- Current version: v0.2.0 (after Sprint 1.2.0)
- Target version: v0.3.0
