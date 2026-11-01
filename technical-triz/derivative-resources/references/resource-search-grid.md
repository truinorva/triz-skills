<!-- 
  Based on the Derivative Resources Analysis Prompt (Extended TRIZ Framework V4.0)
  Copyright (c) 2025-2026 Tanasak Pheunghua
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# The resource search grid

Used at step 3 (existing resource inventory, Table A) and step 4 (characterization) of
`SKILL.md`. The inventory is built by sweeping two dimensions against each other — **where** a
resource sits and **what kind** of resource it is. Going down only one dimension is how the
obvious resources get found and the useful ones get missed.

---

## Dimension 1 — Source (*where it sits*)

| Source | What to look at |
|---|---|
| **Product** | the object the main function acts on — its substance, surfaces, shape, state, motion, temperature, its own waste |
| **Tool** | whatever performs the function — substance, field, motion, wear, heat it gives off, its idle periods |
| **Subsystem** | components below the system: parts, joints, coatings, fluids, controls, sensors already fitted |
| **System** | the system as a whole: its structure, its cycles, its unused capacity, its information |
| **Super-system** | the plant, line, building, vehicle, organization the system sits in; neighbouring machines |
| **Immediate environment** | air, moisture, dust, ambient temperature, light, gravity, pressure, vibration right at the problem |
| **Wider environment** | weather, day/night, seasons, ground, infrastructure, external supply |
| **Waste and by-products** | scrap, swarf, dust, off-gas, waste heat, waste water, noise, rejects, spoilage, downtime |
| **Cheap or free** | anything abundant and unpriced — air, water, gravity, ambient heat, sunlight, existing data |

## Dimension 2 — Type (*what kind it is*)

| Type | What to look at |
|---|---|
| **Substance** | solids, liquids, gases, powders, coatings, films, residues, the void itself |
| **Field / energy** | mechanical, acoustic, thermal, chemical, electrical, magnetic, electromagnetic, intermolecular, biological (MATChEMIB) |
| **Space** | volumes, gaps, cavities, surfaces, interfaces, directions, orientations, nesting room |
| **Time** | cycle times, pauses, idle periods, transients, lead times, periodicity, the moment before and after |
| **Information** | sensor signals, logs, counters, timestamps, operator knowledge, records, patterns, the defect itself as a signal |
| **Function** | functions already performed, including harmful and excessive ones |
| **Structure** | arrangement, hierarchy, symmetry, modularity, porosity, microstructure |
| **Component** | existing parts that could take on a second duty |
| **Connection** | joints, contacts, couplings, channels, networks |
| **Shape / geometry** | contours, radii, taper, roughness, aspect ratios |
| **Flow** | flows of substance, energy, information, money, people — their direction, rate, pulsation |
| **Parameter / property** | temperature, pressure, density, viscosity, conductivity, pH, hardness, and every gradient of them |
| **System effect** | emergent effects: resonance, self-organization, equilibrium, feedback already present |

## Sweeping the grid

Look past the obvious. The resources that get overlooked most often are:

air · water · surfaces · gaps and voids · pressure · gravity · heat · vibration · noise · motion ·
inertia · gradients of any kind · waste · unused capacity · data and signals · timing · idle time ·
geometry · existing functions

Fill Table A with what is actually there, and write `unknown` wherever a value is not known.

---

## Characterization criteria (step 4)

| Criterion | Scale |
|---|---|
| Quantity | insufficient / sufficient / abundant |
| Readiness | ready to use / needs preparation / needs development |
| Usefulness | harmful / neutral / useful |
| Cost | free / low / medium / high |
| Accessibility | direct / indirect / blocked |
| Controllability | high / medium / low / none |
| Stability | stable / varying / unpredictable |
| Compatibility | compatible / conditional / incompatible |
| Present in OZ | yes / partly / no |
| Present in OT | yes / partly / no |

Afterwards, flag the resources that are **free**, **waste**, **harmful**, **underused**, or
**present in both the OZ and the OT**. Those five flags mark where the strong derivatives come
from — a harmful effect that is already in the operating zone at the operating time is the single
most promising starting point in the table.

---

## Resource priority rule (steps 10 and 13)

When two candidates compete, the one higher on this list wins. Drop to a lower level only when
the higher ones are inadequate.

| Level | Resource |
|---|---|
| 1 | existing resources in the OZ and the OT |
| 2 | internal system resources |
| 3 | super-system and environment resources |
| 4 | waste, harmful, cheap, free resources |
| 5 | small modifications of existing resources |
| 6 | larger modifications |
| 7 | new external substances, fields or components |

Level 7 is not forbidden — it is the admission that levels 1–6 were searched and found wanting,
and it should be stated as such.
