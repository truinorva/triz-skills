---
name: interactive-trimming
description: "Interactive TRIZ TRIMMING with extended rules (A, B, C, D, E, X) — guides users interactively through trimming components from technical systems using an expanded set of rules including external components, new markets, and better alternatives. Use this skill when the user wants a more interactive or extended trimming approach, mentions 'interactive trimming', or wants to explore additional trimming strategies beyond the basic A/B/C rules."
---

<!-- 
  Based on the Interactive TRIMMING Prompt
  Copyright (c) 2025 Tanasak Pheunghua
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# Interactive TRIMMING (Extended Rules)

Guide users interactively through the TRIZ TRIMMING process step by step, using an expanded set of rules to identify and remove unnecessary components while maintaining or improving the main function.

## Interaction flow

1. **Technical system.** Ask the user for the technical system to apply TRIMMING. Wait for response.

2. **Function analysis.** Explain what a function is and define Function Carrier and Object of Function. Ask the user to perform Component Analysis (Super-system, System, Sub-system). Then create a function table:

   | Tool | Action | Object | Result | Function |
   |---|---|---|---|---|

3. **Select component to trim.** Ask the user to select the component (Tool) they wish to trim. Show list of tools from Component Analysis.

4. **Formulate the Trimming Key Problem** as a contradiction:
   - If = [Specific action on system]
   - Then = [Positive change]
   - But = [Negative change]
   - Key Problem: "How can we [achieve positive effect] without [negative effect]?"

5. **Apply extended TRIMMING rules:**

### Rule A — Remove Object
Can we remove the object of the Tool's function entirely?

### Rule X — Use External Component
Can other external components (from outside the system) perform the same function?

### Rule B — Empower Object
Can the Object perform the function by itself?

### Rule C — Use Another Component
Can another system component perform the function?

### Rule D — Find New Market
Can this trimmed (simplified) system be valuable in a new or niche market?

### Rule E — Use Better Alternative
Can an external, better, or cheaper component do the job?

## Key definitions

- **Function:** An action performed by one component to change or maintain a parameter of another component.
- **Function Carrier:** The object that performs a function in a system.
- **Object of Function:** The component whose parameter is affected by the function.

## Example

| Tool | Action | Object | Result | Function |
|---|---|---|---|---|
| Toothbrush | remove | Plaque | Cleaner teeth | to remove plaque |
