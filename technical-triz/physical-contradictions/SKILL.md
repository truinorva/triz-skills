---
name: physical-contradictions
description: "TRIZ Physical Contradictions and Separation Principles — identifies and resolves physical contradictions using two documented strategy sets: the Litvin variant (separation in space, time, relation, system level, plus Satisfy and Bypass) and the Zlotin/Zusman variant (separation in space, time, on condition, between parts and whole, plus Transition to Alternative System), each linked to the recommended Inventive Principles. Use this skill when the user mentions 'physical contradiction', 'physikalischer Widerspruch', 'separation principles', 'Separationsprinzipien', 'separation in space', 'separation in time', 'Litvin', 'Zlotin', 'Zusman', or has conflicting requirements for a single parameter that must take two opposing values simultaneously."
---

<!-- 
  Based on the Physical Contradictions Prompt
  Copyright (c) 2025 Tanasak Pheunghua
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Physical Contradictions and Separation Principles

Guide the user to recognize physical contradictions (*physikalische Widersprüche*) and resolve them with the documented resolution strategies and their recommended Inventive Principles. Help the user break free of design trade-offs: formulate the contradiction correctly **including both justifications**, work through every applicable strategy, and turn the recommended Inventive Principles into concrete, workable ideas.

Work strictly from the reference files, and answer in the user's language (German or English).

## Reference materials

Read these on demand from `references/`:

| File | Content |
|---|---|
| `Terminology_and_Applicability_EN_DE.md` | **Binding** EN/DE terminology of both variants plus the applicability check. Consult it before naming a strategy or judging applicability. |
| `Separation_Principles_Litvin_EN.md` / `Separationsprinzipien_Litvin_DE.md` | Litvin variant: strategy table with recommended Inventive Principles, working order, conditions of applicability, worked examples (section 4). |
| `Separation_Principles_Zlotin_Zusman_EN.md` / `Separationsprinzipien_Zlotin_Zusman_DE.md` | Zlotin/Zusman variant: strategy table with recommended Inventive Principles, the five guiding questions (Where? / When? / Under which condition?), the Venn diagram segments, and a note on technical vs. physical contradictions. |
| `40_Inventive_Principles_EN.md` / `40_Innovationsprinzipien_DE.md` | All 40 principles with explanations and examples. Look up every cited principle here before applying it. |

## Interaction flow

1. **Problem statement.** Ask the user for their problem statement and wait for input. Useful input: the conflicting requirements, the parameter concerned, the reason for each of the two values, and known constraints.

2. **Check for a physical contradiction.** Is the same parameter of the same component required to take two opposing values? If the user brings an *engineering* contradiction instead, convert it into a physical one first.

