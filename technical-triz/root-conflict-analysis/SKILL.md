---
name: root-conflict-analysis
description: "TRIZ Root Conflict Analysis (RCA+) — a domain-independent technique for defining, structuring, and visually representing problems by discovering contradictions. Extends classical Root Cause Analysis by identifying causes that produce both positive and negative effects simultaneously. Applicable to engineering, product, process, service, and business/management problems. Use this skill when the user mentions 'root conflict analysis', 'RCA+', 'Grundkonfliktanalyse', or wants to decompose a complex problem into its underlying contradictions rather than just finding root causes."
---

<!-- 
  Based on Souchkov's Root Conflict Analysis (RCA+) methodology.
  Skill implementation Copyright (c) 2026 Jens Traeger
  Licensed under the MIT License -- see LICENSE in the repository root.
-->

# Root Conflict Analysis (RCA+)

Act as an expert in Root Conflict Analysis (RCA+), a technique developed by Valeri Souchkov that combines ideas from Root Cause Analysis, Theory of Constraints, and TRIZ. Guide users step by step through building an RCA+ diagram that decomposes a problem into its underlying causes and contradictions.

RCA+ is domain-independent and applies equally to technical/engineering systems and business/management systems.

## Why RCA+ instead of classical Root Cause Analysis?

Classical Root Cause Analysis focuses on finding the lowest cause in a causal chain and eliminating it. RCA+ differs in two important ways:

1. **Contradictions, not just causes.** Often a cause contributes to both a negative and a positive effect. Simply eliminating the cause would destroy the positive effect. RCA+ identifies these contradiction causes so they can be resolved inventively rather than by brute elimination.

2. **Closer to the problem is better.** Instead of drilling to the deepest root cause, RCA+ targets contradictions that reside as close as possible to the general negative effect. Experience with hundreds of problems shows that solving a contradiction closer to the top problem provides more ideal solutions.

## Four categories of problems

RCA+ can analyze four categories of problems:

1. **Negative effect** — something happens that we do not want at all (a failure, defect, damage, loss, complaint).
2. **Insufficient effect** — a desired result is not achieved with the required degree of performance, quality, or completeness.
3. **Excessive effect** — a desired result is achieved but wastes too much of a costly resource.
4. **Ineffective control** — we have the means of control but the process of control is too slow, inaccurate, or unreliable.

## Four types of causes

Every cause in an RCA+ diagram is classified as one of four types:

| Tag | Type | Meaning |
|---|---|---|
| **N** | Negative | The cause is entirely negative; we want to eliminate it. Can be factual (verified) or assumptive (unverified, shown with dashed box). |
| **N+P** | Negative + Positive | The same cause produces both a negative and a positive effect. This is a **contradiction cause** — the core discovery of RCA+. |
| **NC** | Non-Changeable | The cause contributes negatively but cannot be eliminated or modified (beyond our control, e.g. laws of nature, policy, supersystem constraints). |
| **P** | Positive | A positive effect produced by a contradiction cause. Listed in the diagram and the summary table for completeness. |

## The 9 steps of RCA+

### Step 1 — State the general negative effect

Ask the user for the top-level problem. It must be formulated as a single sentence and must belong to one of the four problem categories above. Start the RCA+ diagram with this effect at the top.

If the user has already provided enough context, skip asking and proceed directly.

### Step 2 — Find the causes

Ask: **"What causes this effect to occur?"** or **"What is a cause of this effect?"**

A cause must be stated as one of:
- A **function**: subject + action + object (e.g. "Knife scratches table surface", "Manager delays decisions", "Customer returns product").
- A **relative parameter value**: property + relative value (e.g. "Temperature is too high", "Marketing budget is too low", "Speed of delivery is too slow").
- A **change of a property**: direction + property + relative value (e.g. "Decrease of temperature is too fast", "Increase of workload is too rapid").
- A **radical state change**: (e.g. "Ice melts", "Key employee leaves", "Advertisement was abandoned").

Important: avoid the question "Why?" — it can be interpreted as asking for a goal ("what for?") rather than a cause. Always ask "What causes ...?"

Each cause must be a sentence, not a single word.

Mark causes as **factual** (verified) or **assumptive** (unverified, to be confirmed later). Assumptive causes should be indicated with a note.

### Step 3 — Check AND / OR relationships

After identifying a cause, check whether it alone is sufficient to produce the negative effect, or whether additional causes acting together are needed.

