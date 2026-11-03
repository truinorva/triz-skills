<!-- 
  Based on the TRIZ Function Analysis Prompt
  Copyright (c) 2025 Jens Traeger
  Licensed under the MIT License — see the LICENSE file shipped with this Skill.
-->

# Function model — CSV export

Reference for the `function-analysis` skill. Read it once the function table is finished, before offering the CSV export.

---

## Asking for it

After the table is finished, ask whether the user wants it as CSV — and then **stop** and wait for the answer.

- Ask in the user's own language and in your own words. The wording in this file is an instruction, not a sentence to print: never quote it, and never ask in English inside a German answer.
- Never answer your own question by outputting the CSV straight away.

## Column layout

```
Carrier,Carrier Type,Action,Object,Object Type,Status,Parameter
```

| Column | Content | Language |
|---|---|---|
| `Carrier` | the component that acts | language of the analysis |
| `Carrier Type` | `standard` \| `super` \| `target` | **always English** |
| `Action` | one short active verb | language of the analysis |
| `Object` | the component that is acted on | language of the analysis |
| `Object Type` | `standard` \| `super` \| `target` | **always English** |
| `Status` | `normal` \| `insufficient` \| `excessive` \| `harmful` | **always English** |
| `Parameter` | the parameter that changes or is kept | language of the analysis |

- **Type:** `standard` is a system component, `super` a super-system element, `target` the target of the main function.
- **Status** carries category and degree of fulfillment together: a useful function is `normal`, `insufficient` or `excessive`; a harmful function is `harmful`.
- Quote any field that contains a comma.

## Why the structure words stay English

The header row, the type words and the status words are the controlled vocabulary of this format and stay English even in a German analysis. An importer identifies the columns by these keys; a translated header is read as data, and the model starts with a phantom function. Names, verbs and parameters stay in the language of the analysis.

## Example

German analysis, English structure words:

```
Carrier,Carrier Type,Action,Object,Object Type,Status,Parameter
Hand,super,drueckt,Hebel,standard,normal,Position
Schneidrad,standard,schneidet,Pizza,target,normal,Struktur
Schneidrad,standard,verletzt,Finger,super,harmful,Unversehrtheit
```

## What to tell the user

Tell the user that the file can be imported into any function-model tool that reads this column layout, and that the two type columns already carry the component classification, so it does not have to be entered again. Name no specific tool: the column layout is the interface.
