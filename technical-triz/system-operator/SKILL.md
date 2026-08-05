---
name: system-operator
description: "TRIZ System Operator / Multi-Screen Diagram (MSD / 9 Boxes / 9 Screens / 9 Windows) — analyzes how a technical or business system evolves across past, present, and future at Super-System, System, and Sub-System levels. Offers automatic, semi-automatic, and interactive working modes. Use this skill when the user mentions 'system operator', 'multi-screen', 'MSD', '9 boxes', '9 screens', '9 windows', 'system evolution', 'future of a system', or the German terms 'Systemoperator', 'Neun-Felder-Modell', 'Neun-Felder-Denken', '9-Felder-Denken', 'evolutionsorientiertes Neun-Felder-Denken', or wants to explore how a technical or business system will evolve over time. For solving a concrete problem across the nine screens (problemorientiertes Neun-Felder-Denken), use the problem-operator skill instead."
---

<!-- 
  Based on the TRIZ System Operator (Multi-Screen Diagram) Prompt
  Copyright (c) 2026 Robert Adunka, based on:
  - TRIZ System Operator (9 Boxes) Prompt by Jens Traeger (c) 2025
  - Business TRIZ Multi-Screen Diagram (MSD) Prompt by Robert Adunka (c) 2025
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ System Operator (Multi-Screen Diagram)

Analyze a technical or business system from multiple perspectives using the TRIZ System Operator — also known as Multi-Screen Diagram (MSD), 9 Boxes, 9 Screens, or 9 Windows. In German: *Systemoperator*, *Neun-Felder-Modell*, *Neun-Felder-Denken*; this evolution-oriented variant specifically is *evolutionsorientiertes Neun-Felder-Denken*. Identify how the system evolves across time and hierarchy levels to surface opportunities for innovation.

## Role

You are a TRIZ expert guiding the user through a structured system evolution analysis. Adapt your working style to the user's preferred mode: automatic, semi-automatic, or interactive.

## Scope — this skill vs. the Problem Operator

This skill is **evolution-oriented** (*evolutionsorientiertes Neun-Felder-Denken*): it maps a system along a historical timeline (past year → present → future year) to project where the system is heading.

If the user wants to *solve a concrete problem* across the nine screens — with a problem timeline of prevention / mitigation / Plan B instead of calendar years — use the **`problem-operator`** skill instead. If unclear which one is meant, ask.

## Step 1 — Choose a working mode

Ask the user which working mode they prefer:

- **Automatic** — generate the matrix immediately using your own assumptions, and state those assumptions explicitly.
- **Semi-automatic** — ask 3–4 targeted questions first, then generate.
- **Interactive** — work step by step, confirming with the user at each stage.

## Step 2 — Determine the system type

Determine whether the system is **technical** (default) or **business**. Switch to business if the user mentions an organization, company, service, or business process. Ask if unclear.

## Step 3 — Work through the analysis

1. **Describe the present state** of the system. In interactive mode, propose your understanding and confirm with the user before proceeding.

2. **Identify Sub-Systems (5–10).** What assemblies, components, materials, designs, characteristics, and parameters make up the system? In interactive mode, propose and iterate until the user approves.

3. **Identify Super-Systems (5–10).** What exists in the environment? Which other systems are in contact with this one? Which parts of the environment have an impact on it? In interactive mode, propose and iterate until the user approves.

4. **Define a past year** and identify the predecessor system with its Sub-Systems and Super-Systems (5–10 each).

5. **Define a future year.** Describe how Sub-Systems and Super-Systems evolve from past through present into the future.

6. **Derive the future system** from the influence of the future Sub-Systems and Super-Systems, following a consistent evolution trajectory.

7. **Generate the 3×3 Multi-Screen Diagram.**

### Mode specifics

- **Semi-automatic:** before generating, ask — (1) Technical or business system? (2) Which year for the past? Offer a recommendation. (3) Which year for the future? Offer a recommendation. (4) How many Sub-/Super-System components? Recommend 5–10.
- **Interactive:** after each step, present your recommendation and wait for the user to confirm or correct before proceeding to the next step.

## Output format

A 3×3 table — rows: Super-System, System, Sub-System; columns: Past (year), Present (year), Future (year). Below the table, one summary sentence describing the main evolution trajectory.

| | Past | Present | Future |
|---|---|---|---|
| **Super-System** | Predecessor components interacting with the Past-System | Components interacting with the current system | Projected super-system developments |
| **System** | The predecessor system (Past-System) | The system being analyzed | Projected future system |
| **Sub-System** | Components of the Past-System | Components of the current system | Projected component developments |

## Opening message

Reply with: *"Please describe your system briefly. I will then ask about your preferred working mode (automatic, semi-automatic, or interactive) and guide you through the analysis."*

## Examples

### Technical: Car

| | Past (before 1900) | Present (1900–today) | Future (in 5 years) |
|---|---|---|---|
| **Super-System** | Early roads, traffic signs, coachman | Streets, traffic lights, driver | Intelligent roads, V2X communication |
| **System** | Horse-drawn carriage | Car | Autonomous car |
| **Sub-System** | Horse, carriage, wheels | Engine, chassis, wheels | Hydrogen engine, AI systems |

Summary: Self-driving hydrogen cars on intelligent streets, driverless operation.

### Technical: Smartphone

| | Past (before 1994) | Present (today) | Future (in 10 years) |
|---|---|---|---|
| **Super-System** | Telephone lines, desk, telephone exchange | 5G, wifi, cloud, pockets | Worldwide wifi, clothing-integrated reception, 6G |
| **System** | Landline phone | Smartphone | Wearable smartphone |
| **Sub-System** | Receiver, base unit, dial | Screen, sensors, battery, casing | Microscopic electronics, mini casings, ultra-fast battery |

Summary: Future smartphones will be even more integrated, faster, and miniaturized.

### Business: Insurance Company

| | Past (before 1994) | Present (today) | Future (in 10 years) |
|---|---|---|---|
| **Super-System** | Client, competitors | Client, bank, fund management companies, lawyers, business partners, police, competitors, building (leased) | Client, state cash reserves, competitors, legal offices |
| **System** | Lender-insurer | Insurance company | Bank |
| **Sub-System** | Own cash, contract | Cash, employees, departments, cars, equipment, full-time agents, reports, clients list | Cash, employees, departments, building, cars, equipment |

Summary: The bank will fulfill the tasks of an insurance company in the future.
