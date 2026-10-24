import { useState, useEffect, useCallback } from 'react'
import demo from './attested-demo.json'

// Live proof section for the landing page: three things a visitor can actually do, right now.
//  1. Verify a signed ORP v0.3 passport in their own browser (Ed25519, offline) — then tamper and watch it fail.
//  2. Validate a real ORP document against the hosted REST API.
//  3. Use the shipped artifacts: PyPI (live version), GitHub, MCP config.

type Verdict = { valid: boolean; tier: string | null; computed_hash: string | null; errors: string[] }

const EXAMPLES = [
  { id: 'danish_property_tax_reform', label: 'Policy · full', hint: 'All five layers, prospective' },
  { id: 'github_copilot_training_data', label: 'AI training · post-hoc', hint: 'Reconstructed after the fact' },
  { id: 'minimal_basic', label: 'Minimal · L1 only', hint: 'What `orp new --compliance basic` gives you' },
  { id: 'broken_record', label: 'Broken', hint: 'Required fields deleted' },
]

const LAYERS: [string, string][] = [
  ['l1_data_provenance', 'L1 Provenance'],
  ['l2_consequence_simulation', 'L2 Consequence'],
  ['l3_empathy_mapping', 'L3 Empathy'],
  ['l4_accountability_ledger', 'L4 Accountability'],
  ['l5_fork_registry', 'L5 Lineage'],
]

const MCP_SNIPPET = `{
  "mcpServers": {
    "openreason": {
      "command": "node",
      "args": ["/path/to/openreason/mcp/dist/index.js"]
    }
  }
}`

function short(s: string | null | undefined, head = 18, tail = 8) {
  if (!s) return ''
  return s.length > head + tail + 1 ? `${s.slice(0, head)}…${s.slice(-tail)}` : s
}

