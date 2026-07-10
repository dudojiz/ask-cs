#!/usr/bin/env python3
from __future__ import annotations

"""Keep SUMMARY.md and folder README question lists synchronized.

Automation scope:
- includes: non-root folder README question sections and markdown question files
- excludes: root-level markdown files such as README.md, SUMMARY.md and templates
"""

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = REPO_ROOT / "SUMMARY.md"
QUESTION_HEADER = "## 질문"
QUESTION_LIST_HEADER = "## 질문 목록"
READ_ME_NAME = "README.md"
ROOT_EXCLUDED = {"README.md", "SUMMARY.md", "TEMPLATE.md", "REFERENCES.md", "AGENTS.md"}
LINK_PATTERN = re.compile(r"\(([^)]+)\)")
README_LINK_BULLET_PATTERN = re.compile(r"^-\s+\[([^\]]+)\]\(([^)]+)\)\s*$")
README_TEXT_BULLET_PATTERN = re.compile(r"^-\s+(.+?)\s*$")


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


def normalize_link_path(link: str) -> str:
    return str(Path(link)).replace("\\", "/")


def iter_folder_question_files(folder: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(folder.glob("*.md"), key=lambda p: p.name):
        if path.name == READ_ME_NAME:
            continue
        files.append(path)
    return files


def build_missing_entries(summary_lines: list[str]) -> dict[str, list[tuple[str, str]]]:
    existing_links = set()
    folder_line_info: dict[str, tuple[int, int]] = {}
    folder_pattern = re.compile(r"^(\s*)\* \[.+\]\((.+?/README\.md)\)$")

    for index, line in enumerate(summary_lines):
        folder_match = folder_pattern.match(line)
        if folder_match:
            indent = len(folder_match.group(1))
            folder_path = str(Path(folder_match.group(2)).parent).replace("\\", "/")
            folder_line_info[folder_path] = (index, indent)
        for match in LINK_PATTERN.findall(line):
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


def build_question_catalog(folder: Path) -> tuple[dict[str, str], list[tuple[str, str]]]:
    title_to_rel_name: dict[str, str] = {}
    ordered_questions: list[tuple[str, str]] = []

    for file_path in iter_folder_question_files(folder):
        title = extract_title(file_path)
        if not title:
            continue
        rel_name = file_path.name
        ordered_questions.append((title, rel_name))
        title_to_rel_name.setdefault(title, rel_name)

    return title_to_rel_name, ordered_questions


def build_missing_readme_entries(readme_path: Path, lines: list[str]) -> tuple[int, int, list[tuple[str, str]], list[str]]:
    section_idx = -1
    for i, line in enumerate(lines):
        if line.strip() == QUESTION_LIST_HEADER:
            section_idx = i
            break

    if section_idx == -1:
        return -1, -1, [], []

    section_end = len(lines)
    for i in range(section_idx + 1, len(lines)):
        if lines[i].startswith("## "):
            section_end = i
            break

    title_to_rel_name, ordered_questions = build_question_catalog(readme_path.parent)
    existing_links: set[str] = set()
    normalized_section_lines: list[str] = []
    section_changes: list[str] = []

    for line in lines[section_idx + 1 : section_end]:
        link_bullet_match = README_LINK_BULLET_PATTERN.match(line.strip())
        if link_bullet_match:
            title = link_bullet_match.group(1).strip()
            rel_name = normalize_link_path(link_bullet_match.group(2))
            if rel_name in existing_links:
                section_changes.append(f"remove duplicate link: {rel_name}")
                continue
            existing_links.add(rel_name)
            normalized_section_lines.append(f"- [{title}]({rel_name})")
            continue

        text_bullet_match = README_TEXT_BULLET_PATTERN.match(line.strip())
        if text_bullet_match:
            text = text_bullet_match.group(1).strip()
            rel_name = title_to_rel_name.get(text)
            if rel_name and rel_name not in existing_links:
                normalized_section_lines.append(f"- [{text}]({rel_name})")
                existing_links.add(rel_name)
                section_changes.append(f"normalize text bullet to link: {text}")
                continue

        normalized_section_lines.append(line)

    lines[section_idx + 1 : section_end] = normalized_section_lines
    section_end = section_idx + 1 + len(normalized_section_lines)

    missing: list[tuple[str, str]] = []
    for title, rel_name in ordered_questions:
        if rel_name in existing_links:
            continue
        missing.append((title, rel_name))

    return section_idx, section_end, missing, section_changes


def update_readme_question_list(readme_path: Path, content: str) -> tuple[str, list[str]]:
    lines = content.splitlines()
    section_idx, section_end, missing_entries, section_changes = build_missing_readme_entries(readme_path, lines)
    if section_idx == -1:
        unchanged = content if content.endswith("\n") else content + "\n"
        return unchanged, []

    insert_idx = section_end
    while insert_idx > section_idx + 1 and lines[insert_idx - 1].strip() == "":
        insert_idx -= 1

    new_lines = [f"- [{title}]({path})" for title, path in missing_entries]
    lines[insert_idx:insert_idx] = new_lines
    if new_lines:
        section_changes.extend([f"add missing link: {path}" for _, path in missing_entries])
    return "\n".join(lines) + "\n", section_changes


def iter_readme_files() -> list[Path]:
    readmes: list[Path] = []
    for path in REPO_ROOT.rglob(READ_ME_NAME):
        if ".git" in path.parts or ".github" in path.parts:
            continue
        rel = path.relative_to(REPO_ROOT)
        if rel.parent == Path("."):
            continue
        readmes.append(path)
    return sorted(readmes, key=lambda p: str(p.relative_to(REPO_ROOT)))


def main() -> int:
    parser = argparse.ArgumentParser(description="Update SUMMARY.md and README question lists from question markdown files.")
    parser.add_argument("--check", action="store_true", help="Exit with failure if generated files need updates.")
    args = parser.parse_args()

    original = SUMMARY_PATH.read_text(encoding="utf-8")
    updated = update_summary(original)
    updated_readmes: list[tuple[Path, str]] = []
    out_of_date_files: list[str] = []
    readme_change_details: dict[str, list[str]] = {}

    for readme_path in iter_readme_files():
        original_readme = readme_path.read_text(encoding="utf-8")
        updated_readme, changes = update_readme_question_list(readme_path, original_readme)
        if original_readme != updated_readme:
            rel_path = str(readme_path.relative_to(REPO_ROOT)).replace("\\", "/")
            out_of_date_files.append(rel_path)
            updated_readmes.append((readme_path, updated_readme))
            readme_change_details[rel_path] = changes

    if args.check:
        if original != updated or out_of_date_files:
            print("Generated markdown files are out of date. Run: python scripts/update_summary.py")
            if original != updated:
                print("- SUMMARY.md")
            for rel_path in out_of_date_files:
                print(f"- {rel_path}")
                for detail in readme_change_details.get(rel_path, []):
                    print(f"  - {detail}")
            return 1
        print("SUMMARY.md and README question lists are up to date.")
        return 0

    changed = False
    if original != updated:
        SUMMARY_PATH.write_text(updated, encoding="utf-8")
        changed = True

    for readme_path, updated_content in updated_readmes:
        readme_path.write_text(updated_content, encoding="utf-8")
        changed = True

    if changed:
        print("Generated markdown files updated.")
    else:
        print("No changes needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
