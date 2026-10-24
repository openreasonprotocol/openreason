import { DocsThemeConfig, useConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  // ─── Logo ─────────────────────────────────────────────────────────────────
  logo: (
    <div style={{ display: 'flex', alignItems: 'center', gap: '11px' }}>
      <svg width="27" height="27" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <polygon points="16,3 27,9.5 27,22.5 16,29 5,22.5 5,9.5" fill="none" stroke="currentColor" strokeWidth="2.6" strokeLinejoin="round" strokeLinecap="round" />
      </svg>
      <span style={{ fontFamily: "'Funnel Display', sans-serif", fontWeight: 700, fontSize: '16px', letterSpacing: '0.005em' }}>Public Reason Project</span>
    </div>
  ),
  logoLink: '/',

  // Remove the GitLab icon from the top-right nav (cleaner)
  project: {},

  // ─── Edit link ────────────────────────────────────────────────────────────
  docsRepositoryBase: 'https://gitlab.com/publicreason/orp/-/blob/main/docs-site/pages',
  editLink: { content: () => null },

  // ─── Last-updated timestamp ───────────────────────────────────────────────
  // Disabled: the per-page git timestamp made every unchanged page read as stale
  // ("Last updated on April 8"). The spec version is the meaningful currency marker.
  gitTimestamp: null,

  // ─── Head / SEO ───────────────────────────────────────────────────────────
  head() {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const { frontMatter, title } = useConfig()
    const pageTitle = title ? `${title} — OpenReason Protocol` : 'OpenReason Protocol'
    const description =
      frontMatter.description ??
      'OpenReason Protocol (ORP) — A standard for transparent, reproducible, and accountable policy reasoning.'
    const ogImage = 'https://docs.publicreasonproject.org/og-image.png'
    const siteUrl = 'https://docs.publicreasonproject.org'

    return (
      <>
        {/* Basic Meta Tags */}
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content={description} />
        <meta name="keywords" content="OpenReason, ORP, policy reasoning, transparency, accountability, data provenance, public policy, AI ethics, decision making" />
        <meta name="author" content="Public Reason Project" />
        <meta name="robots" content="index, follow" />

        {/* Open Graph / Facebook */}
        <meta property="og:type" content="website" />
        <meta property="og:url" content={siteUrl} />
        <meta property="og:title" content={pageTitle} />
        <meta property="og:description" content={description} />
        <meta property="og:image" content={ogImage} />
        <meta property="og:site_name" content="OpenReason Protocol" />

        {/* Twitter Card */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content={pageTitle} />
        <meta name="twitter:description" content={description} />
        <meta name="twitter:image" content={ogImage} />

        {/* Canonical URL */}
        <link rel="canonical" href={siteUrl} />

        {/* Favicons */}
        <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
        <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
        <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
        <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />

        <title>{pageTitle}</title>
      </>
    )
  },

  // ─── Dark mode ────────────────────────────────────────────────────────────
  // Force dark (industrial console) mode
  darkMode: false,
  nextThemes: { defaultTheme: 'dark', forcedTheme: 'dark' },

  // ─── Sidebar ──────────────────────────────────────────────────────────────
  sidebar: {
    defaultMenuCollapseLevel: 0,  // 0 = expand all sections by default
    toggleButton: false,
  },

  // ─── TOC ──────────────────────────────────────────────────────────────────
  toc: {
    backToTop: true,
    title: (
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8F9BA8" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
        <line x1="21" x2="3" y1="6" y2="6"/>
        <line x1="15" x2="3" y1="12" y2="12"/>
        <line x1="17" x2="3" y1="18" y2="18"/>
      </svg>
    ),
  },

  // ─── Footer ───────────────────────────────────────────────────────────────
  footer: {
    content: (
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          width: '100%',
          fontSize: '13px',
          color: '#4A4A4A',
        }}
      >
        <span>© {new Date().getFullYear()} Public Reason Project — OpenReason Protocol</span>
        <span style={{ display: 'flex', gap: '24px' }}>
          <a href="https://gitlab.com/publicreason/orp">GitLab</a>
          <a href="https://pypi.org/project/orp-validator/">PyPI</a>
          <a href="mailto:hello@publicreasonproject.org">Contact</a>
        </span>
      </div>
    ),
  },

  // ─── Top Navigation ───────────────────────────────────────────────────────
  navbar: {
    extraContent: (
      <div className="pr-navlinks">
        <a href="/what-it-is">What it is</a>
        <a href="/how-it-works">How it works</a>
        <a href="/about">About</a>
      </div>
    )
  },

  // ─── Navigation arrows ────────────────────────────────────────────────────
  navigation: {
    prev: true,
    next: true,
  },

  // ─── Search ───────────────────────────────────────────────────────────────
  search: {
    placeholder: 'Search docs…',
  },

  // ─── Feedback ─────────────────────────────────────────────────────────────
  feedback: {
    content: null, // Remove "Was this helpful?" clutter
  },
}

export default config
