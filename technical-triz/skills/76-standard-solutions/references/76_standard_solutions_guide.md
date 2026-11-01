# Working guide for the 76 Standard Solutions

This file carries the procedural knowledge that belongs to the 76 Standard Solutions: an entry path
for users without TRIZ knowledge, an overview of the five classes with their group numbering,
working instructions per class, the diagnostic questions for choosing a class, and the systematic
Belski variant matrix.

It does **not** contain the standards themselves. Their definitions are in
`76_Standard_Solutions_EN.md` and `76_Standardloesungen_DE.md`. This guide says which class and
group to go to; those files say what the individual standard prescribes.

---

## 1. Guided entry for users without TRIZ knowledge

Use this path when the user has no prior TRIZ knowledge. It works in everyday language and does not
require familiarity with TRIZ terminology or with the 76 Standard Solutions. Translate the user's
answers into TRIZ logic in the background and select the solution pathway from them — do not make
the user learn the vocabulary first.

Open the session with:

> Welcome! You don't need to know TRIZ to begin. Just tell me in your own words what's not working
> or what you want to improve.

**Step 1 — Understand the problem.** Ask:
- What is your goal?
- What is not working as expected?
- What is happening instead?

**Step 2 — Identify the system elements.** Help the user name them:
- Substances involved — materials, people, machines, documents
- Actions or effects between them — pressing, heating, measuring, transferring

Build an initial Substance-Field Model (SFM) from these.

**Step 3 — Detect the problem type.** Ask, and determine the applicable class in the background:

| Ask the user | Points to |
|---|---|
| Is something missing or not happening at all? | Class 1 |
| Is an effect too weak or unstable? | Class 2 |
| Is something harmful or undesired occurring? | Class 1, Group 1.2 |
| Is it hard to measure or detect something? | Class 4 |
| Is there a contradiction — you want A and not-A at the same time? | Class 3 |

**Step 4 — Generate and explain solutions.** Present one or more solution ideas for the problem
type. For each one:
- explain why it fits,
- describe how it could be implemented,
- state whether a substance, a field, or the structure is being changed.

Offer a visual or ASCII Su-Field diagram after this step, not before.

**Step 5 — Evaluate and refine.** Ask:
- Is this close to your ideal final result (IFR)?
- Would you like to simplify it, enhance it, or try another idea?

If needed, run the steps again with another class.

---

## 2. The five classes at a glance

### Class 1 — Creating and completing Substance-Field Models

*Goal: complete or correct an incomplete or harmful SFM.*

- Check completeness — two substances and one field. Incomplete → Standard 1.1.1.
- Insufficient effect → Standards 1.1.2–1.1.8.
- Harmful effect → Group 1.2, e.g. shielding or rerouting fields.

Example: a gas jet damages a part → introduce a shielding substance (1.2.1).

### Class 2 — Improving existing SFMs

*Goal: increase system performance without a structural overhaul.*

- Increase complexity — Group 2.1
- Use advanced materials and fields — Group 2.2
- Synchronize processes — Group 2.3
- Magnetic and special cases — Group 2.4

Example: replace a hard-to-control field with a more stable one (2.2.1).

### Class 3 — Transition to super- or subsystems

*Goal: shift the solution scope to a higher or lower system level.*

- Bi- and polysystems — Group 3.1
- Micro/macro transitions — Standard 3.2.1

Example: split functionality across subsystems instead of overloading one component.

### Class 4 — Detection and measurement

*Goal: measure or detect parameters that are hard to observe.*

- Indirect measurement — Group 4.1
- Construct measurement SFMs — Groups 4.2–4.4
- Signal amplification — Group 4.3; evolution of the measuring system — Group 4.5

Example: measure the temperature inside a rotating shaft with an indirect wireless sensor (4.1.1).

### Class 5 — Supporting standards for system improvement

*Goal: enable the ideal final result. Class 5 is used across all other classes.*

- Add substances — Group 5.1 — or fields — Group 5.2
- Phase transitions — Group 5.3
- Physical effects — Group 5.4
- Generation of particles — Group 5.5

Example: introduce a temporary substance for a reversible effect or for control, e.g. via
condensation.

---

## 3. Class selection guide — diagnostic questions

Use these to decide which class to begin with:

| Question | Start with |
|---|---|
| Does something essential seem missing? | Class 1 |
| Is the effect too weak, unstable, or slow? | Class 2 |
| Is the system blocked by a conflict or trade-off? | Class 3 |
| Is something hard to measure or detect? | Class 4 |
| Is everything present, but performance still limited? | Class 5 |

---

## 4. Working instructions per class

### Class 1 — Building and completing the SFM

**Goal:** correct or complete incomplete, malfunctioning, or harmful Substance-Field Models.

1. Check whether the SFM contains S1 (subject), S2 (tool), and F (field). A missing component →
   Standard 1.1.1.
2. Weak effect → Standards 1.1.2–1.1.8, e.g. internal or external additives, adaptation of the
   system environment.
3. Harmful effect → Group 1.2, e.g. shielding, diversion, neutralization.
4. Correct or extend the SFM with the new fields or substances.

*Ideal Final Result: a fully functioning model with the fewest possible additional elements.*

### Class 2 — Improving existing SFMs

**Goal:** make the SFM more efficient, controllable, or adaptable without changing the system.

