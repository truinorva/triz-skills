# RCA+ Method Knowledge

Detailed method rules for the Root Conflict Analysis (RCA+) skill.

---

## Lookup Map

- For the purpose and background of RCA+, use section 1.
- For definitions of cause types, relationships, and problem categories, use section 2.
- For the 9-step analytical workflow, use section 3.
- For deciding RCA vs. RCA+, use section 4.
- For quality rules, use section 5.

---

## 1. Purpose of RCA+

Root Conflict Analysis (RCA+) was developed by Valeri Souchkov. It combines ideas from Root Cause Analysis, Theory of Constraints, and TRIZ. RCA+ extends classical Root Cause Analysis in two fundamental ways:

1. **Contradictions, not just causes.** Often a cause contributes to both a negative and a positive effect. Simply eliminating the cause would destroy the positive effect. RCA+ identifies these contradiction causes so they can be resolved inventively rather than by brute elimination.

2. **Closer to the problem is better.** Instead of drilling to the deepest root cause, RCA+ targets contradictions that reside as close as possible to the general negative effect. Experience with hundreds of problems shows that solving a contradiction closer to the top problem provides more ideal solutions.

RCA+ is domain-independent and applies equally to technical/engineering systems and business/management systems.

---

## 2. Core Concepts

### Four Problem Categories

RCA+ can analyze four categories of problems:

1. **Negative effect** — something happens that we do not want at all (a failure, defect, damage, loss, complaint).
2. **Insufficient effect** — a desired result is not achieved with the required degree of performance, quality, or completeness.
3. **Excessive effect** — a desired result is achieved but wastes too much of a costly resource.
4. **Ineffective control** — we have the means of control but the process of control is too slow, inaccurate, or unreliable.

### Four Types of Causes

Every cause in an RCA+ diagram is classified as one of four types:

| Tag | Type | Meaning |
|---|---|---|
| **N** | Negative | The cause is entirely negative; we want to eliminate it. Can be factual (verified) or assumptive (unverified, shown with dashed box). |
| **N+P** | Negative + Positive | The same cause produces both a negative and a positive effect. This is a **contradiction cause** — the core discovery of RCA+. |
| **NC** | Non-Changeable | The cause contributes negatively but cannot be eliminated or modified (beyond our control, e.g. laws of nature, policy, supersystem constraints). |
| **P** | Positive | A positive effect produced by a contradiction cause. Listed in the diagram and the summary table for completeness. |

### Cause Formulation

A cause must be stated as one of:

- A **function**: subject + action + object (e.g. "Knife scratches table surface", "Manager delays decisions", "Customer returns product").
- A **relative parameter value**: property + relative value (e.g. "Temperature is too high", "Marketing budget is too low", "Speed of delivery is too slow").
- A **change of a property**: direction + property + relative value (e.g. "Decrease of temperature is too fast", "Increase of workload is too rapid").
- A **radical state change**: (e.g. "Ice melts", "Key employee leaves", "Advertisement was abandoned").

Each cause must be a sentence, not a single word. Avoid the question "Why?" — it can be interpreted as asking for a goal ("what for?") rather than a cause. Always ask "What causes ...?"

### Factual vs. Assumptive Causes

- **Factual cause**: Verified by data or observation.
- **Assumptive cause**: Hypothetical, requires verification. Mark clearly in the diagram and table.

### AND / OR Relationships

- **AND relationship**: Multiple causes are all required together to produce the effect. Removing any single one would eliminate the effect. Finding all AND-related causes is essential — the more causes related with AND, the more opportunities to solve the problem.
- **OR relationship**: Causes contribute independently. Each alone can produce the effect.

For specific problems, causes are usually AND-related. For broad failure prevention, causes can be AND or OR.

### Contradiction Cause (N+P)

A contradiction cause is the key finding of RCA+. It means the cause cannot simply be eliminated without also losing the positive effect. When a cause produces multiple positive effects, select only the most important one for the diagram.

