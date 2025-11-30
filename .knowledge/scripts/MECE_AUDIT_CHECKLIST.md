# MECE Audit Checklist

> Quarterly checklist for ensuring MECE compliance across .knowledge documents

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Pre-Audit Preparation](#2-pre-audit-preparation)
- [3. ME (Mutually Exclusive) Checks](#3-me-mutually-exclusive-checks)
- [4. CE (Collectively Exhaustive) Checks](#4-ce-collectively-exhaustive-checks)
- [5. Cross-Reference Validation](#5-cross-reference-validation)
- [6. Audit Report Template](#6-audit-report-template)

---

## 1. Overview

### 1.1 MECE Principle

| Aspect | Definition | Violation Example |
|--------|------------|-------------------|
| **ME** (Mutually Exclusive) | No overlapping content | Same table in two files |
| **CE** (Collectively Exhaustive) | Complete coverage | Missing topic in INDEX |

### 1.2 Audit Frequency

| Audit Type | Frequency | Scope |
|------------|-----------|-------|
| Full audit | Quarterly | All .knowledge |
| Spot check | Monthly | New/modified files |
| CI check | Per commit | Automated scripts |

---

## 2. Pre-Audit Preparation

### 2.1 Run Automated Checks

```bash
# Run markdown format check
python .knowledge/scripts/check_markdown.py

# Run link validation
python .knowledge/scripts/check_links.py
```

### 2.2 Generate File Inventory

```bash
# Count files per directory
find .knowledge -name "*.md" | cut -d'/' -f2 | sort | uniq -c
```

### 2.3 Checklist

- [ ] Automated checks pass with no errors
- [ ] File counts match INDEX.md totals
- [ ] No new directories without INDEX.md

---

## 3. ME (Mutually Exclusive) Checks

### 3.1 High-Risk Overlap Areas

| Area | Files to Compare | Common Overlap |
|------|------------------|----------------|
| Quick references | `core/QUICK_REFERENCE.md` vs `core/DEFAULTS.md` | Timeout tiers, autonomy levels |
| Quick references | `core/QUICK_REFERENCE.md` vs `references/KNOWLEDGE_QUICK_REF.md` | Knowledge organization |
| Guidelines vs Practices | `guidelines/*.md` vs `practices/**/*.md` | Implementation details |
| Frameworks vs Templates | `frameworks/**/*.md` vs `templates/*.md` | Example code |

### 3.2 ME Audit Checklist

- [ ] **core/** - No duplicate definitions between PRINCIPLES, DEFAULTS, QUICK_REFERENCE
- [ ] **guidelines/** - Each guideline unique, no overlap with practices
- [ ] **frameworks/** - Each framework has single SSOT, others reference
- [ ] **practices/** - Implementation details only, theory in frameworks
- [ ] **templates/** - Templates only, no duplicate content from frameworks
- [ ] **scenarios/** - Context-specific, no generic content

### 3.3 Overlap Detection Method

1. Search for identical table headers across files
2. Compare section titles for duplicates
3. Check for copy-pasted code blocks
4. Verify SSOT references are used (not copies)

---

## 4. CE (Collectively Exhaustive) Checks

### 4.1 Coverage Verification

| Layer | Required Coverage |
|-------|-------------------|
| core/ | Philosophy, defaults, quick reference |
| guidelines/ | All language/domain guidelines |
| frameworks/ | All reusable patterns |
| practices/ | All implementation guides |
| references/ | Glossary, checklists |
| scenarios/ | All project types |
| templates/ | All document types |

### 4.2 CE Audit Checklist

- [ ] **INDEX files** - All files listed in parent INDEX
- [ ] **File counts** - INDEX totals match actual counts
- [ ] **Topic coverage** - No gaps in subject matter
- [ ] **Cross-references** - All related docs linked
- [ ] **New content** - Recent additions properly categorized

### 4.3 Gap Detection Method

1. Compare INDEX file lists with actual directory contents
2. Review "Related" sections for missing links
3. Check for orphan files (not in any INDEX)
4. Verify all external references are documented

---

## 5. Cross-Reference Validation

### 5.1 Reference Types

| Type | Format | Example |
|------|--------|---------|
| SSOT reference | "See X for definition" | "See `ROLE_PERSONA.md` for expert roles" |
| Related link | `- path — description` | `- .knowledge/core/PRINCIPLES.md — Core philosophy` |
| Inline reference | `(see Section X)` | "(see CONFLICT_RESOLUTION.md §4.7)" |

### 5.2 Validation Checklist

- [ ] All SSOT references point to correct source
- [ ] No circular references (A→B→A)
- [ ] Related sections have 3-5 links
- [ ] All links resolve to existing files
- [ ] Link descriptions are accurate

---

## 6. Audit Report Template

````markdown
# MECE Audit Report

**Date**: YYYY-MM-DD
**Auditor**: [Name]
**Scope**: [Full / Partial - specify areas]

## Summary

| Check | Status | Issues |
|-------|--------|--------|
| Automated checks | ✓/✗ | [count] |
| ME compliance | ✓/✗ | [count] |
| CE compliance | ✓/✗ | [count] |
| Cross-references | ✓/✗ | [count] |

## ME Violations Found

| File 1 | File 2 | Overlap Description | Resolution |
|--------|--------|---------------------|------------|
| | | | |

## CE Gaps Found

| Area | Missing Content | Priority | Action |
|------|-----------------|----------|--------|
| | | | |

## Cross-Reference Issues

| File | Line | Issue | Fix |
|------|------|-------|-----|
| | | | |

## Actions Taken

1. [Action 1]
2. [Action 2]

## Recommendations

1. [Recommendation 1]
2. [Recommendation 2]

---
*Audit completed on YYYY-MM-DD*
````

---

## Related

- `.knowledge/practices/engineering/methodology/MECE.md` — MECE principle details
- `.knowledge/practices/documentation/KNOWLEDGE_MAINTENANCE_SOP.md` — Maintenance procedures
- `.knowledge/practices/documentation/QUARTERLY_REVIEW_PROCESS.md` — Review process
- `.knowledge/scripts/check_markdown.py` — Automated format checker
- `.knowledge/scripts/check_links.py` — Link validator

---

*AI Collaboration Knowledge Base*
