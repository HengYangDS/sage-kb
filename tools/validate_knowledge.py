#!/usr/bin/env python3
"""
Knowledge Base Validation Script

Validates .knowledge directory for:
- No frontmatter (Frontmatter Policy compliance)
- MECE boundary compliance (no project-specific references)
- Broken internal links
- Format consistency
- File structure compliance

Usage:
    python tools/validate_knowledge.py [--fix]
"""

import re
import sys
from pathlib import Path
from typing import List

# Configuration
KNOWLEDGE_DIR = Path(__file__).parent.parent / ".knowledge"

# MECE Boundary Configuration
# Patterns that should NOT appear in .knowledge/ (project-specific content)
FORBIDDEN_PATTERNS = [
    (r'\bSAGE\b', "Project name 'SAGE'"),
    (r'sage-kb', "Repository name 'sage-kb'"),
    (r'config/sage\.yaml', "Project-specific config path"),
    (r'Part of SAGE', "Project-branded footer"),
]

# Files allowed to contain project references (for historical docs or integration examples)
MECE_EXCEPTIONS = [
    "VERSION.md",       # Version history may reference project
    "CONTEXT.md",       # Scenario context files contain project-specific examples
    "INTEGRATION.md",   # Integration patterns contain project-specific code examples
]

# Expected generic footer
EXPECTED_FOOTER = "*AI Collaboration Knowledge Base*"


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

    def add_error(self, msg: str):
        self.errors.append(msg)

    def add_warning(self, msg: str):
        self.warnings.append(msg)

    def add_info(self, msg: str):
        self.info.append(msg)

    @property
    def has_errors(self) -> bool:
        return len(self.errors) > 0


def get_all_md_files(directory: Path) -> List[Path]:
    """Get all markdown files in directory recursively."""
    return list(directory.rglob("*.md"))


def check_no_frontmatter(file_path: Path, content: str, result: ValidationResult):
    """
    Check that file does NOT have YAML frontmatter.
    
    Per Frontmatter Policy (PROJECT_DIRECTORY_STRUCTURE.md Section 7.3):
    - Documents start directly with `# Title`, no YAML frontmatter
    - Version tracking via Git, not in-document metadata
    """
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)

    if content.startswith("---"):
        result.add_error(
            f"{rel_path}: Violates Frontmatter Policy - "
            "documents must start with '# Title', not YAML frontmatter"
        )


def check_mece_boundaries(file_path: Path, content: str, result: ValidationResult):
    """
    Check MECE boundary compliance.
    
    Per MECE Boundaries (PROJECT_DIRECTORY_STRUCTURE.md Section 3):
    - .knowledge/ must be universal/generic
    - No project-specific names, paths, or branding
    """
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)

    # Skip exception files
    if file_path.name in MECE_EXCEPTIONS:
        return

    for pattern, description in FORBIDDEN_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            result.add_error(
                f"{rel_path}: Violates MECE Boundary - "
                f"contains {description} ({len(matches)} occurrence(s))"
            )


def check_generic_footer(file_path: Path, content: str, result: ValidationResult):
    """Check that file uses generic footer, not project-branded."""
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)

    # Skip index files (may have different footer structure)
    if file_path.name.upper() == "INDEX.MD":
        return

    if EXPECTED_FOOTER not in content:
        result.add_warning(
            f"{rel_path}: Missing generic footer '{EXPECTED_FOOTER}'"
        )


def check_internal_links(file_path: Path, content: str, result: ValidationResult):
    """Check for broken internal links."""
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)

    # Find markdown links to .md files
    link_pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    links = re.findall(link_pattern, content)

    for link_text, link_path in links:
        # Skip external links
        if link_path.startswith("http"):
            continue

        # Resolve link path
        if link_path.startswith(".knowledge/") or link_path.startswith(".context/"):
            target = KNOWLEDGE_DIR.parent / link_path
        elif link_path.startswith("./"):
            target = file_path.parent / link_path[2:]
        else:
            target = file_path.parent / link_path

        if not target.exists():
            result.add_error(f"{rel_path}: Broken link '{link_path}'")


def check_format(file_path: Path, content: str, result: ValidationResult):
    """Check document format compliance."""
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)
    lines = content.split('\n')

    # Check for H1 title (should be first non-empty line for frontmatter-free docs)
    non_empty_lines = [l for l in lines if l.strip()]
    if non_empty_lines and not non_empty_lines[0].startswith('# '):
        result.add_warning(f"{rel_path}: First line should be H1 title '# ...'")

    # Check for Related section (recommended)
    has_related = '## Related' in content
    if not has_related and file_path.name.upper() != 'INDEX.MD':
        result.add_info(f"{rel_path}: Missing Related section")

    # Check line count
    if len(lines) > 300:
        result.add_warning(f"{rel_path}: File exceeds 300 lines ({len(lines)})")


def validate_knowledge_base() -> ValidationResult:
    """Run all validations on knowledge base."""
    result = ValidationResult()

    if not KNOWLEDGE_DIR.exists():
        result.add_error(f"Knowledge directory not found: {KNOWLEDGE_DIR}")
        return result

    md_files = get_all_md_files(KNOWLEDGE_DIR)
    result.add_info(f"Found {len(md_files)} markdown files")

    for file_path in md_files:
        try:
            content = file_path.read_text(encoding='utf-8')
            check_no_frontmatter(file_path, content, result)
            check_mece_boundaries(file_path, content, result)
            check_generic_footer(file_path, content, result)
            check_internal_links(file_path, content, result)
            check_format(file_path, content, result)
        except Exception as e:
            result.add_error(f"{file_path}: Read error - {e}")

    return result


def main():
    """Main entry point."""
    print("=" * 60)
    print("Knowledge Base Validation")
    print("=" * 60)

    result = validate_knowledge_base()

    # Print results
    if result.info:
        print(f"\n📋 Info ({len(result.info)}):")
        for msg in result.info[:5]:
            print(f"  ℹ️  {msg}")
        if len(result.info) > 5:
            print(f"  ... and {len(result.info) - 5} more")

    if result.warnings:
        print(f"\n⚠️  Warnings ({len(result.warnings)}):")
        for msg in result.warnings[:10]:
            print(f"  ⚠️  {msg}")
        if len(result.warnings) > 10:
            print(f"  ... and {len(result.warnings) - 10} more")

    if result.errors:
        print(f"\n❌ Errors ({len(result.errors)}):")
        for msg in result.errors:
            print(f"  ❌ {msg}")

    # Summary
    print("\n" + "=" * 60)
    print(f"Summary: {len(result.errors)} errors, {len(result.warnings)} warnings")
    print("=" * 60)

    return 1 if result.has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
