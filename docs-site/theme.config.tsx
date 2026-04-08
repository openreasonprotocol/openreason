import { DocsThemeConfig, useConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  // ─── Logo ─────────────────────────────────────────────────────────────────
  logo: (
    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
      <svg width="24" height="24" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
        <line x1="16" y1="30" x2="16" y2="16" stroke="#1a5490" strokeWidth="3" strokeLinecap="round"/>
        <path d="M 16 16 Q 10 13, 4 10" fill="none" stroke="#1a5490" strokeWidth="3" strokeLinecap="round"/>
        <circle cx="4" cy="10" r="3" fill="#1a5490"/>
        <path d="M 16 16 Q 22 13, 28 10" fill="none" stroke="#1a5490" strokeWidth="3" strokeLinecap="round"/>
        <circle cx="28" cy="10" r="3" fill="#1a5490"/>
        <line x1="16" y1="16" x2="16" y2="2" stroke="#1a5490" strokeWidth="3" strokeLinecap="round"/>
        <circle cx="16" cy="2" r="3" fill="#1a5490"/>
        <circle cx="16" cy="16" r="3.5" fill="#d97706"/>
      </svg>
      <div style={{ display: 'flex', flexDirection: 'column', lineHeight: '1.2' }}>
        <span style={{ fontWeight: 700, fontSize: '16px' }}>Public Reason Project</span>
        <span style={{ fontSize: '12px', color: '#666' }}>OpenReason Protocol</span>
      </div>
    </div>
  ),
  logoLink: '/',

  // Remove the GitLab icon from the top-right nav (cleaner)
  project: {},

  // ─── Edit link ────────────────────────────────────────────────────────────
  docsRepositoryBase: 'https://gitlab.com/publicreason/orp/-/blob/main/docs-site/pages',
  editLink: { content: () => null },

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
  // Force light mode
  darkMode: false,

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
    extraContent: null
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
