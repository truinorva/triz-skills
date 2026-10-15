<!-- 
  Based on the Derivative Resources Analysis Prompt (Extended TRIZ Framework V4.0)
  Copyright (c) 2025-2026 Tanasak Pheunghua
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# The derivative resource operator catalogue

An operator turns an existing resource (`R0`) into a derivative resource (`R1`), which can be fed
back in to produce `R2` and `R3`. Used at step 6 (classical) and step 7 (extended) of `SKILL.md`.

Two sets, and **every derivative must be labelled as one of them**:

- **Classical ARIZ Core** — operators A–F. The minimal-change transformations of classical
  TRIZ/ARIZ. Try these first: they stay closest to the system as it is.
- **Extended Framework** — operator groups 7A–7J. Everything beyond substance-level change:
  fields, waste, space, time, information, function, interaction, process, drift.

For each hit, record the existing resource, the operator, the mechanism, the new property, and the
useful function it might serve — and mark the mechanism `HYPOTHESIS` unless known science supports
it.

---

# Part 1 — Classical ARIZ Core (operators A–F)

## A — Mixture

Combine two or more substances **already present** in or around the system.

Produces: alloys, composites, suspensions, emulsions, foams, solutions, slurries, doped
materials — with properties neither constituent had.

Examples: waste fibres + waste plastic → a durable composite · swarf + binder → a filler ·
dust + water → a paste that no longer flies.

## B — Substance + void

Introduce or exploit emptiness: a gap, cavity, bubble, pore, channel, hollow, vacuum.

Produces: lower mass, insulation, compliance, capillarity, buoyancy, controlled collapse,
a place to put something, a path for a flow.

Examples: foamed filler → mass down, stiffness kept · porous surface → lubricant reservoir ·
bubbles in a liquid → acoustic damping · a deliberate cavity → the room a sensor needed.

## C — Phase or state change

Move a substance between solid, liquid, gas, plasma, gel, glassy, crystalline, dissolved,
adsorbed — or exploit the transition itself.

Produces: large volume and property jumps, latent heat, cleaning action, handling advantages,
a substance that disappears after use.

Examples: freeze the liqueur core so it can be handled as a solid · ice that sublimates away
after serving as a fixture · boiling that lifts a deposit off a wall · condensation as a free
source of clean water.

## D — Decomposition, destruction, separation, combustion

Break a resource down instead of building it up: grind, dissolve, electrolyse, pyrolyse, filter,
centrifuge, burn.

Produces: fragments, powders, fibres, ions, radicals, gases, fractions, heat — often more useful
than the intact original.

Examples: burn the waste → process heat (`R1`) and ash as a filler (`R1`) · grind the reject part
→ abrasive · electrolyse the process water → gas for a local field.

## E — Transition between structural levels

Move the problem up or down the structural ladder: assembly → part → material → microstructure →
molecule → atom → ion → elementary particle → field.

Produces: at a lower level, properties and degrees of freedom the whole object did not offer; at
a higher level, system effects a single part cannot show.

Examples: replace a rigid tool with a granular one, then with a magnetic fluid, then with a field
alone · texture the surface instead of changing the part · work on the oxide layer rather than
the metal.

## F — Available field and field combinations

Use the fields that are already there, or combine two of them. The MATChEMIB list: **M**echanical,
**A**coustic, **T**hermal, **Ch**emical, **E**lectrical, **M**agnetic, **I**ntermolecular,
**B**iological — plus electromagnetic.

Produces: a function performed with no new substance at all, which is the cheapest derivative
there is.

Examples: existing machine vibration → free agitation for the neighbouring process · gravity
instead of a conveyor · the motor's waste heat → the drying field · magnetic field + thermal
field → controlled local heating.

---

# Part 2 — Extended Framework (operator groups 7A–7J)

## 7A — Combining

Cross two resources that are not usually considered together:

| Combination | Produces |
|---|---|
| substance × substance | mixtures, coatings, reactions — see operator A |
| substance × field | a substance made controllable; magnetic fluids, heated media, charged powders |
| field × field | interference, resonance, beat frequencies, standing waves, combined gradients |
| substance × space | layering, nesting, filling a void, surface patterning |
| resource × time | a resource present only at the right moment; pulsing, pre-positioning |
| resource × information | a resource that reports its own state; a part that is also a gauge |

