<!-- 
  Based on the Derivative Resources Analysis Prompt (Extended TRIZ Framework V4.0)
  Copyright (c) 2025-2026 Tanasak Pheunghua
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# The 14 steps, the three tables and the report

Full specification of the procedure summarized in `SKILL.md`. The operator catalogue used in
steps 6 and 7 is in `derivative-resource-operators.md`; the inventory grid used in steps 3 and 4
is in `resource-search-grid.md`.

---

## Step 1 — Problem framing

Check that these are known:

- the technical system or process,
- its Main Useful Function (*Hauptnutzfunktion*),
- the problem or improvement objective,
- the constraints,
- the operating conditions.

If essential items are missing, ask only the minimum questions needed. If the user already
supplied something, proceed without asking again.

**Output:** Problem Statement · Main Useful Function · Desired Improvement · Constraints ·
System Boundary.

If you *infer* the Main Useful Function rather than being told it, say so explicitly and ask for
confirmation before building on it.

## Step 2 — Problem localization

Identify:

- the conflict or contradiction, both technical and physical;
- the product and the tool;
- the useful interaction;
- the harmful, excessive, insufficient or missing interaction.

Then define:

- **Operating Zone (OZ)** — *where* the problem occurs;
- **Operating Time (OT)** — *when*: before, during, after, idle, transition, periodic.

**Output:** a short Problem Focus table and an OT table.

| Problem Focus | |
|---|---|
| Product | |
| Tool | |
| Useful interaction | |
| Harmful / insufficient / missing interaction | |
| Technical contradiction | |
| Physical contradiction | |
| Operating Zone (OZ) | |

| OT phase | Present? | What happens | Resources free in this phase |
|---|---|---|---|
| Before | | | |
| During | | | |
| After | | | |
| Idle | | | |
| Transition | | | |
| Periodic | | | |

## Step 3 — Existing resource inventory (Table A)

Sweep the two-dimensional grid in `resource-search-grid.md` — every **source** against every
**type**. Record what exists, not what you would like to exist.

**Table A columns:**

| ID | Source | Type | Resource / Property | Current value or state | Location and time | Current role |
|---|---|---|---|---|---|---|

- `ID` — `A1`, `A2`, … so later tables can refer to the row.
- `Current value or state` — write `unknown` rather than guessing. A guessed temperature,
  pressure or material is worse than an admitted gap.
- `Current role` — what the resource does today, including *nothing* and *does harm*.

## Step 4 — Resource characterization

For the important resources, rate:

| Criterion | Scale |
|---|---|
| Quantity | insufficient / sufficient / abundant |
| Readiness | ready to use / needs preparation / needs development |
| Usefulness | harmful / neutral / useful |
| Cost | free / low / medium / high |
| Accessibility | direct / indirect / blocked |
| Controllability | high / medium / low / none |
| Stability | stable / varying / unpredictable |
| Compatibility | compatible / conditional / incompatible |
| Present in OZ | yes / partly / no |
| Present in OT | yes / partly / no |

Then flag the resources that are **free**, **waste**, **harmful**, **underused**, or **present in
the OZ and the OT** — those four groups are where the strong derivatives come from.

## Step 5 — Target effects

Before generating a single derivative, define what is actually needed: the Required Function,
the Desired Effect and the Target Object. Examples: reduce adhesion, remove deposit, detect
condition, separate two phases, absorb vibration.

Give each one an ID `E1`, `E2`, … Every derivative later has to point at one of them, which is
what keeps the analysis from degenerating into a list of curiosities.

## Step 6 — Classical derived resources

For each promising substance resource, test the six classical operators A–F from
`derivative-resource-operators.md`. Record:

| Existing Resource | Transformation | Derivative Resource | New Property / Effect | Possible Useful Function |
|---|---|---|---|---|

## Step 7 — Extended derivatives

Work through operator groups 7A–7J from `derivative-resource-operators.md`. Do not stop at the
first group that yields something — the groups find different things, and 7F (informational) in
particular tends to produce the cheapest candidates.

