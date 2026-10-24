// Parity harness: run the bundled Worker against example docs and dump JSON
// outputs to /tmp/worker-*.json, so they can be compared to the Python validator.
import { readFileSync } from "node:fs";
import worker from "../dist/index.js";

const EX = "../../examples";
const files = {
  danish: `${EX}/danish_property_tax_reform.yaml`,
  imagenet: `${EX}/imagenet_training_data.yaml`,
  laion: `${EX}/laion5b_training_data.yaml`,
};
const read = (p) => readFileSync(new URL(p, import.meta.url), "utf8");

async function call(path, payload, method = "POST") {
  const req = new Request(`https://api.publicreasonproject.org${path}`, {
    method,
    headers: { "Content-Type": "application/json", Origin: "https://docs.publicreasonproject.org" },
    body: method === "POST" ? JSON.stringify(payload) : undefined,
  });
  const res = await worker.fetch(req);
  const text = await res.text();
  let json;
  try { json = JSON.parse(text); } catch { json = text; }
  return { status: res.status, cors: res.headers.get("access-control-allow-origin"), json };
}

const out = {};

// health + root
out.health = await call("/health", null, "GET");
out.root = await call("/", null, "GET");

// validate each example
for (const [name, path] of Object.entries(files)) {
  out[`validate_${name}`] = await call("/api/v1/validate", { document: read(path) });
  out[`check_${name}`] = await call("/api/v1/check", { document: read(path) });
}

// diff: danish vs imagenet (different docs)
out.diff_d_vs_i = await call("/api/v1/diff", {
  document1: read(files.danish),
  document2: read(files.imagenet),
});
// diff: identical
out.diff_identical = await call("/api/v1/diff", {
  document1: read(files.danish),
  document2: read(files.danish),
});

// error cases
out.bad_yaml = await call("/api/v1/validate", { document: "key: : : bad" });
out.scalar = await call("/api/v1/validate", { document: "just a string" });
out.missing_field = await call("/api/v1/validate", {});
out.preflight = await call("/api/v1/validate", null, "OPTIONS");

console.log(JSON.stringify(out, null, 2));
