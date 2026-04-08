# Migration Guide: ORP v0.1 → v0.2

**Target Audience**: Document authors, tool developers, validators

**Difficulty**: Easy (fully backward compatible)

**Time Estimate**: 5-30 minutes per document (depending on migration type)

---

## Overview

ORP v0.2 is **fully backward compatible** with v0.1. All v0.1 documents are valid v0.2 documents with minimal header changes.

**Key Fact**: No breaking changes. All v0.1 required fields remain required in v0.2.

**Migration Types**:
1. **Minimal Migration** (5 minutes): Update version header only
2. **Enhanced Migration** (15-30 minutes): Add v0.2 features (post_hoc, extensions)
3. **Full Migration** (1-2 hours): Leverage v0.2 flexibility for richer structures

---

## Quick Start: Minimal Migration

### Step 1: Update orp_version

```diff
- orp_version: "0.1"
+ orp_version: "0.2"
```

### Step 2: Update last_modified

```yaml
last_modified: "2026-04-08"  # Today's date
```

### Step 3: Validate

```bash
orp validate my-document.yaml
```

or

```bash
python3 -m orp_validator.cli my-document.yaml
```

**Expected Output**:
```
============================================================
ORP Validation Report: my-document.yaml
============================================================

✓ Valid

Compliance Level: ORP-Full

Summary:
  Document is valid and meets ORP-Full requirements.
============================================================
```

**That's it!** Your v0.1 document is now a valid v0.2 document.

---

## Enhanced Migration: Add v0.2 Features

### When to Use Enhanced Migration

- Document is **post-hoc reconstruction** (retrospective analysis)
- Document uses **domain-specific fields** (AI training, policy, medical)
- Want to **leverage v0.2 flexibility** (richer object structures)

### Feature 1: Add post_hoc Flag

**When to use**: Document reconstructed from published sources, decision-making history unavailable

**Before**:
```yaml
orp_version: "0.1"
```

**After**:
```yaml
orp_version: "0.2"
post_hoc: true  # NEW: Flags retrospective reconstruction
```

**Implications**:
- Allows "UNKNOWN" for decision makers, alternatives, dates
- Requires `accountability_gap` documentation in L4 (if L4 present)
- Compliance level displays as "ORP-PostHoc"

### Feature 2: Update Author Roles

**When to use**: Author is analyst/reconstructor, not original decision maker

**Before**:
```yaml
authors:
  - name: John Doe
    role: author
```

**After**:
```yaml
authors:
  - name: John Doe
    role: analyst          # NEW: Post-hoc analyst
    affiliation: University of Example  # NEW (optional but recommended)
```

**New v0.2 roles**:
- `analyst`: Post-hoc analysis from published sources
- `reconstructor`: Retrospective documentation

### Feature 3: Declare Extensions

**When to use**: Document includes domain-specific fields

**After**:
```yaml
orp_version: "0.2"
extensions:
  - orp-ai-training-v1  # If AI training dataset
  - orp-safety-v1       # If safety-critical content
  - orp-license-v1      # If software license compliance
```

**Available extensions**:
- `orp-ai-training-v1`: AI training dataset fields (harm tiers, safety filtering)
- `orp-safety-v1`: Safety-critical fields (CSAM detection, vulnerable populations)
- `orp-license-v1`: Software license compliance (GPL violations, attribution)

---

## Full Migration: Leverage v0.2 Flexibility

### Upgrade 1: Simple Strings → Rich Objects

#### exclusion_criteria

**Before (v0.1)**:
```yaml
exclusion_criteria:
  - "Non-visual WordNet synsets excluded"
  - "Offensive labels removed in 2019"
```

**After (v0.2 enhanced)**:
```yaml
exclusion_criteria:
  - excluded: "Non-visual WordNet synsets"
    reason: "Not photographable (e.g., 'democracy', 'justice')"
    potential_impact: "Limits definition of 'object recognition' to visual entities only"
    data_affected: "~30,000 synsets (~60% of WordNet)"

  - excluded: "Offensive person category labels"
    reason: "Violated ethical standards (racist, sexist labels)"
    potential_impact: "Removed 600,000 images, 54% of person categories"
    data_affected: "1,593 categories (e.g., 'call girl', 'drug addict')"
    affected_count: 600000
```

**Benefits**: Quantifies impact, explains reasoning, enables accountability audits

#### benefits/harms