## Step 8 — Chains

Extend the promising resources one generation at a time: `R0 → R1 → R2 → R3`.

Stop a chain when:

- no new useful property appears,
- the cost explodes,
- feasibility becomes poor,
- or the required function is achieved.

**State the stop reason for every chain.** A chain abandoned without a reason looks the same as
one nobody tried.

## Step 9 — Derivative table (Table B)

**Table B columns:**

| DR ID | Source resource and location | Transformation operator | Mechanism | Derivative resource and generation | New property / effect | Useful function and target | Classical / Extended | Evidence or assumption |
|---|---|---|---|---|---|---|---|---|

Split it into **B1 (Classical ARIZ Core)** and **B2 (Extended Framework)** — nine columns in one
table is unreadable, and the split also enforces the labelling. Fold the source location into the
source column and the target into the function column to keep the width manageable.

## Step 10 — Evaluation (Table C)

Rate each candidate High / Medium / Low on: availability · transformation effort · cost ·
proximity to the OZ · availability in the OT · controllability · function match · feasibility ·
complexity · safety · environment · novelty · confidence.

For the report, condense to the columns a decision actually needs:

| DR ID | Required Function | Main Advantage | Main Limitation | Resource Expenditure | Feasibility | Risk | Confidence | Priority |
|---|---|---|---|---|---|---|---|---|

Prefer candidates that use internal resources, need little modification, perform the function
directly, exploit waste or harm, and raise ideality.

## Step 11 — Solution concepts

**Derivative Resource + Useful Function + Target = Solution Concept.**

For each lead concept, state these three separately — collapsing them is the most common failure
of this analysis:

1. **Derivative Resource** — what was created or revealed.
2. **Application** — what it could do.
3. **Solution Concept** — how to implement it in the system.

## Step 12 — Verification

For each lead concept, check:

- Does it perform the required function?
- Does it resolve or reduce the problem?
- Does it violate a constraint?
- Does it introduce a new harm?
- Does it need a new resource that defeats the purpose?
- Is the mechanism credible?
- Is it controllable?
- Does it need an experiment?

Where the facts are uncertain, write *Verification required*. Never fabricate mechanisms,
material properties or data to fill a gap.

## Step 13 — Resource priority rule

Use resources in this order, dropping to a lower level only when the higher ones are inadequate:

1. existing resources in the OZ and the OT,
2. internal system resources,
3. super-system and environment resources,
4. waste, harmful, cheap and free resources,
5. small modifications,
6. larger modifications,
7. new external substances, fields or components.

## Step 14 — Iteration

If no strong concept emerged:

- reconsider the Main Useful Function, the problem formulation, the system boundary, the OZ and
  the OT;
- search the resources that were ignored the first time;
- generate second-generation derivatives from the `R1` results;
- examine the super-system;
- search for scientific effects;
- repeat.

---

## Report structure

Deliver the sections in this order:

1. Problem Understanding
2. Main Useful Function
3. Operating Zone / Operating Time
4. Existing Resource Inventory (Table A)
5. Important Resource Properties
6. Required Effects
7. Classical Derived Resources (Table B1)
8. Extended Derivative Resources (Table B2)
9. Derivative Resource Chains
10. Candidate Evaluation (Table C)
11. Recommended Solution Concepts
12. Assumptions / Unknowns
13. Verification Required
14. Suggested Next Analysis

Fourteen sections with several wide tables do not fit a chat reply. Deliver the analysis as a
shareable document, keep a short summary in the chat, and write the document in the user's
language.

## Source policy

- Uploaded documents and the user's own data are the primary evidence.
- Cite reliable sources for specific physical, chemical or engineering effects where practical.
- Always distinguish **known fact**, **source-supported inference** and **engineering
  hypothesis**, and never present a hypothesis as established fact.
- Compute simple derived numbers from the user's data — averages per event, ratios between lines
  — and label them *computed*.
- List missing data explicitly under *Assumptions / Unknowns*; never guess values such as
  temperature, pressure or material.
- Mention it if a deadline or date in the source material has already passed.
