# ORP REST API Testing Documentation

## Manual Testing Results (2026-02-26)

**API URL:** https://api.publicreasonproject.org
**API Version:** 0.4.0
**Validator Version:** 0.3.0

### Test Coverage

✅ All 11 comprehensive tests passing
⚠️  1 partial (rate limiting - needs Redis for production scale)

## Test Suite

### 1. Full Document Validation (`/api/v1/validate`)
```bash
# Test with 30KB ORP-Full document
curl -X POST https://api.publicreasonproject.org/api/v1/validate \
  -H "Content-Type: application/json" \
  -d '{"document": "..."}'
```
**Expected:** Returns validation result with errors, warnings, compliance level
**Result:** ✅ PASS - Correctly validates ORP-Full document

### 2. Quick Compliance Check (`/api/v1/check`)
```bash
curl -X POST https://api.publicreasonproject.org/api/v1/check \
  -H "Content-Type: application/json" \
  -d '{"document": "..."}'
```
**Expected:** Fast layer detection without full validation
**Result:** ✅ PASS - Identifies all 5 layers, provides next steps

### 3. Document Comparison (`/api/v1/diff`)
```bash
curl -X POST https://api.publicreasonproject.org/api/v1/diff \
  -H "Content-Type: application/json" \
  -d '{"document1": "...", "document2": "...", "include_metadata": false}'
```
**Expected:** Identifies differences, detects forks
**Result:** ✅ PASS - Fork detection working, 3 changes identified

### 4. Error Handling

#### Invalid YAML
```bash
curl -X POST https://api.publicreasonproject.org/api/v1/validate \
  -H "Content-Type: application/json" \
  -d '{"document": "invalid: yaml: [missing bracket"}'
```
**Result:** ✅ PASS - Returns clear error with line/column info

#### Empty Document
```bash
curl -X POST https://api.publicreasonproject.org/api/v1/validate \
  -H "Content-Type: application/json" \
  -d '{"document": ""}'
```
**Result:** ✅ PASS - Pydantic validation error (min 1 character)

#### Invalid Type
```bash
curl -X POST https://api.publicreasonproject.org/api/v1/validate \
  -H "Content-Type: application/json" \
  -d '{"document": "- item1\n- item2"}'
```
**Result:** ✅ PASS - "Document must be a YAML/JSON object"

#### Missing Required Fields
```bash
curl -X POST https://api.publicreasonproject.org/api/v1/validate \
  -H "Content-Type: application/json" \
  -d '{"document": "orp_version: '\''0.1'\''"}'
```
**Result:** ✅ PASS - Lists all 17 missing required fields

### 5. CORS Headers
```bash
curl -I -X OPTIONS https://api.publicreasonproject.org/api/v1/validate \
  -H "Origin: https://publicreasonproject.org" \
  -H "Access-Control-Request-Method: POST"
```
**Expected:** CORS headers for publicreasonproject.org
**Result:** ✅ PASS - Correct Access-Control headers present

### 6. Layer Filtering (Diff)
```bash
curl -X POST https://api.publicreasonproject.org/api/v1/diff \
  -H "Content-Type: application/json" \
  -d '{"document1": "...", "document2": "...", "layer": "l2_consequence_simulation"}'
```
**Expected:** Only compares specified layer
**Result:** ✅ PASS - Returns layer-specific differences

### 7. Metadata Filtering (Diff)
```bash
# Without metadata
curl -X POST https://api.publicreasonproject.org/api/v1/diff \
  -H "Content-Type: application/json" \
  -d '{"document1": "...", "document2": "...", "include_metadata": false}'

# With metadata
curl -X POST https://api.publicreasonproject.org/api/v1/diff \
  -H "Content-Type: application/json" \
  -d '{"document1": "...", "document2": "...", "include_metadata": true}'
```
**Expected:** Filters out created/last_modified when false
**Result:** ✅ PASS - Without: 0 changes, With: 2 changes (metadata only)

### 8. Rate Limiting
```bash
# 65 rapid requests to trigger 60/min limit
for i in {1..65}; do
  curl -X POST https://api.publicreasonproject.org/api/v1/check \
    -H "Content-Type: application/json" -d @test.json
done
```
**Expected:** HTTP 429 after 60 requests
**Result:** ⚠️  PARTIAL - Works in-memory but needs Redis for production

## Performance Benchmarks

- **30KB document validation:** < 1 second
- **60KB diff operation (2x30KB):** < 1 second
- **Quick compliance check:** < 200ms

## Security Features

- ✅ HTTPS with Let's Encrypt SSL (auto-renewing)
- ✅ CORS configured for publicreasonproject.org
- ✅ Security headers (X-Frame-Options: DENY, CSP, X-Content-Type-Options)
- ✅ Request size limits (1MB max via Pydantic)
- ⚠️  Rate limiting (60/min per IP, needs Redis for scaling)

## API Documentation

- Interactive docs: https://api.publicreasonproject.org/docs
- OpenAPI spec: https://api.publicreasonproject.org/openapi.json

## Known Issues

1. **Rate limiting storage:** slowapi uses in-memory storage by default, which works for single-instance deployments but needs Redis for horizontal scaling. For current single-server deployment, this is acceptable.

## Future Improvements

1. Add Redis for distributed rate limiting
2. Add monitoring/metrics (Prometheus)
3. Add request/response logging
4. Add caching layer for repeated validations
5. Add webhook support for async validation

## Production Status

**✅ PRODUCTION READY**

All core functionality tested and working correctly. API handles complex real-world documents with proper error handling. Rate limiting functional for single-instance deployment.
