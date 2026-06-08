---
name: ideality
description: "TRIZ Ideality — optimize technical systems by reducing harm, enhancing usefulness, managing resources, and adding new functions. Use this skill when the user wants to increase system ideality, reduce complexity, improve performance without adding resources, define the ideal system, or mentions 'ideality', 'ideal system', 'ideal final result', 'IFR', or wants to move a system toward its ideal state."
---

<!-- 
  Based on the TRIZ Ideality Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Ideality

Support the user in increasing system ideality through structured TRIZ methods — by reducing harm, enhancing usefulness, managing resources, and suggesting new functions.

## Interaction flow

1. **Describe the system.** Ask the user to describe a technical system (real or hypothetical).

2. **Apply four strategies:**
   - **Reduce or eliminate harmful effects** — identify and minimize negative side effects
   - **Increase useful functions and benefits** — enhance what the system does well
   - **Maintain or reduce resource usage** — achieve more with less
   - **Add new useful functions** — expand what the system can do

3. **For each strategy,** provide specific suggestions and identify potential contradictions.

4. **Follow-up.** Ask the user if they want to explore one of the four strategies in more detail. Apply that strategy and identify Engineering or Physical Contradictions if applicable.

5. **Ideality modeling.** Formulate the ideal version of the given system: delivering its main function without existing or harmful effects. Consider if other systems can achieve the same or better functionality.

## The Ideal Technical System

An ideal system performs its main function without existing and without side effects.

Examples:
- The ideal lawn mower cuts grass without existing.
- The ideal car key starts the car without existing.

## TRIZ Resource Types

Resources that can be leveraged to increase ideality:
- **Material:** substances and objects in or around the system
- **Field-like (MATChEMIB):** Mechanical, Acoustic, Thermal, Chemical, Electromagnetic, Intermolecular, Biological
- **Spatial:** Surfaces, Volumes, Directions, Shapes
- **Temporal:** Time points, Time periods, Breaks, Idle times
- **Functional:** Existing functions in system
- **Informational:** Data and signals

## Contradiction definitions

**Engineering Contradiction:** "IF ..., THEN ..., BUT ..." — improving one feature leads to deterioration of another.

**Physical Contradiction:** A component should have two opposing properties — "... TO ..., AND ... TO ..."
