# Sprint 1-8.0: Cloudflare Migration (DigitalOcean → Cloudflare)

**Version:** `sprint-1.8.0`
**Status:** Completed
**Start Date:** 2026-06-26
**Target End Date:** 2026-07-03
**Actual End Date:** 2026-06-26

> **DEPLOYED & LIVE (2026-06-26):** Migration complete except the droplet soak/decommission.
> - `https://api.publicreasonproject.org` → Worker `openreason-api` (SSL active, validate/check/diff verified live)
> - `https://docs.publicreasonproject.org` → Pages `openreason-docs` (SSL active, site renders)
> - Stale droplet A records for `api`/`docs` deleted; MX/TXT (email) preserved.
> - WAF rate-limiting rule active on `/api/v1/*`: 10 req/10s per IP (= 60/min; free
>   plan only permits a 10s window, so this is the equivalent rate, not a literal 60/60s).
> - Account: `085d6025...` (Asbjorn@bullrise.co). Cloudflare API token used for deploy
>   is to be **rotated** by Asbjørn.
> - **Task 5 DONE:** Droplet `orp-api-fra` (554628875 / 134.209.250.174) destroyed 2026-06-26
>   at user request (hobby project, no soak). Both domains verified 200 post-destroy.
>   CLAUDE.md updated. (Soak was waived by the user.)

**Code Target Version:** `v0.4.1` (infrastructure only — no protocol changes)
**Protocol Version Supported:** `0.2` (and `0.1` backward compatible)

---

## Sprint Goal

Move both production services off the DigitalOcean droplet (134.209.250.174) onto
Cloudflare's free tier: the static docs site to **Cloudflare Pages**, and the
validator API to a **TypeScript Cloudflare Worker**. Decommission the droplet once
both are verified live on their existing custom domains.

---

## Why now / motivation

- **Cost:** The DO droplet is a recurring monthly cost. Cloudflare Pages + Workers
  free tier covers our current traffic at $0 (100k Worker requests/day, unlimited
  static Pages requests).
- **Operations:** No more nginx, Docker, Let's Encrypt renewal, or manual
  `scp`/`ssh`/`tar` deploys (the dead permission rules we just cleaned out of
  `.claude/settings.local.json` were all manual droplet deploys — this sprint
  removes that whole workflow).
- **Performance:** Workers have ~0ms cold start (V8 isolates) vs. a Dockerized
  Python/uvicorn process; Pages serves static assets from Cloudflare's edge.
- **Architecture fit:** Matches the Workers/KV edge-first stack already used elsewhere.

---

## Current State (what we're migrating)

| Service | Domain | Stack today | Target |
|---|---|---|---|
| Docs site | `docs.publicreasonproject.org` | Nextra/Next.js `output: 'export'` → static `out/`, served by nginx | **Cloudflare Pages** |
| Validator API | `api.publicreasonproject.org` | FastAPI + `orp-validator` PyPI pkg, slowapi rate limiting, Docker + nginx + Let's Encrypt | **TypeScript Worker** |

**Unaffected (no change needed):**
- `orp-validator` PyPI package and the `orp` CLI — hosted on PyPI, not the droplet.
- The JSON Schemas (`orp_validator/schemas/orp-v0.1.schema.json`,
  `orp-v0.2.schema.json`) — language-agnostic; the Worker bundles them directly.

---

## Target Architecture

```
                         Cloudflare DNS (zone: publicreasonproject.org)
                                        │
          ┌─────────────────────────────┼─────────────────────────────┐
          │                             │                             │
  docs.publicreasonproject.org   api.publicreasonproject.org   publicreasonproject.org
          │                             │                        (apex — unchanged
   Cloudflare Pages              Cloudflare Worker                 or future)
   (static export of             (TS: js-yaml + ajv +
    docs-site/out/)               ported check/diff logic)
                                        │
                                  WAF Rate Limiting Rule
                                  (60 req/min per IP — replaces slowapi)
```

---

## Scope

