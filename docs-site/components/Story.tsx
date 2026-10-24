import { useState, useEffect, useCallback, type ReactNode } from 'react'

type Slide = { tone: 'accent' | 'dark'; n: string; text: ReactNode; sub?: string }

const SLIDES: Slide[] = [
  {
    tone: 'accent',
    n: '01',
    text: <>Big decisions rest on reasoning you <u>can’t see</u>.</>,
    sub: 'The data behind them. The assumptions inside them. Who they affect.',
  },
  {
    tone: 'dark',
    n: '02',
    text: <>So we argue about <b>who to trust</b> — instead of what’s true.</>,
  },
  {
    tone: 'dark',
    n: '03',
    text: <>OpenReason makes the reasoning an <b>object</b>.</>,
    sub: 'Structured. Inspectable. Forkable.',
  },
  {
    tone: 'dark',
    n: '04',
    text: <>Anyone can fork it and re-run it. Disagreement becomes <b>locatable</b>.</>,
  },
  {
    tone: 'dark',
    n: '05',
    text: <>And now a machine can <b>verify</b> it — offline, in milliseconds.</>,
  },
]

export default function Story() {
  const [i, setI] = useState<number>(0)
  const [paused, setPaused] = useState<boolean>(false)
  const go = useCallback((n: number) => setI((n + SLIDES.length) % SLIDES.length), [])

  useEffect(() => {
    if (paused) return
    const t = setInterval(() => setI((x) => (x + 1) % SLIDES.length), 5200)
    return () => clearInterval(t)
  }, [paused])

  const s = SLIDES[i]
  return (
    <div
      className={`pr-story${s.tone === 'accent' ? ' is-accent' : ''}`}
      onMouseEnter={() => setPaused(true)}
      onMouseLeave={() => setPaused(false)}
    >
      <div className="pr-story-top">
        <span>The story</span>
        <span>{s.n} / 0{SLIDES.length}</span>
      </div>

      <div className="pr-story-body" key={i}>
        <p className="pr-story-text">{s.text}</p>
        {s.sub ? <p className="pr-story-sub">{s.sub}</p> : null}
      </div>

      <div className="pr-story-ctrl">
        <button aria-label="Previous slide" onClick={() => go(i - 1)}>←</button>
        <div className="pr-story-dots">
          {SLIDES.map((_, k) => (
            <button
              key={k}
              aria-label={`Go to slide ${k + 1}`}
              className={k === i ? 'on' : ''}
              onClick={() => go(k)}
            />
          ))}
        </div>
        <button aria-label="Next slide" onClick={() => go(i + 1)}>→</button>
      </div>
    </div>
  )
}
