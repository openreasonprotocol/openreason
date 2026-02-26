# ORP REST API Test Suite

Comprehensive automated test suite for the OpenReason Protocol REST API.

## Test Coverage

**39 tests | 96% coverage**

- **Validate endpoint:** 12 tests
- **Check endpoint:** 7 tests
- **Diff endpoint:** 11 tests
- **Security:** 12 tests

## Running Tests

### Run all tests
```bash
cd api
source .venv/bin/activate
pytest tests/ -v
```

### Run with coverage
```bash
pytest tests/ -v --cov=. --cov-report=term-missing --cov-fail-under=80
```

### Run specific test file
```bash
pytest tests/test_validate_endpoint.py -v
```

### Run specific test
```bash
pytest tests/test_validate_endpoint.py::TestValidateEndpoint::test_validate_orp_full_success -v
```

## Test Structure

```
tests/
├── __init__.py
├── conftest.py                 # Shared fixtures
├── test_validate_endpoint.py   # /api/v1/validate tests
├── test_check_endpoint.py      # /api/v1/check tests
├── test_diff_endpoint.py       # /api/v1/diff tests
└── test_security.py            # CORS, headers, security tests
```

## Fixtures

Defined in `conftest.py`:

- `client` - FastAPI TestClient
- `valid_orp_basic` - Minimal ORP-Basic document
- `valid_orp_full` - Complete ORP-Full document
- `invalid_yaml` - Malformed YAML
- `yaml_array` - Valid YAML but wrong type
- `minimal_document` - Document with only orp_version

## CI/CD Integration

Tests run automatically on:
- All merge requests
- Commits to main branch
- Tagged releases

Configured in `.gitlab-ci.yml` under `test:api` job.

### CI/CD Requirements
- Python 3.11+
- pytest >= 7.4.0
- pytest-cov >= 4.1.0
- httpx >= 0.24.0 (for TestClient)

## Test Categories

### Validation Tests (`test_validate_endpoint.py`)
- Valid ORP documents (Basic, Standard, Full)
- Invalid YAML syntax
- Invalid document structure
- Missing required fields
- Size limits (1MB max)
- JSON vs YAML formats
- Metadata extraction

### Compliance Check Tests (`test_check_endpoint.py`)
- Layer detection for all compliance levels
- Performance vs full validation
- Quick failure on invalid input
- Next steps guidance

### Diff Tests (`test_diff_endpoint.py`)
- Identical document detection
- Fork relationship detection
- Metadata filtering
- Layer-specific comparison
- Nested field changes
- Change type detection (added, removed, changed)

### Security Tests (`test_security.py`)
- CORS headers (production domain + localhost)
- Security headers (X-Frame-Options, CSP, etc.)
- Request size limits
- Invalid HTTP methods
- SQL injection attempts
- XSS attempts
- OpenAPI documentation accessibility

## Coverage Requirements

- Minimum: 80% (enforced by CI/CD)
- Current: 96%

Coverage report generated in `htmlcov/` directory.

## Adding New Tests

1. Create test file in `tests/` directory
2. Import `TestClient` and `app` from `main`
3. Use fixtures from `conftest.py`
4. Follow naming convention: `test_*.py`, `Test*` classes, `test_*` methods
5. Run tests locally before pushing
6. Ensure coverage stays above 80%

Example:
```python
from fastapi.testclient import TestClient
from main import app

class TestNewFeature:
    def test_new_endpoint(self, client):
        response = client.get("/new-endpoint")
        assert response.status_code == 200
```

## Known Issues

None currently. All 39 tests passing.

## Future Test Additions

- Load testing / stress testing
- Rate limiting with Redis backend
- Webhook functionality (when implemented)
- Caching layer (when implemented)
- Async validation (when implemented)
