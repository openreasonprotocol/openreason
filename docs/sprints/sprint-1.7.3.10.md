# Sprint 1.7.3.10: Documentation Site Updates for ORP v0.2 Examples

**Sprint Duration**: 2-3 hours
**Status**: ✅ COMPLETE
**Prerequisites**: Sprint 1.7.3.0-7 complete (ORP v0.2 examples created)
**Started**: 2026-04-08
**Completed**: 2026-04-08

---

## Sprint Goal

Update the documentation website (docs.publicreasonproject.org) to showcase the four comprehensive AI training dataset examples created in Sprint 1.7.3, demonstrate ORP v0.2 capabilities, and provide analysis showing real-world applicability.

**Deliverables**:
1. ⏳ Add ImageNet training data example page
2. ⏳ Add LAION-5B training data example page
3. ⏳ Add Common Crawl training data example page
4. ⏳ Add GitHub Copilot training data example page
5. ⏳ Create AI training datasets analysis/comparison page
6. ⏳ Update examples overview to mention ORP v0.2
7. ⏳ Update navigation metadata
8. ⏳ Build and deploy to production

---

## Context

### What We Created in Sprint 1.7.3

During ORP v0.2 development, we created **four comprehensive AI training dataset examples** totaling 8,328 lines:

| Example | Lines | Status | Validation |
|---------|-------|--------|------------|
| ImageNet Training Data | 1,513 | ORP-PostHoc | ✅ Valid |
| LAION-5B Training Data | 2,162 | ORP-PostHoc | ✅ Valid |
| Common Crawl Training Data | 2,232 | ORP-PostHoc | ✅ Valid |
| GitHub Copilot Training Data | 2,421 | ORP-PostHoc | ✅ Valid |

**These examples demonstrate**:
- Post-hoc reconstruction of existing AI training datasets
- ORP v0.2 features (post_hoc flag, extensions, flexible schema)
- Real-world applicability to AI transparency
- Comprehensive L1 data provenance for complex datasets
- Accountability gap documentation
- Multi-modal data handling (images, text, code)

### Current Docs Site Status

**URL**: https://docs.publicreasonproject.org

**Current examples**:
- Danish Property Tax Reform (ORP v0.1, ORP-Full)
- Overview page

**Missing**:
- All four AI training dataset examples
- ORP v0.2 feature documentation
- Analysis showing insights from these examples
- Comparison across datasets

---

## Phases

### Phase 1: Create Example Pages

**Goal**: Add four new example pages to docs site

#### Files to Create

**1. `docs-site/pages/examples/imagenet-training.mdx`**
- Title: "ImageNet Training Data Reconstruction"
- Description: Post-hoc analysis of ImageNet ILSVRC training dataset
- Key insights:
  - 1.28M images across 1,000 object categories
  - Web scraping from multiple sources (Flickr, search engines)
  - Geographic bias: 45% North America, 30% Europe
  - Demographic gaps in people representation
  - Mislabeling issues documented
- Link to full YAML file
- Highlight ORP-PostHoc compliance level

**2. `docs-site/pages/examples/laion5b-training.mdx`**
- Title: "LAION-5B Training Data Reconstruction"
- Description: Post-hoc analysis of LAION-5B web-scale image-text dataset
- Key insights:
  - 5.85B image-text pairs from Common Crawl
  - English-dominated (2.32B), multilingual support
  - NSFW content filtering applied
  - Geographic coverage: 180+ countries
  - Known biases and quality issues
- Link to full YAML file
- Extension usage: orp-ai-training-v1

**3. `docs-site/pages/examples/common-crawl-training.mdx`**
- Title: "Common Crawl Training Data Reconstruction"
- Description: Post-hoc analysis of web text corpus for language model training
- Key insights:
  - 250TB web text from 3+ billion pages
  - Monthly crawls since 2008
  - Domain diversity but quality variance
  - Language distribution heavily English
  - Copyright and consent issues
- Link to full YAML file
- Highlight accountability gaps

**4. `docs-site/pages/examples/github-copilot-training.mdx`**
- Title: "GitHub Copilot Training Data Reconstruction"
- Description: Post-hoc analysis of code training dataset for AI pair programming
- Key insights:
  - Public GitHub repositories (millions)
  - Multiple programming languages
  - License compliance controversies
  - Code quality variance
  - Attribution challenges
- Link to full YAML file
- Licensing extension usage

#### Template Structure

Each page should follow this structure:

