# ORP Examples

This directory contains reference implementations of ORP-compliant documents demonstrating the protocol in practice.

---

## Danish Property Tax Reform

**File:** `danish_property_tax_reform.yaml`
**Compliance Level:** ORP-Full
**Domain:** Policy
**Status:** Open for comment

### What It Demonstrates

This document proposes a hybrid Land Value Tax (LVT) and smoothed profit tax system to replace Denmark's current property tax regime. It demonstrates:

- **L1 - Data Provenance**: Multiple datasets with detailed cleaning decisions, exclusion criteria, and known limitations
- **L2 - Consequence Simulation**: Economic modeling with 4 scenarios showing different property types and holding periods
- **L3 - Empathy Mapping**: Stakeholder analysis across homeowner types, renters, and municipalities
- **L4 - Accountability Ledger**: Decision log showing key methodological choices and alternatives considered
- **L5 - Fork Registry**: Metadata for fork tracking and explicit invitation to propose alternative assumptions

### Why This Example Matters

1. **Real Complexity**: Not a toy example - this is a genuine policy proposal with real economic modeling
2. **Demonstrates All Layers**: Shows how all 5 ORP layers work together in practice
3. **Honest About Limitations**: Documents what data is missing, what assumptions are approximations
4. **Invites Challenge**: Explicitly designed to be forked with different rate combinations or modeling approaches

### How to Use This Example

**Validate it:**
```bash
orp validate examples/danish_property_tax_reform.yaml
```

**Check compliance:**
```bash
orp check examples/danish_property_tax_reform.yaml
```

**Learn from it:**
- Read through each layer to see how ORP structures policy reasoning
- Notice the L1 cleaning decisions - this is where bias typically hides
- See L2 scenarios - how assumptions drive outcomes
- Study L3 stakeholder mapping - who wins, who loses, who's missing
- Review L4 accountability - who decided what and why
- Consider L5 - what would *you* fork and change?

### Fork This Document

This example is explicitly designed to be challenged:

**Disagree with the LVT rate?** Fork it and change `l2_consequence_simulation.variables.independent` to use 0.5% or 1.5% instead of 1%.

**Think the profit tax should be higher?** Fork it and update the scenarios with your preferred rate.

**Believe the stakeholder analysis missed a group?** Fork it and add them to `l3_empathy_mapping.stakeholder_map`.

**Have better data?** Fork it and replace the illustrative datasets in L1 with real transaction data from Danmarks Statistik.

The diff between your fork and the original will show exactly where you disagree - making the debate precise and productive rather than rhetorical.

---

## Original Markdown Version

The original narrative explanation is available in `danish_property_tax_reform.md`. The YAML version in this directory is the validated, schema-compliant extract.

The markdown is useful for understanding the *reasoning*. The YAML is useful for *validating*, *comparing*, and *forking* that reasoning.

---

## Adding Your Own Example

Have an ORP-compliant document you'd like to contribute as a reference?

1. Validate it first: `orp validate your-document.yaml`
2. Ensure it achieves at least ORP-Standard compliance
3. Add it to this directory
4. Update this README with a description
5. Submit a merge request to https://gitlab.com/publicreason/orp

See `docs/CONTRIBUTING.md` for guidelines.

---

*These examples are living documents. As the ORP specification evolves, examples may be updated to reflect new requirements or best practices.*
