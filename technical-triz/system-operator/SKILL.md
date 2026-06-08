---
name: system-operator
description: "TRIZ System Operator (9 Boxes / 9 Screens) — analyzes technical systems from multiple perspectives across past, present, and future at Super-System, System, and Sub-System levels. Supports both evolution-oriented and problem-oriented modes. Use this skill when the user mentions 'system operator', '9 boxes', '9 screens', or wants to analyze how a technical system evolves over time or solve a problem by examining it across time and system hierarchy levels."
---

<!-- 
  Based on the TRIZ System Operator (9 Boxes) Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ System Operator (9 Boxes)

Analyze a technical system from multiple perspectives using the TRIZ 9 Boxes (9 Screens) model. This structured approach identifies issues, constraints, and opportunities for improvement.

## Two modes

Distinguish between **Evolution-Oriented** and **Problem-Oriented** 9 Boxes. Use Evolution-Oriented as default. If the user mentions a problem or it becomes clear from context, switch to Problem-Oriented. Ask for clarification if unclear.

## Evolution-Oriented Mode

1. **Describe the system.** Ask the user to describe the current state of the technical system.

2. **Generate the 9 Boxes matrix (3x3):**
   - Rows: Supersystem, System, Subsystem
   - Columns: Past, Present, Future
   - Ask users if they want to specify time points
   - Fill in details for each cell

| | Past | Present | Future |
|---|---|---|---|
| **Supersystem** | Predecessor components interacting with Past-System | Components interacting with current system | Projected supersystem developments |
| **System** | The predecessor system | The system being analyzed | Projected future system |
| **Subsystem** | Components of the Past-System | Components of current system | Projected component developments |

## Problem-Oriented Mode

1. **Define the problem** and overall goal.
2. **Use the problem-timeline:** Past = before the problem, Present = during, Future = after.
3. **System Present:** Record the specific problem and system. Fill in with a guiding question and find solutions.
4. **Subsystem Present:** Break down subsystems with guiding questions and solutions.
5. **Supersystem Present:** Analyze the environment.
6. **Past (Before the problem):** Analyze System, Subsystem, Supersystem for solutions.
7. **Future (After the problem):** Define the overall goal and analyze each level for solutions to still reach it.

**Output:** Two tables — one with relevant questions per cell, one with proposed solutions per cell. State the overall goal.

## Examples

### Evolution-Oriented: Car

| | Past (before 1900) | Present (1900–today) | Future (in 5 years) |
|---|---|---|---|
| **Supersystem** | Early roads, traffic signs, coachman | Streets, traffic lights, driver | Intelligent roads |
| **System** | Horse-drawn carriage | Car | Autonomous car |
| **Subsystem** | Horse, carriage, wheels | Engine, chassis, wheels | Hydrogen engine, AI systems |

### Problem-Oriented: Leaking Pens in Shirt Pockets

**Problem:** Ink stains shirts. **Overall Goal:** Ensure neat appearance.

**Past solutions:** Paper uses pigment capsules (no ink in pen); Pen requires constant actuation to write; Retraction mechanism in grip section.

**Present solutions:** Shirt neutralizes ink; Pen retracts refill when vertical; Clip locks only when refill is retracted.

**Future solutions:** Shirt pocket is ink-resistant; Pen includes cleaning agent compartment; Ink is water-soluble for easy washing.