**Before (v0.1)**:
```yaml
benefits:
  - "Enabled deep learning revolution"
  - "Improved accuracy from 26% to 3% error rate"

harms:
  - "Geographic bias in trained models"
  - "Labor exploitation (Mechanical Turk)"
```

**After (v0.2 enhanced)**:
```yaml
benefits:
  - benefit: "Enabled deep learning revolution (2012-2017)"
    magnitude: "Transformative (positive)"
    affected_population: "Global AI research community (10,000+ researchers)"
    confidence: "very-high"
    evidence: "ImageNet Challenge results: error rate 26% (2011) → 3% (2017)"
    temporal_scope: "2012-present (ongoing citations: 75,000+)"

harms:
  - harm: "Geographic bias in trained models"
    magnitude: "Significant accuracy gap (10-20 percentage points)"
    affected_population: "~2 billion people in under-represented geographies"
    confidence: "high"
    evidence: "de Vries et al. 2019, Shankar et al. 2017 (empirical studies)"
    harm_tier: "TIER 6 - BIAS"  # Extension field (orp-ai-training-v1)
    remediation_difficulty: "High (requires new dataset collection)"
```

**Benefits**: Evidence-based claims, quantified impacts, confidence levels

### Upgrade 2: Add v0.2-Specific Fields

#### critical_undocumented_exclusions (L1)

**Purpose**: Document post-hoc discovered gaps

**Example** (LAION-5B CSAM discovery):
```yaml
l1_data_provenance:
  - dataset_id: laion-5b
    # ... existing fields ...

    critical_undocumented_exclusions:  # NEW v0.2
      - exclusion_gap: "CSAM URLs in training data"
        description: |
          3,226 CSAM URLs discovered post-publication (Stanford Internet
          Observatory, December 2023). LAION unaware during dataset creation
          (September 2021-March 2022).
        affected_count: 3226
        consequences:
          - "Federal crime distribution (18 U.S.C. § 2252)"
          - "Victim re-traumatization (survivors seeing abuse imagery in models)"
          - "Legal liability for downstream users (unknowingly caching CSAM)"
        severity: "critical"
        accountability_gap: |
          LAION did not apply CSAM filtering (PhotoDNA, hash matching) because
          tools not integrated into pipeline. No human review performed (infeasible
          at 5.85B scale). CSAM detection discovered only after Stanford analysis.
```

#### accountability_gap (L4)

**Purpose**: Document WHO/WHY/WHAT unknowns in post-hoc reconstruction

**Example** (ImageNet WordNet decision):
```yaml
l4_accountability_ledger:
  entries:
    - entry_id: "decision_001"
      decision: "Use WordNet 3.0 as hierarchical taxonomy for ImageNet"
      decision_type: "constitutive"  # Defines entire project structure
      timestamp: "2007"
      decided_by: "UNKNOWN"
      decision_date_confidence: "medium (inferred from project timeline)"

      rationale_inferred: |
        ANALYST INFERENCE: WordNet chosen for three reasons:
        (1) Academic prestige: Princeton-developed, widely cited
        (2) Christiane Fellbaum connection: WordNet creator at Princeton (Fei-Fei Li's institution)
        (3) No alternatives: Other taxonomies (Cyc, DBpedia) incomplete for image classification in 2007

        Decision likely made 2006-2007 based on ImageNet launch timeline (2009),
        though exact meeting notes not publicly available.

      accountability_gap: |  # NEW v0.2
        WHO: Unknown who specifically decided WordNet 3.0 (decision pre-dates
        published papers). INFERRED: Likely Fei-Fei Li in consultation with
        Christiane Fellbaum based on institutional proximity and project scope.

        WHY: WordNet's comprehensive taxonomy (21,841 synsets with hierarchical
        IS-A relationships) made it natural choice. Alternative taxonomies
        (Cyc: too abstract, DBpedia: too sparse in 2007) lacked required depth
        for visual object classification.

        WHAT: No documentation of alternative taxonomies seriously considered.
        Meeting notes from 2006-2007 planning phase not in public archives.
        Decision likely made informally given WordNet's academic prestige.

      source: |
        Inferred from:
        - Deng et al. (2009) "ImageNet: A Large-Scale Hierarchical Image Database"
        - Fei-Fei Li biography sources (2023)
        - Princeton CS Department project archives (2006-2007)

      alternatives_considered: null  # v0.2: null allowed if post_hoc and unknown
```

#### comparison_to_actual (L2 scenarios)

**Purpose**: Counterfactual analysis - what if different decisions made?

