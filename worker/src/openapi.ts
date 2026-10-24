// Static OpenAPI 3.0 spec + Redoc page, replacing FastAPI's auto-generated docs.

export const openApiSpec = {
  openapi: "3.0.3",
  info: {
    title: "OpenReason Protocol Validator API",
    description:
      "REST API for validating OpenReason Protocol (ORP) documents. " +
      "Supports ORP v0.1 (backward compatible) and v0.2 (post-hoc reconstruction, " +
      "extensions, flexible schema).",
    version: "0.4.1",
  },
  servers: [{ url: "https://api.publicreasonproject.org" }],
  paths: {
    "/": { get: { summary: "API information", responses: { "200": { description: "OK" } } } },
    "/health": { get: { summary: "Health check", responses: { "200": { description: "OK" } } } },
    "/api/v1/validate": {
      post: {
        summary: "Validate ORP document",
        description: "Full JSON Schema validation with errors, warnings, compliance level.",
        requestBody: {
          required: true,
          content: {
            "application/json": {
              schema: {
                type: "object",
                required: ["document"],
                properties: { document: { type: "string", maxLength: 1048576 } },
              },
            },
          },
        },
        responses: {
          "200": { description: "Validation completed" },
          "400": { description: "Invalid YAML/JSON" },
          "413": { description: "Request too large (>1MB)" },
          "429": { description: "Rate limit exceeded" },
        },
      },
    },
    "/api/v1/check": {
      post: {
        summary: "Quick compliance check",
        requestBody: {
          required: true,
          content: {
            "application/json": {
              schema: {
                type: "object",
                required: ["document"],
                properties: { document: { type: "string", maxLength: 1048576 } },
              },
            },
          },
        },
        responses: {
          "200": { description: "Compliance check completed" },
          "400": { description: "Invalid YAML/JSON" },
          "429": { description: "Rate limit exceeded" },
        },
      },
    },
    "/api/v1/diff": {
      post: {
        summary: "Compare two ORP documents",
        requestBody: {
          required: true,
          content: {
            "application/json": {
              schema: {
                type: "object",
                required: ["document1", "document2"],
                properties: {
                  document1: { type: "string", maxLength: 1048576 },
                  document2: { type: "string", maxLength: 1048576 },
                  include_metadata: { type: "boolean", default: false },
                  layer: { type: "string", nullable: true },
                },
              },
            },
          },
        },
        responses: {
          "200": { description: "Comparison completed" },
          "400": { description: "Invalid documents" },
          "429": { description: "Rate limit exceeded" },
        },
      },
    },
  },
} as const;

export const redocPage = `<!doctype html>
<html>
  <head>
    <title>OpenReason Validator API</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>body { margin: 0; padding: 0; }</style>
  </head>
  <body>
    <redoc spec-url="/openapi.json"></redoc>
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
  </body>
</html>`;
