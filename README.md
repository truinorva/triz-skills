# triz-skills

**Universal TRIZ Skills for Claude – open, structured, and future-proof**

This repository contains a growing, curated library of **TRIZ** (Theory of Inventive Problem Solving) **Skills for Anthropic's Claude** – covering both **technical** and **business** TRIZ, from Contradiction Analysis and Function Analysis to Trimming, the 76 Standard Solutions, Ideality, and Resource Analysis.

Every Skill is kept **unzipped, one folder per Skill**, so it can be read, edited, and extended with any standard text editor (e.g. VS Code, Notepad++, BBEdit) and collaborated on with normal Git workflows.

> Maintained by **Truinorva**. Companion repository to [`triz-prompt-engineering`](https://github.com/jenson500/triz-prompt-engineering).

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
- 📦 **ZIP = release** – develop unzipped in Git, ship as ZIPs built on demand and attached to a GitHub Release; no archives are stored in the repo (see [Releasing](#-releasing-packaging-the-skills))
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
├── scripts/
│   └── build_skills.py           # packages every Skill folder into a release ZIP
├── .github/workflows/
│   └── release.yml               # validates on every push/PR, publishes ZIPs on a tag
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

dist/                             # build output — git-ignored, never committed
```

This layout mirrors `triz-prompt-engineering`: the same separation of *business* vs. *technical* TRIZ, with each tool isolated in its own self-contained folder, and a shared `docs/` folder for guides.

---

## 📚 Skill Index

### Business TRIZ (`business-triz/`)

| Skill | What it does |
|-------|--------------|
| [`business-function-analysis`](business-triz/business-function-analysis/) | Non-engineer Function Analysis using simplified TRIZ for everyday domains (education, healthcare, retail, HR, hospitality). |
| [`perception-mapping`](business-triz/perception-mapping/) | Surfaces stakeholder beliefs, builds Leads-To networks, and exposes hidden contradictions in teams and organizations. |
| [`solutions-at-system-levels`](business-triz/solutions-at-system-levels/) | Generates business solution ideas by exploring super-system and sub-system resources across the system hierarchy. |

### Technical TRIZ (`technical-triz/`)

| Skill | What it does |
|-------|--------------|
| [`76-standard-solutions`](technical-triz/76-standard-solutions/) | Substance-Field (Su-Field) modelling and the 76 Standard Solutions across 5 classes. |
| [`cause-effect-chain-analysis`](technical-triz/cause-effect-chain-analysis/) | Cause & Effect Chain Analysis (CECA) / RCA to trace defects to root causes and contradictions. |
| [`contradiction-solver`](technical-triz/contradiction-solver/) | Resolves engineering contradictions via the Altshuller Matrix and Matrix 2003, and applies the 40 Inventive Principles. Hands physical contradictions over to [`physical-contradictions`](technical-triz/physical-contradictions/). |
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
| [`physical-contradictions`](technical-triz/physical-contradictions/) | Resolves physical contradictions via two documented strategy sets — the Litvin and the Zlotin/Zusman variant — each linked to the recommended Inventive Principles. |
| [`problem-operator`](technical-triz/problem-operator/) | Problem-Oriented Nine Screen Approach — solves a problem across a prevention / mitigation / Plan B timeline at all three system levels. |
| [`resource-analysis`](technical-triz/resource-analysis/) | Discovers and exploits the six TRIZ resource types (MATChEMIB). |
| [`root-cause-analysis`](technical-triz/root-cause-analysis/) | Systematic RCA for engineering failures based on scientific principles and physical parameters. |
| [`root-conflict-analysis`](technical-triz/root-conflict-analysis/) | Root Conflict Analysis (RCA+) — decomposes problems into underlying contradictions. |
| [`smart-little-people`](technical-triz/smart-little-people/) | Smart Little People (SLP) modelling to overcome psychological inertia. |
| [`sustainability-assessment`](technical-triz/sustainability-assessment/) | Rapid, expert-estimation sustainability assessment of processes and product-use phases via TRIZ Function Analysis, Circular Economy principles and the UN SDGs — ranks harm hotspots without LCA software. |
| [`system-description`](technical-triz/system-description/) | System Description (Mini-ISQ) — a structured starting point before other TRIZ tools. |
| [`system-operator`](technical-triz/system-operator/) | System Operator / Multi-Screen Diagram (MSD / 9 Boxes / 9 Screens / 9 Windows) — evolution of technical *and* business systems, with automatic, semi-automatic and interactive modes. |
| [`trimming`](technical-triz/trimming/) | Classical Trimming (rules A, B, C) to simplify systems and cut cost. |

---

## ▶️ Using a Skill with Claude

1. **Download the Skill's ZIP** from the [latest release](../../releases/latest) — one archive per Skill, ready to install.
2. **Install it** into your Claude environment (e.g. Claude, Cowork, Claude Code) as a Skill.
3. Describe your problem; Claude activates the matching Skill based on its `description`.

Install one Skill per ZIP — Claude installs a Skill from an archive rooted in that Skill's own folder, so there is deliberately no combined "all Skills" archive to import.

During development you can also point Claude directly at an unzipped Skill folder in this repo.

---

## 📦 Releasing (packaging the Skills)

**ZIPs are build artefacts, not repository content.** They are never committed — `dist/` and `*.zip` are git-ignored. Every archive is rebuilt from the Skill folders and published as a GitHub Release asset, so each Skill exists exactly once in Git: as its editable folder.

### Archive layout

Claude installs a Skill from an archive whose **root entry is the Skill folder itself**:

```plaintext
contradiction-solver.zip
└── contradiction-solver/          # folder name == frontmatter `name`
    ├── SKILL.md
    └── references/...
```

**One archive holds exactly one Skill.** That single top-level folder *is* the format, so an archive bundling several Skills side by side cannot be imported into Claude at all. An all-in-one `triz-skills-all.zip` was briefly offered with `v1.0.0` and withdrawn for exactly this reason — the build no longer produces one, and no release carries one. Please do not reintroduce it. Installing the full library means installing the individual ZIPs.

### Cutting a release

Tag the commit and push the tag — the [`Package Skills`](.github/workflows/release.yml) workflow builds all archives and attaches them to the release:

```bash
git tag -a v1.0.0 -m "Release v1.0.0" && git push origin v1.0.0
```

The release then carries one ZIP per Skill plus `SHA256SUMS.txt` — and deliberately no combined "all Skills" archive, since Claude cannot import one (see [Archive layout](#archive-layout)).

### Building locally

```bash
python scripts/build_skills.py
```

This writes the same archives into `dist/`. Useful flags:

| Flag | Effect |
|------|--------|
| `--check` | Validate every Skill and exit without writing files |
| `--out DIR` | Write somewhere other than `dist/` |

The build packages **only Git-tracked files**, so untracked scratch files and OS junk (`.DS_Store`, `Thumbs.db`) can never leak into a release.

Packaged content is always byte-identical to the committed bytes, on every platform: entries are sorted, carry a fixed timestamp, and text files are normalized to LF, so a Windows checkout (which Git hands you with CRLF) produces the same file contents as a Linux one. The compressed archive itself can still differ in size between machines, because that depends on the `zlib` build behind Python — rebuilding in the same environment is byte-identical.

### What the build enforces

The same validation runs locally and in CI (on every push and pull request), so a Skill that cannot be packaged fails before it reaches a release:

- `SKILL.md` exists and starts with YAML frontmatter carrying `name` and `description`
- `name` is lowercase-hyphenated and **matches the folder name**
- no two Skills share a `name`
- every Skill has committed files
- each finished archive really contains `<name>/SKILL.md` at exactly one top-level folder

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
