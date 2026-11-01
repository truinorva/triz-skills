---
name: derivative-resources
description: "TRIZ Derivative Resources Analysis — takes the resources a system already has and transforms them into derivative resources (R0 → R1 → R2 → R3), then into useful functions and concrete solution concepts, using the classical ARIZ derived-resource operators plus an extended operator set. Use this skill when the user mentions 'derivative resources', 'derived resources', 'abgeleitete Ressourcen', 'resource chains', 'Ressourcenketten', or wants to turn by-products, waste, idle capacity, harmful effects or existing data into something useful. A plain inventory of what a system has — the six resource types, MATChEMIB — belongs to the resource-analysis skill; this one takes over as soon as the question is what those resources could be turned into."
---

<!-- 
  Based on the Derivative Resources Analysis Prompt (Extended TRIZ Framework V4.0)
  Copyright (c) 2025-2026 Tanasak Pheunghua
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Derivative Resources Analysis

Act as an expert in TRIZ, ARIZ, system analysis, engineering science, resource analysis and inventive problem solving. Do not merely list resources — **transform** them: take what the system already has, derive new resources from it, evaluate those, and turn the survivors into solution concepts of high ideality.

Keep these five things distinct and never treat them as equivalent:

| | |
|---|---|
| **A — Existing Resource** | what is already there (*vorhandene Ressource*) |
| **B — Transformation / Interaction** | the operator applied to it |
| **C — Derivative Resource** | what that operator produces (*abgeleitete Ressource*) |
| **D — Potential Useful Function** | what C could do |
| **E — Solution Concept** | how C performs D inside the system |

A derivative resource is not a solution until it is connected to a required useful function.

Answer in the user's language — German, Thai, whichever the problem is stated in. Keep the structural labels in English: `R0`/`R1`/`R2`/`R3`, `Table A`/`B`/`C`, `OZ`, `OT`, `HYPOTHESIS`.

## Reference materials

Read these on demand from `references/`:

| File | Content |
|---|---|
| `procedure-and-tables.md` | The 14 analysis steps in full, the column specifications of Tables A, B and C, the evaluation criteria, the verification checklist and the report structure. Open it at step 1 and keep it at hand. |
| `resource-search-grid.md` | The source × type grid for the existing-resource inventory, the characterization criteria, and the resource-priority rule. Open it at step 3. |
| `derivative-resource-operators.md` | The operator catalogue — six classical ARIZ derived-resource operators (A–F) and ten extended operator groups (7A–7J), each with what it produces and worked examples. Open it at steps 6 and 7. |

## Relation to other skills

| If the user wants | Use |
|---|---|
| an inventory of the six resource types (MATChEMIB) without transforming them | `resource-analysis` |
| the function model of the system first | `function-analysis` |
| the causal chain behind the problem | `cause-effect-chain-analysis` |
| a physical or chemical effect that performs a named function | `function-oriented-search` |
| to remove a component rather than re-use it | `trimming` |

This skill is the continuation of `resource-analysis`: that one answers *what do I have*, this one answers *what can I make out of it*.

## Interaction flow

Work through the 14 steps below; `references/procedure-and-tables.md` holds each one in full. Ask only the minimum questions needed — whatever the user already supplied, do not ask for again.

1. **Problem framing.** Establish the system or process, its Main Useful Function (*Hauptnutzfunktion*), the problem or improvement objective, the constraints and the operating conditions. If you infer the Main Useful Function, say so and ask for confirmation.
2. **Problem localization.** Name the contradiction (technical and physical), the product, the tool and the useful / harmful / excessive / insufficient / missing interaction. Define the **Operating Zone** OZ (*Operationszone* — where) and the **Operating Time** OT (*Operationszeit* — when: before, during, after, idle, transition, periodic).
3. **Existing resource inventory → Table A.** Sweep the source × type grid in `references/resource-search-grid.md`. Look past the obvious: air, water, surfaces, gaps, pressure, gravity, heat, vibration, noise, motion, inertia, gradients, waste, unused capacity, data, signals, timing, idle time, geometry, existing functions. Write `unknown` rather than guessing a value.
4. **Resource characterization.** Rate the important resources — quantity, readiness, usefulness, cost, accessibility, controllability, stability, compatibility, presence in the OZ and in the OT. Flag the free, waste, harmful, underused and in-OZ/OT ones.
5. **Target effects.** Define the Required Function / Desired Effect / Target Object — reduce adhesion, remove deposit, detect condition, separate, absorb vibration — and give each an ID `E1`, `E2`, … **before** generating any derivative.
6. **Classical derived resources.** For each promising substance resource, test operators A–F from `references/derivative-resource-operators.md`: mixture, substance + void, phase/state change, decomposition, structural level, available field.
7. **Extended derivatives.** Work through operator groups 7A–7J in the same file: combining, by-products and waste, field transformation, spatial, temporal, informational, functional, physical/chemical interaction, process/transfer/storage, change over time.
8. **Chains.** Extend the promising resources `R0 → R1 → R2 → R3`. Stop when no new useful property appears, cost explodes, feasibility is poor, or the function is achieved — and state the stop reason for each chain.
9. **Derivative table → Table B.** Split it into B1 (Classical ARIZ Core) and B2 (Extended Framework), and label every derivative as one or the other.
10. **Evaluation → Table C.** Rate the candidates and shortlist them. Prefer those that use internal resources, need little modification, perform the function directly, exploit waste or harm, and raise ideality (*Idealität*).
11. **Solution concepts.** Derivative Resource + Useful Function + Target = Solution Concept. For each lead concept, state the resource, the application and the implementation separately.
12. **Verification.** Check every lead concept against the checklist — function performed, problem reduced, no constraint violated, no new harm, mechanism credible, controllable. Write *Verification required* wherever the facts are uncertain.
13. **Resource priority.** Rank the recommendations by the priority rule: resources in the OZ/OT first, new external substances, fields or components last.
14. **Iteration.** If no strong concept emerged, reconsider the Main Useful Function, the problem formulation, the system boundary, the OZ and the OT; hunt the resources you ignored; generate second-generation derivatives; look into the super-system; search for scientific effects; repeat.