export default function LiveProof() {
  // ---- 1. verify in browser ----
  const [doc, setDoc] = useState<Record<string, unknown>>(demo as Record<string, unknown>)
  const [tampered, setTampered] = useState(false)
  const [verdict, setVerdict] = useState<Verdict | null>(null)
  const [verifying, setVerifying] = useState(false)
  const [ms, setMs] = useState<number | null>(null)

  const verify = useCallback(async (d: Record<string, unknown>) => {
    setVerifying(true)
    const t0 = performance.now()
    try {
      const sdk = await import('@openreason/sdk')
      const r = await sdk.verifyAttestation(d, (kid: string) => kid)
      setVerdict({ valid: r.valid, tier: r.tier, computed_hash: r.computed_hash, errors: r.errors })
    } catch (e) {
      setVerdict({ valid: false, tier: null, computed_hash: null, errors: [String((e as Error).message)] })
    } finally {
      setMs(Math.round(performance.now() - t0))
      setVerifying(false)
    }
  }, [])

  const tamper = () => {
    const t = JSON.parse(JSON.stringify(demo)) as Record<string, unknown>
    const l1 = t.l1_data_provenance as Record<string, unknown>
    l1.known_exclusions = [] // quietly delete the admitted exclusion — the classic move
    setDoc(t); setTampered(true); setVerdict(null); setMs(null)
  }
  const restore = () => { setDoc(demo as Record<string, unknown>); setTampered(false); setVerdict(null); setMs(null) }

  const sig = (demo.attestation.signatures[0] as unknown) as { kid: string; alg: string; signed_at: string }

  // ---- 2. validate via API ----
  const [exampleId, setExampleId] = useState(EXAMPLES[0].id)
  const [apiResult, setApiResult] = useState<any>(null)
  const [apiErr, setApiErr] = useState<string | null>(null)
  const [apiBusy, setApiBusy] = useState(false)
  const [apiMs, setApiMs] = useState<number | null>(null)

  const validate = async () => {
    setApiBusy(true); setApiErr(null); setApiResult(null)
    const t0 = performance.now()
    try {
      const yaml = await (await fetch(`/examples/${exampleId}.yaml`)).text()
      const res = await fetch('https://api.publicreasonproject.org/api/v1/validate', {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ document: yaml }),
      })
      if (!res.ok) throw new Error(`API ${res.status}`)
      setApiResult(await res.json())
    } catch (e) {
      setApiErr((e as Error).message)
    } finally {
      setApiMs(Math.round(performance.now() - t0)); setApiBusy(false)
    }
  }

  // ---- 3. live PyPI version ----
  const [pypi, setPypi] = useState<string | null>(null)
  useEffect(() => {
    fetch('https://pypi.org/pypi/orp-validator/json').then(r => r.json()).then(j => setPypi(j?.info?.version ?? null)).catch(() => {})
  }, [])
  const [copied, setCopied] = useState(false)
  const copy = async () => { try { await navigator.clipboard.writeText(MCP_SNIPPET); setCopied(true); setTimeout(() => setCopied(false), 1600) } catch {} }

  return (
    <div className="pr-live">
      {/* 1 — verify in your browser */}
      <div className="pr-live-card">
        <div className="pr-live-head">
          <span className="pr-k">In your browser · offline</span>
          <h3>Verify a signed passport</h3>
          <p>A real ORP v0.3 document, signed with Ed25519. Your browser recomputes the canonical hash and checks the
          signature against the key in the <code>did:key</code>. No server is asked — and nothing is asked to trust us.</p>
        </div>
        <div className={`pr-live-doc ${tampered ? 'is-tampered' : ''}`}>
          <div className="pr-live-row"><span>document</span><b>{String((doc as any).title)}</b></div>
          <div className="pr-live-row"><span>known_exclusions</span>
            <b className={tampered ? 'is-changed' : ''}>{((doc as any).l1_data_provenance.known_exclusions as string[]).length
              ? (doc as any).l1_data_provenance.known_exclusions[0] : <i>— (removed)</i>}</b></div>
          <div className="pr-live-row"><span>signer</span><b title={sig.kid}>{short(sig.kid, 22, 6)}</b></div>
          <div className="pr-live-row"><span>claimed hash</span><b title={demo.attestation.hash}>{short(demo.attestation.hash, 22, 8)}</b></div>
        </div>
        <div className="pr-cta-row pr-live-actions">
          <button className="pr-btn primary" onClick={() => verify(doc)} disabled={verifying}>{verifying ? 'Verifying…' : 'Verify signature'}</button>
          {!tampered
            ? <button className="pr-btn" onClick={tamper}>Tamper with it</button>
            : <button className="pr-btn" onClick={restore}>Restore original</button>}
        </div>
        {verdict && (
          <div className={`pr-live-verdict ${verdict.valid ? 'ok' : 'bad'}`} role="status">
            <div className="pr-live-verdict-top">
              <b>{verdict.valid ? 'VERIFIED' : 'REJECTED'}</b>
              <span>{verdict.valid ? `trust tier: ${verdict.tier}` : 'signature does not cover this content'}{ms !== null ? ` · ${ms} ms` : ''}</span>
            </div>
            {verdict.valid
              ? <div className="pr-live-mono">computed {short(verdict.computed_hash, 22, 8)} = claimed</div>
              : <div className="pr-live-mono">{verdict.errors[0]?.split(':')[0]}{verdict.computed_hash ? ` — computed ${short(verdict.computed_hash, 14, 6)}` : ''}</div>}
          </div>
        )}
        <div className="pr-live-foot">Same result from <a href="/tools/python-api">Python</a>, the <a href="/tools/javascript-sdk">JS SDK</a> or an agent via <a href="/tools/mcp">MCP</a>.</div>
      </div>

      {/* 2 — validate against the API */}
      <div className="pr-live-card">
        <div className="pr-live-head">
          <span className="pr-k">Hosted API · live</span>
          <h3>Validate a real document</h3>
          <p>Four different documents — a full policy analysis, a post-hoc AI-training reconstruction, a bare minimum, and a
          broken one — sent to the public validator at <code>api.publicreasonproject.org</code>. The response is whatever the
          API says right now, and it should differ.</p>
        </div>
        <div className="pr-live-pick">
          {EXAMPLES.map(e => (
            <button key={e.id} title={e.hint} className={`pr-live-chip ${exampleId === e.id ? 'is-on' : ''}`} onClick={() => { setExampleId(e.id); setApiResult(null); setApiErr(null) }}>{e.label}</button>
          ))}
        </div>
        <div className="pr-cta-row pr-live-actions">
          <button className="pr-btn primary" onClick={validate} disabled={apiBusy}>{apiBusy ? 'Validating…' : 'POST /api/v1/validate'}</button>
          <a className="pr-btn" href="/tools/validator">Paste your own →</a>
        </div>
        {apiErr && <div className="pr-live-verdict bad"><div className="pr-live-verdict-top"><b>ERROR</b><span>{apiErr}</span></div></div>}
        {apiResult && (
          <div className={`pr-live-verdict ${apiResult.valid ? 'ok' : 'bad'}`} role="status">
            <div className="pr-live-verdict-top">
              <b>{apiResult.valid ? 'VALID' : 'INVALID'}</b>
              <span>{apiResult.compliance_level}{apiMs !== null ? ` · ${apiMs} ms` : ''}</span>
            </div>
            <div className="pr-live-layers">
              {LAYERS.map(([k, label]) => (
                <span key={k} className={`pr-live-layer ${apiResult.layers_present?.[k] ? 'is-on' : ''}`}>{label}</span>
              ))}
            </div>
            <div className="pr-live-mono">{apiResult.metadata?.title ? `“${apiResult.metadata.title}”` : 'untitled'}{apiResult.metadata?.domain ? ` · ${apiResult.metadata.domain}` : ''}{apiResult.metadata?.orp_version ? ` · v${apiResult.metadata.orp_version}` : ''}</div>
            {apiResult.errors?.length
              ? <div className="pr-live-mono">{apiResult.errors.length} error{apiResult.errors.length > 1 ? 's' : ''} — {apiResult.errors[0]}</div>
              : apiResult.warnings?.length
                ? <div className="pr-live-mono">{apiResult.warnings.length} warning{apiResult.warnings.length > 1 ? 's' : ''} — {String(apiResult.warnings[0]).slice(0, 110)}{String(apiResult.warnings[0]).length > 110 ? '…' : ''}</div>
                : <div className="pr-live-mono">0 warnings · 0 errors</div>}
          </div>
        )}
        <div className="pr-live-foot">Spec: <a href="/tools/rest-api">REST API</a> · validates v0.1 and v0.2 today; v0.3 profiles via the <a href="/tools/cli">CLI</a>.</div>
      </div>

      {/* 3 — use it */}
      <div className="pr-live-rail">
        <a className="pr-live-rail-item" href="https://pypi.org/project/orp-validator/">
          <span className="pr-k">PyPI</span>
          <code>pip install orp-validator</code>
          <em>{pypi ? `v${pypi} · live` : 'Python 3.9+'}</em>
        </a>
        <a className="pr-live-rail-item" href="https://github.com/openreasonprotocol/openreason">
          <span className="pr-k">Source</span>
          <code>openreasonprotocol/openreason</code>
          <em>Apache-2.0 · issues &amp; discussion</em>
        </a>
        <button className="pr-live-rail-item" onClick={copy}>
          <span className="pr-k">MCP server</span>
          <code>"openreason": {'{'} command … {'}'}</code>
          <em>{copied ? 'Copied' : 'Copy agent config'}</em>
        </button>
        <a className="pr-live-rail-item" href="/tools/javascript-sdk">
          <span className="pr-k">JavaScript</span>
          <code>@openreason/sdk</code>
          <em>Node + browser · npm coming</em>
        </a>
      </div>
    </div>
  )
}
