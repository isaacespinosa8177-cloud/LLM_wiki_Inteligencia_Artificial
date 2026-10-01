#!/usr/bin/env python3
"""Mechanical health check for the wiki.

Usage:
    python3 tools/lint_wiki.py

Reports:
  - broken relative links (target file missing)
  - pages not reachable from wiki/index.md by following links
  - pages missing frontmatter or required keys
Exits with status 1 if anything is wrong.
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
INDEX = WIKI / "index.md"
NO_FRONTMATTER = {INDEX, WIKI / "log.md"}
REQUIRED = ("title", "type", "tags", "sources", "updated")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def links_of(page):
    text = page.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
    for target in LINK.findall(text):
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        path = unquote(target.split("#", 1)[0])
        yield target, (page.parent / path).resolve()


def frontmatter_keys(page):
    text = page.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return None
    return {line.split(":", 1)[0].strip() for line in m.group(1).splitlines() if ":" in line}


def main():
    pages = sorted(WIKI.rglob("*.md"))
    problems = []

    for page in pages:
        for target, resolved in links_of(page):
            if not resolved.exists():
                problems.append(f"broken link  {page.relative_to(ROOT)} -> {target}")

    seen, stack = set(), [INDEX.resolve()]
    while stack:
        page = stack.pop()
        if page in seen or page.suffix != ".md" or WIKI not in page.parents:
            continue
        seen.add(page)
        stack.extend(r for _, r in links_of(page) if r.exists())
    for page in pages:
        if page.resolve() not in seen:
            problems.append(f"orphan       {page.relative_to(ROOT)} (not reachable from index.md)")

    for page in pages:
        if page in NO_FRONTMATTER:
            continue
        keys = frontmatter_keys(page)
        if keys is None:
            problems.append(f"frontmatter  {page.relative_to(ROOT)} has none")
        else:
            missing = [k for k in REQUIRED if k not in keys]
            if missing:
                problems.append(f"frontmatter  {page.relative_to(ROOT)} missing {missing}")

    for p in problems:
        print(p)
    print(f"{len(pages)} pages checked, {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
