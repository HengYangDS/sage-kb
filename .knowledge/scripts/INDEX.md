# Scripts

> Automation tools for .knowledge documentation maintenance

---

## Table of Contents

- [1. Available Scripts](#1-available-scripts)
- [2. Usage](#2-usage)
- [3. CI Integration](#3-ci-integration)

---

## 1. Available Scripts

| Script | Purpose | Run Frequency |
|--------|---------|---------------|
| `check_markdown.py` | Validate Markdown format, code blocks, structure | Per commit |
| `check_links.py` | Validate cross-references and Related links | Per commit |
| `pre-commit-hook.sh` | Git pre-commit hook for local validation | Per commit |
| `MECE_AUDIT_CHECKLIST.md` | Manual MECE compliance checklist | Quarterly |

---

## 2. Usage

### 2.1 Markdown Format Check

```bash
# Check entire .knowledge directory
python .knowledge/scripts/check_markdown.py

# Check specific file
python .knowledge/scripts/check_markdown.py .knowledge/templates/ADR.md

# Check specific directory
python .knowledge/scripts/check_markdown.py .knowledge/practices/
```

**Checks performed:**
- Code block backtick matching (open/close)
- Document structure (H1, Related, Footer)
- Related section link count (3-5 recommended)

### 2.2 Link Validation

```bash
# Check all links
python .knowledge/scripts/check_links.py

# Check specific file
python .knowledge/scripts/check_links.py .knowledge/core/INDEX.md
```

**Checks performed:**
- Broken links (target file doesn't exist)
- Path format (should use `.knowledge/` prefix)

### 2.3 MECE Audit

Manual process using `MECE_AUDIT_CHECKLIST.md`:

1. Run automated checks first
2. Follow ME (Mutually Exclusive) checklist
3. Follow CE (Collectively Exhaustive) checklist
4. Document findings in audit report

---

## 3. CI Integration

### 3.1 GitHub Actions Example

```yaml
name: Documentation Check

on:
  push:
    paths:
      - '.knowledge/**'
  pull_request:
    paths:
      - '.knowledge/**'

jobs:
  check-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Check Markdown Format
        run: python .knowledge/scripts/check_markdown.py
      
      - name: Check Links
        run: python .knowledge/scripts/check_links.py
```

### 3.2 Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check only staged .md files in .knowledge
STAGED_MD=$(git diff --cached --name-only --diff-filter=ACM | grep '\.knowledge/.*\.md$')

if [ -n "$STAGED_MD" ]; then
    echo "Checking documentation..."
    python .knowledge/scripts/check_markdown.py
    if [ $? -ne 0 ]; then
        echo "Documentation check failed. Please fix errors before committing."
        exit 1
    fi
fi
```

---

## Related

- `.knowledge/practices/documentation/KNOWLEDGE_MAINTENANCE_SOP.md` — Maintenance procedures
- `.knowledge/practices/documentation/QUARTERLY_REVIEW_PROCESS.md` — Review process
- `.knowledge/practices/engineering/methodology/MECE.md` — MECE principle

---

*AI Collaboration Knowledge Base*
