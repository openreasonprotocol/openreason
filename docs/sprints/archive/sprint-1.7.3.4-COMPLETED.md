# Sprint 1.7.3.4: Empirical Validation of AI Training Dataset Examples

**Sprint Duration:** 1 day (2026-04-08)
**Status:** In Progress
**Prerequisites:** Sprints 1.7.3.0-1.7.3.3 complete (4 AI dataset examples drafted)

---

## Sprint Goal

**Run actual ORP v0.1 schema validation** on all 4 AI training dataset examples (ImageNet, LAION-5B, Common Crawl, GitHub Copilot) to capture **real validation errors** rather than **inferred/anticipated errors**.

This sprint establishes the **empirical foundation** for Sprint 1.7.3.5 (Schema Consolidation), ensuring ORP v0.2 design is grounded in **actual validation failures** not guesses.

---

## Background: Why This Sprint is Necessary

### Problem with Current Approach

In Sprints 1.7.3.0-1.7.3.3, I documented **anticipated errors** in each README:
- ImageNet: "85 errors expected"
- LAION-5B: "88 errors expected"
- Common Crawl: "71 errors expected"
- GitHub Copilot: "30-50 errors expected"
- **Total: 274-294 errors (guessed)**

**These error counts are INFERRED**, not measured:
- ❌ Never actually ran validator on documents
- ❌ Guessed errors based on "I added field X, schema probably doesn't support it"
- ❌ Cannot distinguish schema gaps from document bugs
- ❌ Risk: Design ORP v0.2 to fix non-existent problems

### Empirical Validation Approach

This sprint runs **actual validation** to:
- ✅ Measure real error counts (not guesses)
- ✅ Capture exact error messages (schema paths, line numbers, error types)
- ✅ Categorize errors by root cause (missing fields, type mismatches, additionalProperties violations)
- ✅ Prioritize fixes by frequency (errors in all 4 docs = P0, errors in 1 doc = P2)
- ✅ Distinguish schema design issues from document bugs

---

## Tasks

### Task 1: Set Up Validation Environment

**Goal**: Install ORP validator dependencies in isolated environment

**Steps**:
1. Create Python virtual environment (avoid system package conflicts)
2. Install `pyyaml` and `jsonschema` (validator dependencies)
3. Verify `orp_validator` module loads correctly
4. Test validator on simple document (ensure working before full validation)

**Deliverable**: Working validation environment

---

### Task 2: Validate All 4 Documents

**Goal**: Run ORP v0.1 schema validation on all 4 AI dataset examples, capture full error output

**Documents to Validate**:
1. `examples/imagenet_training_data.yaml` (1,513 lines)
2. `examples/laion5b_training_data.yaml` (2,162 lines)
3. `examples/common_crawl_training_data.yaml` (2,232 lines)
4. `examples/github_copilot_training_data.yaml` (2,421 lines)

**Validation Command**:
```bash
python3 -m orp_validator.cli validate <file.yaml> 2>&1 | tee <file>_validation.txt
```

**Capture for Each Document**:
- Total error count (actual vs anticipated)
- Full error messages (schema path, validation rule violated, line numbers)
- Validation success/failure status
- Any warnings or non-fatal issues

**Deliverables**:
- `examples/imagenet/validation_output.txt`
- `examples/laion5b/validation_output.txt`
- `examples/common_crawl/validation_output.txt`
- `examples/github_copilot/validation_output.txt`

---

### Task 3: Error Categorization and Analysis

**Goal**: Analyze validation errors across all 4 documents to identify patterns

**Analysis Steps**:

1. **Count actual errors** (compare to anticipated):
   ```
   | Document | Anticipated | Actual | Difference |
   |----------|-------------|--------|------------|
   | ImageNet | 85 | ??? | ??? |
   | LAION-5B | 88 | ??? | ??? |
   | Common Crawl | 71 | ??? | ??? |
   | GitHub Copilot | 30-50 | ??? | ??? |
   | **TOTAL** | 274-294 | ??? | ??? |
   ```

2. **Categorize errors by type**:
   - **additionalProperties violations**: New fields I added not in ORP v0.1 schema
   - **Type mismatches**: Used `object` where schema expects `array` (or vice versa)
   - **Required field missing**: Schema requires field, but I didn't provide
   - **Enum violations**: Used value not in schema's allowed list
   - **Format violations**: String doesn't match expected format (date, URI, etc.)

3. **Categorize errors by schema location**:
   ```
   | Schema Path | Error Type | Frequency | Documents Affected |
   |-------------|------------|-----------|---------------------|
   | l1_data_provenance.temporal_metadata | additionalProperties | 4 | All |
   | l1_data_provenance.critical_undocumented_exclusions.accountability_gap | additionalProperties | 4 | All |
   | l2_consequence_simulation.variables | Type mismatch (array vs object) | 4 | All |
   | ... | ... | ... | ... |
   ```

4. **Prioritize fixes for Sprint 1.7.3.5**:
   - **P0 (Critical)**: Errors in all 4 documents (schema MUST support these patterns)
   - **P1 (High)**: Errors in 3/4 documents (common pattern, high value to fix)
   - **P2 (Medium)**: Errors in 2/4 documents (moderately common)
   - **P3 (Low)**: Errors in 1 document (domain-specific, maybe extension not core schema)

