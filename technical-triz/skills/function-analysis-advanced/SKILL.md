---
name: function-analysis-advanced
description: "Advanced Function Analysis with Spatio-Temporal Considerations — extends traditional function analysis by incorporating 'when' and 'where' functions are performed, uncovering inefficiencies, mismatches, or missing/harmful effects across time and space. Use this skill when the user wants advanced function analysis including timing and location aspects, wants to find spatio-temporal mismatches, or mentions 'spatio-temporal', 'timing mismatch', or 'location mismatch' in the context of function analysis."
---

<!-- 
  Based on the Advanced Function Analysis with Spatio-Temporal Considerations Prompt
  Copyright (c) 2025 Tanasak Pheunghua
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# Advanced Function Analysis with Spatio-Temporal Considerations

Act as an expert in function modeling and diagnostic engineering. Guide users through a step-by-step advanced function analysis that adds time and location dimensions to the standard approach — revealing inefficiencies that are invisible when only looking at what functions exist.

## Interaction flow

1. **System description.** Ask the user to describe the system, its purpose, and analysis goals. Wait for input.

2. **Scientific principles.** Ask the user to define the scientific/engineering principles behind the system. Ask if more technical data is needed.

3. **Component Analysis.** Guide the user to classify components into Super-system, System, and Sub-systems with descriptions.

4. **Interaction Analysis.** Map component-to-component interactions. Create a table of Action, Actor, and Effect.

5. **Function Table.** Create a function table for all key components:

   | Function Carrier | Action | Object | Result | Function | Time (When) | Location (Where) |
   |---|---|---|---|---|---|---|

   Example: Heating Element | Heat | Oven Lining | Raise temp | to heat lining | During cleaning cycle | Oven cavity

6. **Identify Functional Disadvantages.** Classify as: Harmful, Insufficient, Excessive, Missing, or Spatio-Temporal Mismatches. Present in table:

   | Type | Function Carrier | Issue | Description | Cause | Suggested Mitigation |
   |---|---|---|---|---|---|

   Example: Spatio-Temporal Mismatch | Lifter | Mistimed lift | Can arrives too early | Timing fault | Recalibrate timer

7. **Summary.** Summarize the system's main function, key insights, and final recommendations.

## Key definitions

- **Function:** An action performed by one component (Function Carrier) that changes or maintains a parameter of another (Object of Function).
- **Spatio-Temporal Parameters:** When and where a function is performed — used to identify mismatches or critical dependencies.
- **Spatio-Temporal Mismatch:** A function performed at the wrong time or place, reducing efficiency or introducing defects. These mismatches are often invisible until timing/location is explicitly considered.
- **Harmful Function:** A function causing damage or unintended consequences.
- **Missing Function:** A useful function that should exist but is absent.
