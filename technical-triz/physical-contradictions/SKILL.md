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

Read these on demand from `references/`. Where a file exists in an EN and a DE version, open the version matching the user's language — the strategy and principle names are binding only in their own language.

| File | Content |
|---|---|
| `Terminology_and_Applicability_EN_DE.md` | **Binding** EN/DE terminology of both variants (sections 1–3) plus the applicability check (section 5). Consult it before naming a strategy or judging applicability. |
| `Separation_Principles_Litvin_EN.md` / `Separationsprinzipien_Litvin_DE.md` | Litvin variant: strategy table with recommended Inventive Principles, working order, conditions of applicability (section 3), worked examples with further applicability hints per method (section 4). |
| `Separation_Principles_Zlotin_Zusman_EN.md` / `Separationsprinzipien_Zlotin_Zusman_DE.md` | Zlotin/Zusman variant: strategy table with recommended Inventive Principles, the five guiding questions (Where? / When? / Under which condition?), and the Venn diagram segments (section 3). |
| `40_Inventive_Principles_EN.md` / `40_Innovationsprinzipien_DE.md` | All 40 principles with explanations and examples. Look up every cited principle here before applying it. |

*Names used inside the reference files come from the upstream prompt repository.* `physical_contradictions.xml` means this `SKILL.md`; the folder `contradiction_solver_40_inventive_principles` means `../contradiction-solver/references/` in this repository.

## Relation to other skills

Engineering contradictions, Altshuller Matrix / Matrix 2003 lookups, and free application of the 40 Inventive Principles belong to `contradiction-solver`; contradictions extracted from patent texts to `patent-analyzer`. This skill takes over as soon as one parameter of one component must take two opposing values.

## Interaction flow

1. **Problem statement.** Ask the user for their problem statement and wait for input. Useful input: the conflicting requirements, the parameter concerned, the reason for each of the two values, and known constraints.

2. **Check for a physical contradiction.** Is the same parameter of the same component required to take two opposing values? If the user brings an *engineering* contradiction instead, convert it first: name the improving and the worsening parameter — if both refer to the **same** parameter of the same component, that parameter with its two required values *is* the physical contradiction; otherwise ask which single parameter carries the trade-off. Keep the engineering contradiction on record — `contradiction-solver` can work it with the Matrix in parallel.

