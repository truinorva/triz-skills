---
name: contradiction-solver
description: "TRIZ Contradiction Solver and 40 Inventive Principles — resolves engineering and physical contradictions using the Altshuller Matrix, Matrix 2003, and the 40 Inventive Principles. Use this skill whenever the user mentions 'contradiction', 'inventive principles', '40 principles', 'Altshuller', 'Matrix 2003', 'engineering contradiction', 'technical contradiction', 'technischer Widerspruch', 'physical contradiction', 'physikalischer Widerspruch', 'IF THEN BUT', 'WENN DANN ABER', or wants to solve a technical trade-off, improve a system parameter without worsening another, or apply TRIZ contradiction analysis. For a purely physical contradiction — one parameter of one component required to take two opposing values — prefer the 'physical-contradictions' skill, which carries both documented strategy sets and the applicability check; use this skill for engineering contradictions, matrix lookups, and free application of the 40 Inventive Principles."
---

<!-- 
  Based on the TRIZ Contradiction Solver and 40 Inventive Principles Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Contradiction Solver and 40 Inventive Principles

Identify and solve engineering and physical contradictions using TRIZ principles and tools such as the Altshuller Matrix, Matrix 2003, and the 40 Inventive Principles.

## Reference files

All reference data is in the `references/` directory. Read files as needed:

- **40 Inventive Principles:** `40_Inventive_Principles_EN.md` (English), `40_Innovationsprinzipien_DE.md` (German) — detailed descriptions with synonyms, sub-principles, and examples
- **Application guidance:** `40IP_Applications.csv` — whether each principle applies to component, system, or environment
- **Altshuller Matrix:** `Altshuller_39_Parameters.csv` (parameters), `Altshuller_Contradiction_Matrix_AI.csv` (matrix lookup)
- **Matrix 2003:** `Matrix_2003_Parameters.csv` (parameters), `Matrix_2003_AI.csv` (matrix lookup)
- **Process guides:** `Solving_Engineering_Contradictions_Altshuller_Matrix.txt`, `Solving_Engineering_Contradictions_Matrix_2003.txt`, `Solving_Physical_Contradictions.txt`
- **Examples:** `examples.txt`

The process guides tell you to look principles up in "40 Inventive Principles Booklet EN.pdf" / "40 Innovationsprinzipien Booklet DE.pdf". Those are historical file names — use `40_Inventive_Principles_EN.md` / `40_Innovationsprinzipien_DE.md` in `references/` instead.

## Interaction flow

1. **Problem input.** Ask the user for a problem statement or task. Wait for user input.

2. **Identify the contradiction type:** engineering contradiction or physical contradiction. Help the user formulate at least a goal or problem.

3. **Apply the appropriate method:**
   - If an engineering contradiction is given: ask whether to use the Altshuller Matrix or Matrix 2003, then follow the corresponding process guide step by step
   - If a physical contradiction is given: prefer the `physical-contradictions` skill; if it is not available, follow the process in `Solving_Physical_Contradictions.txt` step by step, with the corrections under *Solving physical contradictions* below
   - If no contradiction is specified: apply the 40 Inventive Principles directly and analyze their applicability to the user's case

4. **System context.** When analyzing the technical system, classify it into super-system, technical system, and sub-system via component analysis.

## Key definitions

### Engineering Contradiction
A statement where improving one feature leads to deterioration of another.
- English: "IF ..., THEN ..., BUT ..."
- German: "WENN ..., DANN ..., ABER ..."

**Both names mean the same thing.** *Engineering contradiction (EC)* and *technical contradiction (TC)* are two names for one concept — a parametric model in which improving one parameter of the engineering system worsens another. Understand either term when the user uses it, in English or German (*technischer Widerspruch*). The house style of the Truinorva glossary leads with *technical contradiction*; the TRIZ prompt sources and VDI 4521 use *engineering contradiction*.

Example: "IF the engine gets stronger, THEN the car can go faster, BUT it consumes more fuel."

### Physical Contradiction
A situation where a parameter must simultaneously take two opposing values for valid reasons (goal or natural law).
- English: "... TO ..., AND ... TO ..."
- German: "... DAMIT ..., UND ... DAMIT ..."

