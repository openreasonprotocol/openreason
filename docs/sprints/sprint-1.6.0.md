# Sprint 1.6.0: Documentation Website

**Version:** `sprint-1.6.0`
**Status:** Planned
**Start Date:** TBD
**Target End Date:** TBD
**Actual End Date:** (if completed)

**Code Target Version:** `v0.5.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Launch publicreasonproject.org with comprehensive documentation, examples, and an interactive validator widget to make OpenReason accessible to external users.

---

## Scope

### In Scope
- Static documentation site using MkDocs Material
- Content migration from `docs/` directory
- Interactive validator widget (paste YAML → validate via REST API)
- Examples showcase (Danish Property Tax)
- GitLab Pages deployment to publicreasonproject.org
- Mobile-responsive design
- Search functionality
- Navigation and site structure
- Social media cards (Open Graph)

### Explicitly Out of Scope
- User accounts or authentication
- Document hosting/repository
- Discussion forums (maybe Phase 2)
- Blog/news section (add later if needed)
- Multi-language support (English only for now)
- Video tutorials (Phase 2)

---

## Tasks

### Task 1: Choose and Configure Static Site Generator
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Set up MkDocs Material for documentation site.

**Acceptance Criteria:**
- [ ] Install MkDocs Material: `pip install mkdocs-material`
- [ ] Create `mkdocs.yml` configuration:
  - Site name: "OpenReason Protocol"
  - Repo: https://gitlab.com/publicreason/orp
  - Theme: Material with custom colors
  - Features: navigation tabs, instant loading, search
- [ ] Create `docs-site/` directory (separate from `docs/`)
- [ ] Test local build: `mkdocs serve`
- [ ] Site loads at http://localhost:8000

**Dependencies:**
- None

---

### Task 2: Design Site Structure
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Plan navigation and information architecture.

**Acceptance Criteria:**
- [ ] Navigation structure:
  ```
  Home
  Getting Started
    - Quick Start
    - Installation
    - Your First Document
  Protocol
    - Overview
    - Specification (ORP_SPEC)
    - Philosophy (REE_PHILOSOPHY)
    - Compliance Levels
  Documentation
    - CLI Reference
    - Python API
    - REST API
  Examples
    - Danish Property Tax Reform
    - (More later)
  Community
    - Contributing
    - Governance
    - Roadmap
  ```
- [ ] Homepage sections:
  1. Hero: What is OpenReason?
  2. Quick Start: Install + validate in 60 seconds
  3. Interactive Validator: Try it now
  4. Features: Why use ORP?
  5. Examples: See it in action
  6. Call to Action: Get involved
- [ ] Footer: Links, GitHub/GitLab, License

**Dependencies:**
- Task 1 complete

---

### Task 3: Migrate and Adapt Content
**Owner:** TBD
**Estimate:** 3 hours
**Status:** Not Started

**Description:**
Move existing documentation into MkDocs structure.

**Acceptance Criteria:**
- [ ] Convert to MkDocs format:
  - `README.md` → `docs-site/index.md` (homepage)
  - `docs/specs/ORP_SPEC.md` → `docs-site/protocol/specification.md`
  - `docs/specs/REE_PHILOSOPHY.md` → `docs-site/protocol/philosophy.md`
  - `docs/CONTRIBUTING.md` → `docs-site/community/contributing.md`
  - `docs/governance/GOVERNANCE.md` → `docs-site/community/governance.md`
  - `docs/ROADMAP.md` → `docs-site/community/roadmap.md`
- [ ] Create new pages:
  - `docs-site/getting-started/quickstart.md`
  - `docs-site/getting-started/installation.md`
  - `docs-site/getting-started/first-document.md`
  - `docs-site/documentation/cli.md`
  - `docs-site/documentation/python-api.md`
  - `docs-site/documentation/rest-api.md`
  - `docs-site/examples/index.md`
  - `docs-site/examples/danish-property-tax.md`
- [ ] Adapt writing style for web (shorter paragraphs, clearer headings)
- [ ] Fix internal links to work in MkDocs
- [ ] Add navigation breadcrumbs

**Dependencies:**
- Task 2 complete
- Sprint 1.3 complete (Danish example)
- Sprint 1.4 complete (PyPI install)
- Sprint 1.5 complete (REST API docs)

---

### Task 4: Create Interactive Validator Widget
**Owner:** TBD
**Estimate:** 4 hours
**Status:** Not Started

**Description:**
Build browser-based YAML validator using REST API.

**Acceptance Criteria:**
- [ ] Create `docs-site/validator.md` or embed in homepage
- [ ] HTML/JavaScript widget with:
  - Large text area for YAML input
  - "Validate" button
  - Loading indicator
  - Results panel showing:
    - ✓/✗ Valid status
    - Compliance level (with badge)
    - Layers present (checkmarks)
    - Errors (if any)
    - Warnings (if any)
  - "Load Example" button (loads Danish example)
  - "Clear" button
- [ ] Uses `fetch()` to call `https://api.publicreasonproject.org/api/v1/validate`
- [ ] Handles API errors gracefully
- [ ] Syntax highlighting for YAML (optional, nice-to-have)
- [ ] Mobile-friendly (text area resizes)
- [ ] Works in all modern browsers