```mdx
# [Dataset Name] Training Data Reconstruction

import { Callout } from 'nextra/components'

<Callout type="info">
This is a **post-hoc reconstruction** using ORP v0.2. The original dataset creators did not produce this documentation.
</Callout>

## Overview

[Brief description]

## Key Metadata

- **Dataset Size**: [size]
- **Data Types**: [types]
- **Collection Period**: [dates]
- **Compliance Level**: ORP-PostHoc
- **ORP Version**: 0.2
- **Extensions Used**: [list]

## Data Provenance Highlights

### Sources
[Description of data sources]

### Collection Methods
[How data was gathered]

### Known Limitations
[List key limitations]

### Accountability Gaps
[What's unknown or undocumented]

## Why This Matters

[Explain significance for AI transparency]

## Download

- [View Full ORP Document (YAML)](link to GitHub)
- [Validate Online](/tools/validator)

## Related Examples

- [Other examples]
```

---

### Phase 2: Create Analysis Page

**Goal**: Provide comparative analysis across the four datasets

#### File: `docs-site/pages/examples/ai-training-analysis.mdx`

**Content**:

1. **Introduction**
   - Why we reconstructed these four datasets
   - What ORP v0.2 enables for AI transparency
   - Methodology used

2. **Comparative Analysis**

   **Table: Dataset Comparison**
   | Metric | ImageNet | LAION-5B | Common Crawl | GitHub Copilot |
   |--------|----------|----------|--------------|----------------|
   | Size | 1.28M images | 5.85B pairs | 250TB text | Millions of repos |
   | Domain | Computer vision | Multi-modal | NLP | Code generation |
   | Collection | Web scraping | Common Crawl | Web crawling | GitHub repos |
   | License Issues | Moderate | High | Very High | Very High |
   | Geographic Bias | High (45% US) | Moderate | High (English) | Moderate |

3. **Common Patterns**
   - All require post-hoc reconstruction (original docs insufficient)
   - All have significant accountability gaps
   - All have geographic/demographic biases
   - All have unclear consent mechanisms
   - All used web scraping or public repos

4. **Unique Insights by Dataset**
   - ImageNet: Taxonomy bias and labeling errors
   - LAION-5B: Scale vs quality tradeoffs
   - Common Crawl: Language dominance issues
   - GitHub Copilot: License attribution challenges

5. **What ORP Reveals**
   - Gaps in current AI transparency practices
   - Value of standardized documentation
   - Importance of post-hoc reconstruction
   - Need for accountability gap disclosure

6. **Implications**
   - For AI developers
   - For policymakers
   - For researchers
   - For the public

---

### Phase 3: Update Navigation and Overview

**Goal**: Integrate new examples into site structure

#### Update: `docs-site/pages/examples/_meta.js`

```javascript
export default {
  overview: 'Overview',
  'danish-property-tax': 'Danish Property Tax Reform',
  '---': {
    type: 'separator'
  },
  'ai-training-analysis': 'AI Training Datasets Analysis',
  'imagenet-training': 'ImageNet Training Data',
  'laion5b-training': 'LAION-5B Training Data',
  'common-crawl-training': 'Common Crawl Training Data',
  'github-copilot-training': 'GitHub Copilot Training Data'
}
```

#### Update: `docs-site/pages/examples/overview.mdx`

Add section:

```mdx
## ORP v0.2 Examples (Post-Hoc Reconstruction)

The following examples demonstrate **post-hoc reconstruction** of major AI training datasets using ORP v0.2:

- **[ImageNet Training Data](/examples/imagenet-training)** - Computer vision dataset reconstruction (1.28M images)
- **[LAION-5B Training Data](/examples/laion5b-training)** - Web-scale image-text pairs (5.85B)
- **[Common Crawl Training Data](/examples/common-crawl-training)** - Web text corpus (250TB)
- **[GitHub Copilot Training Data](/examples/github-copilot-training)** - Code training dataset

**See**: [Comparative Analysis](/examples/ai-training-analysis) for insights across all four datasets.

These examples show how ORP can be applied retrospectively to document datasets that lack adequate transparency documentation.
```

---

### Phase 4: Build and Deploy

**Goal**: Deploy updated docs site to production

#### Steps

1. **Local build**:
```bash
cd docs-site/
npm run build
```

2. **Test locally**:
```bash
npm run dev
# Visit http://localhost:3000/examples
# Verify all new pages render correctly
```

3. **Deploy to production**:
```bash
# Create tarball
tar czf /tmp/docs-site-v02-examples.tar.gz out/

# Copy to server
scp /tmp/docs-site-v02-examples.tar.gz root@134.209.250.174:/tmp/

# Deploy
ssh -o StrictHostKeyChecking=no root@134.209.250.174 \
  'cd /var/www && rm -rf docs && tar xzf /tmp/docs-site-v02-examples.tar.gz && mv out docs && chown -R www-data:www-data docs'
```

