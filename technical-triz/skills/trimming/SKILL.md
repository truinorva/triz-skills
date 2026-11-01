---
name: trimming
description: "TRIZ Trimming and Trimming Rules — streamlines engineering systems by identifying and eliminating unnecessary components while preserving essential functions using Rules A, B, and C. Use this skill when the user mentions 'trimming', 'trim components', 'simplify system', 'eliminate components', or wants to reduce system complexity, remove unnecessary parts, or apply TRIZ trimming rules to cut costs and simplify designs."
---

<!-- 
  Based on the TRIZ Trimming and Trimming Rules Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Trimming and Trimming Rules

Guide the user through step-by-step application of TRIZ Trimming to identify and eliminate unnecessary components while preserving essential functions.

## Interaction flow

1. **Describe the system.** Ask the user to describe the technical system they want to apply Trimming to.

2. **Component analysis.** Guide them through identifying super-system, system, and sub-system components.

3. **Function analysis.** Perform function analysis in tabular form: Tool | Action | Object | Result | Function

4. **Select component to trim.** Ask the user which component (Tool) from the function analysis they want to trim.

5. **Formulate the Trimming Key Problem:**
   - "If we trim [Component], Then [Positive Outcome], But [Negative Outcome]"
   - Generate: "How can we achieve [Positive Outcome] without [Negative Outcome]?"

6. **Solve using Trimming Rules.**

## Trimming Rules

### Rule A — Remove the object
The tool (function carrier) can be trimmed if the object of its useful function is removed.

### Rule B — Object performs the function itself
The tool can be trimmed if the object performs the useful function itself.

### Rule C — Another component takes over
The tool can be trimmed if another component performs the function. Apply these guidelines:
1. Component performs the same function on the same object
2. Component performs the same function on a different object
3. Component performs another function on the same object
4. Component has the resources to perform the function

## Key concepts

A system is defined by its main function. The targets of the system are those components whose parameters are changed by this main function.

**Examples:**
- A car's main function is to move passengers and cargo (targets)
- A toothbrush removes plaque (object) by changing its location
- A refrigerator moves heat to the outside — making it similar in function to a heater
