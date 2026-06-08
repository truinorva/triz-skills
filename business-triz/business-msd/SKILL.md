---
name: business-msd
description: "TRIZ Multi-Screen Diagram (MSD / 9 Boxes / 9 Windows) for business and technical systems. Use this skill whenever the user wants to analyze a system's past, present, and future evolution at Super-System, System, and Sub-System levels. Triggers on mentions of 'multi-screen', 'MSD', '9 boxes', '9 windows', '9 screens', 'system evolution', 'future of a system', or any request to explore how a business or technical system will evolve over time."
---

<!-- 
  Based on the Business TRIZ Multi-Screen Diagram (MSD) Prompt
  Copyright (c) 2025 Robert Adunka, based on the System Operator Prompt by Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Multi-Screen Diagram (MSD)

Guide the user through a TRIZ Multi-Screen Diagram (also known as 9 Boxes, 9 Windows, or 9 Screens) to explore a system's past, present, and future at the Super-System, System, and Sub-System levels. This structured approach surfaces issues, constraints, and opportunities for innovation.

## When to use

This skill works for both technical systems (e.g., cars, smartphones, machines) and business systems (e.g., insurance companies, banks, retail). Default to **Business MSD** unless the user explicitly mentions a technical system or the context makes it clear.

## Interaction flow

1. **Clarify the system.** If the user hasn't named a system yet, ask them to describe it. Determine whether to use Business or Technical MSD. If unclear, ask.

2. **Describe the present state.** Ask the user to describe the current state of their system. If you already have enough information, propose your understanding and ask for confirmation.

3. **Identify Sub-Systems and Super-Systems.** Fragment the system into 5–10 sub-systems and 5–10 super-systems.
   - Sub-Systems: What assemblies, components, materials, designs, characteristics, and parameters make up the system?
   - Super-Systems: What exists in the environment? Which other systems interact with this one? Which environmental factors impact the system?
   - Present your recommendations first, then ask the user to confirm or correct. Iterate until approved.

4. **Look at the past.** Define a past year and identify the system's predecessor. Define that predecessor's Sub-Systems and Super-Systems using the same approach.

5. **Project the future.** Define a future year. Describe how Super-Systems and Sub-Systems evolve from past through present into the future.

6. **Derive the future system.** Based on the influence of future Super-Systems and Sub-Systems, define how the system itself must evolve — following a consistent trajectory from past through present into the future.

7. **Generate the MSD table.** Produce a 3x3 matrix:
   - Rows: Super-System, System, Sub-System
   - Columns: Past (with year), Present (with year), Future (with year)
   - Fill in details for each cell based on the steps above.

## Background

The TRIZ Multi-Screen Diagram predicts future developments based on past and present analysis.

| | Past | Present | Future |
|---|---|---|---|
| **Super-System** | Predecessor components interacting with the Past-System | Components interacting with the current system | Projected supersystem developments |
| **System** | The predecessor system (Past-System) | The system being analyzed | Projected future system |
| **Sub-System** | Components of the Past-System | Components of the current system | Projected component developments |

## Examples

### Technical Example: Car

| | Past (before 1900) | Present (1900–today) | Future (in 5 years) |
|---|---|---|---|
| **Super-System** | Early roads, traffic signs, coachman | Streets, traffic lights, driver | Intelligent roads |
| **System** | Horse-drawn carriage | Car | Autonomous car |
| **Sub-System** | Horse, carriage, wheels | Engine, chassis, wheels | Hydrogen engine, AI systems |

Summary: Self-driving hydrogen cars on intelligent streets, driverless operation.

### Technical Example: Smartphone

| | Past (before 1994) | Present (today) | Future (in 10 years) |
|---|---|---|---|
| **Super-System** | Telephone lines, desk, telephone exchange | 5G, wifi, cloud, pockets | Worldwide wifi, clothing-integrated reception, 6G |
| **System** | Landline phone | Smartphone | Wearable smartphone |
| **Sub-System** | Receiver, base unit, dial | Screen, sensors, battery, casing | Microscopic electronics, mini casings, ultra-fast battery |

Summary: Future smartphones will be even more integrated, faster, and miniaturized.

### Business Example: Insurance Company

| | Past (before 1994) | Present (today) | Future (in 10 years) |
|---|---|---|---|
| **Super-System** | Client, competitors | Client, bank, fund management, lawyers, partners, police, competitors, building | Client, state cash reserves, competitors, legal offices |
| **System** | Lender-insurer | Insurance Company | Bank |
| **Sub-System** | Own cash, contract | Cash, employees, departments, cars, equipment, agents, reports, clients list | Cash, employees, departments, building, cars, equipment |

Summary: The bank will fulfill the tasks of an insurance company in the future.
