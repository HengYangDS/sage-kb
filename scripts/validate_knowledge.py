#!/usr/bin/env python3
"""
Knowledge Base Validation Script
Validates .knowledge directory for broken links, missing metadata, format consistency.
Usage: python scripts/validate_knowledge.py
"""

import os
import re
import sys
from pathlib import Path
from typing import List

KNOWLEDGE_DIR = Path(__file__).parent.parent / ".knowledge"
REQUIRED_METADATA = ["version", "last_updated", "status", "tokens"]

class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
    
    def add_error(self, msg: str): self.errors.append(msg)
    def add_warning(self, msg: str): self.warnings.append(msg)
    def add_info(self, msg: str): self.info.append(msg)
    
    @property
    def has_errors(self) -> bool: return len(self.errors) > 0

def get_all_md_files(directory: Path) -> List[Path]:
    return list(directory.rglob("*.md"))

def check_metadata(file_path: Path, content: str, result: ValidationResult):
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)
    if not content.startswith("---"):
        result.add_warning(f"{rel_path}: Missing YAML front matter")
        return
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        result.add_warning(f"{rel_path}: Invalid YAML front matter format")
        return
    front_matter = match.group(1)
    for field in REQUIRED_METADATA:
        if field not in front_matter:
            result.add_warning(f"{rel_path}: Missing metadata field '{field}'")

def check_internal_links(file_path: Path, content: str, result: ValidationResult):
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)
    link_pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    links = re.findall(link_pattern, content)
    for link_text, link_path in links:
        if link_path.startswith("http"): continue
        if link_path.startswith(".knowledge/"):
            target = KNOWLEDGE_DIR.parent / link_path
        elif link_path.startswith("./"):
            target = file_path.parent / link_path[2:]
        else:
            target = file_path.parent / link_path
        if not target.exists():
            result.add_error(f"{rel_path}: Broken link '{link_path}'")

def check_format(file_path: Path, content: str, result: ValidationResult):
    rel_path = file_path.relative_to(KNOWLEDGE_DIR.parent)
    lines = content.split('\n')
    has_h1 = any(line.startswith('# ') for line in lines)
    if not has_h1:
        result.add_warning(f"{rel_path}: Missing H1 title")
    if len(lines) > 300:
        result.add_warning(f"{rel_path}: File exceeds 300 lines ({len(lines)})")

def validate_knowledge_base() -> ValidationResult:
    result = ValidationResult()
    if not KNOWLEDGE_DIR.exists():
        result.add_error(f"Knowledge directory not found: {KNOWLEDGE_DIR}")
        return result
    md_files = get_all_md_files(KNOWLEDGE_DIR)
    result.add_info(f"Found {len(md_files)} markdown files")
    for file_path in md_files:
        try:
            content = file_path.read_text(encoding='utf-8')
            check_metadata(file_path, content, result)
            check_internal_links(file_path, content, result)
            check_format(file_path, content, result)
        except Exception as e:
            result.add_error(f"{file_path}: Read error - {e}")
    return result

def main():
    print("=" * 60)
    print("SAGE Knowledge Base Validation")
    print("=" * 60)
    result = validate_knowledge_base()
    if result.info:
        print(f"\n[INFO] ({len(result.info)}):")
        for msg in result.info[:5]: print(f"  {msg}")
    if result.warnings:
        print(f"\n[WARN] ({len(result.warnings)}):")
        for msg in result.warnings[:15]: print(f"  {msg}")
        if len(result.warnings) > 15: print(f"  ... and {len(result.warnings) - 15} more")
    if result.errors:
        print(f"\n[ERROR] ({len(result.errors)}):")
        for msg in result.errors: print(f"  {msg}")
    print("\n" + "=" * 60)
    print(f"Summary: {len(result.errors)} errors, {len(result.warnings)} warnings")
    print("=" * 60)
    return 1 if result.has_errors else 0

if __name__ == "__main__":
    sys.exit(main())