- **AND relationship**: multiple causes are all required together to produce the effect. Removing any single one would eliminate the effect. Finding all AND-related causes is essential — the more causes related with AND, the more opportunities to solve the problem.
- **OR relationship**: causes contribute independently. Each alone can produce the effect.

For specific problems, causes are usually AND-related. For broad failure prevention, causes can be AND or OR.

### Step 4 — Check for positive effects (classify each cause)

For every cause identified so far, ask: **"Does this cause also produce a positive effect?"**

Classify each cause:
- **N** — purely negative, no positive effect
- **N+P** — produces both a positive and a negative effect (this is a **contradiction cause**)
- **NC** — negative but non-changeable (beyond our control)
- **P** — positive effect (always connected to an N+P cause)

A contradiction cause (N+P) is the key finding. It means the cause cannot simply be eliminated without also losing the positive effect.

When a cause produces multiple positive effects, select only the most important one for the diagram.

### Step 5 — Continue the top-down analysis

For each **N-type** cause (purely negative, no positive effect), repeat Step 2: ask "What causes this effect?"

**Stop** expanding a branch when you reach:
- A **contradiction cause** (N+P) — we stop because the positive effect already identifies the underlying reason for the cause's existence.
- A **non-changeable cause** (NC) — we cannot influence it.
- A **requirement or demand** that cannot be changed (policy, specification, law of nature).

Do **not** continue deeper analysis for contradiction causes or non-changeable causes.

### Step 6 — Check AND relationships for new causes

For each newly added cause, repeat Step 3: check if it is the only cause or if additional AND-related causes exist.

Continue Steps 5 and 6 iteratively until all branches either end at a contradiction (N+P), a non-changeable cause (NC), or a requirement.

### Step 7 — Create the summary table

Create a table of all revealed causes with their classifications:

| ID | Cause | Type | Positive Effect | Negative Effect |
|---|---|---|---|---|

- List every cause from the RCA+ diagram.
- Type is one of: **N**, **N+P**, **NC**, **P**.
- For N+P causes, fill both Positive Effect and Negative Effect columns.
- For N causes, leave Positive Effect empty.
- For NC causes, leave Positive Effect empty.
- For P causes (positive effects of contradiction causes), list them for completeness.

### Step 8 — Formulate the problems

Formulate the problems revealed by the RCA+ diagram:

For **N-type** causes:
- Function: "How to eliminate / prevent [N-cause]?"
- Parameter value: "How to reduce / control [N-cause]?"

For **N+P-type** causes (contradictions), formulate both:
- **Technical contradiction** (pair of contradicting effects): "How to ensure [N+P-cause] to enable [positive effect] but to avoid [negative effect]?"
- **Physical contradiction** (opposite states of the cause): "[N+P-cause] should be present/high/strong to [positive effect] AND should be absent/low/weak to avoid [negative effect]."

### Step 9 — Recommend problems for solving

Present a prioritized list of problems to solve. For each problem, state:
- The cause and its type
- What contradiction or negative effect it addresses
- Why this problem is a good candidate for solving (proximity to the top problem, feasibility of change, alignment with objectives)

Use these selection guidelines:
- **AND causes**: solving any one of the contradiction causes eliminates the entire negative effect.
- **OR causes**: all must be solved to fully prevent the negative effect.
- **Closer to the top** is generally preferred — it provides more ideal solutions.
- **Contradiction causes involving fewer components** are easier to resolve.
- **Contradiction causes involving system elements** (rather than supersystem) are preferred since those elements are easier to change.
- N-type causes without underlying contradictions are the simplest to address — they can be directly eliminated.

Do **not** solve the problems at this stage. The actual solving can take place with other TRIZ methods (Contradiction Matrix, 40 Inventive Principles, Separation Principles, ARIZ, Inventive Standards, etc.) upon the user's request.

## Cause formulation guidelines

When thinking about causes, consider these categories to avoid missing any:

**For technical/engineering problems:** time, space, geometry, information, property, supersystem, materials, fields, energy.

**For business/management problems:** people, processes, information, resources, organization, technology, market, regulation, strategy, culture.

## Reference files

For additional detail, read:
- `references/root_conflict_analysis_method.md` — full definitions, cause types, stopping rules, quality rules
- `references/root_conflict_analysis_tables.md` — detailed table and output format specifications
- `references/root_conflict_analysis_templates.md` — contradiction formulation templates, solution directions, report structure
- `references/root_conflict_analysis_examples.md` — worked examples: toothbrush (technical), sales (business), waste bin (compact with solution directions)
