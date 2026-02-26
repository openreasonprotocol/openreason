"""Tests for security features (CORS, headers, rate limiting)."""

import pytest


class TestSecurity:
    """Test suite for security features."""

    def test_cors_headers_valid_origin(self, client):
        """Test CORS headers for valid origin."""
        response = client.options(
            "/api/v1/validate",
            headers={
                "Origin": "https://publicreasonproject.org",
                "Access-Control-Request-Method": "POST"
            }
        )
        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "https://publicreasonproject.org"

    def test_cors_headers_localhost_origin(self, client):
        """Test CORS headers for localhost origin (development)."""
        response = client.options(
            "/api/v1/validate",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "POST"
            }
        )
        # Localhost should be allowed (200) or rejected (400) based on config
        # Both are acceptable in production vs dev
        assert response.status_code in [200, 400]
        if response.status_code == 200:
            cors_header = response.headers.get("access-control-allow-origin", "")
            assert "localhost" in cors_header or cors_header == "*"

    def test_security_headers_present(self, client, valid_orp_basic):
        """Test that security headers are present in responses."""
        response = client.post(
            "/api/v1/validate",
            json={"document": valid_orp_basic}
        )
        headers = response.headers

        # Check for security headers
        assert "x-content-type-options" in headers
        assert headers["x-content-type-options"] == "nosniff"

        assert "x-frame-options" in headers
        assert headers["x-frame-options"] == "DENY"

        assert "content-security-policy" in headers
        assert "default-src 'none'" in headers["content-security-policy"]

    def test_request_size_limit(self, client):
        """Test that requests exceeding 1MB are rejected."""
        # Create document > 1MB
        huge_doc = "summary: " + "A" * (1048577)
        response = client.post(
            "/api/v1/validate",
            json={"document": huge_doc}
        )
        assert response.status_code == 422  # Pydantic validation error

    def test_health_endpoint_no_auth(self, client):
        """Test that health endpoint doesn't require authentication."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "version" in data

    def test_openapi_docs_accessible(self, client):
        """Test that API documentation is accessible."""
        response = client.get("/docs")
        assert response.status_code == 200
        assert "swagger" in response.text.lower() or "openapi" in response.text.lower()

    def test_openapi_json_accessible(self, client):
        """Test that OpenAPI JSON spec is accessible."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "paths" in data
        assert "/api/v1/validate" in data["paths"]

    def test_invalid_http_method(self, client):
        """Test that invalid HTTP methods are rejected."""
        response = client.put("/api/v1/validate", json={"document": "test"})
        assert response.status_code == 405  # Method Not Allowed

    def test_missing_content_type(self, client):
        """Test request without Content-Type header."""
        response = client.post(
            "/api/v1/validate",
            data='{"document": "test"}',
            headers={}
        )
        # Should either reject or handle gracefully
        assert response.status_code in [400, 415, 422]

    def test_sql_injection_attempt(self, client):
        """Test that SQL injection attempts don't cause issues."""
        malicious_doc = """
orp_version: '0.1'; DROP TABLE users; --
document_id: test-001
title: Test
"""
        response = client.post(
            "/api/v1/validate",
            json={"document": malicious_doc}
        )
        # Should process without error (we don't have SQL)
        assert response.status_code in [200, 400]

    def test_xss_attempt(self, client):
        """Test that XSS attempts are safely handled."""
        xss_doc = """
orp_version: '0.1'
document_id: <script>alert('XSS')</script>
title: Test
"""
        response = client.post(
            "/api/v1/validate",
            json={"document": xss_doc}
        )
        # Should process document, script tags become part of string
        assert response.status_code in [200, 400]
        data = response.json()
        # Ensure script tag isn't executed in response
        assert "text/html" not in response.headers.get("content-type", "")