### Stopping Rules

Stop expanding a branch when you reach:

- A **contradiction cause** (N+P) — the positive effect already identifies the underlying reason for the cause's existence.
- A **non-changeable cause** (NC) — we cannot influence it.
- A **requirement or demand** that cannot be changed (policy, specification, law of nature).

### Cause Exploration Categories

When thinking about causes, consider these categories to avoid missing any:

**For technical/engineering problems:** time, space, geometry, information, property, supersystem, materials, fields, energy.

**For business/management problems:** people, processes, information, resources, organization, technology, market, regulation, strategy, culture.

---

## 3. The 9 Steps of RCA+

### Step 1 — State the general negative effect

The top-level problem must be formulated as a single sentence and must belong to one of the four problem categories. Start the RCA+ diagram with this effect at the top.

### Step 2 — Find the causes

Ask: "What causes this effect to occur?" or "What is a cause of this effect?"

Each cause must be formulated as a function, relative parameter value, change of property, or radical state change (see Cause Formulation above). Mark causes as factual or assumptive.

### Step 3 — Check AND / OR relationships

After identifying a cause, check whether it alone is sufficient to produce the negative effect, or whether additional causes acting together are needed.

### Step 4 — Check for positive effects (classify each cause)

For every cause identified, ask: "Does this cause also produce a positive effect?" Classify each cause as N, N+P, NC, or P.

### Step 5 — Continue the top-down analysis

For each N-type cause (purely negative, no positive effect), repeat Step 2: ask "What causes this effect?"

Do not continue deeper analysis for contradiction causes (N+P) or non-changeable causes (NC).

### Step 6 — Check AND relationships for new causes

For each newly added cause, repeat Step 3.

Continue Steps 5 and 6 iteratively until all branches end at a contradiction (N+P), a non-changeable cause (NC), or a requirement.

### Step 7 — Create the summary table

Create a table of all revealed causes with their classifications. See `root_conflict_analysis_tables.md` for the table format.

### Step 8 — Formulate the problems

Formulate the problems revealed by the RCA+ diagram. See `root_conflict_analysis_templates.md` for formulation templates.

### Step 9 — Recommend problems for solving

Present a prioritized list of problems to solve. Do not solve the problems at this stage.

Selection guidelines:
- **AND causes**: solving any one of the contradiction causes eliminates the entire negative effect.
- **OR causes**: all must be solved to fully prevent the negative effect.
- **Closer to the top** is generally preferred — it provides more ideal solutions.
- **Contradiction causes involving fewer components** are easier to resolve.
- **Contradiction causes involving system elements** (rather than supersystem) are preferred since those elements are easier to change.
- N-type causes without underlying contradictions are the simplest to address — they can be directly eliminated.

---

## 4. RCA vs. RCA+

RCA is limited to identifying root causes of undesirable effects. RCA+ identifies both root causes and root conflicts (contradiction causes).

Useful decision rules:

- If the system is underdeveloped or defective, RCA may be sufficient.
- If the system is mature and generally works, but improvement is difficult because every change has disadvantages, RCA+ is often more suitable.
- Mature products usually have fewer simple root causes and more contradictions.
- A problem caused by an actionable root cause indicates a defect or unfinished development.
- A problem caused by a contradiction cause indicates that a useful design decision also creates harm.

---

## 5. Quality Rules

- Each cause must be a sentence, not a single word.
- Always check for AND-related causes — breadth of analysis reveals more solution opportunities.
- Do not skip Step 4 — checking for positive effects is what makes RCA+ more powerful than plain RCA.
- Mark assumptive causes clearly; they require verification.
- Do not continue deeper analysis beyond contradiction causes (N+P) or non-changeable causes (NC).
- Keep the diagram top-down and readable.
- Distinguish clearly between N-type causes (can be eliminated) and N+P-type causes (require inventive resolution).
