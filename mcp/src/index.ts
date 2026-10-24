#!/usr/bin/env node
// OpenReason MCP server — gives any AI agent native ORP capabilities:
// validate a document, verify its cryptographic attestation (offline), and
// explain the protocol. Wraps @openreason/sdk. Transport: stdio.

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import yaml from "js-yaml";
import {
  validateDocument,
  checkDocument,
  verifyAttestation,
  type ResolveKey,
  type KeyMaterial,
} from "@openreason/sdk";

type Doc = Record<string, unknown>;

function parseDoc(input: string): Doc {
  const trimmed = input.trim();
  if (trimmed.startsWith("{")) return JSON.parse(trimmed) as Doc;
  return yaml.load(trimmed) as Doc; // YAML is a superset of JSON
}

const EXPLAIN: Record<string, string> = {
  overview:
    "OpenReason Protocol (ORP) turns the reasoning behind a decision into a structured, inspectable, " +
    "verifiable object. It never dictates conclusions — it exposes the reasoning so it can be checked. " +
    "Five layers: L1 Data Provenance, L2 Consequence Simulation, L3 Empathy Mapping, L4 Accountability " +
    "Ledger, L5 Fork Registry.",
  layers:
    "L1 Data Provenance — where the data came from, funding, exclusions, limitations. " +
    "L2 Consequence Simulation — modelled outcomes under stated assumptions. " +
    "L3 Empathy Mapping — who is affected, including those absent from the data. " +
    "L4 Accountability Ledger — who decided what, when, why. " +
    "L5 Fork Registry — alternative assumptions and what they produce.",
  "trust-tiers":
    "A verified ORP document carries a trust tier that never exceeds what the signatures prove: " +
    "self_declared → attested → verified → full (plus posthoc). A machine verifies the attestation " +
    "offline (recompute the hash, check the Ed25519 signature against a resolved key) and reads how far to trust it.",
  attestation:
    "An ORP v0.3 document can carry a detached Ed25519 attestation over the RFC 8785 (JCS) canonical bytes " +
    "of the document minus its own attestation block, hashed as sha256:<hex>. Verification is offline and " +
    "needs no contact with the publisher — only the public key (via did:key or JWK).",
  compliance:
    "Validation yields a compliance level: ORP-Basic (L1), ORP-Standard (L1+L2+L4), ORP-Full (all five layers), " +
    "or ORP-PostHoc. Non-compliant documents fail the header/schema checks.",
};

const server = new McpServer({ name: "openreason", version: "0.1.0" });

server.tool(
  "orp_validate",
  "Validate an OpenReason Protocol document (JSON or YAML). Returns its compliance level, which of the five layers are present, and any errors or warnings.",
  { document: z.string().describe("The ORP document as a JSON or YAML string.") },
  async ({ document }) => {
    try {
      const doc = parseDoc(document);
      const result = validateDocument(doc);
      const check = checkDocument(doc);
      return { content: [{ type: "text", text: JSON.stringify({ ...result, ...check }, null, 2) }] };
    } catch (e) {
      return { isError: true, content: [{ type: "text", text: `parse/validate error: ${(e as Error).message}` }] };
    }
  },
);

server.tool(
  "orp_verify_attestation",
  "Cryptographically verify an ORP v0.3 document's attestation offline: recompute the canonical hash and check the Ed25519 signatures. Returns validity, the trust tier, the computed hash, and a per-signature verdict.",
  {
    document: z.string().describe("The ORP document as a JSON or YAML string."),
    keys: z
      .record(z.string())
      .optional()
      .describe("Optional map of signature kid -> key material (a did:key, base64url raw key, or JWK x value). If a kid is itself a did:key it resolves without this map."),
  },
  async ({ document, keys }) => {
    try {
      const doc = parseDoc(document);
      const resolve: ResolveKey = (kid: string): KeyMaterial => {
        if (keys && kid in keys) return keys[kid];
        if (kid.startsWith("did:key:")) return kid; // self-describing public key
        throw new Error(`no key for kid ${kid}`);
      };
      const result = await verifyAttestation(doc, resolve);
      return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
    } catch (e) {
      return { isError: true, content: [{ type: "text", text: `verify error: ${(e as Error).message}` }] };
    }
  },
);

server.tool(
  "orp_explain",
  "Explain a concept of the OpenReason Protocol in plain terms.",
  { topic: z.enum(["overview", "layers", "trust-tiers", "attestation", "compliance"]).describe("Which concept to explain.") },
  async ({ topic }) => ({ content: [{ type: "text", text: EXPLAIN[topic] ?? EXPLAIN.overview }] }),
);

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("openreason-mcp: ready on stdio (tools: orp_validate, orp_verify_attestation, orp_explain)");
