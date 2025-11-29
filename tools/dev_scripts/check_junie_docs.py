#!/usr/bin/env python3
"""
Junie Configuration Documentation Consistency Checker

Verifies that:
1. All .md files in .junie/configuration/ are listed in README.md
2. All files listed in README.md exist in the directory
3. Directory structure in .junie/README.md matches actual structure

Usage:
    python tools/dev_scripts/check_junie_docs.py
"""

import re
import sys
from pathlib import Path


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent.parent


def get_config_dir_files(project_root: Path) -> set[str]:
    """Get all .md files in .junie/configuration/ directory."""
    config_dir = project_root / ".junie" / "configuration"
    if not config_dir.exists():
        return set()
    return {f.name for f in config_dir.glob("*.md")}


def get_readme_listed_files(project_root: Path) -> set[str]:
    """Extract file names listed in configuration/README.md."""
    readme_path = project_root / ".junie" / "configuration" / "README.md"
    if not readme_path.exists():
        return set()

    content = readme_path.read_text(encoding="utf-8")
    # Match patterns like [📋 Introduction](01-introduction.md)
    pattern = r"\[.*?\]\((\d{2}-[\w-]+\.md)\)"
    matches = re.findall(pattern, content)
    # Also add README.md itself as it's always expected
    return set(matches) | {"README.md"}


def get_junie_readme_structure(project_root: Path) -> set[str]:
    """Extract configuration files listed in .junie/README.md directory structure."""
    readme_path = project_root / ".junie" / "README.md"
    if not readme_path.exists():
        return set()

    content = readme_path.read_text(encoding="utf-8")
    # Match patterns like │   ├── 01-introduction.md or │   └── 10-glossary.md
    pattern = r"[├└]── (\d{2}-[\w-]+\.md)"
    matches = re.findall(pattern, content)
    return set(matches) | {"README.md"}


def check_consistency() -> tuple[bool, list[str]]:
    """Check documentation consistency and return (success, messages)."""
    project_root = get_project_root()
    messages = []
    success = True

    # Get file sets
    actual_files = get_config_dir_files(project_root)
    readme_files = get_readme_listed_files(project_root)
    junie_readme_files = get_junie_readme_structure(project_root)

    # Check 1: Files in directory but not in configuration/README.md
    missing_in_readme = actual_files - readme_files
    if missing_in_readme:
        success = False
        messages.append(
            f"❌ Files in directory but not in configuration/README.md: {sorted(missing_in_readme)}"
        )

    # Check 2: Files in configuration/README.md but not in directory
    missing_in_dir = readme_files - actual_files
    if missing_in_dir:
        success = False
        messages.append(
            f"❌ Files in configuration/README.md but not in directory: {sorted(missing_in_dir)}"
        )

    # Check 3: Files in directory but not in .junie/README.md structure
    missing_in_junie_readme = actual_files - junie_readme_files
    if missing_in_junie_readme:
        success = False
        messages.append(
            f"❌ Files in directory but not in .junie/README.md: {sorted(missing_in_junie_readme)}"
        )

    # Check 4: Files in .junie/README.md but not in directory
    extra_in_junie_readme = junie_readme_files - actual_files
    if extra_in_junie_readme:
        success = False
        messages.append(
            f"❌ Files in .junie/README.md but not in directory: {sorted(extra_in_junie_readme)}"
        )

    if success:
        messages.append(f"✅ All {len(actual_files)} configuration docs are consistent")
        messages.append("   - configuration/README.md ✓")
        messages.append("   - .junie/README.md ✓")

    return success, messages


def main() -> int:
    """Main entry point."""
    print("Checking Junie configuration documentation consistency...\n")

    success, messages = check_consistency()

    for msg in messages:
        print(msg)

    print()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