Example: "A boat should be wide TO prevent capsizing, AND it should be narrow TO make it go fast."

Always include both reasons — they are necessary to identify solutions. A justification takes one of two forms: a goal or requirement to be achieved, or a law of nature or inherent property. **A requirement without such a justification is not a contradiction — it points to a solution.**

Full form, and the form to use when handing over to the `physical-contradictions` skill:

> **[Parameter]** of **[component]** SHOULD be **[value 1]** IN ORDER TO **[justification 1]** AND SHOULD be **[value 2]** IN ORDER TO **[justification 2]**.

plus the **Key Problem**: *"How can we [positive effect] without [negative effect]?"*

### Nomenclature
In English: refer to Genrikh Saulovich Altshuller and the Altshuller Matrix.
In German: refer to Genrich Saulowitsch Altschuller and the Altschuller Matrix.

## Solving engineering contradictions

The Altshuller Matrix and Matrix 2003 have **different** parameter sets — keep them clearly separated.

For the **Altshuller Matrix**: read `Solving_Engineering_Contradictions_Altshuller_Matrix.txt` and follow its 7 steps. Use `Altshuller_39_Parameters.csv` for parameters and `Altshuller_Contradiction_Matrix_AI.csv` for the matrix lookup.

For the **Matrix 2003**: read `Solving_Engineering_Contradictions_Matrix_2003.txt` and follow its 7 steps. Use `Matrix_2003_Parameters.csv` for parameters and `Matrix_2003_AI.csv` for the matrix lookup.

**Match Matrix 2003 parameters by their two-digit number, not by their wording**, and cite them as number plus canonical name, e.g. `03 Length/Angle of Moving Object`. A bare number is always a parameter; an Inventive Principle is always written `IP #n`. Their ranges overlap — parameters run 01–48, principles 1–40 — so never drop the `IP #`.

## Solving physical contradictions

**Hand over if you can.** If the `physical-contradictions` skill is available, use it instead of the process below. It carries both documented strategy sets — the Litvin variant and the Zlotin/Zusman variant — with binding EN/DE terminology, an explicit applicability check, and the recommended Inventive Principles per strategy. Hand the contradiction over in the full form given under *Key definitions*.

Otherwise follow `Solving_Physical_Contradictions.txt` step by step. Help the user express a parameter with two opposing values and justify both sides.

**Terminology.** The binding names of the six methods are *Separation in space*, *Separation in time*, *Separation in relation*, *Separation in system level*, *Satisfy*, *Bypass* (DE: *Separation im Raum*, *Separation in der Zeit*, *Separation in der Beziehung*, *Separation durch Systemübergang*, *Befriedigung*, *Umgehung*). The file's variant wordings — "separation at the system level", "separation in place", "satisying" — denote the same six methods; use the binding names in your answer.

**Applicability.** Judge each method and give a reason for every "not applicable":

- *Space* and *time* apply only if the places or periods concerned do **not** overlap. Different but overlapping periods are not enough — a door is a compromise, not a resolution.
- *Relation* requires that the two justifications originate from two different components — **components of the super-system count** — and that a usable property in which they differ can be found.
- *System level* is in principle always applicable; the question is only whether a concrete solution can be derived from it. Never mark it "not applicable" without having tried.
- *Satisfy* fits when the two requirements refer to almost — but not exactly — the same property (different frames of reference, smart materials, scientific effects).
- *Bypass* fits when the contradiction follows from the chosen **operating principle** rather than from the **purpose** of the system. Last resort.

Work the six methods in the order given by the file, document ideas for **every** applicable method, and cite each principle with number and name — never numbers alone.

## Ambiguous tasks (no clear contradiction)

If no Engineering Contradiction or Physical Contradiction is given or can be derived, apply the 40 Inventive Principles directly: look up principles in `40_Inventive_Principles_EN.md` (or DE version), consider synonyms, sub-principles, and examples. Use `40IP_Applications.csv` to recommend whether the principle applies to component, system, or environment level.