### In Scope
1. Move the `publicreasonproject.org` DNS zone to Cloudflare (if not already there).
2. Deploy `docs-site` to Cloudflare Pages with custom domain `docs.publicreasonproject.org`.
3. Rewrite the validator API as a TypeScript Worker (`validate`, `check`, `diff`,
   `/health`, `/`) with custom domain `api.publicreasonproject.org`.
4. Replicate rate limiting (60/min per IP) via a Cloudflare WAF Rate Limiting Rule.
5. Replicate CORS allow-list and security headers in the Worker.
6. Ship a static `openapi.json` + Swagger/Redoc page to replace FastAPI's auto-docs.
7. DNS cutover for both subdomains; verify against the existing API test suite.
8. Decommission the DO droplet after a soak period.

### Explicitly Out of Scope
- Any protocol/schema changes (this is infrastructure only).
- Rewriting the Python `orp-validator` package or CLI (stays on PyPI).
- New API endpoints or features.
- Migrating the GitLab CI pipeline wholesale — we add Cloudflare deploy steps but
  keep existing Python tests as-is.
- A hosted SPARQL endpoint or triple store (separate future work).

---

## Tasks

### Task 1: Cloudflare account + DNS zone
**Estimate:** 1–2 h (mostly DNS propagation wait)
**Status:** ✅ DONE — zone active on Cloudflare; old droplet A records removed, MX/TXT kept

**Description:**
Ensure the `publicreasonproject.org` zone is managed by Cloudflare. Check current
nameservers first — if DNS is at the registrar or DO, add the zone to Cloudflare and
update nameservers at the registrar. Keep existing A/MX/TXT records intact during the
move (especially any email/MX records — copy them exactly).

**Acceptance Criteria:**
- [ ] `dig NS publicreasonproject.org` returns Cloudflare nameservers
- [ ] All pre-existing records (apex, MX, TXT/SPF, any others) reproduced in Cloudflare
- [ ] `wrangler` CLI installed and authenticated (`wrangler login`)

**Dependencies:** Registrar access. **Do not** delete the DO droplet yet — the
`docs` and `api` A records still point at it until cutover (Tasks 4–5).

---

### Task 2: Docs site → Cloudflare Pages
**Estimate:** 2–3 h
**Status:** ✅ DONE — deployed to Pages `openreason-docs`, custom domain live with SSL

**Description:**
The docs site is already a static export (`next.config.mjs` has `output: 'export'`),
so this is a build + deploy with no code changes. Two options — prefer Git integration:

- **Option A (recommended):** Connect the GitLab repo to Cloudflare Pages. Build
  command `npm run build`, output dir `docs-site/out`, root dir `docs-site`. Auto-deploy
  on push to `main`.
- **Option B (manual / first test):** `cd docs-site && npm run build && wrangler pages deploy out --project-name openreason-docs`

Then attach the custom domain `docs.publicreasonproject.org` in Pages settings (this
is where the DNS record flips to Pages — see Task 4).

**Acceptance Criteria:**
- [ ] `*.pages.dev` preview URL renders the full docs site (spot-check `/`, `/protocol/specification`, `/tools/jsonld`, `/tools/sparql`)
- [ ] Build succeeds in CI (or via `wrangler pages deploy`)
- [ ] Custom domain attached and serving over HTTPS (Cloudflare-managed cert)

**Dependencies:** Task 1.

---

### Task 3: Validator API → TypeScript Worker
**Estimate:** 1–1.5 days
**Status:** ✅ DONE — deployed as Worker `openreason-api`, custom domain live with SSL

**Description:**
Rewrite the three endpoints as a Worker. The logic maps cleanly from the Python:

