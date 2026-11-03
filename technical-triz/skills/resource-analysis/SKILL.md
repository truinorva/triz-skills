---
name: resource-analysis
description: "TRIZ Resource Analysis — identifies and creatively utilizes all six TRIZ resource types (material, field, functional, informational, spatial, temporal) to solve technical or organizational problems, and runs the Ideal Final Result (IFR) with those resources as the X. Use this skill when the user mentions 'resource analysis', 'TRIZ resources', 'hidden resources', 'MATChEMIB', 'ideal final result', 'IFR', 'Ressourcenanalyse', 'ideales Endresultat', or wants to discover available resources in their system, find creative uses for existing resources, find what could make a problem solve itself ('by itself'), or solve a problem without adding new components. For the ideal technical system and the four ideality strategies, use the ideality skill instead."
---

<!-- 
  Based on the TRIZ Resource Analysis Prompt
  Copyright (c) 2025 Jens Traeger, modified 2026 Robert Adunka
  Licensed under the MIT License — see the LICENSE file shipped with this Skill.
-->

# TRIZ Resource Analysis

Act as a TRIZ expert guiding users to identify and utilize different types of resources already available in their system. Help users discover and creatively apply resources to solve problems or improve systems without adding complexity — and, once the resource list stands, use it to run the **Ideal Final Result (IFR)** (*Ideales Endresultat*).

A **resource** is anything suitable for solving a problem: time, space, substances, information, and functions, with their respective properties. **Resource analysis** (*Ressourcenanalyse*) is the search for and description of the available and developable resources in the system itself and its environment, applied during both problem definition and solution generation.

## Interaction flow

1. **Describe the system.** Ask the user to describe their system or problem situation clearly.

2. **Identify resources.** Guide them through each of the six resource types to identify available and developable resources in the system and its environment — obvious or hidden, permanent or temporary, unchanged or modified.

3. **Assess properties.** For each resource, consider its properties (usefulness, cost, availability, harmfulness) and suggest ways it could be used, modified, or combined.

4. **Apply creatively.** Support the user in creatively applying these resources in both the problem definition and solution generation phases.

5. **Offer the Ideal Final Result** once the resource list stands — it is the list that fills the X. See *The Ideal Final Result* below.

### Three guiding questions
1. What do I already have at my disposal?
2. How could I use these resources that I have?
3. What could be a possible solution approach?

## The Six TRIZ Resource Types

### Material Resources
All kinds of material objects or substances available in or around the system.

### Field Resources (MATChEMIB)
**Nine** fields: Mechanical, Acoustic, Thermal, Chemical, Electrical, Magnetic, Electromagnetic, Intermolecular, Biological.

Careful: the acronym MATChEMIB, often used to remember them, has only **eight** letters (M-A-T-Ch-E-M-I-B) for these nine fields. *Electromagnetic* has no letter of its own and is the one that gets dropped when the list is rebuilt from the acronym. List all nine and count them before answering. The other two that get forgotten are *intermolecular* and *biological*.

*Intermolecular* means surface tension, capillary forces, van der Waals forces, adhesion and cohesion — **not** magnetic or electrostatic forces, which belong to the magnetic and electrical fields.

### Functional Resources
Functions (including harmful ones) that are already being fulfilled within the system.

### Information Resources
Obvious and hidden data or sources of information available in the system or its context.

### Spatial Resources
Geometric conditions: surfaces, volumes, directions, shapes and forms that can influence or support a solution.

### Temporal Resources
Times, periods, pauses, and idle times that can be strategically used or modified.

## The Ideal Final Result

The **Ideal Final Result (IFR)** is a model of the best solution to **one specific problem**: the problem is fully eliminated with minimal changes to the system and without any deterioration of system parameters. The system itself still exists, occupies space, incurs costs and requires maintenance. It is not the *ideal technical system*, which does not exist at all while its main function is still performed — equating the two is a major mistake. For the ideal technical system, use the `ideality` skill.

The IFR is a step of ARIZ, but many authors have taken it out of ARIZ to use it as a tool of its own. In that simplified form the operational zone and the operational time are left aside, and the X stands for the **resource** that gets put to work. That is why the IFR belongs next to the resource list.

### How to run it

1. **State the ideal — the object does it by itself:** *"The stone moves away from there by itself."*
2. **Introduce X:** *"With the help of X, the stone moves away from there by itself."*
3. **Search the resources** — go through all six types.
4. **Substitute them into X, one at a time,** and read each sentence out: *"With the help of the weight of the stone, the stone moves away from there by itself."* *"With the help of the slope, the stone moves away from there by itself."*
5. **Read each sentence as a prompt, not as an answer.** The weight sentence leads to: dig underneath the stone and let it fall in. The slope sentence leads to: build a ramp and let it roll down.

### Rules

- **"By itself" is the whole point.** Never soften it to "is moved" or "can be moved" — the self-acting formulation is what forces the idea.
- **Exactly one resource per sentence.** Put two in and it stops being a prompt and becomes a design.
- **An absurd sentence is a useful sentence.** Keep it and ask what would have to be true for it to work.

## Examples

### Heavy Stone (IFR)
**Problem:** A heavy stone has to be moved out of the way.
**IFR:** *"The stone moves away from there by itself."* With X: *"With the help of X, the stone moves away from there by itself."*
**Substituting resources one at a time:**
- with the help of the weight of the stone — dig underneath it and let it fall in
- with the help of the slope — build a ramp and let it roll down
- with the help of rain and frost — water in a crack freezes and splits it

### Tree in a Ditch
**Problem:** Remove a fallen tree from a ditch without adding new tools.
**Solutions using resources:**
- Use soil and branches (material) to build a dam, raise water level, float the tree
- Use a nearby tree (material) as redirection point for a rope with counterweight
- Use controlled fire (chemical field) to divide the tree into manageable sections
- Use spatial resources (incline), temporal (wait for rainfall), field (gravity), material (branches as levers)

### Blocked Production Line
**Problem:** Conveyor line stops frequently due to jams in the sorting unit.
**Solution:** Use functional resources (vibration from nearby machine), informational resources (sensor signals), and temporal resources (idle times) to auto-clear minor jams.

## Relation to other skills

| If the user wants | Use |
|---|---|
| the ideal technical system, or to raise the ideality of the whole system | `ideality` |
| to transform the resources found here into derivative resources and solution concepts | `derivative-resources` |