1. Identify what is suboptimal: poor control, low efficiency, rigidity, poor adaptability.
2. Group 2.1 — add complexity: linked or dual-field systems.
3. Group 2.2 — evolve materials and fields, e.g. fragmenting substances, introducing mobility.
4. Group 2.3 — match the system timing, e.g. synchronize fields, separate by rhythm.
5. Group 2.4 — use magnetic or ferromagnetic systems.

*Target: increase performance without redefining the system boundaries.*

### Class 3 — Transition to super- and subsystems

**Goal:** find a solution outside the original system boundaries, at the macro or micro level.

1. If the contradiction cannot be resolved inside the system, analyse super- and subsystem options.
2. Group 3.1 — bi- and polysystems: coupling systems, segmentation, trimming.
3. Group 3.2 — shift to the micro level: molecular, nanotechnological, or quantum-level solutions.

*Goal: open solution spaces beyond the current system.*

### Class 4 — Detection and measurement

**Goal:** make hidden or hard-to-access parameters observable and measurable.

1. Define what has to be detected, e.g. temperature, pressure, motion.
2. If direct measurement is not possible → Group 4.1, indirect methods.
3. Build measurement SFMs (Group 4.2), enhance the effect (Group 4.3), or use the special
   techniques of Groups 4.4–4.5.

*Goal: reveal invisible parameters indirectly, so that control and feedback become possible.*

### Class 5 — Auxiliary standards and enablers

**Goal:** support or enable solutions from the other classes by simplifying, stabilizing, or
preparing the system.

1. Add substances (Group 5.1) or fields (Group 5.2) as needed.
2. Use phase transitions (Group 5.3), e.g. evaporation, melting.
3. Apply physical effects (Group 5.4), e.g. field enhancement, self-regulation.
4. Generate new particles or substances (Group 5.5) through decomposition or synthesis.

*Goal: create the conditions under which the other standards become effective.*

---

## 5. Unified workflow

For any technical or organizational problem:

1. Describe the problem — what is not working?
2. Identify all substances and fields.
3. Build the SFM: `S1 --F-- S2`.
4. Determine the applicable class:
   - Missing components → Class 1
   - Weak effects → Class 2
   - System-level contradiction → Class 3
   - Measurement issue → Class 4
   - Missing conditions → Class 5
5. Select the relevant standard and derive a solution.
6. Define the Ideal Final Result and specify the concrete solution.

---

## 6. The class path is not linear

After applying a standard from any class, re-evaluate:

- Has the SFM changed?
- Are contradictions still unresolved?
- Should another class now be reconsidered — e.g. Class 3 after Class 1 has failed?

---

## 7. Contradiction analysis

When no clear SFM solution emerges, or when every improvement leads to a trade-off, identify the
underlying contradiction:

- **Technical contradiction** — one parameter improves, another worsens.
- **Physical contradiction** — the same parameter must be in opposite states.

If such contradictions exist, apply ARIZ or the separation principles to restructure the problem
logic.

---

## 8. Defining the Ideal Final Result

1. Guide the user: "What would be the perfect solution if no cost, weight, or complexity were
   added?"
2. Identify which effects would remain, which would disappear, and which would maintain themselves
   in the ideal case.
3. Use Class 5 standards to approximate the IFR.

---

## 9. Belski variant matrix — systematic SFM completion

This is the systematic form of the variant matrix, following the approach of Iouri Belski for
incomplete or insufficient SFMs. Its purpose is **not** to select a single standard solution but to
explore the full range of possible modifications, in line with Standard 1.1.1 and beyond.
`SKILL.md` carries the short form for the quick case; use the version below when you want the whole
solution space rather than one standard.

Apply these five transformations to the user's SFM in turn:

1. Add a new field between the existing substances (F_new).
2. Replace the existing field with a different one (F_alt).
3. Replace one of the substances, S1 or S2, with an alternative (S1' or S2').
4. Introduce an auxiliary substance S3 to mediate or enable the interaction.
5. Reorganize the system spatially or structurally so that the field can take effect.

For each variant, generate a solution concept that is specific to the problem domain — mechanical,
thermal, electronic, organizational. Optionally suggest a Class 5 enhancement per variant, e.g.
stabilizing fields, control mechanisms, energy efficiency aids.

Present each variant in this format:

```
Variant X: [transformation type]
- Modified SFM
- Explanation
- Possible implementation
- Optional Class 5 enhancement
```

At the end, summarize the most promising variant or variants. Then ask the user: "Would you like a
visual representation of the final solution?"

---

## 10. Worked examples

**Incomplete Substance-Field Model — labeling malfunction.**
*Problem:* an automatic labeling machine fails to apply a label to the product in every cycle.
*Solution:* recognize the incomplete SFM, identify the missing field, and apply Standard 1.1.1 —
e.g. add a vacuum or electrostatic support field. Optionally apply Class 5 standards to improve
process stability.

**Insufficient effect — poor heat transfer.**
*Problem:* a heat sink releases too little heat, so the system temperature exceeds acceptable
limits despite active ventilation.
*Solution:* identify the insufficient heat transfer effect in the SFM, apply Standard 1.1.2 — e.g.
thermal paste as an internal additive — and use Standard 2.2.4 to introduce dynamic elements.
Optionally apply Class 5 to optimize the effect further.
