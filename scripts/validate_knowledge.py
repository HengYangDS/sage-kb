#!/usr/bin/env python3
"""
SAGE Knowledge Base Validation Script

Validates:
- Broken links
- Missing metadata (YAML front matter)
- File length warnings (>300 lines)
- Format consistency
"""

import os
import re
from pathlib import Path

KNOWLEDGE_DIR = Path(__file__).parent.parent / ".knowledge"
MAX_LINES = 300


def get_markdown_files(directory: Path) -> list[Path]:
    """Get all markdown files in directory recursively."""
    return list(directory.rglob("*.md"))


def check_yaml_frontmatter(file_path: Path) -> tuple[bool, str]:
    """Check if file has YAML front matter."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
            if first_line != "---":
                return False, "Missing YAML front matter"
        return True, ""
    except Exception as e:
        return False, f"Error reading file: {e}"


def check_file_length(file_path: Path) -> tuple[bool, int]:
    """Check if file exceeds maximum line count."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = sum(1 for _ in f)
        return lines <= MAX_LINES, lines
    except Exception as e:
        return True, 0


def check_internal_links(file_path: Path, all_files: set[str]) -> list[str]:
    """Check for broken internal links."""
    broken = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Match markdown links: [text](path)
        link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'
        for match in re.finditer(link_pattern, content):
            link = match.group(2)
            # Skip external links, anchors, and special protocols
            if link.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            # Remove anchor from link
            link = link.split('#')[0]
            if not link:
                continue
            # Resolve path
            if link.startswith('.knowledge/') or link.startswith('.context/') or link.startswith('.junie/'):
                # Project-root-relative path (starts with dot directory)
                resolved = (KNOWLEDGE_DIR.parent / link).resolve()
            elif link.startswith('./') or link.startswith('../'):
                # Relative path from current file
                resolved = (file_path.parent / link).resolve()
            elif link.startswith('.'):
                # Other dot-prefixed paths - treat as project root relative
                resolved = (KNOWLEDGE_DIR.parent / link).resolve()
            else:
                # Assume relative to current file for simple filenames
                resolved = (file_path.parent / link).resolve()

            if not resolved.exists():
                broken.append(link)
    except Exception as e:
        pass
    return broken


def validate():
    """Run all validations."""
    print("=" * 60)
    print("SAGE Knowledge Base Validation")
    print("=" * 60)

    if not KNOWLEDGE_DIR.exists():
        print(f"[ERROR] Knowledge directory not found: {KNOWLEDGE_DIR}")
        return 1

    files = get_markdown_files(KNOWLEDGE_DIR)
    all_file_paths = {str(f.resolve()) for f in files}

    print(f"[INFO] Found {len(files)} markdown files")
    print()

    errors = []
    warnings = []

    for file_path in sorted(files):
        rel_path = file_path.relative_to(KNOWLEDGE_DIR)

        # Check YAML front matter
        has_meta, meta_msg = check_yaml_frontmatter(file_path)
        if not has_meta:
            warnings.append(f"[WARN] {rel_path}: {meta_msg}")

        # Check file length
        ok_length, lines = check_file_length(file_path)
        if not ok_length:
            warnings.append(f"[WARN] {rel_path}: {lines} lines (>{MAX_LINES})")

        # Check internal links
        broken_links = check_internal_links(file_path, all_file_paths)
        for link in broken_links:
            errors.append(f"[ERROR] {rel_path}: Broken link -> {link}")

    # Print results
    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  {e}")
        print()

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  {w}")
        print()

    print("=" * 60)
    print(f"Summary: {len(errors)} errors, {len(warnings)} warnings")
    print("=" * 60)

    return len(errors)


if __name__ == "__main__":
    exit(validate())
