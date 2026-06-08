---
name: function-analysis
description: "TRIZ Function Analysis for technical systems — identifies tools, actions, objects, and functions, clarifies component relationships, and reveals the system's main function. Use this skill when the user wants to perform a function analysis, identify functions in a technical system, map tools-actions-objects, create a function model, or analyze component interactions. Also trigger on mentions of 'function analysis', 'function model', 'tool-action-object', or 'function carrier'."
---

<!-- 
  Based on the TRIZ Function Analysis Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Function Analysis

Guide users through a structured Function Analysis of a technical system using TRIZ principles.

## Interaction flow

1. **Identify the system.** Ask the user: "What is your interesting technical system?" Wait for input.

2. **Component analysis.** Identify super-system, technical system, and sub-system components.

3. **Interaction analysis.** Analyze interactions between components from the component analysis. Ask: "Can you help me analyze the interactions?"

4. **Function Analysis.** Write all relevant functions in tabular form:

   | Tool | Action | Object | Category (U/H) | Degree of fulfillment (N/I/E or "---") | Changed/retained parameter |
   |---|---|---|---|---|---|

## Key concepts

### Definition of Function
A function is an action performed by one component (the tool / function carrier) to change or maintain a parameter of another component (the object of the function). Examples: Broom moves dirt. Helmet stops stone. Display informs user.

### Function Classification
Functions are either useful (U) or harmful (H). Only useful functions are graded:
- **N** = Normal (adequate performance)
- **I** = Insufficient (underperforming)
- **E** = Excessive (overperforming)

Harmful functions receive "---" for degree of fulfillment.

### Magic Wand Test
To verify the legitimacy of a function: if removing the tool changes the object, a function exists.

### Main Function and Targets
The main function must always be identified. It determines the target component in the super-system — whose parameter changes due to the system's main function.

**Example:** Main function of an airplane: Transport passengers and cargo. Targets: passengers and cargo. Changed parameter: geographic location.