| Python (`api/`) | Worker (TS) |
|---|---|
| `yaml.safe_load` | `js-yaml` `load()` |
| `orp_validator.validate()` (jsonschema) | `ajv` against bundled `orp-v0.1`/`v0.2` schema, selected by `orp_version` |
| `_determine_compliance` / `_get_next_steps` (routes.py) | direct port — pure functions |
| `_compare_dicts` / `_compare_lists` / `_serialize_value` (diff) | direct port — pure functions |
| CORS middleware | manual headers (allow-list below) |
| security headers middleware | manual headers |
| slowapi `60/minute` | WAF Rate Limiting Rule (Task 4) |
| FastAPI `/docs` Swagger | static `openapi.json` + Redoc HTML route |

Keep response shapes byte-identical to the current API so existing clients and the
`api/tests/` suite still pass when pointed at the new origin.

**Suggested layout** (new `worker/` dir):
```
worker/
  wrangler.toml
  package.json            # ajv, js-yaml, typescript
  src/
    index.ts              # router: /, /health, /api/v1/{validate,check,diff}
    validate.ts           # ajv + schema selection
    check.ts              # ported _determine_compliance / _get_next_steps
    diff.ts               # ported _compare_dicts / _compare_lists
    cors.ts               # allow-list + preflight
    openapi.ts            # static spec + Redoc
  schemas/                # copies of orp-v0.1 / v0.2 .schema.json (build-time import)
```

**CORS allow-list (copy exactly from `api/main.py`):**
`http://localhost:3000`, `http://127.0.0.1:3000`, `https://publicreasonproject.org`,
`https://docs.publicreasonproject.org`, `https://api.publicreasonproject.org` —
methods `GET, POST, OPTIONS`, headers `Content-Type`, credentials off.

**Security headers (copy exactly):** `X-Content-Type-Options: nosniff`,
`X-Frame-Options: DENY`, `Content-Security-Policy: default-src 'none'`,
`X-XSS-Protection: 1; mode=block`.

**Acceptance Criteria:**
- [ ] `/`, `/health` return the same JSON shape (name, version, validator_version, endpoints)
- [ ] `/api/v1/validate` returns `{valid, compliance_level, layers_present, errors, warnings, metadata}` matching the Python output on the example docs
- [ ] `/api/v1/check` and `/api/v1/diff` outputs match Python on the same inputs
- [ ] 1MB request-size cap enforced (return 413)
- [ ] Malformed YAML returns 400 with a useful message
- [ ] Worker bundle under the 1MB gzipped free-tier limit
- [ ] CORS preflight + security headers verified

**Dependencies:** Task 1. Reuse `api/tests/` as the cross-check oracle.

---

### Task 4: DNS cutover + rate limiting
**Estimate:** 2–3 h
**Status:** ✅ DONE — both custom domains cut over; WAF rate-limit rule active (10 req/10s/IP)

**Description:**
- Point `docs.publicreasonproject.org` at the Pages project (proxied/orange-cloud).
- Point `api.publicreasonproject.org` at the Worker via a Workers Custom Domain.
- Add a **WAF Rate Limiting Rule**: 60 requests/min per client IP on
  `api.publicreasonproject.org/api/v1/*`, action = block/429. This replaces slowapi.
  (We use a WAF rule rather than a KV counter because the free KV write quota —
  ~1k/day — is too low for per-request counting; the WAF rule is free and edge-native.)

**Acceptance Criteria:**
- [ ] Both subdomains resolve to Cloudflare and serve correct content over HTTPS
- [ ] Rate limit returns 429 after 60 req/min from one IP
- [ ] Old DO origin no longer receives traffic (check droplet nginx logs go quiet)

**Dependencies:** Tasks 2, 3.

---

### Task 5: Verify, soak, decommission
**Estimate:** Verification 2 h + 48–72 h soak
**Status:** ✅ DONE — droplet destroyed 2026-06-26 (soak waived by user); domains verified 200 post-destroy; CLAUDE.md updated

**Description:**
Run the full API test suite against the live Worker origin and smoke-test the docs
site. Let both run for a 48–72 h soak window with the droplet still available as a
fast rollback. After the soak with no issues, **ask Asbjørn to confirm** before
destroying the droplet, then power it off and delete it.