## 7B — By-products and waste

Treat every output nobody wanted as an input nobody has claimed: scrap, swarf, dust, off-gas,
waste heat, waste water, noise, vibration, rejects, spoilage, downtime, returned goods.

Examples: spent brewing grain → animal feed · waste heat → district heating · CO₂ from
fermentation → carbonation · noise → the condition-monitoring signal.

## 7C — Field transformation

Take a field that exists and change it rather than adding a new one:

increase · decrease · concentrate · disperse · make continuous · make pulsed · redirect ·
modulate · convert to another field · create a gradient · store · transfer elsewhere.

Examples: concentrate diffuse vibration onto one point → a cleaning field · pulse a continuous
heat input → thermal shock that cracks the deposit · convert pressure drop → electricity for the
local sensor · store the braking energy and release it in the next cycle.

## 7D — Spatial derivatives

Derive from geometry and place: unused volume, gaps, surfaces, interfaces, orientation,
asymmetry, nesting, the other side of a wall, the space between two parts.

Examples: use the gap as the metering channel · the inside of the hollow shaft as the coolant
line · reorient the part so gravity does the clamping · the interface itself as the seal.

## 7E — Temporal derivatives

Derive from time: pauses, idle periods, transients, start-up and shut-down, the moment before and
after, periodicity, sequence, duration, the long run.

Examples: do the cleaning in the idle minute that already exists · exploit the start-up transient
as the test signal · act before the problem arises rather than against it · let the slow drift
perform the slow adjustment.

## 7F — Informational derivatives

Usually the cheapest and highest-priority group. Climb the ladder:

| Level | Example |
|---|---|
| raw signal | the current trace, the timestamp, the counter reading |
| feature | peak, slope, duration, spacing, variance |
| pattern | the recurring signature of one failure mode |
| inference | which machine, which batch, which shift |
| useful information | the decision that can now be made |

Examples: the defect itself as a position sensor — where it appears tells you where the cause is ·
existing logs as the history nobody read · two similar lines running under different conditions as
a natural experiment nobody designed · an absent record as the first thing worth capturing.

## 7G — Functional derivatives

Derive from the functions already being performed, including harmful and excessive ones: let an
existing function serve a second purpose, reverse it, or turn the harm into the tool.

Examples: the wear debris becomes the lapping compound · the sealing function also performs the
damping · the excessive clamping force performs the forming · the harmful oxidation forms the
protective layer.

## 7H — Physical and chemical interactions

Derive from an effect that the present substances and fields can produce between them: capillarity,
adsorption, osmosis, thermal expansion, phase transition, surface tension, electrostatics,
catalysis, corrosion, polymerization, biological action.

**This is the group that most invites invention.** Do not claim an interaction is feasible unless
known science supports it, and mark the uncertain ones `HYPOTHESIS` with the experiment that would
settle it.

## 7I — Process, transfer and storage

Derive by moving a resource in space, in time, or between forms: conversion, transport, buffering,
accumulation, release, recirculation, cascading.

Examples: accumulate the trickle until it is useful · recirculate the rinse water through a filter
· cascade the waste heat through three temperature levels · store the off-peak energy as heat.

## 7J — Change over time

Derive from the fact that resources are not constant: wear, drift, ageing, fatigue, settling,
curing, saturation, contamination, learning, seasonal variation.

Examples: the wear profile as the record of the load history · controlled ageing as the
self-adjusting fit · the drift rate as the remaining-life indicator · the contamination layer as
the diffusion barrier.

---

## Beyond `R1`

Any derivative can be the input to another operator. Chains are where this method earns its keep:

> `R0` reject part → **D** decomposition → `R1` powder → **A** mixture with binder → `R2` filler →
> **7G** functional → `R3` filler that also damps the vibration causing the rejects.

Stop a chain when no new useful property appears, cost explodes, feasibility is poor, or the
function is achieved — and say which of the four it was.
