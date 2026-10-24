import { useState, useEffect, useCallback, useRef, type ReactNode } from 'react'

type Kind = 'opaque' | 'vanish' | 'stack' | 'locate' | 'seal' | 'fork'
type Slide = { tone: 'accent' | 'dark'; m: Kind; text: ReactNode; sub?: string }

const ACT: Record<Kind, string> = {
  opaque: 'The problem',
  vanish: 'Machines decide',
  stack: 'OpenReason',
  locate: 'In the open',
  seal: 'For machines',
  fork: 'Open',
}

const SLIDES: Slide[] = [
  { tone: 'accent', m: 'opaque', text: <>Someone just made a decision that affects <u>you</u>.</>, sub: 'Do you know how they got there?' },
  { tone: 'dark', m: 'opaque', text: <>A policy. A ruling. A model’s output.</>, sub: 'You live with the result either way.' },
  { tone: 'dark', m: 'opaque', text: <>You’re told to <b>trust it</b>.</>, sub: 'You’re rarely shown the reasoning.' },
  { tone: 'dark', m: 'opaque', text: <>Not the <b>data</b> it rested on.</>, sub: 'Was it complete? Was it current? Where did it come from?' },
  { tone: 'dark', m: 'opaque', text: <>Not the <b>assumptions</b> inside it.</>, sub: 'Change one, and the answer can change with it.' },
  { tone: 'dark', m: 'opaque', text: <>Not <b>who it leaves worse off</b>.</>, sub: 'Every decision has a cost. Someone carries it.' },
  { tone: 'dark', m: 'opaque', text: <>So we stop asking “is this right?” and start asking “who do we believe?”</>, sub: 'Trust becomes a contest of authority — not of reasoning.' },
  { tone: 'dark', m: 'vanish', text: <>And the deciders aren’t only people anymore.</>, sub: 'Machines reason too — and act on it.' },
  { tone: 'dark', m: 'vanish', text: <>An AI weighs the options, picks one, and <b>moves</b>.</>, sub: 'Faster than anyone can audit in the moment.' },
  { tone: 'dark', m: 'vanish', text: <>When it’s wrong, the reasoning is already <b>gone</b>.</>, sub: 'No record. No way to retrace the step.' },
  { tone: 'dark', m: 'vanish', text: <>We’ve made reasoning <b>invisible</b> —</>, sub: 'exactly when it matters most.' },
  { tone: 'accent', m: 'stack', text: <>It doesn’t have to be.</>, sub: 'Reasoning can be written down — in the open.' },
  { tone: 'dark', m: 'stack', text: <>That’s <b>OpenReason</b>.</>, sub: 'An open standard for the reasoning behind a decision.' },
  { tone: 'dark', m: 'stack', text: <>The <b>sources</b> it drew on.</>, sub: 'Cited, not asserted.' },
  { tone: 'dark', m: 'stack', text: <>The <b>assumptions</b> it made.</>, sub: 'Named, so you can test them.' },
  { tone: 'dark', m: 'stack', text: <>The <b>trade-offs</b> it accepted.</>, sub: 'Visible, not buried.' },
  { tone: 'dark', m: 'stack', text: <>Not a summary written afterward.</>, sub: 'The actual structure — readable by anyone.' },
  { tone: 'dark', m: 'locate', text: <>Now you can <b>check it yourself</b>.</>, sub: 'Re-run it with your own assumptions.' },
  { tone: 'dark', m: 'locate', text: <>Disagreement gets an <b>address</b>.</>, sub: 'Point to the exact line you’d change.' },
  { tone: 'dark', m: 'seal', text: <>And because it’s structured, a <b>machine can read it too</b>.</>, sub: 'Not as text to interpret — as reasoning to check.' },
  { tone: 'dark', m: 'seal', text: <>An agent <b>verifies it itself</b> — offline, in milliseconds.</>, sub: 'Trusting the signed proof, not whoever sent it.' },
  { tone: 'dark', m: 'seal', text: <>It reads <b>how far to trust it</b>.</>, sub: 'Self-declared, attested, verified — the trust tier travels with the reasoning.' },
  { tone: 'dark', m: 'seal', text: <>It honors what the data <b>allows</b> — and proves what it did.</>, sub: 'Usage rules ride along; every use leaves a receipt.' },
  { tone: 'dark', m: 'seal', text: <>So agents can act on each other’s reasoning <b>without blind trust</b>.</>, sub: 'The openness that works for people works for machines.' },
  { tone: 'dark', m: 'fork', text: <>Reasoning you can <b>verify</b> —</>, sub: 'by people and machines.' },
  { tone: 'accent', m: 'fork', text: <>Open. Free. Built to be <b>forked</b>.</>, sub: 'The Public Reason Project.' },
]

const pad = (n: number) => String(n).padStart(2, '0')

const LAYERS: [string, string][] = [
  ['L1', 'Provenance'],
  ['L2', 'Consequence'],
  ['L3', 'Empathy'],
  ['L4', 'Accountability'],
  ['L5', 'Lineage'],
]

