#!/usr/bin/env python3
"""
Document Fixer Script

Fixes common documentation issues:
1. Removes UTF-8 BOM from file start
2. Restores standard footer '*AI Collaboration Knowledge Base*'
3. Ensures file ends with newline

Usage:
    python fix_docs.py [path]
    python fix_docs.py  # fixes entire .knowledge directory
"""

import os
import re
import sys
from pathlib import Path


def fix_file(filepath: Path) -> tuple[bool, list[str]]:
    """Fix a single markdown file.
    
    Returns:
        tuple of (was_modified, list_of_fixes)
    """
    fixes = []
    
    try:
        # Read file as bytes first to detect BOM
        raw_content = filepath.read_bytes()
        
        # Check and remove BOM
        if raw_content.startswith(b'\xef\xbb\xbf'):
            raw_content = raw_content[3:]
            fixes.append("Removed UTF-8 BOM")
        
        # Decode to string
        content = raw_content.decode('utf-8')
        original_content = content
        
        # Fix footer - replace version-specific footers with standard one
        # Pattern matches: *Something v1.0* or *Something Template v1.0* etc.
        footer_pattern = r'\*[A-Za-z\s]+(v[\d.]+|Template v[\d.]+)\*\s*$'
        standard_footer = '*AI Collaboration Knowledge Base*'
        
        if re.search(footer_pattern, content):
            content = re.sub(footer_pattern, standard_footer, content)
            fixes.append("Restored standard footer")
        
        # Add footer if missing (check if standard footer exists anywhere)
        if standard_footer not in content:
            # Add separator and footer at the end
            content = content.rstrip() + '\n\n---\n\n' + standard_footer + '\n'
            fixes.append("Added missing footer")
        
        # Ensure file ends with exactly one newline
        content = content.rstrip() + '\n'
        if original_content != content or fixes:
            if not original_content.endswith('\n'):
                fixes.append("Added trailing newline")
        
        # Write back if changes were made
        if fixes:
            filepath.write_text(content, encoding='utf-8')
            return True, fixes
        
        return False, []
        
    except Exception as e:
        return False, [f"Error: {e}"]


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
    
    # Collect all markdown files
    if base_path.is_file():
        md_files = [base_path]
    else:
        md_files = list(base_path.rglob('*.md'))
    
    # Fix files
    fixed_count = 0
    total_fixes = []
    
    print(f"\n{'='*60}")
    print(f"Document Fixer")
    print(f"{'='*60}")
    print(f"Scanning: {base_path}")
    print(f"Files found: {len(md_files)}")
    print(f"{'='*60}\n")
    
    for md_file in md_files:
        was_modified, fixes = fix_file(md_file)
        if was_modified:
            fixed_count += 1
            rel_path = md_file.relative_to(base_path) if base_path.is_dir() else md_file.name
            print(f"Fixed: {rel_path}")
            for fix in fixes:
                print(f"  - {fix}")
            total_fixes.extend(fixes)
    
    print(f"\n{'='*60}")
    print(f"Summary")
    print(f"{'='*60}")
    print(f"Files scanned: {len(md_files)}")
    print(f"Files fixed: {fixed_count}")
    print(f"Total fixes applied: {len(total_fixes)}")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
