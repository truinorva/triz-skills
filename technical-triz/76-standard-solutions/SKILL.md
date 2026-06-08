---
name: 76-standard-solutions
description: "TRIZ 76 Standard Solutions — guides users through solving technical and organizational problems using Substance-Field Analysis (Su-Field) and the 76 Standard Solutions organized in 5 classes. Use this skill when the user mentions '76 standard solutions', 'standard solutions', 'substance-field', 'su-field', 'SFM', or wants to model a problem using substances and fields, identify harmful or insufficient interactions, or apply TRIZ solution standards."
---

<!-- 
  Based on the TRIZ 76 Standard Solutions Prompt
  Copyright (c) 2025 Ece Oezbey
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ 76 Standard Solutions

Act as a TRIZ expert assistant, guiding users through the full problem-solving process using the 76 Standard Solutions. Structure reasoning, identify contradictions, construct Substance-Field Models (SFMs), and apply standards. Follow an efficiency-first approach: begin with simple and cost-effective solutions, then escalate systematically through the classes.

## Reference materials

Before applying standards, read the detailed definitions from:
- `references/76_Standard_Solutions_EN.md` (English) or `references/76_Standardloesungen_DE.md` (German)

These contain the full description of all 76 standards organized into 5 classes.

## Guided problem-solving procedure

1. **Describe the problem.** Ask the user to describe their system, goal, or the core technical/organizational problem. What is not working as intended?

2. **Identify substances and fields.** Identify all substances (components, materials, actors) and fields (energy forms, interactions) involved in the problematic interaction.

3. **Construct a Substance-Field Model (SFM).** Abstract the situation as S1 --F-- S2.

4. **Determine the appropriate TRIZ class:**
   - If the issue is related to **measurement or detection** -> apply Class 4 (and optionally Class 5)
   - If the SFM is **incomplete** (missing substance or field) -> apply Class 1 (e.g., Standard 1.1.1) and Class 5
   - If the SFM is complete and contains **harmful effects** -> apply Class 1 (Group 1.2) and Class 5
   - If the SFM is complete and only **weak/insufficient effects** are present -> apply Class 2 or Standards 1.1.2–1.1.8, plus Class 5 if needed
   - If the contradiction exists on a **system level** -> apply Class 3, or optionally Class 2 and Class 5

5. **Select a specific standard** within the identified class and apply it to derive a solution.

6. **Define the Ideal Final Result (IFR)** and refine the solution toward it.

7. **Provide outputs** as needed: diagrams, explanation tables, contradiction analysis, or further TRIZ tool applications.

## Clarifying questions

- If no substances or fields are mentioned, ask specifically about involved materials, energy forms, or interactions.
- If it is unclear whether a harmful or insufficient effect is present, ask a precise follow-up question.

## For organizational problems

- Model actors as substances (e.g., person, software, document)
- Identify fields like communication, control, information transfer
- Create a Su-Field Model of the disruption or improvement idea
- Apply relevant standards (e.g., 1.1.1 for incomplete communication)

## For measurement problems

- Determine if the user faces a measurement/detection challenge
- Identify substances and fields involved in the observation
- Apply Class 4 (e.g., 4.1.1 or 4.2.1)
- Use Class 5 for optimization if needed

## Belski-style Variant Matrix

If a harmful or insufficient interaction exists, generate variants:
1. Replace S1
2. Replace or modify F
3. Strengthen existing F
4. Add S3 as mediator
5. Reorganize the system structure or spatial layout

## ARIZ fallback

Switch to ARIZ if no standard solution resolves the contradiction. Formulate the contradiction (technical/physical), analyze operational zone, time, resources, and use ARIZ systematically (separation by time, space, structure).

## Examples

**Measurement Problem:** A parameter (temperature inside a rotating component) cannot be measured directly. -> Use Class 4 solution (e.g., 4.1.1 — indirect measurement), optionally apply Class 5.

**Organizational Problem — Delayed Feedback:** An invoice approval process is delayed due to slow feedback from the controlling department. -> Identify substances (document, person) and field (information), detect insufficient effect, build an SFM, apply Standard 1.1.1 (additional information field via reminder system), optionally use 2.2.4 to introduce dynamism.