const Check = (
  <svg viewBox="0 0 10 10" aria-hidden="true">
    <path d="M2 5.2 L4.3 7.4 L8 3.2" fill="none" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
)

function Motif({ kind }: { kind: Kind }) {
  if (kind === 'opaque' || kind === 'vanish') {
    const vanish = kind === 'vanish'
    return (
      <div className={`pr-motif ${vanish ? 'is-vanish' : 'is-opaque'}`} aria-hidden="true">
        <div className="pr-motif-head"><span>{vanish ? 'ORP · gone' : 'ORP · sealed'}</span><span className="pr-motif-glyph">{vanish ? '⟿' : '▢'}</span></div>
        <div className="pr-motif-bars">
          {[92, 74, 84, 60, 78].map((w, k) => (
            <span key={k} className="pr-motif-bar" style={{ width: `${w}%`, animationDelay: `${k * 0.11}s` }} />
          ))}
        </div>
        <div className="pr-motif-foot">{vanish ? 'already gone' : 'reasoning hidden'}</div>
      </div>
    )
  }

  if (kind === 'stack' || kind === 'locate') {
    const locate = kind === 'locate'
    return (
      <div className="pr-motif is-stack" aria-hidden="true">
        <div className="pr-motif-head"><span>ORP · object</span><span className="pr-dot" /></div>
        <div className="pr-motif-layers">
          {LAYERS.map(([n, label], k) => (
            <div key={k} className={`pr-motif-layer${locate && k === 1 ? ' is-mark' : ''}`} style={{ animationDelay: `${k * 0.09}s` }}>
              <b>{n}</b><span>{label}</span>
              <i className="pr-motif-ck" style={{ animationDelay: `${k * 0.09 + 0.28}s` }}>{Check}</i>
            </div>
          ))}
        </div>
        {locate
          ? <div className="pr-motif-foot is-addr">▸ L2 · consequence</div>
          : <div className="pr-motif-chip">⬡ attested</div>}
      </div>
    )
  }

  if (kind === 'seal') {
    return (
      <div className="pr-motif is-seal" aria-hidden="true">
        <div className="pr-motif-head"><span>ORP · verify</span><span className="pr-dot" /></div>
        <div className="pr-motif-sealart">
          <svg viewBox="0 0 120 120">
            <polygon className="pr-seal-hex" points="60,10 103,35 103,85 60,110 17,85 17,35" fill="none" strokeWidth="2.4" strokeLinejoin="round" />
            <path className="pr-seal-ck" d="M40 60 L54 74 L82 44" fill="none" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </div>
        <div className="pr-motif-chip">⬡ verified · offline</div>
      </div>
    )
  }

  // fork
  return (
    <div className="pr-motif is-fork" aria-hidden="true">
      <div className="pr-motif-head"><span>ORP · fork</span><span className="pr-dot" /></div>
      <div className="pr-motif-sealart">
        <svg viewBox="0 0 140 120">
          <polygon className="pr-fork-a" points="38,20 60,32 60,58 38,70 16,58 16,32" fill="none" strokeWidth="2.4" strokeLinejoin="round" />
          <path className="pr-fork-line" d="M60 45 H86 M86 45 V78" fill="none" strokeWidth="2.2" strokeLinecap="round" />
          <polygon className="pr-fork-b" points="104,60 122,70 122,92 104,102 86,92 86,70" fill="none" strokeWidth="2.4" strokeLinejoin="round" />
        </svg>
      </div>
      <div className="pr-motif-chip">fork · re-run</div>
    </div>
  )
}

