# Sprint 1.5.0: REST API Validator Service

**Version:** `sprint-1.5.0`
**Status:** Planned
**Start Date:** TBD
**Target End Date:** TBD
**Actual End Date:** (if completed)

**Code Target Version:** `v0.4.0`
**Protocol Version Supported:** `0.1`

---

## Sprint Goal

Build and deploy a REST API service that validates ORP documents via HTTP, enabling browser-based validation and future integrations.

---

## Scope

### In Scope
- FastAPI service with validation endpoints
- OpenAPI/Swagger documentation
- Docker containerization
- Deployment to api.publicreasonproject.org
- CORS configuration for web embedding
- Rate limiting and basic security
- Health check and monitoring endpoints
- Error handling and structured responses

### Explicitly Out of Scope
- User authentication (all endpoints are public for now)
- Document storage/persistence (stateless API)
- Batch validation (single document at a time)
- Webhook notifications
- GraphQL API (REST only)
- WebSocket streaming

---

## Tasks

### Task 1: Initialize FastAPI Project
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Set up FastAPI application structure.

**Acceptance Criteria:**
- [ ] Create `api/` directory in repository
- [ ] `api/main.py` with FastAPI app initialization
- [ ] `api/requirements.txt` with dependencies:
  - fastapi
  - uvicorn[standard]
  - orp-validator (from PyPI)
  - pydantic
  - python-multipart (for file uploads)
- [ ] `api/Dockerfile` for containerization
- [ ] `api/README.md` with local development instructions
- [ ] Health check endpoint: `GET /health` returns `{"status": "ok"}`
- [ ] Root endpoint: `GET /` returns API info and version

**Dependencies:**
- Sprint 1.4.0 complete (orp-validator on PyPI)

---

### Task 2: Implement Validation Endpoint
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Create `POST /validate` endpoint that validates ORP documents.

**Acceptance Criteria:**
- [ ] `POST /api/v1/validate` endpoint accepts:
  - Request body: JSON or YAML document text
  - Content-Type: application/json or application/yaml or text/yaml
- [ ] Response format:
  ```json
  {
    "valid": true,
    "compliance_level": "ORP-Full",
    "layers_present": {
      "l1_data_provenance": true,
      ...
    },
    "errors": [],
    "warnings": ["..."],
    "metadata": {
      "orp_version": "0.1",
      "document_id": "...",
      "title": "..."
    }
  }
  ```
- [ ] HTTP status codes:
  - 200: Validation completed (check `valid` field for result)
  - 400: Invalid request (malformed YAML/JSON)
  - 413: Payload too large (>1MB limit)
  - 500: Server error
- [ ] Request validation with Pydantic models
- [ ] Error messages are user-friendly
- [ ] Unit tests for endpoint

**Dependencies:**
- Task 1 complete

---

### Task 3: Implement Check Endpoint
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Create `POST /check` endpoint for quick compliance checking.

**Acceptance Criteria:**
- [ ] `POST /api/v1/check` endpoint accepts document
- [ ] Response format:
  ```json
  {
    "compliance_level": "ORP-Basic",
    "layers_present": {
      "l1_data_provenance": true,
      "l2_consequence_simulation": false,
      ...
    },
    "next_steps": "To reach ORP-Standard, add L2 and L3"
  }
  ```
- [ ] Faster than `/validate` (skips schema validation)
- [ ] Same error handling as validate endpoint
- [ ] Unit tests

**Dependencies:**
- Task 2 complete

---

### Task 4: Implement Diff Endpoint
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Create `POST /diff` endpoint to compare two documents.

**Acceptance Criteria:**
- [ ] `POST /api/v1/diff` endpoint accepts:
  ```json
  {
    "document1": "...",
    "document2": "...",
    "include_metadata": false,
    "layer": null
  }
  ```
