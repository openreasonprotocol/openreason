# Sprint 1.7.3.8: Release orp-validator v0.4.0 to PyPI

**Sprint Duration**: 1-2 hours
**Status**: COMPLETE ✅
**Completed**: 2026-04-08
**Prerequisites**: Sprint 1.7.3.7 complete (ORP v0.2 specification and documentation)

---

## Sprint Goal

Release orp-validator v0.4.0 to PyPI with ORP v0.2 support, making the validator publicly available for adoption.

**Deliverables**:
1. ✅ Version bumped to 0.4.0 throughout codebase
2. ✅ CHANGELOG.md updated with v0.6.0 release notes (project v0.6.0 includes orp-validator v0.4.0)
3. ✅ PyPI package built and tested locally
4. ✅ Published to PyPI
5. ✅ Installation verified from PyPI
6. ✅ Release notes published and GitLab tag v0.6.0 created

---

## Context

### Current State

**Validator Version**: 0.4.0 (already set in `orp_validator/__init__.py`)
**ORP Protocol Version**: 0.2.0
**Last PyPI Release**: 0.3.0 (v0.1 support only)

**What's New in v0.4.0**:
- ORP v0.2 schema support (post-hoc, extensions, flexibility)
- Auto-detection of document version (v0.1 vs v0.2)
- Extension registry tracking (orp-ai-training-v1, orp-safety-v1, orp-license-v1)
- ORP-PostHoc compliance level recognition
- 4 validated examples (8,328 lines)

### Why PyPI Release Matters

- **Public Availability**: Makes validator accessible via `pip install orp-validator`
- **Version Control**: Users can pin to specific versions
- **Dependency Management**: Enables use in other projects
- **Trust Signal**: Official release on PyPI increases adoption confidence

---

## Phases

### Phase 1: Pre-Release Verification ✅

**Goal**: Ensure everything is ready for release

#### 1.1: Verify Version Numbers

```bash
# Check __init__.py
grep "VERSION" orp_validator/__init__.py
# Expected: __version__ = "0.4.0"

# Check pyproject.toml
grep "version" pyproject.toml
# Expected: version = "0.4.0"
```

**Status**: ✅ Already set to 0.4.0

#### 1.2: Run Full Test Suite

```bash
# Validate all examples
python3 -m orp_validator.cli examples/danish_property_tax_reform.yaml
python3 -m orp_validator.cli examples/imagenet_training_data.yaml
python3 -m orp_validator.cli examples/laion5b_training_data.yaml
python3 -m orp_validator.cli examples/common_crawl_training_data.yaml
python3 -m orp_validator.cli examples/github_copilot_training_data.yaml

# Expected: All 5 examples validate successfully
```

#### 1.3: Test CLI Commands

```bash
# Test all CLI commands
orp --version
orp --help
orp new /tmp/test.yaml
orp validate examples/imagenet_training_data.yaml
orp check examples/imagenet_training_data.yaml
orp diff examples/imagenet_training_data.yaml examples/laion5b_training_data.yaml
```

---

### Phase 2: Update CHANGELOG.md

**Goal**: Document v0.4.0 release for users

**File**: `CHANGELOG.md`

**Add**:

```markdown
## [0.4.0] - 2026-04-08

### Added

**ORP v0.2 Support**:
- Auto-detection of document version (`orp_version` field)
- Support for both v0.1 and v0.2 documents
- ORP-PostHoc compliance level recognition
- Extension registry tracking (informational)

**New v0.2 Schema Features**:
- Post-hoc reconstruction support (`post_hoc` flag)
- Domain-specific extensions (orp-ai-training-v1, orp-safety-v1, orp-license-v1)
- Flexible schema validation (`additionalProperties: true` throughout)
- Granular confidence levels (7-point scale)
- Accountability gap documentation

**Examples**:
- ImageNet training data (1,513 lines, ORP-PostHoc)
- LAION-5B training data (2,162 lines, ORP-PostHoc)
- Common Crawl training data (2,232 lines, ORP-PostHoc)
- GitHub Copilot training data (2,421 lines, ORP-PostHoc)

**Documentation**:
- ORP v0.2 Specification (`docs/specs/ORP_V0.2_SPEC.md`)
- Migration Guide (`docs/specs/MIGRATION_V0.1_TO_V0.2.md`)
- Updated README with v0.2 release notes

### Changed

- Schema location: Added `orp_validator/schemas/orp-v0.2.schema.json`
- Validator now loads schema based on document version
- CLI `--orp-version` parameter for explicit version selection

### Fixed

- 311 validation errors from v0.1 schema → 0 errors with v0.2 flexibility
- Supports real-world post-hoc reconstruction documents

### Backward Compatibility

✅ **Fully backward compatible**: All v0.1 documents validate correctly with v0.4.0 validator
```