const Icon = {
  expand: (<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M8 3H3v5" /><path d="M21 8V3h-5" /><path d="M16 21h5v-5" /><path d="M3 16v5h5" /></svg>),
  collapse: (<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M8 3v5H3" /><path d="M16 3v5h5" /><path d="M8 21v-5H3" /><path d="M16 21v-5h5" /></svg>),
  share: (<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><circle cx="18" cy="5" r="3" /><circle cx="6" cy="12" r="3" /><circle cx="18" cy="19" r="3" /><path d="M8.6 10.5l6.8-4M8.6 13.5l6.8 4" /></svg>),
  embed: (<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M8 6l-5 6 5 6" /><path d="M16 6l5 6-5 6" /></svg>),
}

export default function Story({ embed = false }: { embed?: boolean }) {
  const [i, setI] = useState<number>(0)
  const [paused, setPaused] = useState<boolean>(false)
  const [full, setFull] = useState<boolean>(false)
  const [toast, setToast] = useState<string>('')
  const toastT = useRef<ReturnType<typeof setTimeout> | null>(null)
  const fillRef = useRef<HTMLSpanElement | null>(null)
  const progRef = useRef<number>(0)

  const next = useCallback(() => setI((x) => (x + 1) % SLIDES.length), [])
  const prev = useCallback(() => setI((x) => (x - 1 + SLIDES.length) % SLIDES.length), [])

  const flash = useCallback((msg: string) => {
    setToast(msg)
    if (toastT.current) clearTimeout(toastT.current)
    toastT.current = setTimeout(() => setToast(''), 2200)
  }, [])

  // Reset per-slide progress whenever the slide changes.
  useEffect(() => { progRef.current = 0 }, [i])

  // Drive the progress bar continuously across each slide (8s), then advance.
  // Running the fill off a rAF loop (not a one-shot transition) makes it visibly
  // "tick" the whole time, so you can always tell it's playing. Freezes on pause.
  useEffect(() => {
    if (paused && !full) return
    const DUR = 8000
    const base = i / SLIDES.length
    const span = 1 / SLIDES.length
    let raf = 0
    let start: number | null = null
    const step = (ts: number) => {
      if (start === null) start = ts - progRef.current * DUR
      const p = Math.min(1, (ts - start) / DUR)
      progRef.current = p
      if (fillRef.current) fillRef.current.style.width = `${(base + span * p) * 100}%`
      if (p >= 1) { next(); return }
      raf = requestAnimationFrame(step)
    }
    raf = requestAnimationFrame(step)
    return () => cancelAnimationFrame(raf)
  }, [paused, full, i, next])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'ArrowRight') next()
      else if (e.key === 'ArrowLeft') prev()
      else if (e.key === 'Escape' && full) setFull(false)
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [next, prev, full])

  const origin = typeof window !== 'undefined' ? window.location.origin : 'https://docs.publicreasonproject.org'

  const share = useCallback(async () => {
    const url = `${origin}/story`
    const data = { title: 'The OpenReason story', text: 'Reasoning you can verify — by people and machines.', url }
    try {
      if (typeof navigator !== 'undefined' && (navigator as Navigator).share) {
        await (navigator as Navigator).share(data)
        return
      }
    } catch {
      /* cancelled / unsupported — fall through to copy */
    }
    try {
      await navigator.clipboard.writeText(url)
      flash('Link copied')
    } catch {
      flash(url)
    }
  }, [origin, flash])

  const copyEmbed = useCallback(async () => {
    const code = `<iframe src="${origin}/embed" width="100%" height="640" style="border:0;border-radius:14px" title="The OpenReason story" loading="lazy" allow="fullscreen"></iframe>`
    try {
      await navigator.clipboard.writeText(code)
      flash('Embed code copied')
    } catch {
      flash('Copy failed')
    }
  }, [origin, flash])

  const seek = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
    const r = e.currentTarget.getBoundingClientRect()
    const frac = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width))
    setI(Math.min(SLIDES.length - 1, Math.floor(frac * SLIDES.length)))
  }, [])

  const s = SLIDES[i]
  const cls = ['pr-story', s.tone === 'accent' ? 'is-accent' : '', full ? 'is-full' : '', embed ? 'is-embed' : '']
    .filter(Boolean)
    .join(' ')

  return (
    <div className={cls} onMouseEnter={() => setPaused(true)} onMouseLeave={() => setPaused(false)}>
      <div className="pr-story-top">
        <span>{ACT[s.m]}</span>
        <span>{pad(i + 1)} / {pad(SLIDES.length)}</span>
      </div>

      <div className="pr-story-body">
        <div className="pr-story-copy" key={i}>
          <p className="pr-story-text">{s.text}</p>
          {s.sub ? <p className="pr-story-sub">{s.sub}</p> : null}
        </div>
        <div className="pr-story-motif-wrap">
          {/* Draw-based motifs (seal/fork) re-key per slide so they redraw each
              time; the assembling ones persist across their act to stay calm. */}
          <Motif kind={s.m} key={s.m === 'seal' || s.m === 'fork' ? `${s.m}-${i}` : s.m} />
        </div>
      </div>

      <div className="pr-story-ctrl">
        <div className="pr-story-progress" onClick={seek} role="progressbar" aria-valuenow={i + 1} aria-valuemin={1} aria-valuemax={SLIDES.length}>
          <span ref={fillRef} className="pr-story-progress-fill" style={{ width: `${(i / SLIDES.length) * 100}%` }} />
        </div>

        <div className="pr-story-tools">
          {!embed && (
            <>
              <button className="pr-story-tool" aria-label="Share the story" title="Share" onClick={share}>{Icon.share}</button>
              <button className="pr-story-tool" aria-label="Copy embed code" title="Embed" onClick={copyEmbed}>{Icon.embed}</button>
            </>
          )}
          <button
            className="pr-story-tool"
            aria-label={full ? 'Exit fullscreen' : 'Expand to fullscreen'}
            title={full ? 'Exit fullscreen' : 'Fullscreen'}
            onClick={() => setFull((v) => !v)}
          >
            {full ? Icon.collapse : Icon.expand}
          </button>
        </div>
      </div>

      {embed && (
        <a className="pr-story-mark" href={`${origin}/story`} target="_blank" rel="noopener noreferrer">
          publicreasonproject.org
        </a>
      )}

      {toast && <div className="pr-story-toast" role="status">{toast}</div>}
    </div>
  )
}