**Acceptance Criteria:**
- [ ] `cd api && pytest tests/ -v` passes against the Worker base URL
- [ ] Swagger/Redoc reachable at the API's docs route
- [ ] 48–72 h soak with no errors in Cloudflare analytics
- [ ] Asbjørn confirms → droplet destroyed; `api/Dockerfile`, `docker-compose.yml`,
      `nginx.conf`, and droplet deploy docs archived or removed
- [ ] CLAUDE.md "Current Production Services" section updated (DO → Cloudflare)

**Dependencies:** Tasks 1–4. **This is the only irreversible step — gated on explicit confirmation.**

---

## Success Criteria

This sprint is complete when:
1. `docs.publicreasonproject.org` serves from Cloudflare Pages over HTTPS.
2. `api.publicreasonproject.org` serves from a Worker, with all `api/tests/` passing
   against it and responses matching the previous Python API.
3. Rate limiting (60/min/IP) and CORS/security headers are enforced at the edge.
4. The DO droplet is decommissioned and CLAUDE.md reflects the new stack.
5. Monthly hosting cost for these two services is $0.

---

## Dependencies

**Requires from previous work:**
- Existing static export build (`docs-site`, already working).
- Existing JSON Schemas and `api/tests/` suite (used as the correctness oracle).

**Blocks future work:**
- Any future hosted SPARQL endpoint / triple store would build on the Cloudflare setup.

---

## Risks and Unknowns

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| DNS zone move disrupts email (MX) | Med | High | Copy ALL existing records (esp. MX/SPF/TXT) into Cloudflare *before* changing nameservers; verify mail flow post-move |
| `ajv` validates the ORP schema differently than Python `jsonschema` (edge cases) | Med | Med | Diff Worker vs Python output on every `examples/*.yaml`; fix schema-draft/format mismatches before cutover |
| Worker output diverges from Python response shape | Med | Med | Run `api/tests/` against the Worker as the gate (Task 5) |
| 10ms free-tier CPU limit exceeded on large docs | Low | Med | Validation of a 1MB doc is well within budget; load-test with the largest example; upgrade is cheap if ever needed |
| Loss of FastAPI auto-Swagger | High (expected) | Low | Ship static `openapi.json` + Redoc page |
| Rollback needed after cutover | Low | Med | Keep droplet live through the soak; rollback = repoint DNS back |

---

## Decisions Made

### Decision 1: Rewrite the API as a TypeScript Worker (not Python/Pyodide)
**When:** 2026-06-26
**Who:** Asbjørn
**Reasoning:** Pure-JS validation (`js-yaml` + `ajv` over the existing
language-agnostic schemas) gives ~0ms cold starts, fits the free tier comfortably,
and is robust for a public production endpoint. The `check`/`diff` logic is pure
functions that port directly. Matches the existing edge-first Workers stack.
**Alternatives Considered:**
- *Python Worker (Pyodide):* keeps Python but has package-compatibility risk
  (`orp_validator`, `jsonschema`), heavier cold starts, and is more fragile in prod.
- *Keep API on a separate free Python host (Fly/Render):* doesn't meet the
  "everything on Cloudflare" goal and adds another vendor.

### Decision 2: WAF Rate Limiting Rule instead of KV counters
**When:** 2026-06-26
**Reasoning:** Free-tier KV write quota (~1k/day) is too low for per-request
counting. A WAF rate-limiting rule is free, edge-native, and needs no code.

---

## Retrospective

*(Added after sprint completes)*

### What Worked Well
### What Didn't Work
### What We Learned
### What Assumptions Were Wrong
### Changes for Next Sprint

---

## Notes

- Free-tier limits to keep in mind: Workers 100k req/day, 10ms CPU/request, 1MB
  gzipped bundle; Pages unlimited static requests, 500 builds/month; both custom
  domains free.
- The droplet is the rollback path during soak — do not delete until Task 5 confirms.
- Suggested rollout order to minimize risk: **docs site first** (low-risk, proves the
  Pages + DNS flow), then the API.
