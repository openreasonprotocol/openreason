# OpenReason Protocol Validator API

REST API service for validating OpenReason Protocol (ORP) documents via HTTP.

## Quick Start

### Local Development

```bash
# From the api/ directory
cd api/

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API root:** http://localhost:8000/
- **Health check:** http://localhost:8000/health
- **Swagger docs:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### Docker

```bash
# Build image
docker build -t orp-api .

# Run container
docker run -p 8000:8000 orp-api

# Or use docker-compose
docker-compose up
```

## API Endpoints

### `GET /`
API information and available endpoints.

### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "ok",
  "version": "0.4.0",
  "validator_version": "0.3.0"
}
```

### `POST /api/v1/validate`
Validate an ORP document with full schema validation.

**Request:**
```json
{
  "document": "orp_version: '0.1'\ndocument_id: test-001\n..."
}
```

**Response:**
```json
{
  "valid": true,
  "compliance_level": "ORP-Full",
  "layers_present": {
    "l1_data_provenance": true,
    "l2_consequence_simulation": true,
    "l3_empathy_mapping": true,
    "l4_accountability_ledger": true,
    "l5_fork_registry": true
  },
  "errors": [],
  "warnings": ["..."]
}
```

### `POST /api/v1/check`
Quick compliance level check without full validation.

**Request:**
```json
{
  "document": "orp_version: '0.1'\n..."
}
```

**Response:**
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

### `POST /api/v1/diff`
Compare two ORP documents.

**Request:**
```json
{
  "document1": "...",
  "document2": "...",
  "include_metadata": false,
  "layer": null
}
```

**Response:**
```json
{
  "identical": false,
  "is_fork": true,
  "fork_direction": "document2 forked from document1",
  "differences": [...],
  "num_changes": 15
}
```

## Configuration

### Environment Variables

- `HOST` - Server host (default: `0.0.0.0`)
- `PORT` - Server port (default: `8000`)
- `LOG_LEVEL` - Logging level (default: `info`)
- `MAX_BODY_SIZE` - Max request size in bytes (default: `1048576` = 1MB)

### CORS

Configured to allow requests from:
- `http://localhost:*` (development)
- `https://publicreasonproject.org`
- `https://*.publicreasonproject.org`

### Rate Limiting

- 60 requests per minute per IP address
- Returns `429 Too Many Requests` when exceeded

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Code Quality

```bash
# Format code
black api/

# Lint
ruff check api/

# Type check
mypy api/
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment instructions.

## Links

- **Repository:** https://gitlab.com/publicreason/orp
- **PyPI Package:** https://pypi.org/project/orp-validator/
- **Documentation:** https://publicreasonproject.org/docs
- **Issues:** https://gitlab.com/publicreason/orp/-/issues