5. **Distinguish schema gaps from document bugs**:
   - **Schema gap**: Field should be supported but ORP v0.1 doesn't define it → add to v0.2
   - **Document bug**: I used wrong YAML structure → fix my document, not schema
   - **Design decision**: Schema intentionally restrictive → decide if v0.2 should relax

**Deliverables**:
- Error categorization table (by type, by schema path, by priority)
- P0/P1/P2/P3 prioritized fix list for Sprint 1.7.3.5
- Schema gaps vs document bugs analysis

---

### Task 4: Document Validation Findings

**Goal**: Create comprehensive validation report for Sprint 1.7.3.5 input

**Deliverable**: `docs/sprints/sprint-1.7.3.4-validation-report.md`

**Report Contents**:

1. **Executive Summary**:
   - Total actual errors (vs anticipated)
   - Top 5 most frequent error patterns
   - Key findings for ORP v0.2 design

2. **Per-Document Validation Results**:
   - ImageNet: X errors (anticipated 85)
   - LAION-5B: X errors (anticipated 88)
   - Common Crawl: X errors (anticipated 71)
   - GitHub Copilot: X errors (anticipated 30-50)

3. **Error Pattern Analysis**:
   - additionalProperties violations: X errors across Y documents
   - Type mismatches: X errors across Y documents
   - Required field missing: X errors across Y documents

4. **P0 Schema Gaps** (errors in all 4 documents):
   - List of fields/patterns that MUST be added to ORP v0.2
   - Example: `temporal_metadata`, `accountability_gap`, etc.

5. **P1-P3 Schema Gaps** (errors in 1-3 documents):
   - Fields to consider for ORP v0.2 (domain-specific vs core)

6. **Document Bugs Identified**:
   - Errors caused by my YAML structure mistakes (not schema gaps)
   - Need to fix documents before claiming "schema validated"

7. **Recommendations for Sprint 1.7.3.5**:
   - Which schema patterns to adopt (strict core vs flexible extensions)
   - Whether to use `additionalProperties: true` (flexible) vs `false` (strict)
   - Extension registry pattern for domain-specific fields

---

## Success Criteria

- [ ] All 4 documents validated against ORP v0.1 schema
- [ ] Actual error counts measured (not guessed)
- [ ] Errors categorized by type, schema path, and priority
- [ ] P0/P1/P2/P3 fix list created for Sprint 1.7.3.5
- [ ] Validation report documents findings (empirical foundation for v0.2 design)
- [ ] Anticipated errors vs actual errors comparison shows methodology difference

---

## Deliverables

1. **Validation outputs** (4 files):
   - `examples/imagenet/validation_output.txt`
   - `examples/laion5b/validation_output.txt`
   - `examples/common_crawl/validation_output.txt`
   - `examples/github_copilot/validation_output.txt`

2. **Error analysis** (tables/spreadsheets):
   - Error count comparison (anticipated vs actual)
   - Error categorization by type
   - Error categorization by schema path
   - P0/P1/P2/P3 prioritized fix list

3. **Validation report**:
   - `docs/sprints/sprint-1.7.3.4-validation-report.md`

4. **Sprint retrospective**:
   - What we learned from actual validation vs anticipated errors
   - Methodology insights (importance of empirical validation)

---

## Timeline

**Total: 1 day**

- **Hour 1**: Set up validation environment, verify working
- **Hour 2**: Run all 4 validations, capture outputs
- **Hour 3-4**: Analyze errors, categorize by type/path/priority
- **Hour 5-6**: Write validation report, create P0/P1/P2/P3 fix list
- **Hour 7**: Sprint retrospective, handoff to Sprint 1.7.3.5

---

## Dependencies

**Requires**:
- Sprints 1.7.3.0-1.7.3.3 complete (4 AI dataset examples drafted)
- ORP v0.1 schema files (`orp_validator/schemas/*.json`)
- Python environment with `pyyaml`, `jsonschema`

**Blocks**:
- Sprint 1.7.3.5 (Schema Consolidation) - needs validation report as input

---

## Notes

### Why Actual Validation is Critical

1. **Empirical vs Theoretical**: Sprint 1.7.3 is about discovering schema gaps through real-world examples. Guessing errors defeats the purpose.

2. **Avoiding False Positives**: Anticipated errors may not exist (field actually IS supported, I was wrong).

3. **Avoiding False Negatives**: May miss errors I didn't anticipate (schema fails in ways I didn't predict).

4. **Actionable Insights**: Real validator output gives line numbers, schema paths, exact error types → can fix precisely.

5. **Methodology Transparency**: User asked "how can we make sure you not infer already known issues" → actual validation is the only guarantee.

### Expected Findings

Based on document content, likely error patterns:

- **additionalProperties: false violations**: ORP v0.1 schema is strict, I added many new fields (temporal_metadata, accountability_gap, tools_not_used, etc.)
- **Type mismatches**: Likely used `variables: {}` (object) where schema expects `variables: []` (array)
- **List vs object flexibility**: May have structured some fields as objects where schema expects arrays

**BUT**: These are still guesses. Actual validation will reveal truth.

---

**Sprint Start**: 2026-04-08
**Expected Completion**: 2026-04-08 (same day, 7 hours)
**Next Sprint**: 1.7.3.5 (Schema Consolidation - ORP v0.2 Design)
