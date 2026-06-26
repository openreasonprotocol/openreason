// Port of the /api/v1/diff handler + helpers in api/routes.py.

import yaml from "js-yaml";

import type { Doc } from "./validate";

export interface DiffChange {
  type: "added" | "removed" | "changed";
  field: string;
  old_value: string | null;
  new_value: string | null;
}

export interface DiffResult {
  identical: boolean;
  is_fork: boolean;
  fork_direction: string | null;
  differences: DiffChange[];
  num_changes: number;
}

export class DiffError extends Error {}

function isPlainObject(v: unknown): v is Record<string, unknown> {
  return (
    v !== null &&
    typeof v === "object" &&
    !Array.isArray(v) &&
    !(v instanceof Date)
  );
}

// Mirror Python's str()/yaml.dump for display values.
function serializeValue(value: unknown): string {
  if (isPlainObject(value) || Array.isArray(value)) {
    return yaml.dump(value, { flowLevel: 0 }).trim();
  }
  if (value === true) return "True";
  if (value === false) return "False";
  if (value === null || value === undefined) return "None";
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  return String(value);
}

function scalarsEqual(a: unknown, b: unknown): boolean {
  if (a instanceof Date && b instanceof Date) return a.getTime() === b.getTime();
  return a === b;
}

function compareDicts(
  d1: Record<string, unknown>,
  d2: Record<string, unknown>,
  prefix: string,
): DiffChange[] {
  const diffs: DiffChange[] = [];

  // Removed (in d1, not d2)
  for (const key of Object.keys(d1)) {
    if (!(key in d2)) {
      const field = prefix ? `${prefix}.${key}` : key;
      diffs.push({
        type: "removed",
        field,
        old_value: serializeValue(d1[key]),
        new_value: null,
      });
    }
  }

  // Added (in d2, not d1)
  for (const key of Object.keys(d2)) {
    if (!(key in d1)) {
      const field = prefix ? `${prefix}.${key}` : key;
      diffs.push({
        type: "added",
        field,
        old_value: null,
        new_value: serializeValue(d2[key]),
      });
    }
  }

  // Changed (common keys)
  for (const key of Object.keys(d1)) {
    if (!(key in d2)) continue;
    const field = prefix ? `${prefix}.${key}` : key;
    const v1 = d1[key];
    const v2 = d2[key];

    if (isPlainObject(v1) && isPlainObject(v2)) {
      diffs.push(...compareDicts(v1, v2, field));
    } else if (Array.isArray(v1) && Array.isArray(v2)) {
      diffs.push(...compareLists(v1, v2, field));
    } else if (!scalarsEqual(v1, v2)) {
      diffs.push({
        type: "changed",
        field,
        old_value: serializeValue(v1),
        new_value: serializeValue(v2),
      });
    }
  }

  return diffs;
}

function compareLists(l1: unknown[], l2: unknown[], prefix: string): DiffChange[] {
  const diffs: DiffChange[] = [];
  const maxLen = Math.max(l1.length, l2.length);

  for (let i = 0; i < maxLen; i++) {
    const field = `${prefix}[${i}]`;

    if (i >= l2.length) {
      diffs.push({
        type: "removed",
        field,
        old_value: serializeValue(l1[i]),
        new_value: null,
      });
    } else if (i >= l1.length) {
      diffs.push({
        type: "added",
        field,
        old_value: null,
        new_value: serializeValue(l2[i]),
      });
    } else {
      const v1 = l1[i];
      const v2 = l2[i];
      if (isPlainObject(v1) && isPlainObject(v2)) {
        diffs.push(...compareDicts(v1, v2, field));
      } else if (Array.isArray(v1) && Array.isArray(v2)) {
        diffs.push(...compareLists(v1, v2, field));
      } else if (!scalarsEqual(v1, v2)) {
        diffs.push({
          type: "changed",
          field,
          old_value: serializeValue(v1),
          new_value: serializeValue(v2),
        });
      }
    }
  }

  return diffs;
}

export function diffDocuments(
  doc1In: Doc,
  doc2In: Doc,
  includeMetadata: boolean,
  layer: string | null,
): DiffResult {
  // Shallow copies so we can prune without mutating callers.
  let doc1: Record<string, unknown> = { ...doc1In };
  let doc2: Record<string, unknown> = { ...doc2In };

  if (!includeMetadata) {
    for (const f of ["last_modified", "created"]) {
      delete doc1[f];
      delete doc2[f];
    }
  }

  if (layer) {
    if (!(layer in doc1) && !(layer in doc2)) {
      throw new DiffError(`Layer '${layer}' not found in either document`);
    }
    doc1 = { [layer]: layer in doc1 ? doc1[layer] : null };
    doc2 = { [layer]: layer in doc2 ? doc2[layer] : null };
  }

  // Fork detection (same order as Python: after layer filtering).
  let isFork = false;
  let forkDirection: string | null = null;
  if ("forked_from" in doc2) {
    if (doc1.document_id === doc2.forked_from) {
      isFork = true;
      forkDirection = "document2 forked from document1";
    }
  } else if ("forked_from" in doc1) {
    if (doc2.document_id === doc1.forked_from) {
      isFork = true;
      forkDirection = "document1 forked from document2";
    }
  }

  const differences = compareDicts(doc1, doc2, "");

  return {
    identical: differences.length === 0,
    is_fork: isFork,
    fork_direction: forkDirection,
    differences,
    num_changes: differences.length,
  };
}
