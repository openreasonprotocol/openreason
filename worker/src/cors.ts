// CORS allow-list + security headers, copied exactly from api/main.py.

const ALLOWED_ORIGINS = new Set([
  "http://localhost:3000",
  "http://127.0.0.1:3000",
  "https://publicreasonproject.org",
  "https://docs.publicreasonproject.org",
  "https://api.publicreasonproject.org",
  "https://openreasonprotocol.org",
  "https://www.openreasonprotocol.org",
  "https://openreason-docs.pages.dev",
]);

// Cloudflare Pages preview deployments of the docs site (e.g. https://abc123.openreason-docs.pages.dev).
const PREVIEW_ORIGIN = /^https:\/\/[a-z0-9-]+\.openreason-docs\.pages\.dev$/;

function isAllowed(origin: string): boolean {
  return ALLOWED_ORIGINS.has(origin) || PREVIEW_ORIGIN.test(origin);
}

const SECURITY_HEADERS: Record<string, string> = {
  "X-Content-Type-Options": "nosniff",
  "X-Frame-Options": "DENY",
  "Content-Security-Policy": "default-src 'none'",
  "X-XSS-Protection": "1; mode=block",
};

export function corsHeaders(origin: string | null): Record<string, string> {
  const headers: Record<string, string> = {};
  if (origin && isAllowed(origin)) {
    headers["Access-Control-Allow-Origin"] = origin;
    headers["Vary"] = "Origin";
  }
  headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS";
  headers["Access-Control-Allow-Headers"] = "Content-Type";
  return headers;
}

// Build a JSON response with CORS + security headers applied.
export function jsonResponse(
  body: unknown,
  status: number,
  origin: string | null,
): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json",
      ...SECURITY_HEADERS,
      ...corsHeaders(origin),
    },
  });
}

// Preflight (OPTIONS) response.
export function preflight(origin: string | null): Response {
  return new Response(null, {
    status: 204,
    headers: {
      ...SECURITY_HEADERS,
      ...corsHeaders(origin),
    },
  });
}