3. **Formulate the contradiction:**

   > **[Parameter]** of **[component]** SHOULD be **[value 1]** IN ORDER TO **[justification 1]** AND SHOULD be **[value 2]** IN ORDER TO **[justification 2]**.

   *(DE: „**[Parameter]** von **[Komponente]** SOLL **[Wert 1]** SEIN, DAMIT **[Begründung 1]**, UND SOLL **[Wert 2]** SEIN, DAMIT **[Begründung 2]**.")*

   Plus the **Key Problem**: *"How can we [positive effect] without [negative effect]?"* — *(DE: „Wie können wir [positiver Effekt] erreichen, ohne [negativer Effekt]?")*

   If a justification is missing, **ask for it before continuing** — the justifications decide which strategy is applicable at all.

4. **Ask the user which resolution framework to use** (see Modes below). Default if they have no preference: **Mode C**.

5. **Check every strategy** of the chosen framework against the applicability conditions in section 5 of `Terminology_and_Applicability_EN_DE.md`. State for each strategy whether it is applicable **and why**. Read the rows for the variant you are in — the table groups Litvin and Zlotin/Zusman categories by shared test criterion, but section 3 of the same file governs which category is which.

6. **Derive solutions.** For every applicable strategy, look up the recommended Inventive Principles in the variant file and derive at least one concrete solution idea per principle used. Cite each as `IP #<number> <name>`.

7. **Present the result** in tabular form (see Output format).

8. **Offer to continue** — searching across all 40 Inventive Principles, and detailing the most promising ideas.

## Modes

### Mode A — Litvin

Litvin variant only (`Separation_Principles_Litvin_EN.md` / `Separationsprinzipien_Litvin_DE.md`). Work through the six methods in this fixed order, moving on whenever the current method yields no solution. Document ideas for **every** applicable method — do not stop at the first one that works:

1. Separation in space (*Separation im Raum*)
2. Separation in time (*Separation in der Zeit*)
3. Separation in relation (*Separation in der Beziehung*)
4. Separation in system level (*Separation durch Systemübergang*)
5. Satisfy (*Befriedigung*)
6. Bypass (*Umgehung*)

### Mode B — Zlotin/Zusman

Zlotin/Zusman variant only (`Separation_Principles_Zlotin_Zusman_EN.md` / `Separationsprinzipien_Zlotin_Zusman_DE.md`). Check all five strategies:

1. Separation in Space (*Separation im Raum*)
2. Separation in Time (*Separation in der Zeit*)
3. Separation on Condition (*Separation durch Bedingungswechsel*)
4. Separation between the parts and the whole (*Separation zwischen den Einzelteilen und der Gesamtheit*)
5. Transition to Alternative System (*Übergang zu einem alternativen System*) — with four sub-variants: Transition to Sub-System (*Wechsel zum Subsystem*), to Super-System (*Wechsel zum Supersystem*), to Alternative System (*Wechsel zu einem alternativen System*), to Inverse System (*Wechsel zum inversen System*)

If more than one of Space / Time / Condition applies, use the Venn diagram segments in that variant file to pick the most probable principles. Table and Venn diagram are two independent representations from the source and do not always assign the same principle to the same strategy — treat the table as the primary mapping and the diagram as an additional idea generator, never as a correction of the table.

### Mode C — Combined (default)

Run Mode A completely, then Mode B for everything A could not resolve and as an additional idea generator. Present both variants in **separate, labelled sections**, keep their terminology strictly apart, and close with a comparison.

## Key definitions

- **Physical Contradiction.** A single parameter of one component must simultaneously take two opposing values to satisfy conflicting requirements. Complete only with a justification for each value: either (a) a goal or requirement to be achieved, or (b) a law of nature or an inherent property. *A requirement without such a justification indicates a solution, not a contradiction.*

- **Separation.** Resolving a contradiction by distributing the conflicting requirements — across space, time, relation/condition, or system levels — so that each requirement is met where, when, for whom, or on which level it is actually needed.

- **Satisfy and Bypass** (Litvin variant only). *Satisfy:* both requirements are met simultaneously rather than separately, usually because they refer to almost — but not exactly — the same property (smart materials, scientific effects). *Bypass:* the system, typically its operating principle, is changed so that the contradiction becomes irrelevant. Last resort. Applicability test: does the contradiction follow from the chosen **operating principle** rather than from the **purpose** of the system? Only then can Bypass dissolve it.

- **Justification.** Each of the two values needs one, and it takes one of two forms: (a) a goal or requirement that must be achieved — if the parameter had that value, the goal would be met; or (b) a law of nature or an inherent property of a component or material.

## Core rules

- **Never mix the terminology of the two variants.** "Separation on Condition" (Zlotin/Zusman) is not "Separation in relation" (Litvin), and "Separation between the parts and the whole" (Zlotin/Zusman) is not "Separation in system level" (Litvin). Satisfy and Bypass exist only in the Litvin variant.
- **Use exclusively the binding terminology of the selected variant, in the user's language.** The EN/DE tables in sections 1 and 2 of `Terminology_and_Applicability_EN_DE.md` are binding — never paraphrase a strategy name and never translate one yourself.
- **Space and time require non-overlap.** Separation in space and in time are applicable only if the places or periods concerned do **not** overlap. Different but overlapping periods are not sufficient — a door is a compromise, not a resolution.
- **Separation in relation needs two different components.** The two justifications must originate from two different components — **components of the super-system count** (dog vs. thief, sunlight vs. air molecules) — and a usable property in which they differ must be found. The difference alone is not enough.
- **Separation in system level is in principle always applicable** (Litvin). The question is never *whether* it applies but whether a concrete solution can be derived from it, which often takes considerable effort. Never mark it "not applicable" without having tried.
- **The recommended Inventive Principles are short-cuts, not a restriction.** Searching across all 40 principles is always allowed.
- Never present a contradiction without both justifications; ask if one is missing.
- Judge applicability only via the applicability check; give a reason for every "not applicable".
- Cite Inventive Principles with number and name and derive a concrete idea — never list numbers alone.
- **One known conflict in the neighbouring skill.** `contradiction-solver/references/Solving_Physical_Contradictions.txt` lists IP #13 under *Satisfying*. The Litvin 1993 table assigns #13 to *Bypass* only — `Separation_Principles_Litvin_EN.md` governs. All other assignments in that file agree with the Litvin table.
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

The requirements apply at different moments → **separation in time** (IP #15 Dynamization, IP #10 Preliminary Action, IP #34 Discarding and Recovering): fill a frozen liqueur core and cast the shell around it.

### Garage

Closed so the car stays dry, open so you can drive in: the regions do not overlap → **separation in space** (IP #1 Segmentation, IP #2 Separation, IP #3 Local Quality) — a carport.

Justified instead with *"so that no thief gets to the car"*, the regions overlap and the carport fails. This is why the justifications must be captured before choosing a strategy.

More worked examples (swimming pool, house wall, dog flap, sandblasting, chain, roundabout, treadmill, steam locomotive, drill) are in section 4 of the Litvin reference files.
