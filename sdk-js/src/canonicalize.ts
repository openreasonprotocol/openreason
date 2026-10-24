// RFC 8785 (JCS) canonical JSON — faithful port of orp_validator/attestation.py `_canon`.
// Produces the exact UTF-8 bytes the Python reference hashes and signs over, so a
// signature produced by the Python SDK verifies here and vice-versa.
//
// Note on key ordering: RFC 8785 sorts object keys by UTF-16 code units; JS's default
// String sort does exactly that. Python sorts by Unicode code point — identical for the
// BMP (all ORP keys are ASCII), diverging only for astral-plane key names (not used).

export type Json = null | boolean | number | string | Json[] | { [k: string]: Json };

function canonString(s: string): string {
  // JSON.stringify applies RFC 8785-compatible minimal escaping for strings.
  return JSON.stringify(s);
}

function canonNumber(n: number): string {
  if (!Number.isFinite(n)) {
    throw new Error("NaN and Infinity are not permitted in canonical JSON");
  }
  // ECMAScript Number->String (what JSON.stringify uses) is the RFC 8785 number form.
  return JSON.stringify(n);
}

function canon(obj: Json): string {
  if (obj === null) return "null";
  const t = typeof obj;
  if (t === "boolean") return obj ? "true" : "false";
  if (t === "number") return canonNumber(obj as number);
  if (t === "string") return canonString(obj as string);
  if (Array.isArray(obj)) return "[" + obj.map(canon).join(",") + "]";
  if (t === "object") {
    const o = obj as { [k: string]: Json };
    const keys = Object.keys(o).sort(); // UTF-16 code-unit order
    return "{" + keys.map((k) => canonString(k) + ":" + canon(o[k])).join(",") + "}";
  }
  throw new TypeError(`not JSON-serialisable for canonicalisation: ${t}`);
}

/** RFC 8785 canonical UTF-8 bytes of a JSON-compatible value. */
export function canonicalize(obj: unknown): Uint8Array {
  return new TextEncoder().encode(canon(obj as Json));
}

/** The canonical string form (debug / display). */
export function canonicalString(obj: unknown): string {
  return canon(obj as Json);
}
