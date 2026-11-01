---
name: cause-effect-chain-analysis
description: "TRIZ Cause and Effect Chain Analysis (CECA) and Root Cause Analysis (RCA) — guides users through structured causal analysis to identify root causes, key disadvantages, and the contradictions behind them. Use this skill when the user mentions 'CECA', 'cause and effect chain', 'Ursache-Wirkungs-Analyse', 'Ursache-Wirkungs-Kette', 'root cause analysis', 'RCA', or wants to investigate why an engineering problem occurs, trace defects to their root causes, or derive contradictions from causal chains. For a failure investigation whose goal is an investigation plan, corrective actions and a final report rather than contradictions, use the root-cause-analysis skill instead."
---

<!-- 
  Based on the TRIZ CECA and RCA Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Cause and Effect Chain Analysis (CECA) and Root Cause Analysis (RCA)

Guide users through structured Cause and Effect Chain Analysis (CECA) and Root Cause Analysis (RCA) to identify root causes, key disadvantages, and contradictions in technical systems.

## Which procedure, and when to hand over

**CECA** is the default here. It ends in contradictions and key problem statements, which is what the TRIZ tools downstream need — hand those to `contradiction-solver` or `physical-contradictions`.

The **RCA** procedure below is the alternative documented in the same source prompt. If the user's goal is a full failure investigation — physical parameters classified as too high or too low, an investigation plan with data collection methods, containment and corrective actions, and a final report — the `root-cause-analysis` skill covers that in more depth. Offer it.

## CECA Procedure

1. **Problem input.** Ask the user: "What is your interesting engineering problem?" Wait for input.

2. **Identify principles.** Identify scientific or engineering principles relevant to the problem or defect. Then ask: "Do you need to add more details to the relevant principles?"

3. **Determine expertise.** Determine the expertise needed to analyze the problem. Ask: "Do you need to add more expertise?"

4. **Analyze root causes.** Analyze potential root causes using the identified principles and expertise. Explore deeper causes where needed.

5. **Create the CECA** consisting of:
   - List of potential root causes at parameter level of components
   - Identification of key disadvantages of each root cause
   - Contradictions based on minimum/maximum parameter values
   - Key problem statements without solutions

6. **Present in tabulated format.**

7. **User review.** Ask user to review and select the most appropriate key problem.

## Alternative: Root Cause Analysis (RCA)

If the user prefers a classical RCA approach instead of CECA:

1. **Problem input.** Ask the user: "What is your interesting engineering problem?" Wait for input.

2. **Identify principles.** Identify scientific or engineering principles. Then ask: "Do you need to add more details to the relevant principles?"

3. **Determine expertise.** Determine the required expertise. Then ask: "Do you need to add more expertise?"

4. **Analyze root causes** and present findings in tabular format.

5. **Investigation guidelines** including:
   - Data collection methods and frequency
   - Hypothesis testing and relevant tools
   - Investigation procedures and documentation methods

6. **Feedback.** Ask: "Do you have additional methods or tools to suggest?"

7. **Actions.** Provide containment, corrective, and preventive actions based on analysis.

8. **Present findings** in tabular format for clarity.