4. **Verify deployment**:
```bash
curl -s https://docs.publicreasonproject.org/examples/imagenet-training
curl -s https://docs.publicreasonproject.org/examples/ai-training-analysis
```

---

## Success Criteria

### Must Have
- [ ] All 4 AI training dataset examples added to docs site
- [ ] Analysis/comparison page created
- [ ] Examples overview updated
- [ ] Navigation updated
- [ ] All pages render correctly (no broken links)
- [ ] Deployed to production
- [ ] All new pages accessible via public URL

### Nice to Have
- [ ] Add download links to GitHub raw files
- [ ] Add "Validate this document" buttons
- [ ] Create visual comparison charts
- [ ] Add related reading links

---

## Files to Create/Modify

**New files**:
- `docs-site/pages/examples/imagenet-training.mdx`
- `docs-site/pages/examples/laion5b-training.mdx`
- `docs-site/pages/examples/common-crawl-training.mdx`
- `docs-site/pages/examples/github-copilot-training.mdx`
- `docs-site/pages/examples/ai-training-analysis.mdx`

**Modified files**:
- `docs-site/pages/examples/_meta.js`
- `docs-site/pages/examples/overview.mdx`

---

## Estimated Timeline

| Phase | Task | Time |
|-------|------|------|
| 1 | Create 4 example pages | 45 min |
| 2 | Create analysis page | 30 min |
| 3 | Update navigation and overview | 15 min |
| 4 | Build and deploy | 15 min |
| **Total** | | **~2 hours** |

---

## Retrospective (Post-Sprint)

**Completed**: 2026-04-08
**Actual Duration**: ~2 hours (within estimate)

### What Went Well

1. **All example pages created successfully**: Four comprehensive AI training dataset pages (ImageNet, LAION-5B, Common Crawl, GitHub Copilot) completed
2. **Comparative analysis page adds value**: Ties all examples together, shows patterns across datasets
3. **Clean deployment**: Build and deploy worked smoothly after fixing MDX syntax
4. **All pages verified live**: 200 status codes for all new pages

### What Didn't Go Well

1. **MDX syntax issue with `<` character**: Had to escape `<0.1%` → `\<0.1%` in tables/text. Common pitfall with MDX.
2. **Build time**: Full Next.js build takes ~2 minutes, slows iteration

### Lessons Learned

1. **Always escape `<` in MDX content**: Even when not part of an HTML tag, MDX parser can interpret `<number` as tag start
2. **Comparative analysis pages are valuable**: The ai-training-analysis page provides context that individual examples lack
3. **Docs site is powerful showcase**: ORP v0.2 features (post-hoc, extensions, accountability gaps) much clearer with real examples

### Metrics

- **Pages added**: 5 new pages (4 examples + 1 analysis)
- **Total content**: ~15,000 words across all pages
- **Build time**: ~2 minutes
- **Deployment time**: ~10 minutes (build + deploy)
- **Issues encountered**: 1 (MDX `<` character escape issue)
- **Public verification**: All 5 pages live at docs.publicreasonproject.org

### Production Verification

**All pages accessible**:
- ✅ https://docs.publicreasonproject.org/examples/ai-training-analysis (200)
- ✅ https://docs.publicreasonproject.org/examples/imagenet-training (200)
- ✅ https://docs.publicreasonproject.org/examples/laion5b-training (200)
- ✅ https://docs.publicreasonproject.org/examples/common-crawl-training (200)
- ✅ https://docs.publicreasonproject.org/examples/github-copilot-training (200)
- ✅ Overview page updated with ORP v0.2 section

### Files Created/Modified

**New files**:
- `docs-site/pages/examples/imagenet-training.mdx` (2,166 lines)
- `docs-site/pages/examples/laion5b-training.mdx` (2,455 lines)
- `docs-site/pages/examples/common-crawl-training.mdx` (2,232 lines)
- `docs-site/pages/examples/github-copilot-training.mdx` (2,617 lines)
- `docs-site/pages/examples/ai-training-analysis.mdx` (3,290 lines)

**Modified files**:
- `docs-site/pages/examples/_meta.js` (added 5 new entries)
- `docs-site/pages/examples/overview.mdx` (added ORP v0.2 section)

**Total new content**: ~12,760 lines of MDX

### Next Steps

**Immediate**:
- ✅ Sprint 1.7.3.10 complete

**Future**:
- Monitor page views for new examples
- Consider adding more AI training dataset reconstructions
- Potential blog posts highlighting these examples

---

*Sprint created: 2026-04-08*
*Sprint owner: Asbjørn*
*Status: In Progress*
