#!/usr/bin/env python3
"""
Related Links Fixer Script

Adds standard related links to INDEX.md files in scenarios directory.

Usage:
    python fix_related_links.py [path]
    python fix_related_links.py  # fixes entire .knowledge directory
"""

import re
import sys
from pathlib import Path


# Standard links for scenario INDEX.md files
SCENARIO_INDEX_LINKS = [
    ('Parent Index', '../INDEX.md'),
    ('Frameworks', '../../frameworks/INDEX.md'),
    ('Practices', '../../practices/INDEX.md'),
    ('Guidelines', '../../guidelines/INDEX.md'),
]

# Standard links for practices sub-directory INDEX.md files
PRACTICES_INDEX_LINKS = [
    ('Parent Index', '../INDEX.md'),
    ('Frameworks', '../../frameworks/INDEX.md'),
    ('Guidelines', '../../guidelines/INDEX.md'),
]


def fix_related_section(filepath: Path, links: list[tuple[str, str]]) -> tuple[bool, str]:
    """Fix Related section in a markdown file.
    
    Args:
        filepath: Path to the markdown file
        links: List of (title, path) tuples for related links
    
    Returns:
        tuple of (was_modified, message)
    """
    try:
        content = filepath.read_text(encoding='utf-8')
        original_content = content
        
        # Build new Related section
        related_lines = ['## Related']
        for title, path in links:
            related_lines.append(f'- [{title}]({path})')
        new_related = '\n'.join(related_lines)
        
        # Find and replace Related section
        # Pattern: ## Related followed by lines starting with - until --- or ## or EOF
        pattern = r'## Related\s*\n(?:- .*\n)*'
        
        if re.search(pattern, content):
            content = re.sub(pattern, new_related + '\n', content)
        else:
            # No Related section found, this shouldn't happen for INDEX.md
            return False, "No Related section found"
        
        if content != original_content:
            filepath.write_text(content, encoding='utf-8')
            return True, f"Updated Related section with {len(links)} links"
        
        return False, "No changes needed"
        
    except Exception as e:
        return False, f"Error: {e}"


def main():
    """Main entry point."""
    # Determine path to fix
    if len(sys.argv) > 1:
        base_path = Path(sys.argv[1])
    else:
        # Default to .knowledge directory
        script_dir = Path(__file__).parent
        base_path = script_dir.parent
    
    if not base_path.exists():
        print(f"Error: Path does not exist: {base_path}")
        sys.exit(1)
    
    print(f"\n{'='*60}")
    print(f"Related Links Fixer")
    print(f"{'='*60}")
    print(f"Scanning: {base_path}")
    print(f"{'='*60}\n")
    
    fixed_count = 0
    
    # Fix scenarios INDEX.md files
    scenarios_dir = base_path / 'scenarios'
    if scenarios_dir.exists():
        for scenario_dir in scenarios_dir.iterdir():
            if scenario_dir.is_dir():
                index_file = scenario_dir / 'INDEX.md'
                if index_file.exists():
                    was_modified, message = fix_related_section(index_file, SCENARIO_INDEX_LINKS)
                    rel_path = index_file.relative_to(base_path)
                    if was_modified:
                        fixed_count += 1
                        print(f"Fixed: {rel_path}")
                        print(f"  - {message}")
                    else:
                        print(f"Skipped: {rel_path} ({message})")
    
    # Fix practices/decisions/INDEX.md
    practices_decisions_index = base_path / 'practices' / 'decisions' / 'INDEX.md'
    if practices_decisions_index.exists():
        was_modified, message = fix_related_section(practices_decisions_index, PRACTICES_INDEX_LINKS)
        rel_path = practices_decisions_index.relative_to(base_path)
        if was_modified:
            fixed_count += 1
            print(f"Fixed: {rel_path}")
            print(f"  - {message}")
        else:
            print(f"Skipped: {rel_path} ({message})")
    
    print(f"\n{'='*60}")
    print(f"Summary")
    print(f"{'='*60}")
    print(f"Files fixed: {fixed_count}")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
