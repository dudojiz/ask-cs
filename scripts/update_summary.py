#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = REPO_ROOT / "SUMMARY.md"
QUESTION_HEADER = "## 질문"
READ_ME_NAME = "README.md"
ROOT_EXCLUDED = {"README.md", "SUMMARY.md", "TEMPLATE.md", "REFERENCES.md", "AGENTS.md"}


def iter_article_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        if ".git" in path.parts or ".github" in path.parts:
            continue
        rel = path.relative_to(REPO_ROOT)
        if rel.parent == Path(".") and rel.name in ROOT_EXCLUDED:
            continue
        if path.name == READ_ME_NAME:
            continue
        files.append(path)
    return sorted(files, key=lambda p: str(p.relative_to(REPO_ROOT)))


def extract_title(path: Path) -> str | None:
    lines = path.read_text(encoding="utf-8").splitlines()

    for i, line in enumerate(lines):
        if line.strip() == QUESTION_HEADER:
            for j in range(i + 1, len(lines)):
                text = lines[j].strip()
                if not text:
                    continue
                if text.startswith(">"):
                    return text.lstrip(">").strip()
                break

    for line in lines:
        text = line.strip()
        if text.startswith("# "):
            return text[2:].strip()

    return None


def leading_spaces(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def build_missing_entries(summary_lines: list[str]) -> dict[str, list[tuple[str, str]]]:
    existing_links = set()
    folder_line_info: dict[str, tuple[int, int]] = {}
    folder_pattern = re.compile(r"^(\s*)\* \[.+\]\((.+?/README\.md)\)$")
    link_pattern = re.compile(r"\(([^)]+)\)")

    for index, line in enumerate(summary_lines):
        folder_match = folder_pattern.match(line)
        if folder_match:
            indent = len(folder_match.group(1))
            folder_path = str(Path(folder_match.group(2)).parent).replace("\\", "/")
            folder_line_info[folder_path] = (index, indent)
        for match in link_pattern.findall(line):
            existing_links.add(match)

    missing: dict[str, list[tuple[str, str]]] = {}
    for file_path in iter_article_files():
        rel_path = str(file_path.relative_to(REPO_ROOT)).replace("\\", "/")
        if rel_path in existing_links:
            continue
        folder_path = str(Path(rel_path).parent).replace("\\", "/")
        if folder_path not in folder_line_info:
            continue
        title = extract_title(file_path)
        if not title:
            continue
        missing.setdefault(folder_path, []).append((title, rel_path))

    for folder_path in missing:
        missing[folder_path].sort(key=lambda item: item[1])

    return missing


def update_summary(content: str) -> str:
    lines = content.splitlines()
    missing_entries = build_missing_entries(lines)
    if not missing_entries:
        return content if content.endswith("\n") else content + "\n"

    folder_pattern = re.compile(r"^(\s*)\* \[.+\]\((.+?/README\.md)\)$")

    for folder_path in sorted(missing_entries.keys()):
        folder_idx = -1
        folder_indent = 0
        for i, line in enumerate(lines):
            match = folder_pattern.match(line)
            if not match:
                continue
            candidate_folder = str(Path(match.group(2)).parent).replace("\\", "/")
            if candidate_folder == folder_path:
                folder_idx = i
                folder_indent = len(match.group(1))
                break

        if folder_idx == -1:
            continue

        insert_idx = folder_idx + 1
        while insert_idx < len(lines):
            current = lines[insert_idx]
            stripped = current.lstrip(" ")
            if stripped.startswith("* "):
                current_indent = leading_spaces(current)
                if current_indent <= folder_indent:
                    break
            insert_idx += 1

        child_indent = " " * (folder_indent + 2)
        new_lines = [f"{child_indent}* [{title}]({path})" for title, path in missing_entries[folder_path]]
        lines[insert_idx:insert_idx] = new_lines

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Update SUMMARY.md from question markdown files.")
    parser.add_argument("--check", action="store_true", help="Exit with failure if SUMMARY.md needs updates.")
    args = parser.parse_args()

    original = SUMMARY_PATH.read_text(encoding="utf-8")
    updated = update_summary(original)

    if args.check:
        if original != updated:
            print("SUMMARY.md is out of date. Run: python scripts/update_summary.py")
            return 1
        print("SUMMARY.md is up to date.")
        return 0

    if original != updated:
        SUMMARY_PATH.write_text(updated, encoding="utf-8")
        print("SUMMARY.md updated.")
    else:
        print("No changes needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
