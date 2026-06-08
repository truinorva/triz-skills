---
name: sustainability-assessment
description: >
  Guides a structured sustainability assessment of production processes or
  product use phases using TRIZ Function Analysis. USE THIS SKILL whenever
  the user wants to assess environmental harm, identify waste streams, rank
  sustainability hotspots, or focus improvement efforts in any manufacturing,
  assembly, or product-in-use context — even without TRIZ vocabulary.
  Trigger on: "where should we focus", "which step is most harmful",
  "what waste do we generate", "sustainability hotspots", "circular economy",
  "Harm score", "FA-Process", "FA-Product", "most harmful steps",
  "environmental impact of our process", "LCA alternative", "SDG alignment",
  "which step to improve first", "cyclicity matrix". Also trigger proactively
  when a user describes a manufacturing or product context and asks where to
  focus — even with no sustainability vocabulary.
---

<!-- 
  Copyright (c) 2026 Horst Nähler
  Licensed under the MIT License -- see LICENSE in the repository root.
-->

# TRIZ Sustainability Assessment Skill

Guides users through a rapid, expert-estimation-based sustainability assessment
rooted in TRIZ Function Analysis, Circular Economy principles, and the UN SDGs.
No external databases or LCA software required.

> **Important**: This method produces *relative* rankings, not absolute
> environmental metrics. Always clarify this to the user — it is a rapid-scan
> complement to LCA/CFA, not a replacement.

---

## Step 1 — Scope the Analysis

Before doing anything else, ask the user:

1. **What product or process** are they assessing? (Brief description.)
2. **Which lifecycle phase** is in scope? (See lifecycle phases below.)
3. **Which analysis path** do they want to follow?
   - **Path A – FA-Process**: For the *Production / Realization* phase.
     Use when the user wants to assess a manufacturing or assembly process.
   - **Path B – FA-Product**: For the *Utilization / Service* phase.
     Use when the user wants to assess a product during its use phase.

If the user is unsure, recommend Path A for manufacturing contexts and Path B
for product-in-use contexts. If the lifecycle phase is unclear, ask.

Do not assign any scores or start modelling until you have answers to these
three questions.

### Lifecycle Phases (for reference)
1. Development / Design
2. **Production / Realization / Implementation** ← Path A target
3. Distribution
4. **Utilization / Service / Support** ← Path B target
5. Return
6. Reuse / Recycling
7. Landfill (to be eliminated)

---

## Step 2 — Route to the Correct Path

After scoping, **read the relevant reference file in full and keep it in context
for the rest of the session** before proceeding past this step:

- **Path A (FA-Process)** → read `references/path-a-process.md`
- **Path B (FA-Product)** → read `references/path-b-product.md`

Both paths use the **Harm Formula** defined below.

---

## Harm Formula (used in both paths)

```
Harm = (Amount + Cyclicity) × State × Impact
```

| Factor      | Description                                              | Range   |
|-------------|----------------------------------------------------------|---------|
| Amount      | % of input leaving a sub-step as waste (0–100)          | 0–100   |
| Cyclicity   | From the Cyclicity Matrix below                          | 1–24    |
| State       | Aggregate state of the waste (table below)               | 1–5     |
| Impact      | Toxicity / environmental impact (table below)            | 0.5–2   |

**Theoretical limits:** Min ≈ 0.5 · Max = 1,240

If Amount = 0 %, Harm = 0. No further evaluation needed for that loss.

### Aggregate State (State factor)

| State                        | Points |
|------------------------------|--------|
| Solid                        | 1      |
| Liquid                       | 2      |
| Fine dust / nebulised liquid | 3      |
| Gas                          | 4      |
| Field / Radiation            | 5      |

### Potential Impact / Toxicity (Impact factor)

| Classification                                      | Factor |
|-----------------------------------------------------|--------|
| Potentially supporting (biodegradable nutrients)    | 0.5    |
| Neutral                                             | 1      |
| Potentially toxic                                   | 2      |

### Cyclicity Matrix

Combine **Source** (row) × **Destination** (column):

|                    | Reuse | Recycling | Energy | Landfill |
|--------------------|-------|-----------|--------|----------|
| **Source: Reused** |   1   |     2     |    4   |    8     |
| **Source: Recycled**|  2   |     4     |    8   |   16     |
| **Source: Virgin** |   3   |     6     |   12   |   24     |

**Source definitions:**
- *Reused* — Input was previously used; re-entering with minor modification.
- *Recycled* — Input comes from a recycling process or certified sustainable cultivation.
- *Virgin* — Previously unused resource taken directly from the environment.

**Destination definitions:**
- *Reuse* — Waste directly reused in another process with minor modification.
- *Recycling* — Waste fed into a recycling process (material stays as material).
- *Energy* — Waste used as energy source (burning, biogas, composting for heat, composting for growing new material).
- *Landfill* — Waste dumped without further utilisation. Worst option.

> **Recycling vs. Energy distinction**: Recycling keeps material as material
> (re-melting, reforming). Energy converts material to heat/electricity (burning,
> composting). Guide the user to the more accurate category if unsure.

---

## Worked Examples (for calibration)

### Example A: Sheet Metal Cutting Offcut
- Amount = 3 %, Source = Virgin, Destination = Recycling → Cyclicity = 6
- State = Solid = 1, Impact = Neutral = 1
- **Harm = (3 + 6) × 1 × 1 = 9** ← Low harm

### Example B: Soldering Exhaust Gas
- Amount = 100 %, Source = Virgin, Destination = Landfill (vented) → Cyclicity = 24
- State = Gas = 4, Impact = Potentially toxic = 2
- **Harm = (100 + 24) × 4 × 2 = 992** ← Near-maximum harm; top priority

---

## Behavioural Constraints

- **Always ask before scoring.** Never assign factor values on behalf of the
  user without stating assumptions explicitly and inviting correction.
  Subject-matter expert judgement takes precedence over defaults.
- **Never skip or compress steps.** If the user pushes to move faster,
  acknowledge the request and explain which input is still needed before
  proceeding. Skipping steps produces unreliable relative rankings.
- **Clarify ambiguity first.** If a waste stream, source, or destination is
  unclear, ask before proceeding.
- **Consistent scoring matters most.** Relative rankings within a session are
  more valuable than absolute precision. Apply the same criteria throughout.
- **Never position this as an LCA replacement.** Always note that results are
  relative estimations to guide innovation focus.
- **Maintain a professional, methodical tone.** Explain reasoning transparently.

---

## Output Format Templates

### Detailed Function Model Table (Path A)

| Step | Sub-Step | Funct. Cat. | Funct. Rank | Input | Substance Type | Waste/Loss | Amount % | Source | Destination | Cyclicity | State | Impact | Harm |
|------|----------|-------------|-------------|-------|----------------|------------|----------|--------|-------------|-----------|-------|--------|------|

### Summary Portfolio Table (Path A)

| Step | Sum Funct. Rank | Norm. Functionality % | Sum Harm | Norm. Harm % |
|------|-----------------|----------------------|----------|--------------|

### Priority Issues Table (Path B)

| # | Issue | Severity | Frequency | Magnitude | Mitigation Difficulty |
|---|-------|----------|-----------|-----------|-----------------------|

### FA-Product Output (Path B)

- **Component list** with wear/harm flags
- **Critical interaction list** with interaction type and sustainability note
- **Priority Issues Table** (see template above)
- **Recommended next steps** per B6

Use bullet points and headers to structure long outputs. Define any TRIZ term
on first use.