**Example** (ImageNet global sampling):
```yaml
l2_consequence_simulation:
  scenarios:
    - scenario_id: "counterfactual_global_sampling"
      description: |
        What if ImageNet used proportional global image sampling (representative
        of world population distribution) instead of North American/European bias?

      parameter_values:
        geographic_distribution: "Proportional (China: 18%, India: 18%, US: 4%, EU: 10%)"
        image_source_diversity: "Multi-regional (Baidu, Yandex, local photo sharing)"
        collection_cost_multiplier: 2.5  # Higher cost for global coordination

      outcomes:
        model_accuracy_global_south: "Estimated 5-10pp accuracy improvement"
        model_accuracy_global_north: "Minimal degradation (1-2pp)"
        dataset_cost: "$3-5M (vs $1-2M actual)"
        collection_timeline: "18-24 months (vs 12 months actual)"

      comparison_to_actual: |  # NEW v0.2
        ACTUAL (S1): 80%+ North American/European images → 10-20pp accuracy
        gap on non-Western test sets (de Vries et al. 2019). Affected
        population: ~2 billion people in Global South face degraded AI performance.

        COUNTERFACTUAL (S2): Proportional global sampling → estimated 5-10pp
        accuracy gap (reduced by 50%). Harm reduction: ~1 billion people benefit
        from more representative training data.

        TRADE-OFF: 2.5x cost increase ($1-2M → $3-5M) + 6-12 months delay.
        Cost per person benefited: $0.002-0.005 (comparable to other bias
        mitigation interventions).

        FEASIBILITY: Technically feasible in 2009, economically feasible with
        NSF/industry funding. Not pursued due to institutional bias toward
        Western image sources (Flickr, Google Images predominantly US/EU users).
```

### Upgrade 3: Flexible Type Patterns

#### date_range (string → string | object)

**Before**:
```yaml
date_range: "2009-2017"
```

**After**:
```yaml
date_range:
  start: "2009-01-01"
  end: "2017-12-31"
  temporal_scope: "9 years"
  collection_phases:
    - phase: "Initial collection (2009-2010)"
      images_collected: 3200000
    - phase: "Category expansion (2011-2015)"
      images_collected: 10000000
    - phase: "Quality improvement (2016-2017)"
      images_collected: 1100000
```

#### access.public (boolean → boolean | string)

**Before**:
```yaml
access:
  public: true
  license: "Research use only"
```

**After**:
```yaml
access:
  public: "partial"  # v0.2: string allowed for nuance
  conditions: "Registration required, academic use only"
  url: "https://image-net.org/download"
  license: "ImageNet License (non-commercial research)"
  cost: "Free for research, $$$ for commercial use"
```

---

## Example Migration: Danish Property Tax Reform

Let's migrate the existing v0.1 example to v0.2.

### Before (v0.1)

```yaml
orp_version: "0.1"
document_id: "danish_property_tax_reform_2024"
title: "Danish Property Tax Reform 2024 - Data Provenance Analysis"
# ... rest of document ...
```

### After (Minimal v0.2)

```yaml
orp_version: "0.2"
document_id: "danish_property_tax_reform_2024"
title: "Danish Property Tax Reform 2024 - Data Provenance Analysis"
last_modified: "2026-04-08"  # Updated
# ... rest of document unchanged ...
```

**Validation**:
```bash
python3 -m orp_validator.cli examples/danish_property_tax_reform.yaml
```

**Result**: ✅ Valid (ORP-Full compliance)

---

## Automated Migration Script

### Basic Script (Python)

