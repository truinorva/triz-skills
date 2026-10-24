#!/usr/bin/env python3
"""Validate the plugin marketplace and package every Skill as a ZIP archive.

The repository is a plugin marketplace: `.claude-plugin/marketplace.json` lists
the plugins, each plugin folder carries `.claude-plugin/plugin.json`, and its
Skills sit unzipped under `skills/<name>/`. Claude Code and ChatGPT both install
the plugins straight from the repository in that layout, so this script checks
that the marketplace, the plugin manifests and the Skills agree with each other.

A single Skill can also be uploaded on its own (Claude.ai, a ChatGPT Skill
upload). That takes a ZIP whose root entry is the Skill folder itself:

    contradiction-solver.zip
    └── contradiction-solver/
        ├── SKILL.md
        └── references/...

This script builds exactly that, into an output directory that is never committed.

Only files tracked by Git are packaged, so untracked scratch files, editor
backups and OS junk (.DS_Store, Thumbs.db) can never leak into a release.
Packaged content is reproducible across platforms: entries are sorted, carry a
fixed timestamp, and text files are normalized to LF, so a Windows checkout
produces the same file contents as a Linux one. (The compressed archive itself
may still differ in size between machines, since that depends on the zlib build
behind Python.)

One archive per Skill is the only thing worth building. An all-in-one archive
holding every Skill folder side by side was tried and dropped: Claude installs
a Skill from an archive rooted in that one Skill's folder, so a combined ZIP
cannot be imported at all. Please do not add one back.

Usage:
    python scripts/build_skills.py                  # build into dist/
    python scripts/build_skills.py --out /tmp/out   # build elsewhere
    python scripts/build_skills.py --check          # validate only, write nothing
    python scripts/build_skills.py --expect-version 1.1.0   # plugins must carry it
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# The marketplace file lists the plugins. Its location is fixed: Claude Code and
# ChatGPT both look for it here when a repository is added as a marketplace.
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"

# Limits of the Agent Skills format, which Claude and ChatGPT both read. Staying
# inside them keeps every Skill installable on both platforms.
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024

# Fixed timestamp for every archive entry (the ZIP format's own epoch), so that
# rebuilding unchanged content produces an unchanged file.
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


class SkillError(Exception):
    """A Skill folder or plugin manifest that cannot be released as-is."""


def git_tracked_files(path: Path) -> list[str]:
    """Return the repo-relative paths Git tracks under `path`, sorted."""
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", str(path.relative_to(REPO_ROOT).as_posix())],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return sorted(entry for entry in result.stdout.split("\0") if entry)


def load_json(path: Path) -> dict:
    """Read a JSON manifest, or raise SkillError saying what is wrong with it."""
    shown = path.relative_to(REPO_ROOT).as_posix()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SkillError(f"{shown}: file is missing") from None
    except json.JSONDecodeError as exc:
        raise SkillError(f"{shown}: invalid JSON ({exc})") from None
    if not isinstance(data, dict):
        raise SkillError(f"{shown}: must hold a JSON object")
    return data


def validate_plugins(expect_version: str | None) -> dict[str, Path]:
    """Check the marketplace and every plugin manifest; return name -> plugin folder.

    The marketplace entry, the plugin folder and the `name` in plugin.json must
    agree: users install a plugin by its entry name, Claude Code namespaces the
    Skills by the manifest name, and a mismatch would show one plugin under two
    names. All plugins carry the same version, because a release tags the whole
    repository at once, and Claude Code keeps users on a plugin's version until
    it changes.
    """
    marketplace_shown = MARKETPLACE.relative_to(REPO_ROOT).as_posix()
    try:
        marketplace = load_json(MARKETPLACE)
    except SkillError as exc:
        raise SkillError(f"  - {exc}") from None

    entries = marketplace.get("plugins")
    if not isinstance(entries, list) or not entries:
        raise SkillError(f"  - {marketplace_shown}: 'plugins' must list at least one plugin")

    plugins: dict[str, Path] = {}
    versions: dict[str, str] = {}
    problems: list[str] = []

    for entry in entries:
        name = entry.get("name") if isinstance(entry, dict) else None
        source = entry.get("source") if isinstance(entry, dict) else None
        # Only plugins inside this repository: their Skills are validated and
        # packaged from this checkout, which a plugin fetched from elsewhere is not.
        if (
            not isinstance(name, str)
            or not isinstance(source, str)
            or not source.startswith("./")
            or ".." in source
        ):
            problems.append(
                f"{marketplace_shown}: entry {entry!r} needs a 'name' and a "
                "'./'-relative 'source' inside this repository"
            )
            continue

        plugin_dir = REPO_ROOT / source[2:].rstrip("/")
        if plugin_dir.name != name:
            problems.append(
                f"{marketplace_shown}: plugin '{name}' points at '{source}' — "
                "the plugin folder must carry the plugin's name"
            )
            continue

        if name in plugins:
            problems.append(f"{marketplace_shown}: plugin '{name}' is listed twice")
            continue

        try:
            manifest = load_json(plugin_dir / ".claude-plugin" / "plugin.json")
        except SkillError as exc:
            problems.append(str(exc))
            continue

        manifest_shown = f"{name}/.claude-plugin/plugin.json"
        if manifest.get("name") != name:
            problems.append(
                f"{manifest_shown}: name '{manifest.get('name')}' does not match the "
                f"marketplace entry '{name}'"
            )
            continue
        if not manifest.get("description"):
            problems.append(f"{manifest_shown}: has no 'description'")
            continue
        version = manifest.get("version")
        if not isinstance(version, str) or not version:
            problems.append(f"{manifest_shown}: has no 'version'")
            continue

        plugins[name] = plugin_dir
        versions[name] = version

    if len(set(versions.values())) > 1:
        listed = ", ".join(f"{name} {version}" for name, version in versions.items())
        problems.append(
            f"plugins carry different versions ({listed}) — a release tags all of "
            "them at once, so give them the same version"
        )

    if expect_version is not None:
        for name, version in versions.items():
            if version != expect_version:
                problems.append(
                    f"{name}/.claude-plugin/plugin.json: version '{version}' is not "
                    f"the release version '{expect_version}' — bump it before tagging"
                )

    if problems:
        raise SkillError("\n".join(f"  - {p}" for p in problems))

    return plugins


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    """Return the value of a top-level frontmatter key as one string.

    Covers the forms the Skills use: a quoted or plain scalar on the key's own
    line, and a folded (`>`) or literal (`|`) block on the indented lines below
    it. This is no YAML parser, only enough to measure what Claude and ChatGPT
    read.
    """
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}:\s*(.*?)\s*$", line)
        if not match:
            continue

        value = match.group(1)
        if value[:1] in (">", "|"):
            block = []
            for following in lines[index + 1:]:
                if following.strip() and not following[:1].isspace():
                    break
                block.append(following.strip())
            separator = " " if value[0] == ">" else "\n"
            return separator.join(part for part in block if part)

        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        return value

    return None


def read_frontmatter_name(skill_md: Path) -> str:
    """Extract the `name` field from the YAML frontmatter of a SKILL.md."""
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise SkillError(f"{skill_md}: no YAML frontmatter (file must start with '---')")

    end = text.find("\n---", 3)
    if end == -1:
        raise SkillError(f"{skill_md}: unterminated YAML frontmatter")

    frontmatter = text[3:end]
    match = re.search(r"^name:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not match:
        raise SkillError(f"{skill_md}: frontmatter has no 'name' field")

    name = match.group(1).strip().strip("\"'")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        raise SkillError(
            f"{skill_md}: name '{name}' must be lowercase and hyphenated"
        )
    if len(name) > MAX_NAME_LENGTH:
        raise SkillError(
            f"{skill_md}: name '{name}' is longer than {MAX_NAME_LENGTH} characters"
        )

    description = frontmatter_value(frontmatter, "description")
    if not description:
        raise SkillError(f"{skill_md}: frontmatter has no 'description' field")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        raise SkillError(
            f"{skill_md}: description has {len(description)} characters, the "
            f"Agent Skills format allows at most {MAX_DESCRIPTION_LENGTH}"
        )

    return name


def discover_skills(plugins: dict[str, Path]) -> list[Path]:
    """Return every Skill folder of every plugin, sorted by plugin and name.

    A plugin loads its Skills from `skills/<name>/` and nowhere else. A Skill
    folder placed directly in the plugin folder, where the layout before the
    plugins kept it, would be skipped by Claude and ChatGPT without a word, so
    it is reported instead.
    """
    skills = []
    misplaced = []
    for plugin_dir in plugins.values():
        skills_dir = plugin_dir / "skills"
        for candidate in sorted(plugin_dir.iterdir()):
            if candidate != skills_dir and (candidate / "SKILL.md").is_file():
                misplaced.append(
                    f"  - {candidate.relative_to(REPO_ROOT).as_posix()}: Skill "
                    f"folder outside 'skills/' — move it to "
                    f"{skills_dir.relative_to(REPO_ROOT).as_posix()}/{candidate.name}/"
                )
        if not skills_dir.is_dir():
            continue
        for candidate in sorted(skills_dir.iterdir()):
            if (candidate / "SKILL.md").is_file():
                skills.append(candidate)
            elif candidate.is_dir():
                misplaced.append(
                    f"  - {candidate.relative_to(REPO_ROOT).as_posix()}: folder in "
                    "'skills/' without a SKILL.md"
                )

    if misplaced:
        raise SkillError("\n".join(misplaced))
    return skills


def validate(skills: list[Path]) -> dict[str, Path]:
    """Check every Skill and return a name -> folder map, or raise SkillError."""
    if not skills:
        raise SkillError("no Skill folders found in the plugins' skills/ directories")

    by_name: dict[str, Path] = {}
    problems: list[str] = []

    for skill_dir in skills:
        folder = skill_dir.name
        try:
            name = read_frontmatter_name(skill_dir / "SKILL.md")
        except SkillError as exc:
            problems.append(str(exc))
            continue

        # The folder name is the Skill's identity inside the archive, so a
        # mismatch would ship a Skill under the wrong name.
        if name != folder:
            problems.append(
                f"{skill_dir.relative_to(REPO_ROOT).as_posix()}: frontmatter name "
                f"'{name}' does not match the folder name '{folder}'"
            )
            continue

        if name in by_name:
            problems.append(
                f"duplicate Skill name '{name}': "
                f"{by_name[name].relative_to(REPO_ROOT).as_posix()} and "
                f"{skill_dir.relative_to(REPO_ROOT).as_posix()}"
            )
            continue

        tracked = git_tracked_files(skill_dir)
        if not tracked:
            problems.append(
                f"{skill_dir.relative_to(REPO_ROOT).as_posix()}: no Git-tracked "
                "files — commit the Skill before packaging it"
            )
            continue

        by_name[name] = skill_dir

    if problems:
        raise SkillError("\n".join(f"  - {p}" for p in problems))

    return by_name


def normalize(data: bytes) -> bytes:
    """Return text content with LF endings; binary content untouched.

    Git stores text with LF and hands Windows checkouts CRLF, so packaging the
    working tree verbatim would make a Windows build differ from a Linux build
    of the very same commit. Normalizing puts both back on the committed bytes.
    A NUL byte in the first block is the usual, cheap binary test — it keeps
    PNGs, PDFs and XLSX files from being rewritten.
    """
    if b"\0" in data[:8000]:
        return data
    return data.replace(b"\r\n", b"\n")


def add_to_zip(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    """Write one file into the archive with a fixed timestamp."""
    info = zipfile.ZipInfo(arcname, date_time=FIXED_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, normalize(source.read_bytes()))


def build_skill_zip(name: str, skill_dir: Path, out_dir: Path) -> Path:
    """Build <out_dir>/<name>.zip containing <name>/... and return its path."""
    zip_path = out_dir / f"{name}.zip"
    prefix = skill_dir.relative_to(REPO_ROOT).as_posix() + "/"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for tracked in git_tracked_files(skill_dir):
            # technical-triz/skills/trimming/SKILL.md  ->  trimming/SKILL.md
            arcname = f"{name}/{tracked[len(prefix):]}"
            add_to_zip(archive, REPO_ROOT / tracked, arcname)

    verify_zip(zip_path, name)
    return zip_path


def verify_zip(zip_path: Path, name: str) -> None:
    """Assert the archive really is installable: <name>/SKILL.md at its root."""
    with zipfile.ZipFile(zip_path) as archive:
        broken = archive.testzip()
        if broken is not None:
            raise SkillError(f"{zip_path.name}: corrupt entry '{broken}'")

        names = archive.namelist()
        if f"{name}/SKILL.md" not in names:
            raise SkillError(
                f"{zip_path.name}: expected '{name}/SKILL.md' at the archive root, "
                f"found: {names[:5]}"
            )

        roots = {entry.split("/", 1)[0] for entry in names}
        if roots != {name}:
            raise SkillError(
                f"{zip_path.name}: archive must contain exactly one top-level "
                f"folder '{name}', found {sorted(roots)}"
            )


def clear_output_dir(out_dir: Path) -> None:
    """Empty the output directory, refusing anything that is not a build output.

    The build wipes its output directory before writing. A mistyped `--out` must
    therefore never be able to delete real work, so only a directory that is
    empty or holds nothing but previously built archives may be removed.
    """
    if not out_dir.exists():
        out_dir.mkdir(parents=True)
        return

    if not out_dir.is_dir():
        raise SkillError(f"output path '{out_dir}' exists and is not a directory")

    if out_dir.resolve() == REPO_ROOT or (out_dir / ".git").exists():
        raise SkillError(
            f"refusing to use '{out_dir}' as output directory: it is a repository root"
        )

    strays = [
        entry.name
        for entry in out_dir.iterdir()
        if not (entry.is_file() and (entry.suffix == ".zip" or entry.name == "SHA256SUMS.txt"))
    ]
    if strays:
        raise SkillError(
            f"refusing to wipe '{out_dir}': it holds files this script did not "
            f"build ({', '.join(sorted(strays)[:5])}). Use an empty directory."
        )

    shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)


def write_checksums(zips: list[Path], out_dir: Path) -> Path:
    """Write SHA256SUMS.txt so downloads can be verified."""
    lines = []
    for zip_path in sorted(zips):
        digest = hashlib.sha256(zip_path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {zip_path.name}")

    checksums = out_dir / "SHA256SUMS.txt"
    checksums.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return checksums


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--out",
        default="dist",
        help="output directory for the archives (default: dist)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate all Skills and exit without writing anything",
    )
    parser.add_argument(
        "--expect-version",
        metavar="VERSION",
        help="fail unless every plugin.json carries this version "
        "(the release tag without its leading 'v')",
    )
    args = parser.parse_args()

    try:
        plugins = validate_plugins(args.expect_version)
        skills = discover_skills(plugins)
        by_name = validate(skills)
    except SkillError as exc:
        print(f"error: validation failed:\n{exc}", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"error: git failed: {exc.stderr.strip()}", file=sys.stderr)
        return 1

    if args.check:
        print(
            f"OK: {len(by_name)} Skills in {len(plugins)} plugins are valid "
            "and ready to package"
        )
        return 0

    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = REPO_ROOT / out_dir

    # Start from a clean directory so a renamed or removed Skill cannot linger
    # as a stale ZIP and end up attached to the release.
    try:
        clear_output_dir(out_dir)
    except SkillError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    built: list[Path] = []
    try:
        for name, skill_dir in sorted(by_name.items()):
            zip_path = build_skill_zip(name, skill_dir, out_dir)
            built.append(zip_path)
            print(f"  {zip_path.name:<44} {zip_path.stat().st_size:>9,} bytes")
    except SkillError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    write_checksums(built, out_dir)
    shown = out_dir.relative_to(REPO_ROOT) if out_dir.is_relative_to(REPO_ROOT) else out_dir
    print(f"\nBuilt {len(built)} archives in {shown}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
