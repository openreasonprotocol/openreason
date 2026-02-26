"""OpenReason Protocol Validator API.

FastAPI service for validating ORP documents via HTTP.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

import orp_validator
from routes import router as api_router

# Rate limiter configuration
limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])

app = FastAPI(
    title="OpenReason Protocol Validator API",
    description=(
        "REST API for validating OpenReason Protocol (ORP) documents.\n\n"
        "The OpenReason Protocol is a public standard for transparent, "
        "simulatable reasoning in policy, AI, and democratic decision-making."
    ),
    version="0.4.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Add rate limiter to app state
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:*",
        "http://127.0.0.1:*",
        "https://publicreasonproject.org",
        "https://*.publicreasonproject.org",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


# Security headers middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """Add security headers to all responses."""
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'none'"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "name": "OpenReason Protocol Validator API",
        "version": "0.4.0",
        "orp_version": "0.1",
        "validator_version": orp_validator.__version__,
        "endpoints": {
            "health": "/health",
            "documentation": "/docs",
            "validate": "/api/v1/validate",
            "check": "/api/v1/check",
            "diff": "/api/v1/diff",
        },
        "repository": "https://gitlab.com/publicreason/orp",
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "ok",
        "version": "0.4.0",
        "validator_version": orp_validator.__version__,
    }


# Include API routes
app.include_router(api_router)
