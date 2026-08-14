---
name: innovation-checklist
description: "TRIZ Innovation Situation Questionnaire (ISQ / ISQ++) — guides users through the structured ISQ process by presenting questions and capturing responses, with optional Excel export. Use this skill when the user mentions 'ISQ', 'innovation checklist', 'innovation situation questionnaire', or wants a structured questionnaire to analyze their engineering challenge, clarify contradictions, or document their innovation situation."
---

<!-- 
  Based on the TRIZ Innovation Checklist (ISQ) Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see LICENSE in the repository root.
-->

# TRIZ Innovation Checklist (ISQ)

Guide the user through the Innovation Situation Questionnaire (ISQ) process step-by-step, capture all responses accurately, and optionally generate a structured Excel export.

## Assets

The ISQ++ source documents and Excel templates are in `assets/`:
- `assets/TRU_ISQ_EN.pdf` — English ISQ++ questionnaire (authoritative source)
- `assets/TRU_ISQ_DE.pdf` — German ISQ++ questionnaire
- `assets/TRU_ISQ_EN.xlsx` — English Excel export template: header fields `System name` and `Date`, then the question table from row 4 with the columns `Category`, `Question`, `Answer`, `Notes`
- `assets/TRU_ISQ_DE.xlsx` — German Excel export template: header fields `Systemname` and `Datum`, then the question table from row 4 with the columns `Kategorie`, `Frage`, `Antwort`, `Anmerkungen`

**Pick the pair that matches the language of the session** — the German PDF with the German template, the English PDF with the English one. Read the appropriate PDF to obtain the full question set before starting the interview.

## Interaction flow

1. **Present questions** from the ISQ PDF in the defined order. Wait for the user's response before continuing. Do not alter the question order under any circumstances.

2. **Explain as needed.** If clarification is needed, explain TRIZ concepts or provide examples.

3. **Allow flexibility.** Allow the user to skip or revisit questions.

4. **Excel export.** If requested, generate an Excel file from the template:
   - **Fill the two fields above the table.** `B1` takes the system name, `B2` the date. The
     system name is the answer to the opening question both PDFs ask before the first
     category — *"What is the name of the system?"* / *"Wie lautet der Name des Systems?"* —
     which is why it is a header field and not a row of the question table. That table starts
     at row 4.
   - **Match the template to the language of the session.** A German interview exports from
     `TRU_ISQ_DE.xlsx` with the column headers `Kategorie`, `Frage`, `Antwort`, `Anmerkungen`;
     an English one from `TRU_ISQ_EN.xlsx` with `Category`, `Question`, `Answer`, `Notes`.
     Never mix the two — German questions under English headers, or the reverse, make the
     export unusable as a working document.
   - Use the ISQ++ file structure to maintain category and question order
   - Refer to the Excel templates in `assets/` for formatting guidance

5. **Ensure completeness.** Ensure all responses are saved before compiling.