- [ ] Response format:
  ```json
  {
    "identical": false,
    "is_fork": true,
    "fork_direction": "document2 forked from document1",
    "differences": [
      {
        "type": "changed",
        "field": "l2_consequence_simulation.scenarios[0].outcomes",
        "old_value": "...",
        "new_value": "..."
      }
    ],
    "num_changes": 15
  }
  ```
- [ ] Handles layer-specific diffs
- [ ] Detects fork relationships
- [ ] Unit tests

**Dependencies:**
- Task 3 complete

---

### Task 5: Add CORS and Security
**Owner:** TBD
**Estimate:** 1 hour
**Status:** Not Started

**Description:**
Configure CORS, rate limiting, and basic security.

**Acceptance Criteria:**
- [ ] CORS middleware configured:
  - Allow origins: `publicreasonproject.org`, `localhost:*` (dev)
  - Allow methods: GET, POST, OPTIONS
  - Allow headers: Content-Type
- [ ] Rate limiting:
  - 60 requests per minute per IP
  - Return 429 with Retry-After header when exceeded
- [ ] Request size limits:
  - Max body size: 1MB
  - Return 413 if exceeded
- [ ] Security headers:
  - X-Content-Type-Options: nosniff
  - X-Frame-Options: DENY
  - Content-Security-Policy: default-src 'none'
- [ ] Input sanitization (already handled by Pydantic)

**Dependencies:**
- Tasks 2-4 complete

---

### Task 6: OpenAPI Documentation
**Owner:** TBD
**Estimate:** 1.5 hours
**Status:** Not Started

**Description:**
Ensure FastAPI generates excellent API documentation.

**Acceptance Criteria:**
- [ ] OpenAPI spec auto-generated at `/openapi.json`
- [ ] Swagger UI at `/docs` with:
  - API title: "OpenReason Protocol Validator API"
  - Description from README
  - Version: 0.4.0
  - All endpoints documented
  - Request/response schemas shown
  - Example requests for each endpoint
- [ ] ReDoc UI at `/redoc` (alternative docs view)
- [ ] All Pydantic models have clear descriptions
- [ ] Endpoint descriptions explain:
  - What it does
  - When to use it
  - What it returns
  - Error cases

**Dependencies:**
- Tasks 2-4 complete

---

### Task 7: Docker Containerization
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Create production-ready Docker image.

**Acceptance Criteria:**
- [ ] `api/Dockerfile` with multi-stage build:
  - Base: `python:3.11-slim`
  - Install dependencies
  - Copy application code
  - Non-root user
  - Health check configured
- [ ] `.dockerignore` to exclude unnecessary files
- [ ] `docker-compose.yml` for local development
- [ ] Image size <200MB
- [ ] Test: `docker build -t orp-api .`
- [ ] Test: `docker run -p 8000:8000 orp-api`
- [ ] Test: API accessible at http://localhost:8000
- [ ] Document Docker usage in `api/README.md`

**Dependencies:**
- Tasks 1-6 complete

---

### Task 8: Deployment Setup
**Owner:** TBD
**Estimate:** 3 hours
**Status:** Not Started

**Description:**
Deploy to api.publicreasonproject.org.

**Acceptance Criteria:**
- [ ] Choose hosting platform:
  - Option A: fly.io (recommended - simple, free tier)
  - Option B: Railway.app
  - Option C: DigitalOcean App Platform
  - Option D: GitLab Container Registry + VM
