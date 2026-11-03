<!-- 
  Based on the TRIZ Ideality Prompt
  Copyright (c) 2025 Jens Traeger, modified 2026 Robert Adunka
  Licensed under the MIT License — see the LICENSE file shipped with this Skill.
-->

# TRIZ Ideality — method reference

Reference for the `ideality` skill. `SKILL.md` carries the sequence, the rules and the output format; this file carries the background behind the rules and the worked examples. Read it before Step 2 and keep it at hand.

---

## The ideality equation

Ideality (*Idealität*) is the ratio of everything the system gives you to everything it costs you:

```
                     sum of all benefits
    Ideality  =  ----------------------------
                  sum of all payment factors
```

**Benefits** (*Nutzen*): the useful functions the system performs, and how well it performs them.

**Payment factors:** not only money. Also the space the system takes up, the energy and material it consumes, the maintenance it needs, the harm it does to its surroundings, the risk it carries, and the attention it demands from the user.

The four ideality strategies are the four ways to act on this ratio:

| Strategy | Term |
|---|---|
| Increase useful functions and benefits | numerator up |
| Add new useful functions | numerator up |
| Reduce or eliminate harmful effects | denominator down |
| Maintain or reduce resource usage | denominator down |

A system becomes ideal when the payment factors reach zero while the main function is still performed — which is the ideal technical system described below.

### Compare it, do not calculate it

There is no established method for estimating either the benefits or the payment factors of a system; the MATRIZ knowledge base states this explicitly. Any number would be invented, and an invented number looks like a measurement. Therefore:

- Never state an ideality value, score, percentage or ratio as a figure.
- Never compare two systems by a computed number.
- Name the terms instead and compare them in words: which benefits are there, which payment factors dominate, and which strategy attacks the dominant one.

| Usable | Not usable |
|---|---|
| "The denominator is dominated by the waste heat and the maintenance intervals." | "Ideality 0.42" |
| "Variant B removes the largest payment factor, the cleaning effort, and keeps every benefit of A." | "Variant B scores 7/10, variant A 5/10." |

If the user asks for a number, say that ideality is not a measurable quantity and offer the comparison instead.

### Not to be confused with Value in function analysis

*Value* in function analysis **is** calculable: a normalized function index over normalized cost, per component. Ideality applies the same idea to a whole system, where neither term can be measured.

---

## Directions before ideas

What this skill produces is **directions of development**. A direction names a movement — away from what, towards what, and which part of the ideality ratio gets better. An idea names a thing.

**A direction** (cordless screwdriver): *"Take the energy source out of the user's hand. The dominant payment factor is the weight carried in the hand, not the energy itself."*
**Ideas underneath it:** *"(for example a belt battery, or energy fed through the handle)"*.

**Not directions:** *"integrated LED lighting"*, *"Bluetooth screw counting"*, *"brushless motor"*. Those are product features. They name a thing instead of a movement, and they end the user's thinking instead of starting it.

Why the rules in `SKILL.md` are as strict as they are:

- A direction that cannot say which term of the equation it improves gives the user nothing to check it against — it is a feature in disguise.
- An idea standing alone invites the user to judge the idea and forget the direction. One weak example then kills a strong direction.
- Two or three directions keep the analysis readable; eight features turn it into a brainstorming list.
- Concrete ideas are still part of the job. A user who asks for them gets them — placed under their direction, so the direction stays visible.

---

## The ideal technical system and the Ideal Final Result

An **ideal technical system** performs its main function without existing and without side effects.

This is **not** the Ideal Final Result, and equating the two is a well-known mistake — the MATRIZ knowledge base warns about it on both of its pages.

| | Ideal technical system | Ideal Final Result (IFR, *Ideales Endresultat*) |
|---|---|---|
| Describes | the **system** | **one specific problem** |
| Statement | the system does not exist, but its main function is still performed | the problem is fully eliminated with minimal changes to the system and without any deterioration of system parameters |
| The system itself | is gone | still exists, occupies space, incurs costs and requires maintenance |
| Belongs to | ideality and how technical systems develop further | the resource list: the X in "with the help of X, the object does it by itself" is a resource |
| Skill | `ideality` (this one) | `resource-analysis` |

This skill produces the ideal technical system and does not formulate an IFR. If the user asks for one, explain the difference in two sentences, point to `resource-analysis`, and stop. Do not formulate one anyway, and do not pick a sub-problem in order to demonstrate it. Explaining the rule and then breaking it in the same answer is worse than not knowing the rule, because the user believes the result.

### Examples

**Lawn mower.** A lawn mower cuts grass but requires fuel and maintenance, creates noise, and needs a human operator. → The ideal lawn mower cuts grass without existing and without any harmful side effects — e.g., grass that never grows beyond a desired length.

**Car key.** A car key starts the car but can be lost, copied, or broken. → The ideal car key starts the car without existing and without any harmful side effects — e.g., biometric recognition built into the driver's body.

---

## Why the next steps belong to other tools

This skill raises ideality. Deepening the analysis (function model, causal chains, trimming, resources, system levels) and generating solutions (contradictions, the 40 Inventive Principles, separation principles) are the work of other skills — `SKILL.md` lists them by name.

Contradictions, contradiction matrix parameters and inventive principle numbers in particular stay out of this skill. It carries neither the matrix nor the principles, so any such number would be invented — and an invented number looks exactly like a looked-up one, which makes it worse than no answer. `contradiction-solver` reads them from data.