---

### Phase 3: Build and Test Package Locally

**Goal**: Ensure package builds correctly before PyPI upload

#### 3.1: Clean Previous Builds

```bash
# Remove old build artifacts
rm -rf dist/ build/ *.egg-info
```

#### 3.2: Build Package

```bash
# Build source distribution and wheel
python3 -m build

# Expected output:
# - dist/orp-validator-0.4.0.tar.gz
# - dist/orp_validator-0.4.0-py3-none-any.whl
```

#### 3.3: Test Local Installation

```bash
# Create test virtual environment
python3 -m venv /tmp/orp-test-env
source /tmp/orp-test-env/bin/activate

# Install from local wheel
pip install dist/orp_validator-0.4.0-py3-none-any.whl

# Test installation
orp --version
# Expected: orp-validator 0.4.0 (ORP v0.2 support)

# Test validation
orp validate examples/imagenet_training_data.yaml
# Expected: ✓ Valid (ORP-PostHoc)

# Cleanup
deactivate
rm -rf /tmp/orp-test-env
```

---

### Phase 4: Publish to PyPI

**Goal**: Release v0.4.0 to PyPI

#### 4.1: Check PyPI Credentials

```bash
# Verify ~/.pypirc exists with token
cat ~/.pypirc

# Expected format:
# [pypi]
# username = __token__
# password = pypi-AgE...
```

**If missing**: Get token from https://pypi.org/manage/account/token/

#### 4.2: Upload to Test PyPI (Optional but Recommended)

```bash
# Upload to test.pypi.org first
python3 -m twine upload --repository testpypi dist/*

# Test installation from test PyPI
pip install --index-url https://test.pypi.org/simple/ orp-validator==0.4.0

# Validate
orp --version
```

#### 4.3: Upload to Production PyPI

```bash
# Upload to pypi.org
python3 -m twine upload dist/*

# Expected output:
# Uploading distributions to https://upload.pypi.org/legacy/
# Uploading orp_validator-0.4.0-py3-none-any.whl
# 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Uploading orp-validator-0.4.0.tar.gz
# 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Phase 5: Post-Release Verification

**Goal**: Confirm public availability and functionality

#### 5.1: Verify PyPI Listing

**Check**:
- https://pypi.org/project/orp-validator/
- Version 0.4.0 should be listed as latest
- Release date: 2026-04-08
- Description and links correct

#### 5.2: Test Public Installation

```bash
# Fresh environment
python3 -m venv /tmp/orp-public-test
source /tmp/orp-public-test/bin/activate

# Install from PyPI
pip install orp-validator

# Verify version
orp --version
# Expected: orp-validator 0.4.0 (ORP v0.2 support)

# Test with v0.2 document (download from repo)
curl -O https://gitlab.com/publicreason/orp/-/raw/main/examples/imagenet_training_data.yaml
orp validate imagenet_training_data.yaml
# Expected: ✓ Valid (ORP-PostHoc)

# Cleanup
deactivate
rm -rf /tmp/orp-public-test
```

#### 5.3: Update Installation Instructions

Verify README installation instructions work:

```bash
pip install orp-validator
orp --version
```

---

### Phase 6: Release Announcement

**Goal**: Notify community of v0.4.0 availability

#### 6.1: GitLab Release

Create release on GitLab:
- **Tag**: `v0.4.0`
- **Title**: "ORP v0.2 Release - Post-Hoc Reconstruction & Extensions"
- **Description**: Link to CHANGELOG.md v0.4.0 section
- **Assets**: None needed (PyPI is source of truth)

#### 6.2: Update docs.publicreasonproject.org

If docs site exists, update:
- Installation instructions
- Version selector (if applicable)
- Link to v0.2 specification

#### 6.3: Social Media / Community Announcement (Optional)

**Channels**:
- GitLab project updates
- Academic networks (if applicable)
- Policy tech communities

**Message Template**:
```
🎉 ORP v0.2 Released!

orp-validator 0.4.0 now available on PyPI:
pip install orp-validator

New features:
✅ Post-hoc reconstruction support
✅ Domain-specific extensions
✅ 4 AI training dataset examples (8,328 lines)
✅ 100% backward compatible

Docs: https://docs.publicreasonproject.org
Spec: https://gitlab.com/publicreason/orp/-/blob/main/docs/specs/ORP_V0.2_SPEC.md

