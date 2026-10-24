// Port of the /api/v1/check handler in api/routes.py.
// IMPORTANT: the check endpoint has its OWN _determine_compliance, which differs
// from validator.py (post-hoc short-circuits to ORP-PostHoc as soon as L1 exists).
// Ported verbatim to preserve identical behaviour.

import { detectLayers, type Doc, type LayersPresent } from "./validate";

export interface CheckResult {
  compliance_level: string;
  layers_present: LayersPresent;
  next_steps: string;
}

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

function determineCompliance(doc: Doc, layers: LayersPresent): string {
  const hasHeader = REQUIRED_HEADER.every((f) => f in doc);
  if (!hasHeader) return "Non-compliant";

  const isPostHoc = Boolean(doc.post_hoc);
  if (isPostHoc && layers.l1_data_provenance) return "ORP-PostHoc";

  if (
    layers.l1_data_provenance &&
    layers.l2_consequence_simulation &&
    layers.l3_empathy_mapping &&
    layers.l4_accountability_ledger &&
    layers.l5_fork_registry
  ) {
    return "ORP-Full";
  }
  if (
    layers.l1_data_provenance &&
    layers.l2_consequence_simulation &&
    layers.l3_empathy_mapping
  ) {
    return "ORP-Standard";
  }
  if (layers.l1_data_provenance) return "ORP-Basic";

  return "Non-compliant";
}

function getNextSteps(level: string): string {
  switch (level) {
    case "ORP-PostHoc":
      return "Post-hoc reconstruction document. Consider adding L2-L5 for comprehensive analysis.";
    case "ORP-Basic":
      return "To reach ORP-Standard, add L2 (Consequence Simulation) and L3 (Empathy Mapping)";
    case "ORP-Standard":
      return "To reach ORP-Full, add L4 (Accountability Ledger) and L5 (Fork Registry)";
    case "ORP-Full":
      return "Full compliance achieved!";
    default:
      return "Add L1 (Data Provenance) to achieve ORP-Basic compliance";
  }
}

export function checkDocument(doc: Doc): CheckResult {
  const layers = detectLayers(doc);
  const level = determineCompliance(doc, layers);
  return {
    compliance_level: level,
    layers_present: layers,
    next_steps: getNextSteps(level),
  };
}
