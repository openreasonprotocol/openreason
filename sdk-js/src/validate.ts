// Faithful TypeScript port of orp_validator/validator.py (ORPValidator.validate).
//
// Parity notes vs. the Python reference:
//  - Python's Draft7Validator does NOT enforce `format` by default, so ajv is
//    configured with validateFormats:false to match (dates etc. are annotations).
//  - exact error STRINGS from ajv differ cosmetically from jsonschema, but the
//    structural result (valid / compliance_level / layers_present) is identical.
//  - compliance + warnings logic is ported line-for-line from validator.py.

import Ajv, { type ErrorObject, type ValidateFunction } from "ajv";

import schemaV01 from "./schemas/orp-v0.1.schema.json" with { type: "json" };
import schemaV02 from "./schemas/orp-v0.2.schema.json" with { type: "json" };

export type Doc = Record<string, unknown>;

export interface LayersPresent {
  l1_data_provenance: boolean;
  l2_consequence_simulation: boolean;
  l3_empathy_mapping: boolean;
  l4_accountability_ledger: boolean;
  l5_fork_registry: boolean;
}

export interface ValidationResult {
  valid: boolean;
  compliance_level: string;
  layers_present: LayersPresent;
  errors: string[];
  warnings: string[];
}

// Compliance level values (match ComplianceLevel enum in validator.py).
const FULL = "ORP-Full";
const STANDARD = "ORP-Standard";
const BASIC = "ORP-Basic";
const POSTHOC = "ORP-PostHoc";
const NONE = "Non-compliant";

// Compile both schemas once at module load. Draft-07; formats disabled for parity.
const ajv = new (Ajv as any)({ allErrors: true, strict: false, validateFormats: false });
const validators: Record<string, ValidateFunction> = {
  "0.1": ajv.compile(schemaV01 as object),
  "0.2": ajv.compile(schemaV02 as object),
};

const REQUIRED_HEADER = [
  "orp_version",
  "document_id",
  "title",
  "domain",
  "authors",
  "created",
  "last_modified",
  "status",
  "summary",
];

export function detectLayers(doc: Doc): LayersPresent {
  return {
    l1_data_provenance: "l1_data_provenance" in doc,
    l2_consequence_simulation: "l2_consequence_simulation" in doc,
    l3_empathy_mapping: "l3_empathy_mapping" in doc,
    l4_accountability_ledger: "l4_accountability_ledger" in doc,
    l5_fork_registry: "l5_fork_registry" in doc,
  };
}

// Port of validator.py::_determine_compliance (NOTE: differs from the check
// endpoint's own _determine_compliance in routes.py — kept separate on purpose).
function determineCompliance(doc: Doc, layers: LayersPresent): string {
  const hasHeader = REQUIRED_HEADER.every((f) => f in doc);
  if (!hasHeader) return NONE;

  const isPostHoc = Boolean(doc.post_hoc);

  if (
    layers.l1_data_provenance &&
    layers.l2_consequence_simulation &&
    layers.l3_empathy_mapping &&
    layers.l4_accountability_ledger &&
    layers.l5_fork_registry
  ) {
    return isPostHoc ? POSTHOC : FULL;
  }
  if (
    layers.l1_data_provenance &&
    layers.l2_consequence_simulation &&
    layers.l3_empathy_mapping
  ) {
    return isPostHoc ? POSTHOC : STANDARD;
  }
  if (layers.l1_data_provenance) {
    return isPostHoc ? POSTHOC : BASIC;
  }
  return NONE;
}

// Port of validator.py::_generate_warnings.
function generateWarnings(
  doc: Doc,
  layers: LayersPresent,
  compliance: string,
  version: string,
  extensionsLoaded: string[],
): string[] {
  const warnings: string[] = [];

  if ("compliance_level" in doc) {
    const declared = doc.compliance_level;
    if (declared !== compliance && compliance !== NONE) {
      warnings.push(
        `Declared compliance level '${declared}' does not match detected level '${compliance}'`,
      );
    }
  }

  // String comparison, matching Python `self.version >= "0.2"`.
  if (version >= "0.2" && extensionsLoaded.length > 0) {
    warnings.push(
      `Extensions declared: ${extensionsLoaded.join(", ")}. ` +
        "Note: Extension validation is informational only in current version.",
    );
  }

  const isPostHoc = Boolean(doc.post_hoc);
  if (isPostHoc && layers.l4_accountability_ledger) {
    const l4 = doc.l4_accountability_ledger;
    let hasGap = false;
    if (Array.isArray(l4)) {
      hasGap = l4.some(
        (d) => d && typeof d === "object" && "accountability_gap" in d,
      );
    } else if (l4 && typeof l4 === "object") {
      hasGap = "accountability_gap" in l4;
    }
    if (!hasGap) {
      warnings.push(
        "Post-hoc reconstruction should document 'accountability_gap' in L4 " +
          "to explain what decision-making history is unknowable.",
      );
    }
  }

  if (compliance === BASIC || compliance === POSTHOC) {
    if (compliance === BASIC) {
      warnings.push(
        "Document is ORP-Basic. Add L2 (Consequence Simulation) and " +
          "L3 (Empathy Mapping) for ORP-Standard.",
      );
    }
  } else if (compliance === STANDARD) {
    warnings.push(
      "Document is ORP-Standard. Add L4 (Accountability Ledger) and " +
        "L5 (Fork Registry) for ORP-Full.",
    );
  }

  return warnings;
}

// Port of validator.py::_format_error, mapping ajv ErrorObject -> message.
function formatError(err: ErrorObject): string {
  const path =
    err.instancePath === ""
      ? "root"
      : err.instancePath.slice(1).replace(/\//g, ".").replace(/~1/g, "/").replace(/~0/g, "~");

  switch (err.keyword) {
    case "required": {
      const missing = (err.params as { missingProperty: string }).missingProperty;
      return `Missing required field '${missing}' at ${path}`;
    }
    case "type": {
      const expected = (err.params as { type: string }).type;
      return `Field '${path}' has wrong type (expected ${expected})`;
    }
    case "enum": {
      const allowed = (err.params as { allowedValues: unknown[] }).allowedValues;
      return `Field '${path}' must be one of: ${JSON.stringify(allowed)}`;
    }
    case "minLength":
      return `Field '${path}' is too short or empty`;
    case "minItems": {
      const limit = (err.params as { limit: number }).limit;
      return `Array '${path}' must have at least ${limit} items`;
    }
    default:
      return `Validation error at '${path}': ${err.message ?? "invalid"}`;
  }
}

export function validateDocument(doc: Doc): ValidationResult {
  const version = typeof doc.orp_version === "string" ? doc.orp_version : "0.1";
  const validator = validators[version];
  if (!validator) {
    // Mirrors Python raising FileNotFoundError for an unknown schema version.
    throw new Error(`No bundled schema for ORP version '${version}'`);
  }

  const extensionsLoaded = Array.isArray(doc.extensions)
    ? (doc.extensions as string[])
    : [];

  const layers = detectLayers(doc);

  validator(doc);
  const errors = (validator.errors ?? []).map(formatError);

  const compliance = determineCompliance(doc, layers);
  const warnings = generateWarnings(
    doc,
    layers,
    compliance,
    version,
    extensionsLoaded,
  );

  return {
    valid: errors.length === 0,
    compliance_level: compliance,
    layers_present: layers,
    errors,
    warnings,
  };
}
