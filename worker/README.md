# OpenReason Validator API — Cloudflare Worker

TypeScript port of the FastAPI service (`api/`). Same endpoints, same response
shapes, running on Cloudflare Workers' free tier instead of the DigitalOcean droplet.

- `POST /api/v1/validate` — full JSON Schema validation (ajv over the bundled v0.1/v0.2 schemas)
- `POST /api/v1/check` — quick compliance-level check
- `POST /api/v1/diff` — document comparison + fork detection
- `GET /` , `GET /health` — info / health
- `GET /docs` , `GET /openapi.json` — Redoc UI + static OpenAPI spec (replaces FastAPI's auto-docs)

## Why a rewrite (not Python on Cloudflare)

`js-yaml` + `ajv` over the existing **language-agnostic** JSON Schemas means no
Python runtime, ~0ms cold start, and a 1MB→82KB-gzipped bundle that sits well inside
the free tier. The `check`/`diff`/compliance logic is a line-for-line port of
`api/routes.py` and `orp_validator/validator.py`.

## Layout

```
worker/
  src/
    index.ts     # router (ports api/main.py routes + error codes)
    validate.ts  # ports orp_validator/validator.py validate()
    check.ts     # ports the /check endpoint's own compliance logic
    diff.ts      # ports _compare_dicts / _compare_lists / _serialize_value
    cors.ts      # CORS allow-list + security headers (copied from main.py)
    openapi.ts   # static OpenAPI spec + Redoc page
    schemas/     # copies of orp-v0.1 / v0.2 .schema.json (bundled at build)
  scripts/parity.mjs  # runs the bundled worker against examples/ for parity checks
```

> The schema files under `src/schemas/` are **copies** of
> `orp_validator/schemas/orp-v0.{1,2}.schema.json`. If those change, re-copy them.

## Local development

```bash
cd worker
npm install
npm run typecheck            # tsc --noEmit
npx wrangler dev             # local server (miniflare), no login needed
```

## Parity testing (vs. the Python API)

```bash
npx wrangler deploy --dry-run --outdir dist   # bundle without deploying
node scripts/parity.mjs                        # exercise the bundled worker
```

Verified identical to the Python API across all 5 `examples/*.yaml` and error cases
on: `status`, `valid`, `compliance_level`, error/warning counts, `num_changes`,
`identical`, and CORS headers.

**Known cosmetic differences (not structural):**
- Malformed-YAML error *text* differs (js-yaml vs PyYAML phrasing); both return 400.
- The 422 body for a missing/invalid `document` field is `{"detail": "..."}` here vs.
  FastAPI's validation-error list; status code is the same.

## Deploy (requires `wrangler login`)

```bash
cd worker
npx wrangler login                 # OAuth — do NOT paste an API token into files
npx wrangler deploy                # publishes to *.workers.dev
```

Then attach the custom domain (zone must be active on Cloudflare first):
- Dashboard: Workers & Pages → `openreason-api` → Settings → Domains & Routes →
  Add Custom Domain → `api.publicreasonproject.org`
- or uncomment the `[[routes]]` block in `wrangler.toml` and redeploy.

## Rate limiting (replaces slowapi 60/min)

Application code does **not** rate-limit (KV free-tier writes are too low for
per-request counting). Add a Cloudflare **WAF Rate Limiting Rule** instead:

- Match: hostname `api.publicreasonproject.org` AND URI path starts with `/api/v1/`
- Rate: 60 requests / 1 minute, counting by client IP
- Action: Block (returns 429)

## Free-tier limits

Workers: 100k req/day, 10ms CPU/request, 1MB gzipped bundle. Current bundle ~82KB
gzipped; validating a 1MB doc is well within the CPU budget.