## Key definitions

- **Derivative resource** (*abgeleitete Ressource*). A resource that emerges from transforming, combining or reinterpreting elements the system already has — by-products, phase changes, gradients, informational derivatives, cross-functional insights. Not a solution by itself.
- **Resource generation.** `R0` is an existing resource, `R1` the first derivative, `R2` a derivative of a derivative, and so on up to `R3`. Always state the generation.
- **Classical ARIZ Core vs. Extended Framework.** *Classical* covers the minimal-change operators of classical TRIZ/ARIZ: mixtures of existing substances, substance + void, phase or state change, decomposition, transition between structural levels, and existing fields and their combinations. *Extended* covers field/energy derivatives, by-products and waste, spatial, temporal, informational and functional derivatives, physical and chemical interactions, conversion/transfer/storage, parameter change over time, resource chains, and super-system derivatives. **Label every derivative with one of the two.**
- **Operating Zone (OZ) / Operating Time (OT).** Where and when the problem actually occurs. A resource present in the OZ and in the OT outranks an otherwise equal one that is not.
- **Ideality.** Useful functions weighed against harm and cost. A derivative that performs a function with a resource already in the system raises ideality; one that needs a new component lowers it.

## Core rules

1. Prefer resources already in or near the problem, and prefer the minimum modification.
2. Use available resources before introducing foreign substances, fields, components, energy or information.
3. Treat harmful, neutral, waste, idle and underused resources as potential useful resources — the harmful effect is often the best resource in the system.
4. Search properties, parameters, states, gradients, surfaces, structures, interactions, flows and information, not only objects.
5. **Resource priority order:** 1 existing resources in the OZ/OT → 2 internal system resources → 3 super-system and environment → 4 waste, harmful, cheap, free → 5 small modifications → 6 larger modifications → 7 new external substances, fields or components. Drop to a lower level only when the higher ones are inadequate.
6. **Never fabricate a mechanism.** Do not claim a physical or chemical mechanism is feasible unless known science supports it — mark the uncertain ones `HYPOTHESIS`. Never invent material properties or data.
7. Distinguish **known fact**, **source-supported inference** and **engineering hypothesis** throughout, and never present a hypothesis as established fact. Uploaded documents and the user's own data are the primary evidence; cite reliable sources for specific physical, chemical or engineering effects where practical.
8. List missing data explicitly under *Assumptions / Unknowns* instead of guessing values such as temperature, pressure or material. Simple numbers derived from the user's data — averages per event, ratios between lines — are welcome, labelled *computed*.

## Output format

Report in this order: 1 Problem Understanding · 2 Main Useful Function · 3 Operating Zone / Operating Time · 4 Existing Resource Inventory (Table A) · 5 Important Resource Properties · 6 Required Effects · 7 Classical Derived Resources (Table B1) · 8 Extended Derivative Resources (Table B2) · 9 Derivative Resource Chains · 10 Candidate Evaluation (Table C) · 11 Recommended Solution Concepts · 12 Assumptions / Unknowns · 13 Verification Required · 14 Suggested Next Analysis.

Fourteen sections with several wide tables outgrow a chat reply: deliver the analysis as a document and keep a short summary in the chat, in the user's language. The column specification for each table is in `references/procedure-and-tables.md`.

## Examples

**Classical.** Combine waste fibres and plastics into a durable composite (mixture, `R0 → R1`). Foam a filler with gas bubbles to cut mass without losing stiffness (substance + void). Freeze a liqueur core so it can be handled as a solid (phase change).

**Extended.** Spent grain from brewing becomes animal feed (by-product). Waste heat from a plant heats the neighbouring houses (field/energy derivative, super-system). Machine-log timestamps become a condition indicator (informational derivative).

**The cheapest derivatives are usually informational.** The defect itself can serve as a position sensor; existing logs already hold the history; two similar lines running under different conditions are a natural experiment nobody set up. Before proposing hardware, check which records are missing and propose capturing them — and say so if a deadline or date in the source material has already passed.

Natural next steps to offer: collect the missing data and rerun at `R2`; a Function Analysis of the core system (`function-analysis`); a cause-and-effect analysis of the confirmed mechanisms (`cause-effect-chain-analysis`).
