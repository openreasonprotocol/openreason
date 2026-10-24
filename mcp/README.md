# @openreason/mcp

A [Model Context Protocol](https://modelcontextprotocol.io) server that gives any AI agent native [OpenReason Protocol](https://openreasonprotocol.org) capabilities: validate an ORP document, verify its cryptographic attestation offline, and explain the protocol. Wraps `@openreason/sdk`, speaks stdio.

```bash
npx @openreason/mcp
```

Claude Desktop / Claude Code / Cursor configuration:

```json
{
  "mcpServers": {
    "openreason": { "command": "npx", "args": ["-y", "@openreason/mcp"] }
  }
}
```

Tools: `orp_validate` (compliance level + layers), `orp_verify_attestation` (offline Ed25519 verify, trust tier, per-signature verdict; unknown keys fail closed), `orp_explain` (overview, layers, trust-tiers, attestation, compliance).

Docs: https://openreasonprotocol.org/tools/mcp · Source: https://github.com/openreasonprotocol/openreason/tree/main/mcp · Apache-2.0