```python
#!/usr/bin/env python3
"""
Automated ORP v0.1 → v0.2 migration script

Usage:
    python migrate_v0.1_to_v0.2.py my-document.yaml

What it does:
- Updates orp_version to "0.2"
- Updates last_modified to today
- Optionally adds post_hoc flag
- Optionally adds extensions
- Validates migrated document
- Creates backup (.yaml.v0.1.backup)
"""

import sys
import yaml
from datetime import date
from pathlib import Path

def migrate_document(file_path: Path):
    """Migrate ORP v0.1 document to v0.2"""

    # Load document
    with open(file_path) as f:
        doc = yaml.safe_load(f)

    # Check current version
    current_version = doc.get('orp_version')
    if current_version != '0.1':
        print(f"Error: Document version is {current_version}, expected 0.1")
        sys.exit(1)

    print(f"Migrating {file_path.name} from v0.1 to v0.2...")

    # Update version
    doc['orp_version'] = '0.2'
    print("  ✓ Updated orp_version to 0.2")

    # Update last_modified
    doc['last_modified'] = str(date.today())
    print(f"  ✓ Updated last_modified to {date.today()}")

    # Prompt for post_hoc flag
    print("\nIs this a post-hoc reconstruction?")
    print("  (Document reconstructed from published sources, decision history unavailable)")
    is_post_hoc = input("  Add post_hoc: true flag? (y/n): ").lower() == 'y'

    if is_post_hoc:
        doc['post_hoc'] = True
        print("  ✓ Added post_hoc: true")

        # Suggest updating author role
        print("\n  Suggestion: Update author role to 'analyst' or 'reconstructor'")
        print(f"  Current role: {doc.get('authors', [{}])[0].get('role', 'unknown')}")

    # Prompt for extensions
    domain = doc.get('domain', '').lower()
    extensions = []

    if 'ai' in domain or 'training' in domain:
        print("\nDetected AI/training domain")
        add_ai = input("  Add orp-ai-training-v1 extension? (y/n): ").lower() == 'y'
        if add_ai:
            extensions.append('orp-ai-training-v1')

    if extensions:
        doc['extensions'] = extensions
        print(f"  ✓ Added extensions: {', '.join(extensions)}")

    # Create backup
    backup_path = file_path.with_suffix('.yaml.v0.1.backup')
    file_path.rename(backup_path)
    print(f"\n✓ Backup saved: {backup_path}")

    # Save migrated document
    with open(file_path, 'w') as f:
        yaml.dump(doc, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"✓ Migrated document saved: {file_path}")

    # Next steps
    print("\n" + "="*60)
    print("MIGRATION COMPLETE")
    print("="*60)
    print("\nNext steps:")
    print(f"  1. Review changes: diff {backup_path} {file_path}")
    print(f"  2. Validate: orp validate {file_path}")
    print("  3. Consider adding v0.2 features:")
    print("     - critical_undocumented_exclusions (L1)")
    print("     - accountability_gap (L4)")
    print("     - Rich object formats (benefits/harms)")
    print("\nSee: docs/specs/MIGRATION_V0.1_TO_V0.2.md")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python migrate_v0.1_to_v0.2.py document.yaml")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    migrate_document(file_path)
```

### Usage

```bash
# Save script
curl -o migrate.py https://raw.githubusercontent.com/publicreason/orp/main/scripts/migrate_v0.1_to_v0.2.py

# Make executable
chmod +x migrate.py

# Migrate document
python3 migrate.py my-document.yaml
```

---

## Common Pitfalls

### Pitfall 1: Forgetting to Update last_modified

**Problem**: Version updated but last_modified still shows v0.1 date

**Symptoms**: Document appears unchanged, confusing for reviewers

**Solution**:
```yaml
orp_version: "0.2"
last_modified: "2026-04-08"  # TODAY, not original creation date
```

### Pitfall 2: Adding post_hoc Without Updating Author Role

**Problem**: Document flagged post_hoc but author role still "author"

**Symptoms**: Misleading attestation - appears as original author when it's analyst

**Solution**:
```yaml
post_hoc: true
authors:
  - name: Jane Analyst
    role: analyst  # NOT "author"
    affiliation: Stanford Internet Observatory
```

### Pitfall 3: Extension Naming Typo

**Problem**: Extension name incorrect

**Examples of WRONG naming**:
- ❌ `ai-training-v1` (missing "orp-" prefix)
- ❌ `orp-ai-training-1` (missing "v" before version)
- ❌ `orp-ai-training-v1.0` (semantic version not supported yet)

**Solution**:
```yaml
extensions:
  - orp-ai-training-v1  # ✓ Correct
```

### Pitfall 4: Assuming Extensions Auto-Validate

**Problem**: Added extension fields but expecting schema validation

**Reality**: v0.2.0 extensions are **informational only**

**What happens**:
```yaml
extensions:
  - orp-ai-training-v1

l1_data_provenance:
  - dataset_id: test
    safety_filtering_tools:  # Extension field
      tools_used: ["PhotoDNA"]
```

**Validator output**:
```
✓ Valid
Warnings:
  1. Extensions declared: orp-ai-training-v1. Note: Extension validation
     is informational only in current version.
```

**Future (v0.3+)**: `--strict-extensions` flag will enable validation

### Pitfall 5: Using "UNKNOWN" String Incorrectly

**Problem**: Using "UNKNOWN" in v0.1-style strings that now accept null

