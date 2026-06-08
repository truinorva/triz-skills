---
name: contradiction-solver
description: "TRIZ Contradiction Solver and 40 Inventive Principles — resolves engineering and physical contradictions using the Altshuller Matrix, Matrix 2003, and the 40 Inventive Principles. Use this skill whenever the user mentions 'contradiction', 'inventive principles', '40 principles', 'Altshuller', 'Matrix 2003', 'engineering contradiction', 'physical contradiction', 'IF THEN BUT', or wants to solve a technical trade-off, improve a system parameter without worsening another, or apply TRIZ contradiction analysis."
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

## Interaction flow

1. **Problem input.** Ask the user for a problem statement or task. Wait for user input.

2. **Identify the contradiction type:** engineering contradiction or physical contradiction. Help the user formulate at least a goal or problem.

3. **Apply the appropriate method:**
   - If an engineering contradiction is given: ask whether to use the Altshuller Matrix or Matrix 2003, then follow the corresponding process guide step by step
   - If a physical contradiction is given: follow the process in `Solving_Physical_Contradictions.txt` step by step
   - If no contradiction is specified: apply the 40 Inventive Principles directly and analyze their applicability to the user's case

4. **System context.** When analyzing the technical system, classify it into super-system, technical system, and sub-system via component analysis.

## Key definitions

### Engineering Contradiction
A statement where improving one feature leads to deterioration of another.
- English: "IF ..., THEN ..., BUT ..."
- German: "WENN ..., DANN ..., ABER ..."

Example: "IF the engine gets stronger, THEN the car can go faster, BUT it consumes more fuel."

### Physical Contradiction
A situation where a parameter must simultaneously take two opposing values for valid reasons (goal or natural law).
- English: "... TO ..., AND ... TO ..."
- German: "... DAMIT ..., UND ... DAMIT ..."

Example: "A boat should be wide TO prevent capsizing, AND it should be narrow TO make it go fast."

Always include both reasons — they are necessary to identify solutions.

### Nomenclature
In English: refer to Genrikh Saulovich Altshuller and the Altshuller Matrix.
In German: refer to Genrich Saulowitsch Altschuller and the Altschuller Matrix.

## Solving engineering contradictions

The Altshuller Matrix and Matrix 2003 have **different** parameter sets — keep them clearly separated.

For the **Altshuller Matrix**: read `Solving_Engineering_Contradictions_Altshuller_Matrix.txt` and follow its 7 steps. Use `Altshuller_39_Parameters.csv` for parameters and `Altshuller_Contradiction_Matrix_AI.csv` for the matrix lookup.

For the **Matrix 2003**: read `Solving_Engineering_Contradictions_Matrix_2003.txt` and follow its 7 steps. Use `Matrix_2003_Parameters.csv` for parameters and `Matrix_2003_AI.csv` for the matrix lookup.

## Solving physical contradictions

Read `Solving_Physical_Contradictions.txt` and follow its instructions step by step. Help the user express a parameter with two opposing values and justify both sides.

## Ambiguous tasks (no clear contradiction)

If no Engineering Contradiction or Physical Contradiction is given or can be derived, apply the 40 Inventive Principles directly: look up principles in `40_Inventive_Principles_EN.md` (or DE version), consider synonyms, sub-principles, and examples. Use `40IP_Applications.csv` to recommend whether the principle applies to component, system, or environment level.
