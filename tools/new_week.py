#!/usr/bin/env python3
"""Scaffold the folder for a new week.

Usage:
    python tools/new_week.py 4 "The Data Model, Numbers and Text"

Creates part-1-python/week-04-the-data-model-numbers-and-text/ (or part-2-ml-ai/ for weeks 17+)
with a README from the template and the standard subfolders. Refuses to overwrite an existing week.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "templates" / "week" / "README.md"
SUBFOLDERS = ("lessons", "problems", "mini-project")

# Words that add nothing to a folder name.
STOPWORDS = {"the", "a", "an", "and", "of", "in", "to", "for", "with"}


def slugify(title: str) -> str:
    """Turn a lesson title into a short, readable folder slug."""
    words = re.sub(r"[^a-z0-9\s-]", "", title.lower()).split()
    kept = [w for w in words if w not in STOPWORDS] or words
    return "-".join(kept)[:60].strip("-")


def part_for(week: int) -> str:
    return "part-1-python" if week <= 16 else "part-2-ml-ai"


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__.strip())
        return 2

    try:
        week = int(argv[1])
    except ValueError:
        print(f"error: week must be a number, got {argv[1]!r}")
        return 2

    if not 0 <= week <= 58:
        print(f"error: week must be between 0 and 58, got {week}")
        return 2

    title = argv[2].strip()
    if not title:
        print("error: title must not be empty")
        return 2

    part = ROOT / part_for(week)
    # Guard on the week number, not the full name: two different titles for the same week would
    # otherwise both succeed and leave week 4 sitting in two folders.
    existing = sorted(part.glob(f"week-{week:02d}-*"))
    if existing:
        print(f"error: week {week} already exists as {existing[0].relative_to(ROOT)}")
        print("       nothing written. Rename or remove it first if you meant to redo it.")
        return 1

    folder = part / f"week-{week:02d}-{slugify(title)}"

    # A week that starts on a Monday reads better in the README than today's date.
    today = dt.date.today()
    monday = today - dt.timedelta(days=today.weekday())
    dates = f"{monday:%d %b %Y} – {monday + dt.timedelta(days=6):%d %b %Y}"

    readme = (
        TEMPLATE.read_text(encoding="utf-8")
        .replace("{{N}}", str(week))
        .replace("{{TITLE}}", title)
        .replace("{{DATES}}", dates)
    )

    folder.mkdir(parents=True)
    (folder / "README.md").write_text(readme, encoding="utf-8")
    for sub in SUBFOLDERS:
        d = folder / sub
        d.mkdir()
        # git does not track empty directories.
        (d / ".gitkeep").touch()

    rel = folder.relative_to(ROOT)
    print(f"created {rel}")
    print(f"next:   fill in {rel / 'README.md'} as you go, not at the end of the week")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
