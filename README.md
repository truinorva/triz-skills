# triz-skills

**Universal TRIZ Skills for Claude and ChatGPT – open, structured, and future-proof**

This repository contains a growing, curated library of **TRIZ** (Theory of Inventive Problem Solving) **Skills for Anthropic's Claude and OpenAI's ChatGPT** – covering both **technical** and **business** TRIZ, from Contradiction Analysis and Function Analysis to Trimming, the 76 Standard Solutions, Ideality, and Resource Analysis.

The repository is a **plugin marketplace**: Claude Code, Claude organizations, ChatGPT workspaces and Codex install the Skills straight from here, as two plugins – `technical-triz` and `business-triz`. Every Skill is kept **unzipped, one folder per Skill**, so it can be read, edited, and extended with any standard text editor (e.g. VS Code, Notepad++, BBEdit) and collaborated on with normal Git workflows.

> Maintained by **Truinorva**. Companion repository to [`triz-prompt-engineering`](https://github.com/jenson500/triz-prompt-engineering).

---

## 🌐 Purpose

Our goal is to make TRIZ knowledge usable and sustainable in the age of AI – platform-independent, transparent, and free from proprietary constraints.

This approach allows for:

- Reusable, agent-ready TRIZ methods that Claude and ChatGPT can activate on demand
- Future-proof archiving and documentation in plain text
- Simplified integration into company-specific innovation workflows

---

## 🔧 Key Features

- ✅ **Self-contained Skills** – each Skill is one folder with a `SKILL.md` plus optional `references/` and `assets/`
- 🔌 **One marketplace for Claude and ChatGPT** – both read the same `.claude-plugin/marketplace.json`, so there is no second copy of anything per platform
- 🧭 **Two plugins** – `technical-triz` for engineering, `business-triz` for organizational and people-centric problems
- 📦 **ZIP per Skill for single uploads** – built on demand and attached to a GitHub Release; no archives are stored in the repo (see [Releasing](#-releasing))
- 📖 **English-first, term-bilingual** – content is written in English, with key terms also given in another language (e.g. German) so the AI handles terminology correctly
- ⚖️ **MIT License** – open use, including commercial applications
- 📁 **Git-based collaboration** – with versioning, issue tracking, and a curated main branch
- 🔀 **Pull-request workflow** – changes are made in a feature branch and merged into `main` via PR

---

## 🧩 Skills, plugins, and the marketplace

A *Skill* is a folder that packages instructions, reference data, and optional helper files so an AI assistant can reliably perform a specialized task. At minimum it contains a `SKILL.md` file with YAML frontmatter (a `name` and a `description`). The assistant reads the `description` to decide *when* to activate the Skill, then follows the body of `SKILL.md` to do the work, loading files from `references/` only as needed. Claude and ChatGPT read the same open Agent Skills format, so one `SKILL.md` serves both.

A *plugin* bundles Skills: they sit under its `skills/` folder, next to a manifest at `.claude-plugin/plugin.json`. A *marketplace* lists plugins in `.claude-plugin/marketplace.json`. ChatGPT accepts this Claude-compatible format as is, which is why the repository carries one set of manifests and not two.

---

## 📂 Directory Structure

```plaintext
triz-skills/
│
├── .claude-plugin/
│   └── marketplace.json          # lists the two plugins; read by Claude and ChatGPT
├── docs/                         # placeholder; the authoring & packaging guidance is in this README
├── scripts/
│   └── build_skills.py           # validates the marketplace, packages every Skill into a release ZIP
├── .github/workflows/
│   └── release.yml               # validates on every push/PR, publishes ZIPs on a tag
│
├── business-triz/                # plugin: TRIZ for organizational, service & people-centric problems
│   ├── .claude-plugin/
│   │   └── plugin.json           # plugin name, version, description
│   └── skills/
│       └── <skill-name>/
│           ├── SKILL.md
│           ├── references/       # (optional) knowledge the assistant reads on demand
│           └── assets/           # (optional) files the Skill ships and hands on
│
├── technical-triz/               # plugin: classical engineering-oriented TRIZ
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills/
│       └── <skill-name>/
│           ├── SKILL.md
│           ├── references/
│           └── assets/
│
├── LICENSE
└── README.md

dist/                             # build output — git-ignored, never committed
```

This layout mirrors `triz-prompt-engineering`: the same separation of *business* vs. *technical* TRIZ, with each tool isolated in its own self-contained folder, and a shared `docs/` folder for guides.

---

## 📚 Skill Index

### Business TRIZ (plugin `business-triz`)

| Skill | What it does |
|-------|--------------|
| [`business-function-analysis`](business-triz/skills/business-function-analysis/) | Non-engineer Function Analysis using simplified TRIZ for everyday domains (education, healthcare, retail, HR, hospitality). |
| [`perception-mapping`](business-triz/skills/perception-mapping/) | Surfaces stakeholder beliefs, builds Leads-To networks, and exposes hidden contradictions in teams and organizations. |
| [`solutions-at-system-levels`](business-triz/skills/solutions-at-system-levels/) | Generates business solution ideas by exploring super-system and sub-system resources across the system hierarchy. |

### Technical TRIZ (plugin `technical-triz`)

| Skill | What it does |
|-------|--------------|
| [`76-standard-solutions`](technical-triz/skills/76-standard-solutions/) | Substance-Field (Su-Field) modelling and the 76 Standard Solutions across 5 classes. |
| [`cause-effect-chain-analysis`](technical-triz/skills/cause-effect-chain-analysis/) | Cause & Effect Chain Analysis (CECA) / RCA to trace defects to root causes and contradictions. |
| [`contradiction-solver`](technical-triz/skills/contradiction-solver/) | Resolves engineering contradictions via the Altshuller Matrix and Matrix 2003, and applies the 40 Inventive Principles. Hands physical contradictions over to [`physical-contradictions`](technical-triz/skills/physical-contradictions/). |
| [`feature-transfer`](technical-triz/skills/feature-transfer/) | Enhances a system by adopting beneficial features from alternative/competing systems. |
| [`function-analysis`](technical-triz/skills/function-analysis/) | Maps tools-actions-objects and reveals a technical system's main function. |
| [`function-analysis-advanced`](technical-triz/skills/function-analysis-advanced/) | Adds spatio-temporal (when/where) considerations to Function Analysis. |
| [`function-interaction-analysis`](technical-triz/skills/function-interaction-analysis/) | Maps component interactions based on energy/matter/information flow. |
| [`function-oriented-search`](technical-triz/skills/function-oriented-search/) | FOS / MOS and Scientific Effects search for solutions from other domains and nature. |
| [`ideality`](technical-triz/skills/ideality/) | Moves a system toward its Ideal Final Result (IFR) by balancing useful vs. harmful functions. |
| [`innovation-checklist`](technical-triz/skills/innovation-checklist/) | The Innovation Situation Questionnaire (ISQ / ISQ++) for structured problem framing. |
| [`interactive-trimming`](technical-triz/skills/interactive-trimming/) | Extended interactive Trimming with rules A, B, C, D, E, X. |
| [`mpv-analysis`](technical-triz/skills/mpv-analysis/) | Identifies Parameters of Value (PV) and Main Parameters of Value (MPV). |
| [`patent-analyzer`](technical-triz/skills/patent-analyzer/) | Extracts TRIZ parameters and contradictions from patent texts. |
| [`physical-contradictions`](technical-triz/skills/physical-contradictions/) | Resolves physical contradictions via two documented strategy sets — the Litvin and the Zlotin/Zusman variant — each linked to the recommended Inventive Principles. |
| [`problem-operator`](technical-triz/skills/problem-operator/) | Problem-Oriented Nine Screen Approach — solves a problem across a prevention / mitigation / Plan B timeline at all three system levels. |
| [`resource-analysis`](technical-triz/skills/resource-analysis/) | Discovers and exploits the six TRIZ resource types (MATChEMIB). |
| [`root-cause-analysis`](technical-triz/skills/root-cause-analysis/) | Systematic RCA for engineering failures based on scientific principles and physical parameters. |
| [`root-conflict-analysis`](technical-triz/skills/root-conflict-analysis/) | Root Conflict Analysis (RCA+) — decomposes problems into underlying contradictions. |
| [`smart-little-people`](technical-triz/skills/smart-little-people/) | Smart Little People (SLP) modelling to overcome psychological inertia. |
| [`sustainability-assessment`](technical-triz/skills/sustainability-assessment/) | Rapid, expert-estimation sustainability assessment of processes and product-use phases via TRIZ Function Analysis, Circular Economy principles and the UN SDGs — ranks harm hotspots without LCA software. |
| [`system-description`](technical-triz/skills/system-description/) | System Description (Mini-ISQ) — a structured starting point before other TRIZ tools. |
| [`system-operator`](technical-triz/skills/system-operator/) | System Operator / Multi-Screen Diagram (MSD / 9 Boxes / 9 Screens / 9 Windows) — evolution of technical *and* business systems, with automatic, semi-automatic and interactive modes. |
| [`trimming`](technical-triz/skills/trimming/) | Classical Trimming (rules A, B, C) to simplify systems and cut cost. |

---

## ▶️ Installing the Skills

The marketplace is called `truinorva-triz` and offers two plugins. Install one or both; each brings all Skills of its family. Once installed, describe your problem and the assistant activates the matching Skill based on its `description`.

### Claude Code

```bash
claude plugin marketplace add truinorva/triz-skills
claude plugin install technical-triz@truinorva-triz
claude plugin install business-triz@truinorva-triz
```

Inside a session, `/plugin marketplace add truinorva/triz-skills` and `/plugin install technical-triz@truinorva-triz` do the same. The Skills then appear under the plugin's name, e.g. `technical-triz:contradiction-solver`.

### Claude organizations (Claude.ai, Claude Desktop, Cowork)

An organization Owner syncs the marketplace under **Organization settings → Plugins & skills → Add → Sync from GitHub** and sets who gets which plugin. Claude's organization sync accepts only **private or internal** marketplace repositories, so sync a private copy of this repository, not `truinorva/triz-skills` itself, and pull new releases into that copy.

### Claude.ai without an organization

Download the Skill ZIPs from the [latest release](../../releases/latest) and upload each one as a Skill — one archive per Skill (see [Archive layout](#archive-layout-single-skill-uploads)).

### ChatGPT workspaces (Business, Enterprise, Edu)

A workspace admin imports the marketplace under **Plugins → Add → Import marketplace** in the workspace's admin settings: repository `truinorva/triz-skills`, *Path* left empty. Then set the installation policy (*Available* or *Installed*) per role for `technical-triz` and `business-triz`. The workspace picks up changes from the repository daily; **Sync now** fetches them at once. Members cannot import a marketplace themselves.

### Codex and the ChatGPT desktop app

```bash
codex plugin marketplace add truinorva/triz-skills
```

Then install `technical-triz` and/or `business-triz` from `/plugins` in Codex or from the **Plugins** tab of the desktop app, and start a new chat.

### During development

Point Claude Code at a plugin in your checkout instead of an installed copy:

```bash
claude --plugin-dir ./technical-triz
```

---

## 📦 Releasing

The repository reaches users in two ways, and they update differently:

- **The marketplace is live.** Claude Code and ChatGPT read it from the default branch. ChatGPT workspaces sync it daily, independent of any tag, so whatever is merged into `main` reaches them — keep `main` releasable. Claude Code keeps users on the `version` in each `plugin.json` and offers an update only when that version changes.
- **The ZIPs are per release.** They are build artefacts, not repository content: never committed (`dist/` and `*.zip` are git-ignored), rebuilt from the Skill folders, and published as GitHub Release assets. Each Skill exists exactly once in Git: as its editable folder.

### Cutting a release

1. Set the new `version` in [`technical-triz/.claude-plugin/plugin.json`](technical-triz/.claude-plugin/plugin.json) and [`business-triz/.claude-plugin/plugin.json`](business-triz/.claude-plugin/plugin.json) — both plugins always carry the same version — and merge that into `main`.
2. Tag the commit and push the tag:

   ```bash
   git tag -a v1.1.0 -m "Release v1.1.0" && git push origin v1.1.0
   ```

The [`Package Skills`](.github/workflows/release.yml) workflow refuses a tag whose version differs from the plugins' version, then builds all archives and attaches them to the release: one ZIP per Skill plus `SHA256SUMS.txt` — and deliberately no combined "all Skills" archive (see [Archive layout](#archive-layout-single-skill-uploads)).

### Archive layout (single-Skill uploads)

A single-Skill upload (e.g. to Claude.ai) takes an archive whose **root entry is the Skill folder itself**:

```plaintext
contradiction-solver.zip
└── contradiction-solver/          # folder name == frontmatter `name`
    ├── SKILL.md
    ├── references/...
    └── assets/...                 # if the Skill ships any
```

**One archive holds exactly one Skill.** That single top-level folder *is* the format, so an archive bundling several Skills side by side cannot be imported at all. An all-in-one `triz-skills-all.zip` was briefly offered with `v1.0.0` and withdrawn for exactly this reason — the build no longer produces one, and no release carries one. Please do not reintroduce it. Installing the full library is what the plugins are for.

### Building locally

```bash
python scripts/build_skills.py
```

This validates the marketplace and writes the same archives into `dist/`. Useful flags:

| Flag | Effect |
|------|--------|
| `--check` | Validate the marketplace and every Skill, and exit without writing files |
| `--out DIR` | Write somewhere other than `dist/` |
| `--expect-version VERSION` | Fail unless both plugins carry `VERSION` (CI passes the tag without its `v`) |

The build packages **only Git-tracked files**, so untracked scratch files and OS junk (`.DS_Store`, `Thumbs.db`) can never leak into a release.

Packaged content is always byte-identical to the committed bytes, on every platform: entries are sorted, carry a fixed timestamp, and text files are normalized to LF, so a Windows checkout (which Git hands you with CRLF) produces the same file contents as a Linux one. The compressed archive itself can still differ in size between machines, because that depends on the `zlib` build behind Python — rebuilding in the same environment is byte-identical.

### What the build enforces

The same validation runs locally and in CI (on every push and pull request), so a Skill or plugin that cannot be installed fails before it reaches anyone:

- `.claude-plugin/marketplace.json` lists every plugin with a `./`-relative `source` inside this repository, and the plugin folder carries the plugin's name
- each plugin has `.claude-plugin/plugin.json` with the same `name`, a `description` and a `version`; all plugins carry the same version, and on a release tag it is the tag's version
- every Skill sits in `<plugin>/skills/<name>/` — a Skill folder anywhere else in a plugin, or a folder in `skills/` without a `SKILL.md`, fails the build, because Claude and ChatGPT would skip it without a word
- `SKILL.md` exists and starts with YAML frontmatter carrying `name` and `description`
- `name` is lowercase-hyphenated, at most 64 characters, and **matches the folder name**
- `description` is at most 1024 characters, the limit of the Agent Skills format
- no two Skills share a `name`
- every Skill has committed files
- each finished archive really contains `<name>/SKILL.md` at exactly one top-level folder

To check the manifests against Claude Code's own schema as well, run `claude plugin validate .` and `claude plugin validate ./technical-triz`.

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

Body: step-by-step instructions the assistant should follow, what to ask the
user, which reference files to read, and how to present results.
```

Things to observe:

- **`name`** — lowercase, hyphenated, unique, at most 64 characters, and matching the folder name. This is the Skill's identifier.
- **`description` is the trigger.** It is the *only* thing Claude or ChatGPT sees when deciding whether to activate a Skill. Write it in the third person, state what the Skill does, **and list the words/phrases that should activate it** ("Use this skill when the user mentions …"). Be specific to avoid both false triggers and missed triggers. Aim for roughly 1–3 sentences; the hard limit is 1024 characters.
- **Keep the instructions platform-neutral.** The same `SKILL.md` runs in Claude and in ChatGPT, so describe what to do, not which product feature does it — no product names, no platform-specific tool names.
- **Keep `SKILL.md` lean; push detail into `references/`.** The assistant loads `SKILL.md` up front but reads reference files only when needed. Put long tables, matrices, examples, and images (e.g. the 40 Principles, the Contradiction Matrix, the 76 Standard Solutions) in `references/` and tell `SKILL.md` to read them on demand. This keeps activation cheap and the instructions focused.
- **`references/` for knowledge, `assets/` for files that are handed on.** `references/` holds what the assistant reads to do the work — tables, matrices, method descriptions, examples. `assets/` holds what the Skill ships and passes to the user: templates to fill in, source PDFs, binaries. See [`innovation-checklist`](technical-triz/skills/innovation-checklist/), whose ISQ questionnaires and Excel templates live in `assets/`. Both are optional, and a Skill may have either, both, or neither.
- **Reference paths are relative** to the Skill folder (e.g. `references/40_Inventive_Principles_EN.md`, `assets/TRU_ISQ_EN.xlsx`). Never use absolute or machine-specific paths.
- **Bundle data with the Skill.** Anything the Skill needs (CSVs, Markdown tables, PNG diagrams, helper scripts) lives inside the folder so the Skill is self-contained.
- **Write in English first.** English is the primary language for all `SKILL.md` instructions and documentation.
- **Add key terms in another language to anchor terminology.** Where a precise term or phrasing matters, include the equivalent in another language (e.g. German) inline so the AI maps and handles it correctly. See [`contradiction-solver`](technical-triz/skills/contradiction-solver/) for examples — the contradiction formulation gives both `IF … THEN … BUT …` and `WENN … DANN … ABER …`, and names both *Altshuller Matrix* and *Altschuller Matrix*. Parallel reference files (e.g. `*_EN.md` / `*_DE.md`) are welcome for larger bilingual data sets.
- **One Skill = one folder = one job.** Prefer several focused Skills over one giant Skill; it improves trigger accuracy and reuse.
- **License header.** Add a short license/attribution comment near the top of `SKILL.md` referencing the repo-root `LICENSE`.

A fuller authoring guide and a Skill template will live in [`docs/`](docs/).

---

## 🤝 Collaboration Welcome

This project is open for contributions – while keeping the main branch curated to ensure quality, transparency, and traceability.

Whether you're an AI developer, TRIZ expert, educator, or innovation practitioner – feel free to fork, improve, and suggest new Skills. Let's build a shared, evolving toolkit for AI-enhanced TRIZ applications.

- 💡 **Before you start:** read *Authoring a Skill* and *Releasing* in this README. `docs/` is still a placeholder — the fuller guides announced there do not exist yet.
- 🧩 **Adding a Skill:** create a new folder under `business-triz/skills/` or `technical-triz/skills/`, following the structure above. Make sure `SKILL.md` has a clear, well-triggered `description` and that all reference paths are relative. The plugin picks it up without any change to the manifests.
- 🚩 **Contribution rule:** make commits on a branch other than `main` (e.g. `development`) and submit them via a **pull request** before they are merged into `main`. Everything on `main` reaches ChatGPT workspaces within a day.

---

## ⚖️ License

Released under the **MIT License** — see [`LICENSE`](LICENSE). © 2026 Truinorva.
