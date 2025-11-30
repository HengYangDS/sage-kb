#!/usr/bin/env python3
"""
MECE Boundary Checker for .knowledge/ Directory

Lightweight script for pre-commit hooks to verify:
1. No frontmatter in .knowledge/ files
2. No project-specific references (SAGE, sage-kb, etc.)
3. Generic footer usage

Usage:
    python tools/check_mece_boundaries.py [files...]
    
    If no files provided, checks all .knowledge/*.md files.
    
Exit codes:
    0 - All checks passed
    1 - Violations found

Per MECE Boundaries (PROJECT_DIRECTORY_STRUCTURE.md Section 3):
- .knowledge/ = Universal/Generic (reusable across ANY project)
- .context/ = Project-Specific (only for THIS project)
- .junie/ = AI Tool Config (follows Junie conventions)
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

# Patterns that should NOT appear in .knowledge/ (project-specific content)
FORBIDDEN_PATTERNS: List[Tuple[str, str]] = [
    (r'\bSAGE\b', "Project name 'SAGE'"),
    (r'sage-kb', "Repository name 'sage-kb'"),
    (r'config/sage\.yaml', "Project-specific config path"),
    (r'Part of SAGE', "Project-branded footer"),
]

# Files allowed to contain project references (for historical docs or integration examples)
EXCEPTIONS = {
    "VERSION.md",           # Version history may reference project
    "CONTEXT.md",           # Scenario context files contain project-specific examples
    "INTEGRATION.md",       # Integration patterns contain project-specific code examples
}


def check_file(file_path: Path) -> List[str]:
    """
    Check a single file for MECE boundary violations.
    
    Returns list of error messages (empty if no violations).
    """
    errors = []
    
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return [f"{file_path}: Read error - {e}"]
    
    # Skip exception files
    if file_path.name in EXCEPTIONS:
        return []
    
    # Check 1: No frontmatter
    if content.startswith("---"):
        errors.append(
            f"{file_path}: Frontmatter Policy violation - "
            "must start with '# Title', not YAML frontmatter"
        )
    
    # Check 2: No project-specific patterns
    for pattern, description in FORBIDDEN_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            errors.append(
                f"{file_path}: MECE Boundary violation - "
                f"contains {description} ({len(matches)} occurrence(s))"
            )
    
    return errors


def main() -> int:
    """Main entry point."""
    # Get files to check
    if len(sys.argv) > 1:
        # Files provided as arguments (from pre-commit)
        files = [Path(f) for f in sys.argv[1:] if f.endswith('.md')]
        # Filter to only .knowledge/ files
        files = [f for f in files if '.knowledge' in str(f)]
    else:
        # Check all .knowledge/*.md files
        knowledge_dir = Path(__file__).parent.parent / ".knowledge"
        if not knowledge_dir.exists():
            print("❌ .knowledge/ directory not found")
            return 1
        files = list(knowledge_dir.rglob("*.md"))
    
    if not files:
        return 0  # No files to check
    
    # Run checks
    all_errors = []
    for file_path in files:
        errors = check_file(file_path)
        all_errors.extend(errors)
    
    # Report results
    if all_errors:
        print("[ERROR] MECE Boundary Violations Found:")
        for error in all_errors:
            print(f"  - {error}")
        print(f"\nTotal: {len(all_errors)} violation(s) in {len(files)} file(s)")
        return 1
    
    print(f"[OK] MECE Boundary Check Passed ({len(files)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
