---
name: function-oriented-search
description: "TRIZ Function-Oriented Search (FOS), Method-Oriented Search (MOS), and Scientific Effects exploration — helps users find inventive solutions by searching for scientific effects, natural analogies, and functionally similar solutions from other domains. Use this skill when the user mentions 'function-oriented search', 'FOS', 'MOS', 'scientific effects', 'AskNature', 'Oxford Creativity', or wants to find how other systems or nature solve a similar function."
---

<!-- 
  Based on the TRIZ Function-Oriented Search Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Function-Oriented Search

Generate inventive ideas by exploring scientific effects, natural analogies, or functionally similar solutions through structured TRIZ searches.

## Reference files

Database query schemas are in the `references/` directory:
- `references/oxford_creativity.txt` — allowed query values for Oxford Creativity
- `references/production_inspiration.txt` — allowed query values for ProductionInspiration

## Interaction flow

1. **Problem description.** Ask the user to describe their problem, ideally using TRIZ problem formulation tools (e.g., Substance-Field Analysis, Function Analysis, RCA+).

2. **Choose approach:** Clarify if they want to explore:
   - **(1) Scientific Effects** — abstract the function, suggest relevant physical/chemical/geometric effects
   - **(2) Function-Oriented Search (FOS)** — abstract the problem to a general function, find industries or use-cases with exemplary execution, including nature (AskNature), patents, or industrial examples
   - **(3) Method-Oriented Search (MOS)** — explore proven technical or methodological patterns

3. **Provide database suggestions.** Suggest searches from online resources and, where possible, provide ready-to-use queries. Regardless of chat language, always provide database queries in English.

### Oxford Creativity Database
URL: http://wbam2244.dns-systems.net/EDB_Welcome.php

Three query types are available. Read `references/oxford_creativity.txt` for allowed values:
- **Function Query:** Select an Action + Object (e.g., "Heat" + "Liquid")
- **Parameter Query:** Select an Operation + Parameter (e.g., "Increase" + "Temperature")
- **Transform Query:** Select energy Transform From + To (e.g., "Mechanical" + "Thermal")

### ProductionInspiration Database
URL: http://www.productioninspiration.com/

Read `references/production_inspiration.txt` for allowed values. Select a function and a state (e.g., "Heats" + "Liquid").

### Other Databases
- **MoreInspiration:** http://www.moreinspiration.com/
- **AskNature (Biomimicry):** https://asknature.org/

4. **Select and adapt.** Support the user in selecting and adapting one or more concepts to their specific problem.

## Examples

### Water Extraction from a Well
**Problem:** Manual water extraction using a bucket is inefficient.
**Function:** Move liquids
**Scientific Effects:** Coanda Effect, Centrifugal Force, Siphoning, Archimedean Screw
**FOS Examples:** Hand pump (mechanical engineering), Archimedean screw (ancient irrigation), natural capillary action (plants)

### Heating Water for Coffee
**Problem:** Need to heat water in a remote location without fire.
**Function:** Heat liquids
**Scientific Effects:** Microwave Radiation, Electrical Resistance, Induction Heating
**Solutions:** Microwave oven, immersion heater, induction cooker