**Dependencies:**
- Task 3 complete
- Sprint 1.5 complete (REST API live)

---

### Task 5: Style and Design
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Customize theme to match OpenReason branding.

**Acceptance Criteria:**
- [ ] Color scheme:
  - Primary: Blue (trust, transparency)
  - Accent: Orange or green (action, growth)
  - Keep it professional, not flashy
- [ ] Typography:
  - Readable font (default Material theme is good)
  - Clear hierarchy (h1, h2, h3)
- [ ] Custom CSS in `docs-site/stylesheets/extra.css`:
  - Hero section styling
  - Validator widget styling
  - Example code blocks
  - Call-to-action buttons
- [ ] Logo (if available) in header
- [ ] Favicon
- [ ] Mobile responsive (test on phone)
- [ ] Dark mode support (Material theme built-in)

**Dependencies:**
- Task 4 complete

---

### Task 6: Add Search Functionality
**Owner:** TBD
**Estimate:** 30 minutes
**Status:** Not Started

**Description:**
Configure built-in MkDocs search.

**Acceptance Criteria:**
- [ ] Search enabled in `mkdocs.yml`:
  ```yaml
  plugins:
    - search:
        lang: en
  ```
- [ ] Search box appears in header
- [ ] Test search for key terms:
  - "data provenance"
  - "compliance level"
  - "validate"
  - "fork"
- [ ] Search results are relevant
- [ ] Search works without JavaScript (graceful degradation)

**Dependencies:**
- Task 3 complete (content exists)

---

### Task 7: Configure GitLab Pages
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Deploy site to publicreasonproject.org via GitLab Pages.

**Acceptance Criteria:**
- [ ] Add `.gitlab-ci.yml` pages job:
  ```yaml
  pages:
    stage: deploy
    image: python:3.11
    script:
      - pip install mkdocs-material
      - mkdocs build --strict
      - mv site public
    artifacts:
      paths:
        - public
    only:
      - main
  ```
- [ ] Configure custom domain in GitLab:
  - Settings → Pages → New Domain
  - Add: publicreasonproject.org
  - Get verification TXT record
- [ ] Configure DNS at domain registrar:
  - A record: publicreasonproject.org → GitLab Pages IP
  - TXT record for verification
  - CNAME: www.publicreasonproject.org → publicreasonproject.org
