---
name: function-analysis
description: "TRIZ Function Analysis for technical systems — identifies tools, actions, objects, and functions, clarifies component relationships, and reveals the system's main function. Offers automatic, semi-automatic, and interactive working modes, and exports the finished function model as CSV for import into function-model tools. Use this skill when the user wants to perform a function analysis, identify functions in a technical system, map tools-actions-objects, create a function model, or export one as CSV. Also trigger on mentions of 'function analysis', 'function model', 'Funktionsanalyse', 'Funktionsmodell', 'tool-action-object', 'function carrier', 'Funktionsträger', or 'function model CSV'. For a dedicated map of how components interact along energy, matter, and information flow, use the function-interaction-analysis skill instead."
---

<!-- 
  Based on the TRIZ Function Analysis Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see the LICENSE file shipped with this Skill.
-->

# TRIZ Function Analysis

Guide users through a structured Function Analysis (*Funktionsanalyse*) of a technical system using TRIZ principles.

## Reference materials

Read `references/function_model_csv.md` once the function table is finished, before offering the CSV export. It carries how to offer it, the column layout, the controlled vocabulary, an example, and what to tell the user about importing the file.

## Step 1 — Choose a working mode

Ask the user which working mode they prefer, and wait for the answer:

- **Automatic** — build the whole analysis at once from your own assumptions, and state those assumptions explicitly.
- **Semi-automatic** — ask the four questions below, then build.
- **Interactive** — one step at a time: propose, wait for confirmation, continue.

Naming a system is **not** choosing a mode. If the user describes a system without picking one, ask again instead of assuming automatic.

**Semi-automatic** — ask these four questions before building:

1. Which system, and what is its main function?
2. Where does the system boundary run — what still belongs to the system, what is already super-system?
3. Which components do you already know?
4. Which problem is behind this analysis?

## Step 2 — Interaction flow

1. **Identify the system.** Ask the user: "What is your interesting technical system?" Wait for input.

2. **Component analysis.** Identify super-system, technical system, and sub-system components.

3. **Interaction analysis.** Analyze interactions between components from the component analysis. Ask: "Can you help me analyze the interactions?"

4. **Function Analysis.** Name the main function above the table, then write all relevant functions in tabular form, following the *Rules for the function model* below:

   | Tool | Action | Object | Category (U/H) | Degree of fulfillment (N/I/E or "---") | Changed/retained parameter |
   |---|---|---|---|---|---|

5. **Offer the CSV export.** When the table is finished, ask whether the user wants it as CSV — then **stop and wait** for the answer. See *CSV export* below.

## Rules for the function model

Three rules decide whether the model is usable.

### The system itself never appears in the model
Tool and object are always **components** — parts of the system, or elements of the super-system. The system as a whole is the heading above the model, never a line inside it.

- wrong: *Pizza cutter cuts pizza*
- right: *Cutting wheel cuts pizza*

The component analysis keeps its three levels — super-system, system, sub-system. The rule is about the **table**, not about the component list.

### One short active verb
One line, one verb, active, third person. This is where it fails most reliably, so the counter-examples matter more than the rule:

| | |
|---|---|
| right | *Cutting wheel cuts pizza* |
| passive | NOT: *Pizza is cut by the cutting wheel* |
| nominalisation | NOT: *Cutting wheel performs the cutting* |
| auxiliary | NOT: *Cutting wheel makes it possible that …* |
| two verbs | NOT: *Cutting wheel cuts and holds* — that is two lines |

A verb that needs a helper verb is not a function. If no short verb fits, the function has not been understood yet.

### The main function is named, but is not a line
Name it **above** the table, with its target and the parameter that changes. Do not write it into the table in the form *system – action – target*. In the table it is carried by a **component**:

- Main function: the pizza cutter cuts the pizza. Target: pizza. Parameter: structure.
- In the table: *Cutting wheel cuts pizza* — not *Pizza cutter cuts pizza*.

If no component can be named that carries the main function, the component analysis is incomplete. That is a finding, not a reason to put the system into the table.

## Key concepts

### Definition of Function
A function is an action performed by one component (the tool / function carrier, *Funktionsträger*) to change or maintain a parameter of another component (the object of the function). Examples: Broom moves dirt. Helmet stops stone. Display informs user.

### Function Classification
Functions are either useful (U) or harmful (H). Only useful functions are graded:
- **N** = Normal (adequate performance)
- **I** = Insufficient (underperforming)
- **E** = Excessive (overperforming)

Harmful functions receive "---" for degree of fulfillment.

### Magic Wand Test
To verify the legitimacy of a function: if removing the tool changes the object, a function exists.

### Main Function and Targets
The main function must always be identified. It determines the target component in the super-system — whose parameter changes due to the system's main function. In the CSV, that component carries `target` as its type.

**Example:** Main function of an airplane: Transport passengers and cargo. Targets: passengers and cargo. Changed parameter: geographic location. In the table it reads *Fuselage transports passengers* — not *Airplane transports passengers*.

## CSV export

After the table is finished, ask whether the user wants it as CSV — and then **stop and wait** for the answer. Ask in the user's own language and in your own words; never ask in English inside an answer in another language, and never answer your own question by outputting the CSV straight away.

The layout is `Carrier,Carrier Type,Action,Object,Object Type,Status,Parameter`. The header row, the type words (`standard | super | target`) and the status words (`normal | insufficient | excessive | harmful`) stay **English** even in an analysis in another language; names, verbs and parameters stay in the language of the analysis. The full format is in `references/function_model_csv.md`.
