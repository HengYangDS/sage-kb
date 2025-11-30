#!/usr/bin/env python3
"""
Related Links Checker

Validates that all cross-references in .knowledge documents point to existing files.

Checks:
- Related section links
- Inline markdown links
- Path format (should use .knowledge/ prefix)

Usage:
    python check_links.py [path]
    python check_links.py  # checks entire .knowledge directory
"""

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass
class LinkIssue:
    """Represents a link issue."""
    file: str
    line: int
    link: str
    issue_type: str  # BROKEN, FORMAT


# Placeholder patterns to ignore (example links in documentation)
PLACEHOLDER_PATTERNS = [
    r'^path\d*$',           # path, path1, path2
    r'^url$',               # url
    r'^#$',                 # empty anchor
    r'^\./docs$',           # ./docs (example)
    r'^\./[A-Z]+\.md$',     # ./AUTH.md, ./API.md, ./MODELS.md (examples)
    r'\*',                  # glob patterns like *.md, */*.md
    r'new_topic',           # example paths
    r'new_file\.md$',       # example file
    r'^\.knowledge/old\.md$',  # example old file
]


def is_placeholder_link(link: str) -> bool:
    """Check if a link is a placeholder/example that should be ignored."""
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, link):
            return True
    return False


def extract_links(content: str) -> List[Tuple[int, str]]:
    """Extract all markdown links from content with line numbers.
    
    Only extracts actual markdown links [text](path), not file name references
    in backticks like `filename.md` which are just for display purposes.
    """
    links = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Pattern 1: [text](path) - actual markdown links
        for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', line):
            path = match.group(2)
            if not path.startswith('http') and not path.startswith('#'):
                links.append((i, path))
        
        # Pattern 2: `.knowledge/path/file.md` without backticks (absolute references)
        # Only match if NOT inside backticks (to avoid double-matching)
        for match in re.finditer(r'(?<!`)\.knowledge/[^\s`]+\.md(?!`)', line):
            links.append((i, match.group(0)))
    
    return links


def resolve_link(link: str, source_file: Path, knowledge_root: Path) -> Path:
    """Resolve a link to an absolute path."""
    # Remove any anchor
    link = link.split('#')[0]
    
    if link.startswith('.knowledge/'):
        # Absolute path from knowledge root
        return knowledge_root / link.replace('.knowledge/', '')
    elif link.startswith('./') or link.startswith('../'):
        # Relative path from source file
        return (source_file.parent / link).resolve()
    elif link.startswith('/'):
        # Absolute path (shouldn't be used)
        return Path(link)
    else:
        # Relative path from source file
        return (source_file.parent / link).resolve()


def check_file(filepath: Path, knowledge_root: Path) -> List[LinkIssue]:
    """Check all links in a file."""
    issues = []
    
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [LinkIssue(str(filepath), 0, "", f"Could not read: {e}")]
    
    links = extract_links(content)
    
    for line_num, link in links:
        # Skip placeholder/example links
        if is_placeholder_link(link):
            continue
        
        # Resolve the target path first
        target = resolve_link(link, filepath, knowledge_root)
        
        # Check link format (only if target doesn't exist as relative path)
        if not link.startswith('.knowledge/') and not link.startswith('./') and not link.startswith('../'):
            # Check if it's a relative link that should use .knowledge/ prefix
            # But only report if the target doesn't exist (valid relative links are OK)
            if '/' in link and link.endswith('.md') and not target.exists():
                issues.append(LinkIssue(
                    file=str(filepath),
                    line=line_num,
                    link=link,
                    issue_type="FORMAT"
                ))
        
        # Check if target exists (for non-relative links or links with .knowledge/ prefix)
        if not target.exists():
            # Only report as BROKEN if not already reported as FORMAT
            if link.startswith('.knowledge/') or link.startswith('./') or link.startswith('../'):
                issues.append(LinkIssue(
                    file=str(filepath),
                    line=line_num,
                    link=link,
                    issue_type="BROKEN"
                ))
    
    return issues


def main():
    """Main entry point."""
    # Determine path to check
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1])
    else:
        script_dir = Path(__file__).parent
        base_path = script_dir.parent
    
    if not base_path.exists():
        print(f"Error: Path does not exist: {base_path}")
        sys.exit(1)
    
    # Find knowledge root
    knowledge_root = base_path
    while knowledge_root.name != '.knowledge' and knowledge_root.parent != knowledge_root:
        if (knowledge_root / '.knowledge').exists():
            knowledge_root = knowledge_root / '.knowledge'
            break
        knowledge_root = knowledge_root.parent
    
    # Collect all markdown files
    if base_path.is_file():
        md_files = [base_path]
    else:
        md_files = list(base_path.rglob('*.md'))
        md_files = [f for f in md_files if 'scripts' not in str(f)]
    
    # Run checks
    all_issues = []
    for md_file in md_files:
        issues = check_file(md_file, knowledge_root)
        all_issues.extend(issues)
    
    # Separate by type
    broken = [i for i in all_issues if i.issue_type == "BROKEN"]
    format_issues = [i for i in all_issues if i.issue_type == "FORMAT"]
    
    # Report results
    print(f"\n{'='*60}")
    print(f"Related Links Check Results")
    print(f"{'='*60}")
    print(f"Files checked: {len(md_files)}")
    print(f"Broken links: {len(broken)}")
    print(f"Format issues: {len(format_issues)}")
    print(f"{'='*60}\n")
    
    if broken:
        print(f"\nBROKEN LINKS ({len(broken)}):")
        print("-" * 40)
        for issue in broken:
            print(f"  {issue.file}:{issue.line}")
            print(f"    Link: {issue.link}")
    
    if format_issues:
        print(f"\nFORMAT ISSUES ({len(format_issues)}):")
        print("-" * 40)
        for issue in format_issues:
            print(f"  {issue.file}:{issue.line}")
            print(f"    Link: {issue.link}")
            print(f"    Suggestion: Use `.knowledge/` prefix for absolute paths")
    
    if not broken and not format_issues:
        print("[OK] All links are valid!")
    
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