- [ ] SSL certificate provisioned (Let's Encrypt via GitLab)
- [ ] Test: https://publicreasonproject.org loads
- [ ] Test: https://www.publicreasonproject.org redirects to https://publicreasonproject.org

**Dependencies:**
- Tasks 1-6 complete
- Domain publicreasonproject.org ownership

---

### Task 8: SEO and Social Media
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Optimize for search engines and social sharing.

**Acceptance Criteria:**
- [ ] Meta tags in `mkdocs.yml`:
  ```yaml
  extra:
    social:
      - icon: fontawesome/brands/gitlab
        link: https://gitlab.com/publicreason/orp
      - icon: fontawesome/brands/python
        link: https://pypi.org/project/orp-validator/
  ```
- [ ] Open Graph tags for social media:
  - og:title
  - og:description
  - og:image (create social share image)
  - og:url
- [ ] Structured data (JSON-LD):
  - SoftwareApplication schema
  - Organization schema
- [ ] robots.txt (allow all)
- [ ] sitemap.xml (auto-generated by MkDocs)
- [ ] Test social sharing on Twitter/LinkedIn
- [ ] Google Analytics (optional, ethical tracking)

**Dependencies:**
- Task 7 complete (site is live)

---

### Task 9: Documentation and Launch Checklist
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Final review and launch preparation.

**Acceptance Criteria:**
- [ ] Pre-launch checklist:
  - [ ] All links work (no 404s)
  - [ ] All pages have proper titles
  - [ ] Navigation makes sense
  - [ ] Mobile view tested
  - [ ] Search works
  - [ ] Validator widget works
  - [ ] Examples load correctly
  - [ ] SSL certificate valid
  - [ ] DNS propagated
  - [ ] GitLab Pages deployment successful
- [ ] Update main README.md:
  - Link to publicreasonproject.org as primary docs
  - Keep README as project overview
- [ ] Announce launch:
  - GitLab README badge: ![Website](https://img.shields.io/website?url=https%3A%2F%2Fpublicreasonproject.org)
  - Update CHANGELOG.md with v0.5.0
  - Tag v0.5.0
  - Consider announcement (Twitter, HN, etc.)

**Dependencies:**
- Tasks 1-8 complete

---

## Success Criteria

This sprint is complete when:

1. https://publicreasonproject.org loads with complete documentation
2. Interactive validator widget successfully validates ORP documents
3. All examples (Danish Property Tax) are showcased
4. Site is mobile-responsive and fast
5. Search functionality works
6. SSL certificate is valid
7. GitLab CI automatically deploys on main branch updates
8. SEO and social media metadata is configured

---

## Dependencies

**Requires from previous work:**
- Sprint 1.3.0: Danish Property Tax example (for examples showcase)
- Sprint 1.4.0: PyPI package (for installation instructions)
- Sprint 1.5.0: REST API (for validator widget)

**Blocks future work:**
- Public launch and adoption
- External contributions (need clear docs)

---

## Risks and Unknowns

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| DNS propagation delays | Medium | Low | Set up early, allow 24-48h |
| GitLab Pages limits exceeded | Low | Medium | Monitor usage, docs are static (lightweight) |
| MkDocs learning curve | Low | Low | Well-documented, similar to other SSGs |
| Content quality issues | Medium | High | Review all pages, get feedback before launch |
| Validator widget doesn't work | Low | High | Test thoroughly, have fallback (link to CLI) |

---

## Decisions Made

### Decision 1: MkDocs Material over alternatives
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- Beautiful default theme
- Built for documentation
- GitLab Pages friendly
- Python ecosystem (same as validator)
- Great search functionality
**Alternatives Considered:**
- Sphinx (more complex, Python-focused)
- Docusaurus (React-based, heavier)
- Jekyll (Ruby, older)
- Hugo (Go, steep learning curve)

### Decision 2: GitLab Pages over external hosting
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- Free for open source
- Auto-deploy from repo
- SSL included
- Same ecosystem as code
**Alternatives Considered:**
- Netlify (good but separate platform)
- Vercel (commercial focus)
- GitHub Pages (we're using GitLab)

### Decision 3: Interactive widget over embedded CodeSandbox
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- Custom, lightweight solution
- Uses our REST API directly
- No third-party dependencies
- Full control over UX
**Alternatives Considered:**
- CodeSandbox embed (heavy, overkill)
- REPL.it (separate platform)
- Just link to API docs (less engaging)

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

- Keep homepage concise - link to deeper docs, don't duplicate
- Examples are crucial - showcase the Danish tax reform prominently
- Validator widget is the "try it now" hook - make it prominent
- Documentation should serve two audiences:
  1. Users (how to use ORP)
  2. Contributors (how to help build it)
- Don't over-design - simple, clean, functional
- Optimize for speed - docs sites should load fast

**MkDocs Material Features to Enable:**
- Navigation tabs
- Instant loading
- Search highlighting
- Table of contents (right sidebar)
- Code copy button
- Dark mode toggle
- Social cards (auto-generated)

---

**Reference:**
- See PHASE1_PLAN.md for sprint sequencing rationale
- MkDocs Material: https://squidfunk.github.io/mkdocs-material/
- GitLab Pages: https://docs.gitlab.com/ee/user/project/pages/
