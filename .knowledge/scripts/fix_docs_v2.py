#!/usr/bin/env python3
"""
Document Fixer Script v2

Enhanced version that:
1. Removes UTF-8 BOM from file start
2. Handles various footer formats:
   - Version footers: *Something v1.0*
   - Review footers: *Last reviewed: ...*
   - Preserves review info while adding standard footer
3. Ensures file ends with newline

Usage:
    python fix_docs_v2.py [path]
    python fix_docs_v2.py  # fixes entire .knowledge directory
"""

import os
import re
import sys
from pathlib import Path


STANDARD_FOOTER = '*AI Collaboration Knowledge Base*'


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
        
        # Check if standard footer already exists
        if STANDARD_FOOTER in content:
            # File already has standard footer, just ensure trailing newline
            if not content.endswith('\n'):
                content = content.rstrip() + '\n'
                fixes.append("Added trailing newline")
            
            if fixes:
                filepath.write_text(content, encoding='utf-8')
                return True, fixes
            return False, []
        
        # Patterns for various footer formats
        # Pattern 1: Version footer like *Something v1.0* or *Something Template v1.0*
        version_footer_pattern = r'\*[A-Za-z\s]+(v[\d.]+|Template v[\d.]+)\*'
        
        # Pattern 2: Review footer like *Last reviewed: ...*
        review_footer_pattern = r'\*Last reviewed:.*?\*'
        
        # Find all footer-like patterns at end of file
        lines = content.rstrip().split('\n')
        footer_lines = []
        content_lines = lines[:]
        
        # Scan from end to find footer section
        while content_lines:
            last_line = content_lines[-1].strip()
            
            # Check if this is a footer line
            is_version_footer = re.match(version_footer_pattern, last_line)
            is_review_footer = re.match(review_footer_pattern, last_line)
            is_separator = last_line == '---'
            is_empty = last_line == ''
            
            if is_version_footer or is_review_footer:
                footer_lines.insert(0, content_lines.pop())
            elif is_separator and footer_lines:
                footer_lines.insert(0, content_lines.pop())
            elif is_empty and footer_lines:
                footer_lines.insert(0, content_lines.pop())
            else:
                break
        
        # Rebuild content
        if footer_lines:
            # Remove version footers, keep review footers
            new_footer_lines = []
            for line in footer_lines:
                stripped = line.strip()
                if re.match(review_footer_pattern, stripped):
                    new_footer_lines.append(line)
                elif stripped == '---':
                    continue  # Skip separator, we'll add our own
                elif stripped == '':
                    continue  # Skip empty lines
                # Skip version footers (don't add them)
            
            # Build new footer section
            content = '\n'.join(content_lines)
            content = content.rstrip()
            
            # Add separator and review info if present
            if new_footer_lines:
                review_info = '\n'.join(l.strip() for l in new_footer_lines)
                content += f'\n\n---\n\n{review_info}\n\n{STANDARD_FOOTER}\n'
                fixes.append("Preserved review info, replaced version footer with standard footer")
            else:
                content += f'\n\n---\n\n{STANDARD_FOOTER}\n'
                fixes.append("Replaced version footer with standard footer")
        else:
            # No footer found, add one
            content = content.rstrip() + f'\n\n---\n\n{STANDARD_FOOTER}\n'
            fixes.append("Added missing footer")
        
        # Write back if changes were made
        if content != original_content:
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
        # Exclude scripts directory
        md_files = [f for f in md_files if 'scripts' not in str(f)]
    
    # Fix files
    fixed_count = 0
    total_fixes = []
    
    print(f"\n{'='*60}")
    print(f"Document Fixer v2")
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
