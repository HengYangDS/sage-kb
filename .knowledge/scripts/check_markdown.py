#!/usr/bin/env python3
"""
Markdown Documentation Checker

Validates .knowledge documents against documentation standards:
- Code block format (matching backticks)
- Document structure (H1, TOC, Related, Footer)
- Related section (3-5 links)

Usage:
    python check_markdown.py [path]
    python check_markdown.py  # checks entire .knowledge directory
"""

import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Issue:
    """Represents a documentation issue."""
    file: str
    line: int
    severity: str  # ERROR, WARNING, INFO
    message: str


def check_code_blocks(content: str, filepath: str) -> List[Issue]:
    """Check for mismatched code block backticks.
    
    Handles nested code blocks correctly:
    - When inside a code block with N backticks, lines with <N backticks are content
    - Only lines with exactly N backticks close the block
    """
    issues = []
    lines = content.split('\n')
    stack = []  # Stack of (line_num, backtick_count)
    
    for i, line in enumerate(lines, 1):
        # Match code block start/end (3+ backticks at start of line)
        match = re.match(r'^(`{3,})', line)
        if match:
            backticks = len(match.group(1))
            if not stack:
                # Opening a new code block
                stack.append((i, backticks))
            elif backticks == stack[-1][1]:
                # Closing the code block with matching backticks
                stack.pop()
            elif backticks > stack[-1][1]:
                # More backticks than current block - this is a nested block opener
                # But we're inside a code block, so this is just content
                # Only track if it could be a valid nested block
                pass  # Ignore - it's content inside the outer block
            else:
                # Fewer backticks than current block - this is content, not a closer
                # This is valid nested code block syntax (e.g., ``` inside `````)
                pass  # Ignore - it's content inside the outer block
    
    # Check for unclosed code blocks
    for line_num, backticks in stack:
        issues.append(Issue(
            file=filepath,
            line=line_num,
            severity="ERROR",
            message=f"Unclosed code block with {backticks} backticks"
        ))
    
    return issues


def check_document_structure(content: str, filepath: str) -> List[Issue]:
    """Check document structure (H1, TOC, Related, Footer)."""
    issues = []
    lines = content.split('\n')
    
    # Check for H1 title
    has_h1 = any(line.startswith('# ') and not line.startswith('## ') for line in lines)
    if not has_h1:
        issues.append(Issue(
            file=filepath,
            line=1,
            severity="ERROR",
            message="Missing H1 title"
        ))
    
    # Check for Related section
    has_related = any(line.strip() == '## Related' for line in lines)
    if not has_related:
        issues.append(Issue(
            file=filepath,
            line=len(lines),
            severity="WARNING",
            message="Missing '## Related' section"
        ))
    
    # Check for Footer
    has_footer = '*AI Collaboration Knowledge Base*' in content
    if not has_footer:
        issues.append(Issue(
            file=filepath,
            line=len(lines),
            severity="INFO",
            message="Missing footer '*AI Collaboration Knowledge Base*'"
        ))
    
    return issues


def check_related_links(content: str, filepath: str) -> List[Issue]:
    """Check Related section has 2-5 links (optimal: 3-5).
    
    Thresholds:
    - 0-1 links: WARNING (too few for navigation)
    - 2 links: INFO (acceptable but could be improved)
    - 3-5 links: OK (optimal range)
    - 6+ links: INFO (many links, but not a problem)
    """
    issues = []
    
    # Find Related section
    related_match = re.search(r'## Related\s*\n(.*?)(?=\n---|\n## |\Z)', content, re.DOTALL)
    if related_match:
        related_content = related_match.group(1)
        # Count links (lines starting with -)
        links = [line for line in related_content.split('\n') if line.strip().startswith('-')]
        link_count = len(links)
        
        if link_count < 2:
            # 0-1 links is a warning - too few for useful navigation
            issues.append(Issue(
                file=filepath,
                line=content[:related_match.start()].count('\n') + 1,
                severity="WARNING",
                message=f"Related section has {link_count} links (recommended: 3-5)"
            ))
        elif link_count == 2:
            # 2 links is acceptable but could be improved
            issues.append(Issue(
                file=filepath,
                line=content[:related_match.start()].count('\n') + 1,
                severity="INFO",
                message=f"Related section has {link_count} links (optimal: 3-5)"
            ))
        elif link_count > 5:
            issues.append(Issue(
                file=filepath,
                line=content[:related_match.start()].count('\n') + 1,
                severity="INFO",
                message=f"Related section has {link_count} links (recommended: 3-5)"
            ))
    
    return issues


def check_file(filepath: Path) -> List[Issue]:
    """Run all checks on a single file."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [Issue(str(filepath), 0, "ERROR", f"Could not read file: {e}")]
    
    issues = []
    rel_path = str(filepath)
    
    issues.extend(check_code_blocks(content, rel_path))
    issues.extend(check_document_structure(content, rel_path))
    issues.extend(check_related_links(content, rel_path))
    
    return issues


def main():
    """Main entry point."""
    # Determine path to check
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1])
    else:
        # Default to .knowledge directory
        script_dir = Path(__file__).parent
        base_path = script_dir.parent
    
    if not base_path.exists():
        print(f"Error: Path does not exist: {base_path}")
        sys.exit(1)
    
    # Collect all markdown files
    if base_path.is_file():
        md_files = [base_path]
    else:
        md_files = list(base_path.rglob('*.md'))
        # Exclude scripts directory
        md_files = [f for f in md_files if 'scripts' not in str(f)]
    
    # Run checks
    all_issues = []
    for md_file in md_files:
        issues = check_file(md_file)
        all_issues.extend(issues)
    
    # Report results
    errors = [i for i in all_issues if i.severity == "ERROR"]
    warnings = [i for i in all_issues if i.severity == "WARNING"]
    infos = [i for i in all_issues if i.severity == "INFO"]
    
    print(f"\n{'='*60}")
    print(f"Markdown Documentation Check Results")
    print(f"{'='*60}")
    print(f"Files checked: {len(md_files)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Info: {len(infos)}")
    print(f"{'='*60}\n")
    
    # Print issues by severity
    for severity, issue_list in [("ERROR", errors), ("WARNING", warnings), ("INFO", infos)]:
        if issue_list:
            print(f"\n{severity}S ({len(issue_list)}):")
            print("-" * 40)
            for issue in issue_list:
                print(f"  {issue.file}:{issue.line}")
                print(f"    {issue.message}")
    
    # Exit with error code if there are errors
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