#OpenReason #Transparency #AIEthics
```

---

## Success Criteria

### Must Have
- [x] Version 0.4.0 set in `__init__.py` and `pyproject.toml`
- [ ] CHANGELOG.md updated with v0.4.0 release notes
- [ ] Package built successfully (`.tar.gz` and `.whl`)
- [ ] Uploaded to PyPI
- [ ] Public installation verified (`pip install orp-validator`)
- [ ] All 5 examples validate from PyPI-installed package

### Nice to Have
- [ ] Test PyPI upload first (safety check)
- [ ] GitLab release created with tag
- [ ] Release announcement published
- [ ] Documentation site updated (if exists)

---

## Risks and Mitigations

### Risk 1: PyPI Upload Failure

**Risk**: Invalid credentials, package conflicts, upload errors

**Mitigation**:
- Test with Test PyPI first
- Verify credentials before production upload
- Check for existing version conflicts (`pip install orp-validator==0.4.0` fails if already exists)

### Risk 2: Package Dependencies Missing

**Risk**: Users install but get import errors due to missing deps

**Mitigation**:
- Verify `pyproject.toml` dependencies complete
- Test fresh installation in clean virtualenv
- Check `install_requires` includes all necessary packages

### Risk 3: Backward Compatibility Broken

**Risk**: v0.1 documents fail validation after upgrade

**Mitigation**:
- Test v0.1 documents before release (danish_property_tax_reform.yaml)
- Explicitly validate backward compatibility in test suite
- Document any edge cases in CHANGELOG

---

## Rollback Procedure

If critical issues discovered after PyPI release:

### Option 1: Yank Release (Preferred)

```bash
# Yank release from PyPI (hidden but not deleted)
twine upload --repository pypi --yank "Critical bug, use v0.3.0" dist/*
```

**Effect**: v0.4.0 no longer appears in `pip install` by default, but existing installations unaffected

### Option 2: Hotfix Release (v0.4.1)

If bug fixable quickly:
1. Fix bug
2. Bump version to 0.4.1
3. Release 0.4.1 to PyPI
4. Document issue in CHANGELOG

---

## Files Modified

**Modified**:
- `CHANGELOG.md` (add v0.4.0 release notes)

**Created** (during build):
- `dist/orp-validator-0.4.0.tar.gz`
- `dist/orp_validator-0.4.0-py3-none-any.whl`

---

## Dependencies

**Required Tools**:
- `build`: `pip install build`
- `twine`: `pip install twine`

**PyPI Account**:
- Username: `__token__`
- Token: Stored in `~/.pypirc` or environment variable

**Access**:
- PyPI maintainer access for `orp-validator` package

---

## Estimated Timeline

| Phase | Task | Time |
|-------|------|------|
| 1 | Pre-release verification | 15 min |
| 2 | Update CHANGELOG.md | 10 min |
| 3 | Build and test locally | 15 min |
| 4 | Upload to PyPI | 10 min |
| 5 | Post-release verification | 15 min |
| 6 | Release announcement | 10 min |
| **Total** | | **1-1.5 hours** |

---

## Post-Sprint Actions

After successful release:
1. Monitor PyPI download stats
2. Watch for GitHub/GitLab issues related to v0.4.0
3. Update internal documentation with release learnings
4. Plan Sprint 1.7.3.9 (REST API v0.2 update)

---

## Retrospective (Post-Sprint)

### What Went Well
- All 6 phases completed smoothly without issues
- Pre-release verification caught no errors (all 5 examples validated successfully)
- Build process generated both .tar.gz and .whl successfully
- PyPI upload worked on first attempt
- Public installation verified immediately after upload
- Version management clear: project v0.6.0 includes orp-validator PyPI package v0.4.0

### What Didn't Go Well
- Minor confusion about version numbering: project version (0.6.0) vs package version (0.4.0)
  - Resolved by documenting both in CHANGELOG.md
  - Project had already used v0.4.0 and v0.5.0 for REST API and docs site
- Build warnings about license format and extensions package (non-critical, will address in future sprint)
- pyproject.toml was not updated to 0.4.0 initially (caught and fixed during sprint)

### Lessons Learned
- Always verify both __init__.py and pyproject.toml have matching versions before release
- Project version != package version when there are multiple releases between PyPI updates
- Testing with fresh virtualenvs is essential for catching environment-specific issues
- Having comprehensive examples (8,328 lines) provides strong confidence for releases

### Metrics
- PyPI upload time: ~5 seconds (excellent)
- Package size: 68.9 kB (.whl), 80.3 kB (.tar.gz)
- First verification installation: Immediate (within 2 minutes of upload)
- Issues discovered post-release: 0
- Total sprint time: ~1.5 hours (within estimate)
- Examples validated: 5/5 (100% success rate)

### Next Steps
- Sprint 1.7.3.9: Update REST API at api.publicreasonproject.org to support ORP v0.2
- Monitor PyPI download statistics
- Watch for community feedback and issues

---

*Sprint created: 2026-04-08*
*Sprint completed: 2026-04-08*
*Status: COMPLETE ✅*
*PyPI Release: https://pypi.org/project/orp-validator/0.4.0/*
*GitLab Tag: v0.6.0*