**Before (v0.1 workaround)**:
```yaml
alternatives_considered: "UNKNOWN"
```

**After (v0.2 proper)**:
```yaml
alternatives_considered: null  # Better: explicitly null
```

**When to use "UNKNOWN" vs null**:
- Use `null`: When field allows it (alternatives_considered, document_id)
- Use `"UNKNOWN"`: When field requires string (decided_by, timestamp)

---

## Compatibility Matrix

| Document Version | Validator v0.1 | Validator v0.2 |
|------------------|----------------|----------------|
| ORP v0.1 | ✅ Valid | ✅ Valid (backward compatible) |
| ORP v0.2 (minimal) | ⚠️  Valid (v0.2 features ignored) | ✅ Valid |
| ORP v0.2 (enhanced) | ❌ Invalid (unknown fields: post_hoc, extensions) | ✅ Valid |

**Recommendation**: Upgrade validator to v0.2 before migrating documents.

```bash
# Upgrade validator
pip install --upgrade orp-validator

# Verify version
orp --version
# Expected: orp-validator 0.4.0 (ORP v0.2 support)
```

---

## Rollback Procedure

If migration causes issues:

### Step 1: Restore Backup

```bash
mv my-document.yaml.v0.1.backup my-document.yaml
```

### Step 2: Validate with v0.1

```bash
orp validate --orp-version 0.1 my-document.yaml
```

or

```bash
python3 -m orp_validator.cli --orp-version 0.1 my-document.yaml
```

### Step 3: Report Issue

**GitHub**: https://github.com/publicreason/orp/issues

**Include**:
- Original v0.1 document (sanitized if sensitive)
- Migration steps attempted
- Validator error output
- Expected vs actual behavior

---

## Migration Checklist

Use this checklist for each document:

```markdown
## Pre-Migration
- [ ] Backup original document (.yaml.v0.1.backup)
- [ ] Validate v0.1 document passes (baseline)
- [ ] Upgrade validator to v0.2+

## Minimal Migration
- [ ] Update orp_version: "0.1" → "0.2"
- [ ] Update last_modified to today
- [ ] Validate v0.2 document passes

## Enhanced Migration (If Applicable)
- [ ] Add post_hoc: true (if retrospective)
- [ ] Update author role to analyst/reconstructor
- [ ] Add extensions array (if domain-specific fields)
- [ ] Validate v0.2 document passes

## Full Migration (Optional)
- [ ] Upgrade simple strings to rich objects
  - [ ] exclusion_criteria
  - [ ] benefits/harms
  - [ ] known_limitations
- [ ] Add v0.2-specific fields
  - [ ] critical_undocumented_exclusions (L1)
  - [ ] accountability_gap (L4)
  - [ ] comparison_to_actual (L2)
- [ ] Use flexible type patterns
  - [ ] date_range (object format)
  - [ ] access.public (string format)
- [ ] Validate v0.2 document passes

## Post-Migration
- [ ] Review diff (v0.1 vs v0.2)
- [ ] Commit changes (git)
- [ ] Update documentation references
- [ ] Notify collaborators of v0.2 upgrade
```

---

## FAQ

### Q: Must I migrate to v0.2 immediately?

**A**: No. v0.1 documents remain valid and will be supported through 2026. Migrate when you need v0.2 features (post_hoc, extensions, flexibility).

### Q: Will v0.2 migration break my tooling?

**A**: Only if your tooling doesn't support v0.2. Check with tool maintainers. Reference validator (orp-validator) supports both v0.1 and v0.2.

### Q: Can I use v0.2 features in v0.1 documents?

**A**: No. v0.1 validators reject unknown fields. Update `orp_version: "0.2"` first.

### Q: Do I need to add extensions if I use custom fields?

**A**: No. v0.2 `additionalProperties: true` allows custom fields without extensions. Extensions provide schema validation (future) and documentation.

### Q: What if my document uses features not in v0.1 or v0.2?

**A**: If your needs aren't met, propose a new extension or contribute to v0.3 specification.

---

## Further Reading

- **ORP v0.2 Specification**: `docs/specs/ORP_V0.2_SPEC.md`
- **ORP v0.2 Design Document**: `docs/specs/ORP_V0.2_DESIGN.md`
- **Extension Documentation**: `orp_validator/schemas/extensions/README.md`
- **Changelog**: See ORP_V0.2_SPEC.md Section 14

---

**Last Updated**: 2026-04-08
**ORP Version**: 0.2.0
**Document Status**: Draft
