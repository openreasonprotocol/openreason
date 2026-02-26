"""OpenReason Protocol Validator API.

FastAPI service for validating ORP documents via HTTP.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import orp_validator
from routes import router as api_router

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