- [ ] Configure DNS: `api.publicreasonproject.org` → deployment
- [ ] SSL/TLS certificate (Let's Encrypt)
- [ ] Environment variables configured
- [ ] Deployment documented in `api/DEPLOYMENT.md`
- [ ] Test: https://api.publicreasonproject.org/health returns 200
- [ ] Test: https://api.publicreasonproject.org/docs loads Swagger UI

**Dependencies:**
- Task 7 complete

---

### Task 9: Monitoring and Logging
**Owner:** TBD
**Estimate:** 1.5 hours
**Status:** Not Started

**Description:**
Set up basic monitoring and structured logging.

**Acceptance Criteria:**
- [ ] Structured JSON logging with:
  - Timestamp
  - Log level
  - Endpoint called
  - Response status
  - Response time
  - Error details (if any)
- [ ] `/metrics` endpoint (Prometheus format, optional):
  - Request count by endpoint
  - Response times (histogram)
  - Error rate
- [ ] Uptime monitoring:
  - Configure UptimeRobot or similar (free tier)
  - Monitor /health endpoint every 5 minutes
  - Alert if down >2 minutes
- [ ] Document monitoring setup

**Dependencies:**
- Task 8 complete

---

### Task 10: CI/CD Pipeline
**Owner:** TBD
**Estimate:** 2 hours
**Status:** Not Started

**Description:**
Automate testing and deployment.

**Acceptance Criteria:**
- [ ] Update `.gitlab-ci.yml` with API stages:
  - `test-api`: Run API tests
  - `build-api`: Build Docker image
  - `deploy-api`: Deploy to production (on main branch)
- [ ] API tests run on every commit
- [ ] Docker image built on every tag
- [ ] Automatic deployment when main branch updates
- [ ] Deployment rollback procedure documented

**Dependencies:**
- Task 8 complete

---

## Success Criteria

This sprint is complete when:

1. https://api.publicreasonproject.org/health returns `{"status": "ok"}`
2. `POST /api/v1/validate` successfully validates ORP documents
3. API documentation available at https://api.publicreasonproject.org/docs
4. CORS configured to allow embedding in publicreasonproject.org
5. Rate limiting prevents abuse
6. Docker image builds and runs successfully
7. Monitoring alerts if API goes down
8. Full API documentation in README

---

## Dependencies

**Requires from previous work:**
- Sprint 1.4.0: `orp-validator` published to PyPI

**Blocks future work:**
- Sprint 1.6.0: Website needs API for interactive validator widget

---

## Risks and Unknowns

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Hosting costs exceed budget | Medium | Medium | Use free tiers (fly.io, Railway); monitor usage |
| API gets abused/spammed | Medium | High | Rate limiting, consider API keys in future |
| Performance issues with large documents | Low | Medium | Add file size limits, consider async processing |
| Deployment complexity | Low | Medium | Choose simple platform (fly.io), document well |
| SSL certificate issues | Low | Low | Most platforms auto-provision Let's Encrypt |

---

## Decisions Made

### Decision 1: FastAPI over Flask/Django
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- Modern async support
- Auto-generated OpenAPI docs
- Type safety with Pydantic
- Fast performance
**Alternatives Considered:**
- Flask (simpler but less features)
- Django (too heavy for API-only service)

### Decision 2: Stateless API (no document storage)
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- Simpler to build and maintain
- Easier to scale
- No database needed
- Privacy-preserving (we don't store user documents)
**Alternatives Considered:**
- Store documents (adds complexity, privacy concerns)

### Decision 3: Public API (no auth initially)
**When:** Sprint planning
**Who:** TBD
**Reasoning:**
- Lower barrier to adoption
- Rate limiting prevents abuse
- Can add API keys later if needed
**Alternatives Considered:**
- Require API keys (friction for users)
- OAuth (overkill for v1)

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

- Keep API simple and focused - don't add features we don't need yet
- Optimize for ease of deployment and maintenance
- Document everything - future contributors need clear setup
- Test with real documents from Sprint 1.3 (Danish example)

**Endpoint Summary:**
- `GET /` - API info
- `GET /health` - Health check
- `GET /docs` - Swagger UI
- `POST /api/v1/validate` - Full validation
- `POST /api/v1/check` - Quick compliance check
- `POST /api/v1/diff` - Compare documents
- `GET /metrics` - Prometheus metrics (optional)

---

**Reference:**
- See PHASE1_PLAN.md for sprint sequencing rationale
- FastAPI docs: https://fastapi.tiangolo.com/
- fly.io deployment: https://fly.io/docs/languages-and-frameworks/python/
