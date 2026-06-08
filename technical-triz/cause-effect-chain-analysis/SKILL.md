---
name: cause-effect-chain-analysis
description: "TRIZ Cause and Effect Chain Analysis (CECA) and Root Cause Analysis (RCA) — guides users through structured root cause analysis to identify root causes, key disadvantages, and contradictions in technical systems. Use this skill when the user mentions 'CECA', 'cause and effect chain', 'root cause analysis', 'RCA', or wants to investigate why an engineering problem occurs, trace defects to their root causes, or identify contradictions from causal chains."
---

<!-- 
  Based on the TRIZ CECA and RCA Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Cause and Effect Chain Analysis (CECA) and Root Cause Analysis (RCA)

Guide users through structured Cause and Effect Chain Analysis (CECA) and Root Cause Analysis (RCA) to identify root causes, key disadvantages, and contradictions in technical systems.

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
