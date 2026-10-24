// OpenReason Protocol Validator API — Cloudflare Worker entrypoint.
// TypeScript port of api/main.py + api/routes.py. Stateless; rate limiting is a
// Cloudflare WAF rule (see worker/README.md), not application code.

import yaml from "js-yaml";

import { checkDocument } from "./check";
import { jsonResponse, preflight } from "./cors";
import { diffDocuments, DiffError } from "./diff";
import { openApiSpec, redocPage } from "./openapi";
import { validateDocument, type Doc } from "./validate";

const API_VERSION = "0.4.1";
const VALIDATOR_VERSION = "0.4.0";
const MAX_LEN = 1048576; // 1MB, matches pydantic max_length

function isObject(v: unknown): v is Record<string, unknown> {
  return v !== null && typeof v === "object" && !Array.isArray(v) && !(v instanceof Date);
}

function parseYaml(text: string): unknown {
  // js-yaml `load` is safe by default (no arbitrary object construction).
  return yaml.load(text);
}

export default {
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    const origin = request.headers.get("Origin");

    if (request.method === "OPTIONS") return preflight(origin);

    // --- GET routes ---
    if (request.method === "GET") {
      if (path === "/") {
        return jsonResponse(
          {
            name: "OpenReason Protocol Validator API",
            version: API_VERSION,
            orp_versions_supported: ["0.1", "0.2"],
            validator_version: VALIDATOR_VERSION,
            endpoints: {
              health: "/health",
              documentation: "/docs",
              validate: "/api/v1/validate",
              check: "/api/v1/check",
              diff: "/api/v1/diff",
            },
            repository: "https://gitlab.com/publicreason/orp",
          },
          200,
          origin,
        );
      }
      if (path === "/health") {
        return jsonResponse(
          { status: "ok", version: API_VERSION, validator_version: VALIDATOR_VERSION },
          200,
          origin,
        );
      }
      if (path === "/openapi.json") {
        return jsonResponse(openApiSpec, 200, origin);
      }
      if (path === "/docs" || path === "/redoc") {
        // Relaxed CSP so Redoc's CDN bundle can load (the strict API CSP would block it).
        return new Response(redocPage, {
          status: 200,
          headers: {
            "Content-Type": "text/html; charset=utf-8",
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
          },
        });
      }
    }

    // --- POST routes ---
    if (request.method === "POST") {
      let body: unknown;
      try {
        body = await request.json();
      } catch {
        return jsonResponse({ detail: "Invalid JSON request body" }, 422, origin);
      }
      if (!isObject(body)) {
        return jsonResponse({ detail: "Request body must be a JSON object" }, 422, origin);
      }

      if (path === "/api/v1/validate") return handleValidate(body, origin);
      if (path === "/api/v1/check") return handleCheck(body, origin);
      if (path === "/api/v1/diff") return handleDiff(body, origin);
    }

    return jsonResponse({ detail: "Not found" }, 404, origin);
  },
};

function handleValidate(body: Record<string, unknown>, origin: string | null): Response {
  const document = body.document;
  if (typeof document !== "string" || document.length < 1 || document.length > MAX_LEN) {
    return jsonResponse(
      { detail: "Field 'document' must be a string of length 1..1048576" },
      422,
      origin,
    );
  }

  let parsed: unknown;
  try {
    parsed = parseYaml(document);
  } catch (e) {
    return jsonResponse({ detail: `Invalid YAML/JSON: ${(e as Error).message}` }, 400, origin);
  }
  if (!isObject(parsed)) {
    return jsonResponse(
      { detail: "Document must be a YAML/JSON object (not array or scalar)" },
      400,
      origin,
    );
  }

  try {
    const doc = parsed as Doc;
    const result = validateDocument(doc);
    let metadata: Record<string, string> | null = null;
    if (result.valid) {
      metadata = {
        orp_version: String(doc.orp_version ?? "unknown"),
        document_id: String(doc.document_id ?? "unknown"),
        title: String(doc.title ?? "untitled"),
        domain: String(doc.domain ?? "unknown"),
      };
    }
    return jsonResponse(
      {
        valid: result.valid,
        compliance_level: result.compliance_level,
        layers_present: result.layers_present,
        errors: result.errors,
        warnings: result.warnings,
        metadata,
      },
      200,
      origin,
    );
  } catch (e) {
    return jsonResponse({ detail: `Validation error: ${(e as Error).message}` }, 500, origin);
  }
}

function handleCheck(body: Record<string, unknown>, origin: string | null): Response {
  const document = body.document;
  if (typeof document !== "string" || document.length < 1 || document.length > MAX_LEN) {
    return jsonResponse(
      { detail: "Field 'document' must be a string of length 1..1048576" },
      422,
      origin,
    );
  }

  let parsed: unknown;
  try {
    parsed = parseYaml(document);
  } catch (e) {
    return jsonResponse({ detail: `Invalid YAML/JSON: ${(e as Error).message}` }, 400, origin);
  }
  if (!isObject(parsed)) {
    return jsonResponse({ detail: "Document must be a YAML/JSON object" }, 400, origin);
  }

  try {
    const result = checkDocument(parsed as Doc);
    return jsonResponse(result, 200, origin);
  } catch (e) {
    return jsonResponse({ detail: `Check error: ${(e as Error).message}` }, 500, origin);
  }
}

function handleDiff(body: Record<string, unknown>, origin: string | null): Response {
  const d1 = body.document1;
  const d2 = body.document2;
  if (typeof d1 !== "string" || d1.length > MAX_LEN || typeof d2 !== "string" || d2.length > MAX_LEN) {
    return jsonResponse(
      { detail: "Fields 'document1' and 'document2' must be strings up to 1048576 chars" },
      422,
      origin,
    );
  }
  const includeMetadata = body.include_metadata === true;
  const layer = typeof body.layer === "string" ? body.layer : null;

  let p1: unknown;
  let p2: unknown;
  try {
    p1 = parseYaml(d1);
    p2 = parseYaml(d2);
  } catch (e) {
    return jsonResponse({ detail: `Invalid YAML/JSON: ${(e as Error).message}` }, 400, origin);
  }
  if (!isObject(p1) || !isObject(p2)) {
    return jsonResponse({ detail: "Both documents must be YAML/JSON objects" }, 400, origin);
  }

  try {
    const result = diffDocuments(p1 as Doc, p2 as Doc, includeMetadata, layer);
    return jsonResponse(result, 200, origin);
  } catch (e) {
    if (e instanceof DiffError) {
      return jsonResponse({ detail: e.message }, 400, origin);
    }
    return jsonResponse({ detail: `Diff error: ${(e as Error).message}` }, 500, origin);
  }
}
