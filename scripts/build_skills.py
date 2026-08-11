#!/usr/bin/env python3
"""Package every Skill folder as a Claude-installable ZIP archive.

The repository keeps Skills unzipped, one folder per Skill, because that is what
makes them editable and reviewable in Git. Claude, however, installs a Skill from
a ZIP whose root entry is the Skill folder itself:

    contradiction-solver.zip
    └── contradiction-solver/
        ├── SKILL.md
        └── references/...

This script builds exactly that, into an output directory that is never committed.

Only files tracked by Git are packaged, so untracked scratch files, editor
backups and OS junk (.DS_Store, Thumbs.db) can never leak into a release.
Archives are reproducible: entries are sorted and carry a fixed timestamp, so
identical content always yields a byte-identical ZIP.

Usage:
    python scripts/build_skills.py                  # build into dist/
    python scripts/build_skills.py --out /tmp/out   # build elsewhere
    python scripts/build_skills.py --bundle         # also build the all-in-one ZIP
    python scripts/build_skills.py --check          # validate only, write nothing
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

# Directories that hold Skill folders. Everything else in the repo is ignored.
SKILL_FAMILIES = ("business-triz", "technical-triz")

# Fixed timestamp for every archive entry (the ZIP format's own epoch), so that
# rebuilding unchanged content produces an unchanged file.
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)

REPO_ROOT = Path(__file__).resolve().parent.parent


class SkillError(Exception):
    """A Skill folder that cannot be packaged as-is."""


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
    if not re.search(r"^description:\s*\S", frontmatter, re.MULTILINE):
        raise SkillError(f"{skill_md}: frontmatter has no 'description' field")

    return name


def discover_skills() -> list[Path]:
    """Return every Skill folder in the repo, sorted by name."""
    skills = []
    for family in SKILL_FAMILIES:
        family_dir = REPO_ROOT / family
        if not family_dir.is_dir():
            continue
        for candidate in sorted(family_dir.iterdir()):
            if (candidate / "SKILL.md").is_file():
                skills.append(candidate)
    return skills


def validate(skills: list[Path]) -> dict[str, Path]:
    """Check every Skill and return a name -> folder map, or raise SkillError."""
    if not skills:
        raise SkillError(
            f"no Skill folders found under {'/, '.join(SKILL_FAMILIES)}/"
        )

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


def add_to_zip(archive: zipfile.ZipFile, source: Path, arcname: str) -> None:
    """Write one file into the archive with a fixed timestamp."""
    info = zipfile.ZipInfo(arcname, date_time=FIXED_TIMESTAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, source.read_bytes())


def build_skill_zip(name: str, skill_dir: Path, out_dir: Path) -> Path:
    """Build <out_dir>/<name>.zip containing <name>/... and return its path."""
    zip_path = out_dir / f"{name}.zip"
    prefix = skill_dir.relative_to(REPO_ROOT).as_posix() + "/"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for tracked in git_tracked_files(skill_dir):
            # technical-triz/trimming/SKILL.md  ->  trimming/SKILL.md
            arcname = f"{name}/{tracked[len(prefix):]}"
            add_to_zip(archive, REPO_ROOT / tracked, arcname)

    verify_zip(zip_path, name)
    return zip_path


def build_bundle_zip(by_name: dict[str, Path], out_dir: Path) -> Path:
    """Build one archive holding every Skill folder side by side."""
    zip_path = out_dir / "triz-skills-all.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, skill_dir in sorted(by_name.items()):
            prefix = skill_dir.relative_to(REPO_ROOT).as_posix() + "/"
            for tracked in git_tracked_files(skill_dir):
                add_to_zip(
                    archive,
                    REPO_ROOT / tracked,
                    f"{name}/{tracked[len(prefix):]}",
                )
        for extra in ("README.md", "LICENSE"):
            add_to_zip(archive, REPO_ROOT / extra, extra)

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
        "--bundle",
        action="store_true",
        help="additionally build triz-skills-all.zip with every Skill",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate all Skills and exit without writing anything",
    )
    args = parser.parse_args()

    try:
        skills = discover_skills()
        by_name = validate(skills)
    except SkillError as exc:
        print(f"error: Skill validation failed:\n{exc}", file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"error: git failed: {exc.stderr.strip()}", file=sys.stderr)
        return 1

    if args.check:
        print(f"OK: {len(by_name)} Skills are valid and ready to package")
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

        if args.bundle:
            bundle = build_bundle_zip(by_name, out_dir)
            built.append(bundle)
            print(f"  {bundle.name:<44} {bundle.stat().st_size:>9,} bytes")
    except SkillError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    write_checksums(built, out_dir)
    print(f"\nBuilt {len(built)} archives in {out_dir.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
