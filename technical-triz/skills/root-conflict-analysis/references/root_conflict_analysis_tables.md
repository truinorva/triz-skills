# RCA+ Table and Output Requirements

Detailed output rules for the Root Conflict Analysis (RCA+) skill.

---

## Lookup Map

- For the RCA+ summary table format (Step 7), use section 1.
- For the problem formulation format (Step 8), use section 2.
- For the recommendation format (Step 9), use section 3.

---

## 1. RCA+ Summary Table (Step 7)

After completing the top-down cause-effect analysis, create a single summary table of all revealed causes with their classifications.

### Table format

| ID | Cause | Type | Positive Effect | Negative Effect |
|---|---|---|---|---|

### Column rules

- **ID**: Sequential numeric identifier.
- **Cause**: The cause statement (function, relative parameter value, change of property, or radical state change). Must be a full sentence.
- **Type**: One of **N**, **N+P**, **NC**, or **P**.
- **Positive Effect**: For N+P causes, state the positive effect. For P causes (positive effects of contradiction causes), state the effect. Leave empty for N and NC causes.
- **Negative Effect**: State the negative effect this cause contributes to. For P causes, leave empty.

### Type values

| Tag | Meaning | Positive Effect column | Negative Effect column |
|---|---|---|---|
| N | Purely negative cause | Empty | Filled |
| N+P | Contradiction cause (negative + positive) | Filled | Filled |
| NC | Non-changeable cause | Empty | Filled |
| P | Positive effect of an N+P cause | Filled (the positive effect itself) | Empty |

### Additional rules

- Include every cause from the RCA+ diagram, including positive effects (P) for completeness.
- Mark assumptive causes with a note (e.g. "(assumptive)" after the cause statement).
- List causes in a logical order that reflects the diagram hierarchy.

---

## 2. Problem Formulation Format (Step 8)

For each identified cause, formulate problems based on the cause type.

### For N-type causes (purely negative)

- If the cause is a function: "How to eliminate / prevent [N-cause]?"
- If the cause is a parameter value: "How to reduce / control [N-cause]?"

### For N+P-type causes (contradictions)

Formulate two types of contradictions:

**Technical contradiction** (pair of contradicting effects):
"How to ensure [N+P-cause] to enable [positive effect] but to avoid [negative effect]?"

**Physical contradiction** (opposite states of the cause):
"[N+P-cause] should be present/high/strong to [positive effect] AND should be absent/low/weak to avoid [negative effect]."

### For NC-type causes (non-changeable)

Non-changeable causes are not formulated as problems to solve. They represent constraints within which solutions must operate.

---

## 3. Recommendation Format (Step 9)

Present a prioritized list of problems recommended for solving. For each recommended problem, state:

1. The cause and its type (N, N+P, or NC)
2. The contradiction or negative effect it addresses
3. Why this problem is a good candidate for solving (proximity to the top problem, feasibility of change, alignment with objectives)

Include both a technical contradiction statement (TC) and a physical contradiction statement (PC) for each N+P cause.

Do not solve the problems at this stage. The actual solving can take place with other TRIZ methods (Contradiction Matrix, 40 Inventive Principles, Separation Principles, ARIZ, Inventive Standards, etc.) upon the user's request.
