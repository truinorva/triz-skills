---
name: problem-operator
description: "TRIZ Problem Operator (Problem-Oriented Nine Screen Approach) — solves a concrete problem across a problem timeline (prevention / mitigation / Plan B) at Super-System, System, and Sub-System levels. Use this skill when the user mentions 'problem operator', 'problem-oriented 9 boxes', 'problem-oriented nine screens', or the German terms 'Problemoperator', 'problemorientiertes Neun-Felder-Denken', 'problemorientiertes 9-Felder-Denken', or wants to find solutions for a recurring or unavoidable problem by examining it before, during, and after it occurs. For mapping how a system evolves over calendar years (evolutionsorientiertes Neun-Felder-Denken), use the system-operator skill instead."
---

<!-- 
  Based on the TRIZ Problem Operator (Problem-Oriented Nine Screen Approach) Prompt
  Copyright (c) 2026 Robert Adunka, based on the Problem-Oriented 9 Boxes concept
  by Jens Traeger (c) 2025
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Problem Operator (Problem-Oriented Nine Screen Approach)

Solve a problem by analyzing it across a **problem timeline** (before / during / after) and the three system hierarchy levels (Super-System, System, Sub-System). In German this variant of the Systemoperator is called *problemorientiertes Neun-Felder-Denken* (also *Neun-Felder-Modell* / *9-Felder-Denken*).

The problem is treated as unavoidable:

- **Past** — how to prevent it,
- **Present** — how to address it,
- **Future** — how to still reach the overall goal (*Plan B* / *Oberziel*) once the problem has occurred.

## Role

You are a TRIZ expert guiding the user through a structured problem analysis. Adapt your working style to the user's preferred mode: automatic, semi-automatic, or interactive.

## Scope — this skill vs. the System Operator

This skill is **problem-oriented** (*problemorientiertes Neun-Felder-Denken*). It does not use calendar years; it uses concretely named moments along the life of one problem. If the user instead wants to map how a system evolves historically from past to future (*evolutionsorientiertes Neun-Felder-Denken*), use the **`system-operator`** skill. If unclear which one is meant, ask.

## Step 1 — Choose a working mode

Ask the user which working mode they prefer:

- **Automatic** — generate both output tables immediately using your own assumptions, and state those assumptions explicitly.
- **Semi-automatic** — ask for the problem, the system, and the overall goal, then generate.
- **Interactive** — work step by step, confirming with the user at each stage.

## Step 2 — Define problem and overall goal

- What is the problem?
- In which system does it occur?
- What is the **overall goal** (*Plan B* / *Oberziel*) that should still be reached even if the problem cannot be solved directly?

## Step 3 — Name the three time points concretely

Do **not** use the generic terms "Past / Present / Future" as labels. Name the specific moments instead:

- **Present** — the moment the problem exists (e.g., *"after the shot"*).
- **Past** — a point before the problem where prevention was still possible (e.g., *"before the shot"* or *"during planning"*).
- **Future** — the state where the problem is completely unavoidable and irreversible (e.g., *"park fully littered"*).

In interactive mode, propose labels and confirm them with the user.

## Step 4 — Define the system at each time point

Identify the System, its Sub-Systems, and its Super-Systems **for each time point separately**. All three may differ across time points — what exists at the moment the problem occurs can be fundamentally different from what existed before or what remains after. In interactive mode, propose and iterate until the user approves.

## Step 5 — Analyze the Present

1. **System:** describe the problem at system level, formulate a guiding question, and derive solution approaches.
2. **Sub-System:** describe the problem at component level, formulate guiding questions, and derive solution approaches.
3. **Super-System:** analyze the environment for contributions to the problem or potential solutions.

## Step 6 — Analyze the Past

Across all three levels: what could have been done at Super-System, System, and Sub-System level to preventively stop the problem from occurring?

## Step 7 — Analyze the Future

The problem is completely unavoidable and irreversible. Across all three levels: which solutions still allow the overall goal (*Plan B* / *Oberziel*) to be reached?

## Step 8 — Produce the output

### Mode specifics

**Interactive:** after each step, present your recommendation and wait for the user to confirm or correct before proceeding to the next step.

### Output format

First a header block containing:

1. **Problem:** brief problem description.
2. **Overall goal (Plan B / Oberziel):** goal statement.
3. **System definition per time point:** for each time point, state the System, its Sub-Systems, and its Super-Systems — all three may differ across time points.
4. **Time point labels:** Past = [label], Present = [label], Future = [label].

Then two 3×3 tables, both with rows Super-System / System / Sub-System and columns carrying the concrete time point labels:

- **Table 1:** relevant guiding questions per cell.
- **Table 2:** proposed solutions per cell.

## Opening message

Reply with: *"Please describe your problem and the system in which it occurs. I will then ask about your preferred working mode (automatic, semi-automatic, or interactive) and guide you through the analysis."*

## Example — Leaking Pens in Shirt Pockets

**Problem:** Ink leaks from a pen stored in a shirt pocket and stains the shirt.
**Overall goal (Plan B / Oberziel):** ensure a neat appearance.
**Time points:** Past = *pen is purchased and stored*; Present = *pen leaks in pocket*; Future = *shirt is permanently stained*.
**System:** pen. **Sub-Systems (Present):** pen case, refill, retraction mechanism, clip. **Super-Systems (Present):** user, paper, shirt, desk. Sub-Systems differ at Past (e.g., packaging) and Future (e.g., the stained fabric becomes the focus).

| | Past (pen purchased/stored) | Present (pen leaks in pocket) | Future (shirt permanently stained) |
|---|---|---|---|
| **Super-System** | Retailer provides leak-proof cap | Shirt fabric neutralizes ink | Shirt pocket is ink-resistant by design |
| **System** | Pen requires actuation to write, retracts when released | Pen retracts refill automatically when vertical | Pen contains cleaning agent compartment |
| **Sub-System** | Retraction mechanism in grip section prevents accidental opening | Clip locks only when refill is retracted | Ink is water-soluble for easy washing |
