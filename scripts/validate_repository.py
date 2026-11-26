#!/usr/bin/env python3
"""Validate SADA's documentation-only repository catalogue and local links.

Run from any directory with: python3 scripts/validate_repository.py
The module catalogue in docs/README.md is authoritative; update it deliberately
when modules are added or removed. This script does not validate external URLs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
EXPECTED_MODULE_COUNT = 49
NON_MODULE_DIRECTORIES = {
    "ai",
    "engineering",
    "implementation-roadmap",
    "security-and-governance",
    "shared-standards",
    "system-architecture",
}
INDEX_ROW = re.compile(
    r"^\|\s*(\d+)\s*\|\s*\[([^\]]+)\]\(\./([a-z0-9-]+)/README\.md\)",
    re.MULTILINE,
)
ROOT_LINK = re.compile(r"\]\(docs/([a-z0-9-]+)/README\.md\)")
INLINE_LINK = re.compile(r"(?<!!)\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors: list[str] = []
    docs_index_path = DOCS / "README.md"
    root_readme_path = ROOT / "README.md"

    for required in (docs_index_path, root_readme_path):
        if not required.is_file():
            errors.append(f"missing required file: {required.relative_to(ROOT)}")

    if errors:
        for error in errors:
            fail(error)
        return 1

    index_text = docs_index_path.read_text(encoding="utf-8")
    root_text = root_readme_path.read_text(encoding="utf-8")
    rows = INDEX_ROW.findall(index_text)
    ids = [int(row[0]) for row in rows]
    slugs = [row[2] for row in rows]
    titles = [row[1] for row in rows]

    if len(rows) != EXPECTED_MODULE_COUNT:
        errors.append(
            f"docs/README.md contains {len(rows)} indexed modules; "
            f"expected {EXPECTED_MODULE_COUNT}"
        )
    if len(ids) != len(set(ids)):
        errors.append("duplicate module numbers exist in docs/README.md")
    if len(slugs) != len(set(slugs)):
        errors.append("duplicate module directory identifiers exist in docs/README.md")
    if len(titles) != len(set(titles)):
        errors.append("duplicate module display names exist in docs/README.md")

    indexed = set(slugs)
    discovered = {
        path.name
        for path in DOCS.iterdir()
        if path.is_dir()
        and path.name not in NON_MODULE_DIRECTORIES
        and (path / "README.md").is_file()
    }
    if indexed != discovered:
        missing_index = sorted(discovered - indexed)
        missing_dirs = sorted(indexed - discovered)
        if missing_index:
            errors.append(f"module directories missing from index: {', '.join(missing_index)}")
        if missing_dirs:
            errors.append(f"indexed module directories missing README: {', '.join(missing_dirs)}")

    if len(ids) == EXPECTED_MODULE_COUNT and sorted(ids) != list(
        range(1, EXPECTED_MODULE_COUNT + 1)
    ):
        errors.append("module identifiers must form the unique catalogue sequence 1..49")

    feature_section = root_text.split("## Feature modules", 1)[-1].split("\n## ", 1)[0]
    root_modules = set(ROOT_LINK.findall(feature_section))
    if root_modules != indexed:
        errors.append("root README feature catalogue does not match docs/README.md")

    implementation_statement = re.search(
        r"(?:documentation[- ]only.{0,160}(?:not implemented|has not been implemented)|"
        r"no sada application.{0,180}\bis implemented\b)",
        root_text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if implementation_statement is None:
        errors.append("root README must clearly state the application is documentation-only")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)
        if not text.strip():
            errors.append(f"empty Markdown file: {relative}")
        if not text.endswith("\n"):
            errors.append(f"missing final newline: {relative}")
        if any(line.rstrip("\r\n").endswith((" ", "\t")) for line in text.splitlines(keepends=True)):
            errors.append(f"trailing whitespace: {relative}")

        for match in INLINE_LINK.finditer(text):
            destination = match.group(1) or match.group(2) or ""
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                errors.append(f"broken local link in {relative}: {destination}")

    if errors:
        for error in errors:
            fail(error)
        return 1

    print(
        f"Repository validation passed: {len(indexed)} indexed feature modules; "
        f"{len(markdown_files)} non-empty Markdown files; local links resolve."
    )
    print("External URL availability is not checked by this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