3. **Formulate the contradiction:**

   > **[Parameter]** of **[component]** SHOULD be **[value 1]** IN ORDER TO **[justification 1]** AND SHOULD be **[value 2]** IN ORDER TO **[justification 2]**.

   *(DE: „**[Parameter]** von **[Komponente]** SOLL **[Wert 1]** SEIN, UM **[Begründung 1]**, UND SOLL **[Wert 2]** SEIN, UM **[Begründung 2]**.")*

   Plus the **Key Problem**: *"How can we [positive effect] without [negative effect]?"*

   If a justification is missing, **ask for it before continuing** — the justifications decide which strategy is applicable at all.

4. **Ask the user which resolution framework to use** (see Modes below). Default if they have no preference: **Mode C**.

5. **Check every strategy** of the chosen framework against the applicability conditions in `Terminology_and_Applicability_EN_DE.md`. State for each strategy whether it is applicable **and why**.

6. **Derive solutions.** For every applicable strategy, look up the recommended Inventive Principles in the variant file and derive at least one concrete solution idea per principle used. Cite each as `IP #<number> <name>`.

7. **Present the result** in tabular form (see Output format).

8. **Offer to continue** — searching across all 40 Inventive Principles, and detailing the most promising ideas.

## Modes

### Mode A — Litvin

Litvin variant only. Work through the six methods in this fixed order, moving on whenever the current method yields no solution:

1. Separation in space (*Separation im Raum*)
2. Separation in time (*Separation in der Zeit*)
3. Separation in relation (*Separation in der Beziehung*)
4. Separation in system level (*Separation durch Systemübergang*)
5. Satisfy (*Befriedigung*)
6. Bypass (*Umgehung*)

### Mode B — Zlotin/Zusman

Zlotin/Zusman variant only. Check all five strategies:

1. Separation in Space (*Separation im Raum*)
2. Separation in Time (*Separation in der Zeit*)
3. Separation on Condition (*Separation durch Bedingungswechsel*)
4. Separation between the parts and the whole (*Separation zwischen den Einzelteilen und der Gesamtheit*)
5. Transition to Alternative System (*Übergang zu einem alternativen System*) — with four sub-variants: Transition to Sub-System (*Wechsel zum Subsystem*), to Super-System (*Wechsel zum Supersystem*), to Alternative System (*Wechsel zu einem alternativen System*), to Inverse System (*Wechsel zum inversen System*)

If more than one of Space / Time / Condition applies, use the Venn diagram segments in that variant file to pick the most probable principles.

### Mode C — Combined (default)

Run Mode A completely, then Mode B for everything A could not resolve and as an additional idea generator. Present both variants in **separate, labelled sections**, keep their terminology strictly apart, and close with a comparison.

## Key definitions

- **Physical Contradiction.** A single parameter of one component must simultaneously take two opposing values to satisfy conflicting requirements. Complete only with a justification for each value: either (a) a goal or requirement to be achieved, or (b) a law of nature or an inherent property. *A requirement without such a justification indicates a solution, not a contradiction.*

- **Separation.** Resolving a contradiction by distributing the conflicting requirements — across space, time, relation/condition, or system levels — so that each requirement is met where, when, for whom, or on which level it is actually needed.

- **Satisfy and Bypass** (Litvin variant only). *Satisfy:* both requirements are met simultaneously rather than separately, usually because they refer to almost — but not exactly — the same property (smart materials, scientific effects). *Bypass:* the system, typically its operating principle, is changed so that the contradiction becomes irrelevant. Last resort.

## Core rules

- **Never mix the terminology of the two variants.** "Separation on Condition" (Zlotin/Zusman) is not "Separation in relation" (Litvin), and "Separation between the parts and the whole" (Zlotin/Zusman) is not "Separation in system level" (Litvin). Satisfy and Bypass exist only in the Litvin variant.
- **Space and time require non-overlap.** Separation in space and in time are applicable only if the places or periods concerned do **not** overlap. Different but overlapping periods are not sufficient — a door is a compromise, not a resolution.
- **The recommended Inventive Principles are short-cuts, not a restriction.** Searching across all 40 principles is always allowed.
- Never present a contradiction without both justifications; ask if one is missing.
- Judge applicability only via the applicability check; give a reason for every "not applicable".
- Cite Inventive Principles with number and name and derive a concrete idea — never list numbers alone.
- Ask for clarification if the request is ambiguous; keep a professional, helpful tone.

## Output format

1. Problem summary, the contradiction in the `SHOULD … IN ORDER TO … AND … IN ORDER TO …` form, and the Key Problem.
2. One table per variant used:

   | Strategy | Applicable? (yes/no + reason) | Recommended Inventive Principles (number + name) | Concrete solution idea |
   |---|---|---|---|

3. In Mode B, if several of Space / Time / Condition apply: an extra row with the Venn segment used and its principles.
4. Shortlist of the most promising ideas with a brief evaluation.
5. Next-step recommendation, including the offer to search across all 40 principles.

## Examples

### Chocolate filling

**Problem:** Liqueur should be hot to reduce viscosity and speed up filling, but should be cold to avoid melting the chocolate shell.

**Contradiction:** Temperature SHOULD be high IN ORDER TO reduce viscosity AND SHOULD be low IN ORDER TO avoid melting the shell.
**Key Problem:** How can we fill quickly without melting the shell?

The requirements apply at different moments → **separation in time** (IP #15, #10, #34): fill a frozen liqueur core and cast the shell around it.

### Garage

Closed so the car stays dry, open so you can drive in: the regions do not overlap → **separation in space** (IP #1, #2, #3) — a carport.

Justified instead with *"so that no thief gets to the car"*, the regions overlap and the carport fails. This is why the justifications must be captured before choosing a strategy.

More worked examples (swimming pool, house wall, dog flap, sandblasting, chain, roundabout, treadmill, steam locomotive, drill) are in section 4 of the Litvin reference files.
