# triz-skills

**Universal TRIZ Skills for Claude – open, structured, and future-proof**

This repository contains a growing, curated library of **TRIZ** (Theory of Inventive Problem Solving) **Skills for Anthropic's Claude** – covering both **technical** and **business** TRIZ, from Contradiction Analysis and Function Analysis to Trimming, the 76 Standard Solutions, Ideality, and Resource Analysis.

Every Skill is kept **unzipped, one folder per Skill**, so it can be read, edited, and extended with any standard text editor (e.g. VS Code, Notepad++, BBEdit) and collaborated on with normal Git workflows.

> Maintained by **Truinorva**. Companion repository to [`triz-prompt-engineering`](https://github.com/truinorva/triz-prompt-engineering).

---

## 🌐 Purpose

Our goal is to make TRIZ knowledge usable and sustainable in the age of AI – platform-independent, transparent, and free from proprietary constraints.

This approach allows for:

- Reusable, agent-ready TRIZ methods that Claude can activate on demand
- Future-proof archiving and documentation in plain text
- Simplified integration into company-specific innovation workflows

---

## 🔧 Key Features

- ✅ **Self-contained Skills** – each Skill is one folder with a `SKILL.md` plus optional `references/`
- 📦 **ZIP = release** – develop unzipped in Git, ship by zipping the folder (see [Releasing](#-releasing-packaging-a-skill))
- 🧭 **Two families** – `technical-triz/` for engineering, `business-triz/` for organizational and people-centric problems
- 📖 **English-first, term-bilingual** – content is written in English, with key terms also given in another language (e.g. German) so the AI handles terminology correctly
- ⚖️ **MIT License** – open use, including commercial applications
- 📁 **Git-based collaboration** – with versioning, issue tracking, and a curated main branch
- 🔀 **Pull-request workflow** – changes are made in a feature branch and merged into `main` via PR

---

## 🧩 What is a Claude Skill?

A *Skill* is a folder that packages instructions, reference data, and optional helper scripts so Claude can reliably perform a specialized task. At minimum it contains a `SKILL.md` file with YAML frontmatter (a `name` and a `description`). Claude reads the `description` to decide *when* to activate the Skill, then follows the body of `SKILL.md` to do the work, loading files from `references/` only as needed.

Claude distributes and installs Skills as **ZIP archives**. This repository keeps them **unzipped** for development and collaboration – **releasing a Skill is simply zipping its folder**.

---

## 📂 Directory Structure

```plaintext
triz-skills/
│
├── docs/                         # guides & templates (skill-authoring guide, etc.)
│
├── business-triz/                # TRIZ for organizational, service & people-centric problems
│   └── <skill-name>/
│       ├── SKILL.md
│       └── references/           # (optional) supporting data, tables, images
│
├── technical-triz/               # classical engineering-oriented TRIZ
│   └── <skill-name>/
│       ├── SKILL.md
│       └── references/           # (optional) supporting data, tables, images
│
├── LICENSE
└── README.md
```

This layout mirrors `triz-prompt-engineering`: the same separation of *business* vs. *technical* TRIZ, with each tool isolated in its own self-contained folder, and a shared `docs/` folder for guides.

---

## 📚 Skill Index

### Business TRIZ (`business-triz/`)

| Skill | What it does |
|-------|--------------|
| [`business-function-analysis`](business-triz/business-function-analysis/) | Non-engineer Function Analysis using simplified TRIZ for everyday domains (education, healthcare, retail, HR, hospitality). |
| [`business-msd`](business-triz/business-msd/) | Multi-Screen Diagram (9 Boxes / 9 Windows) to explore a system's past, present and future across super-system, system and sub-system levels. |
| [`perception-mapping`](business-triz/perception-mapping/) | Surfaces stakeholder beliefs, builds Leads-To networks, and exposes hidden contradictions in teams and organizations. |
| [`solutions-at-system-levels`](business-triz/solutions-at-system-levels/) | Generates business solution ideas by exploring super-system and sub-system resources across the system hierarchy. |

### Technical TRIZ (`technical-triz/`)

| Skill | What it does |
|-------|--------------|
| [`76-standard-solutions`](technical-triz/76-standard-solutions/) | Substance-Field (Su-Field) modelling and the 76 Standard Solutions across 5 classes. |
| [`cause-effect-chain-analysis`](technical-triz/cause-effect-chain-analysis/) | Cause & Effect Chain Analysis (CECA) / RCA to trace defects to root causes and contradictions. |
| [`contradiction-solver`](technical-triz/contradiction-solver/) | Resolves engineering & physical contradictions via the Altshuller Matrix, Matrix 2003 and the 40 Inventive Principles. |
| [`derivative-resources`](technical-triz/derivative-resources/) | Finds derivative resources arising through combination, transformation or reinterpretation. |
| [`feature-transfer`](technical-triz/feature-transfer/) | Enhances a system by adopting beneficial features from alternative/competing systems. |
| [`function-analysis`](technical-triz/function-analysis/) | Maps tools-actions-objects and reveals a technical system's main function. |
| [`function-analysis-advanced`](technical-triz/function-analysis-advanced/) | Adds spatio-temporal (when/where) considerations to Function Analysis. |
| [`function-interaction-analysis`](technical-triz/function-interaction-analysis/) | Maps component interactions based on energy/matter/information flow. |
| [`function-oriented-search`](technical-triz/function-oriented-search/) | FOS / MOS and Scientific Effects search for solutions from other domains and nature. |
| [`ideality`](technical-triz/ideality/) | Moves a system toward its Ideal Final Result (IFR) by balancing useful vs. harmful functions. |
| [`innovation-checklist`](technical-triz/innovation-checklist/) | The Innovation Situation Questionnaire (ISQ / ISQ++) for structured problem framing. |
| [`interactive-trimming`](technical-triz/interactive-trimming/) | Extended interactive Trimming with rules A, B, C, D, E, X. |
| [`mpv-analysis`](technical-triz/mpv-analysis/) | Identifies Parameters of Value (PV) and Main Parameters of Value (MPV). |
| [`patent-analyzer`](technical-triz/patent-analyzer/) | Extracts TRIZ parameters and contradictions from patent texts. |
| [`physical-contradictions`](technical-triz/physical-contradictions/) | Resolves physical contradictions via the four Separation Principles. |
| [`resource-analysis`](technical-triz/resource-analysis/) | Discovers and exploits the six TRIZ resource types (MATChEMIB). |
| [`root-cause-analysis`](technical-triz/root-cause-analysis/) | Systematic RCA for engineering failures based on scientific principles and physical parameters. |
| [`root-conflict-analysis`](technical-triz/root-conflict-analysis/) | Root Conflict Analysis (RCA+) — decomposes problems into underlying contradictions. |
| [`smart-little-people`](technical-triz/smart-little-people/) | Smart Little People (SLP) modelling to overcome psychological inertia. |
| [`system-description`](technical-triz/system-description/) | System Description (Mini-ISQ) — a structured starting point before other TRIZ tools. |
| [`system-operator`](technical-triz/system-operator/) | System Operator (9 Boxes / 9 Screens) for time- and hierarchy-based analysis. |
| [`trimming`](technical-triz/trimming/) | Classical Trimming (rules A, B, C) to simplify systems and cut cost. |

---

## ▶️ Using a Skill with Claude

1. **Pick a Skill folder** from `business-triz/` or `technical-triz/`.
2. **Zip the folder** so the `SKILL.md` sits at the archive root (see below).
3. **Install it** into your Claude environment (e.g. Cowork / Claude Code) as a Skill.
4. Describe your problem; Claude activates the matching Skill based on its `description`.

During development you can also point Claude directly at an unzipped Skill folder in this repo.

---

## 📦 Releasing (packaging a Skill)

A release is just a ZIP of the Skill's folder. The `SKILL.md` **must be at the top level of the archive** (not nested inside an extra parent directory).

```bash
# from the repo root — package a single skill
cd technical-triz/contradiction-solver
zip -r ../../contradiction-solver.zip . -x '*.DS_Store' 'Thumbs.db'

# or package every skill in a family
cd technical-triz
for d in */; do (cd "$d" && zip -r "../../${d%/}.zip" . -x '*.DS_Store'); done
```

Verify the archive root contains `SKILL.md`:

```bash
unzip -l contradiction-solver.zip | head
```

---

## ✍️ Authoring a Skill — structure & tips

**Required: `SKILL.md` with YAML frontmatter.**

```markdown
---
name: contradiction-solver
description: "TRIZ Contradiction Solver and 40 Inventive Principles — resolves
  engineering and physical contradictions ... Use this skill whenever the user
  mentions 'contradiction', 'inventive principles', '40 principles', ..."
---

# Human-readable title

Body: step-by-step instructions Claude should follow, what to ask the user,
which reference files to read, and how to present results.
```

Things to observe:

- **`name`** — lowercase, hyphenated, unique, and matching the folder name. This is the Skill's identifier.
- **`description` is the trigger.** It is the *only* thing Claude sees when deciding whether to activate a Skill. Write it in the third person, state what the Skill does, **and list the words/phrases that should activate it** ("Use this skill when the user mentions …"). Be specific to avoid both false triggers and missed triggers. Aim for roughly 1–3 sentences.
- **Keep `SKILL.md` lean; push detail into `references/`.** Claude loads `SKILL.md` up front but reads reference files only when needed. Put long tables, matrices, examples, and images (e.g. the 40 Principles, the Contradiction Matrix, the 76 Standard Solutions) in `references/` and tell `SKILL.md` to read them on demand. This keeps activation cheap and the instructions focused.
- **Reference paths are relative** to the Skill folder (e.g. `references/40_Inventive_Principles_EN.md`). Never use absolute or machine-specific paths.
- **Bundle data with the Skill.** Anything the Skill needs (CSVs, Markdown tables, PNG diagrams, helper scripts) lives inside the folder so the ZIP is self-contained.
- **Write in English first.** English is the primary language for all `SKILL.md` instructions and documentation.
- **Add key terms in another language to anchor terminology.** Where a precise term or phrasing matters, include the equivalent in another language (e.g. German) inline so the AI maps and handles it correctly. See [`contradiction-solver`](technical-triz/contradiction-solver/) for examples — the contradiction formulation gives both `IF … THEN … BUT …` and `WENN … DANN … ABER …`, and names both *Altshuller Matrix* and *Altschuller Matrix*. Parallel reference files (e.g. `*_EN.md` / `*_DE.md`) are welcome for larger bilingual data sets.
- **One Skill = one folder = one job.** Prefer several focused Skills over one giant Skill; it improves trigger accuracy and reuse.
- **License header.** Add a short license/attribution comment near the top of `SKILL.md` referencing the repo-root `LICENSE`.

A fuller authoring guide and a Skill template will live in [`docs/`](docs/).

---

## 🤝 Collaboration Welcome

This project is open for contributions – while keeping the main branch curated to ensure quality, transparency, and traceability.

Whether you're an AI developer, TRIZ expert, educator, or innovation practitioner – feel free to fork, improve, and suggest new Skills. Let's build a shared, evolving toolkit for AI-enhanced TRIZ applications.

- 💡 **Before you start:** check the guides in [`docs/`](docs/).
- 🧩 **Adding a Skill:** create a new folder under `business-triz/` or `technical-triz/`, following the structure above. Make sure `SKILL.md` has a clear, well-triggered `description` and that all reference paths are relative.
- 🚩 **Contribution rule:** make commits on a branch other than `main` (e.g. `development`) and submit them via a **pull request** before they are merged into `main`.

---

## ⚖️ License

Released under the **MIT License** — see [`LICENSE`](LICENSE). © 2026 Truinorva.
