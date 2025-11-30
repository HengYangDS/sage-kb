# Table Standards (SSOT)

> Single source of truth for table creation standards in Markdown documentation

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Design Principles](#2-design-principles)
- [3. Table Types](#3-table-types)
- [4. Syntax Standards](#4-syntax-standards)
- [5. Content Guidelines](#5-content-guidelines)
- [6. Layout Best Practices](#6-layout-best-practices)
- [7. Advanced Techniques](#7-advanced-techniques)
- [8. Anti-Patterns](#8-anti-patterns)
- [9. Troubleshooting](#9-troubleshooting)

---

## 1. Overview

Tables are powerful tools for presenting structured information clearly and efficiently.

| Rule | Requirement |
|------|-------------|
| **Purpose** | Present structured, comparable data |
| **Efficiency** | ~40% token savings vs paragraphs |
| **Readability** | Easy scanning and comparison |
| **Consistency** | Uniform formatting across project |

### 1.1 When to Use Tables

| Scenario | Use Table? | Alternative |
|----------|------------|-------------|
| Comparing multiple items | ✅ Yes | - |
| Key-value pairs (>3) | ✅ Yes | - |
| Multi-attribute data | ✅ Yes | - |
| Sequential steps | ❌ No | Numbered list |
| Single comparison | ❌ No | Inline text |
| Narrative content | ❌ No | Paragraphs |
| Hierarchical data | ❌ No | Nested lists |

---

## 2. Design Principles

Apply 信达雅 (Xin-Da-Ya) and 术法道 (Shu-Fa-Dao) philosophies to create effective tables.

**Priority**: 信 → 达 → 雅 (Faithfulness → Clarity → Elegance)

### 2.1 信 (Faithfulness) — Accurate Representation

| Checkpoint | Requirement |
|------------|-------------|
| **Completeness** | All relevant data included |
| **Accuracy** | Data correctly categorized |
| **Consistency** | Same data format within columns |
| **Traceability** | Source verifiable if applicable |

**术 (Technique)**:
```markdown
| Status | Description |
|--------|-------------|
| ✅ Pass | All tests successful |
| ❌ Fail | One or more tests failed |
| ⚠️ Warn | Tests passed with warnings |
```

**Anti-patterns**:
- ❌ Mixing units without labels (e.g., "100" vs "100ms")
- ❌ Incomplete rows with missing data
- ❌ Inconsistent date/number formats

### 2.2 达 (Clarity) — Clear Communication

| Checkpoint | Requirement |
|------------|-------------|
| **Headers** | Descriptive, concise column names |
| **Alignment** | Logical alignment per data type |
| **Ordering** | Logical row/column sequence |
| **Density** | Appropriate information per cell |

**法 (Method)**:
- Headers describe column content precisely
- Numbers right-aligned, text left-aligned
- Most important columns first
- One concept per cell

**Anti-patterns**:
- ❌ Ambiguous headers (e.g., "Type", "Value" without context)
- ❌ Overly wide cells with paragraphs
- ❌ Random row ordering

### 2.3 雅 (Elegance) — Refined Simplicity

| Checkpoint | Requirement |
|------------|-------------|
| **Minimalism** | No redundant columns |
| **Balance** | Proportional column widths |
| **Consistency** | Uniform cell formatting |
| **Whitespace** | Adequate padding |

**道 (Philosophy)**:
- Every column earns its place
- Visual harmony aids comprehension
- Simplicity reveals essence

**Anti-patterns**:
- ❌ Empty columns "for future use"
- ❌ Excessive formatting (bold + italic + emoji)
- ❌ Inconsistent capitalization

### 2.4 Design Checklist

Before finalizing any table:

1. **信**: Is all data accurate and complete?
2. **达**: Can readers find information in 5 seconds?
3. **雅**: Is every column necessary? Can anything be merged?

---

## 3. Table Types

### 3.1 Classification by Purpose

| Type | Purpose | Example Use |
|------|---------|-------------|
| **Comparison** | Compare items across attributes | Feature matrix |
| **Reference** | Quick lookup of values | API parameters |
| **Mapping** | Show relationships | Status codes |
| **Summary** | Aggregate information | Metrics dashboard |
| **Checklist** | Track completion | Quality checklist |

### 3.2 Classification by Structure

| Structure | Columns | Rows | Best For |
|-----------|---------|------|----------|
| **Simple** | 2-3 | Any | Key-value, definitions |
| **Standard** | 4-6 | 5-15 | Comparisons, references |
| **Wide** | 7+ | Few | Feature matrices |
| **Tall** | 2-3 | 15+ | Lists, logs |

### 3.3 Selection Guide

| Scenario | Recommended Type |
|----------|------------------|
| API endpoint documentation | Reference (3-4 cols) |
| Configuration options | Reference with defaults |
| Feature comparison | Comparison matrix |
| Error codes | Mapping (code → message) |
| Progress tracking | Checklist with status |
| Performance metrics | Summary with numbers |

---

## 4. Syntax Standards

### 4.1 Basic Syntax

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

**Result**:

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### 4.2 Column Alignment

```markdown
| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| Text     | Text     | 123      |
| Longer   | Mid      | 4567     |
```

**Result**:

| Left     | Center   | Right    |
|:---------|:--------:|---------:|
| Text     | Text     | 123      |
| Longer   | Mid      | 4567     |

### 4.3 Alignment Rules

| Data Type | Alignment | Rationale |
|-----------|-----------|-----------|
| Text | Left (`:---`) | Natural reading direction |
| Numbers | Right (`---:`) | Decimal alignment |
| Status/Icons | Center (`:---:`) | Visual balance |
| Mixed | Left | Default safe choice |

### 4.4 Formatting in Cells

| Element | Syntax | Example |
|---------|--------|---------|
| **Bold** | `**text**` | **Important** |
| *Italic* | `*text*` | *emphasis* |
| `Code` | `` `code` `` | `function()` |
| Link | `[text](url)` | [Docs](./docs) |
| Emoji | Unicode/shortcode | ✅ ❌ ⚠️ |

### 4.5 Special Characters

| Character | Escape Method | Example |
|-----------|---------------|---------|
| Pipe `\|` | `\|` or `&#124;` | A `\|` B |
| Backtick | Double backticks | `` `code` `` |
| Line break | `<br>` | Line1<br>Line2 |

---

## 5. Content Guidelines

### 5.1 Header Best Practices

| ❌ Avoid | ✅ Prefer | Reason |
|----------|-----------|--------|
| `Type` | `Data Type` | More specific |
| `Value` | `Default Value` | Clarifies context |
| `Name` | `Parameter Name` | Disambiguates |
| `Info` | `Description` | Standard term |

### 5.2 Cell Content Rules

| Rule | Guideline |
|------|-----------|
| **Length** | Max 50 characters per cell |
| **Sentences** | Avoid full sentences; use phrases |
| **Punctuation** | No ending periods in phrases |
| **Capitalization** | Sentence case for text |
| **Empty cells** | Use `-` or `N/A`, never leave blank |

### 5.3 Consistent Terminology

| Category | Standard Terms |
|----------|----------------|
| **Boolean** | `true`/`false` or Yes/No or ✅/❌ |
| **Status** | Active, Inactive, Pending, Deprecated |
| **Priority** | P0 (Critical), P1, P2, P3 |
| **Required** | Required, Optional, Conditional |

### 5.4 Numeric Data

| Format | Use For | Example |
|--------|---------|---------|
| Integer | Counts, IDs | `42` |
| Decimal | Measurements | `3.14` |
| Percentage | Ratios | `85%` |
| Duration | Time spans | `100ms`, `2s` |
| Range | Min-max | `10-100` |

---

## 6. Layout Best Practices

### 6.1 Column Ordering

| Position | Content Type | Rationale |
|----------|--------------|-----------|
| First | Identifier/Name | Primary lookup key |
| Second | Type/Category | Classification |
| Middle | Attributes | Supporting details |
| Last | Description/Notes | Longest content |

### 6.2 Row Ordering

| Strategy | Use When |
|----------|----------|
| Alphabetical | Reference tables, no natural order |
| Priority/Importance | Action items, features |
| Frequency | Common items first |
| Logical sequence | Steps, dependencies |
| Chronological | Timeline, versions |

### 6.3 Table Size Guidelines

| Metric | Recommended | Maximum |
|--------|-------------|---------|
| Columns | 3-5 | 7 |
| Rows | 5-15 | 25 |
| Cell width | 20-40 chars | 60 chars |
| Total width | 80 chars | 120 chars |

### 6.4 Breaking Large Tables

**When table exceeds limits**:

1. **Split by category**: Create multiple focused tables
2. **Transpose**: Swap rows and columns if helpful
3. **Hierarchical**: Use nested sections with smaller tables
4. **Reference**: Link to detailed sub-documents

**Example split**:

```markdown
### 6.4.1 Core Parameters

| Parameter | Type | Required |
|-----------|------|----------|
| id | string | Yes |
| name | string | Yes |

### 6.4.2 Optional Parameters

| Parameter | Type | Default |
|-----------|------|---------|
| timeout | int | 30 |
| retries | int | 3 |
```

---

## 7. Advanced Techniques

### 7.1 Comparison Matrix

Use for feature comparisons across multiple items:

```markdown
| Feature | Plan A | Plan B | Plan C |
|---------|:------:|:------:|:------:|
| Storage | 10GB | 50GB | Unlimited |
| Users | 5 | 25 | Unlimited |
| Support | Email | Chat | 24/7 |
| Price | Free | $10/mo | $50/mo |
```

### 7.2 Status Dashboard

Use icons for quick visual scanning:

```markdown
| Component | Status | Health |
|-----------|:------:|:------:|
| API | ✅ | 99.9% |
| Database | ✅ | 99.5% |
| Cache | ⚠️ | 95.0% |
| Queue | ❌ | 0% |
```

### 7.3 Decision Matrix

Use for documenting choices:

```markdown
| Criterion | Weight | Option A | Option B |
|-----------|:------:|:--------:|:--------:|
| Cost | 30% | ⭐⭐⭐ | ⭐⭐ |
| Speed | 40% | ⭐⭐ | ⭐⭐⭐ |
| Ease | 30% | ⭐⭐⭐ | ⭐ |
| **Total** | 100% | **2.3** | **2.2** |
```

### 7.4 Nested Information

Use description lists within tables for complex data:

```markdown
| Config | Values |
|--------|--------|
| mode | `development`: Local testing<br>`staging`: Pre-prod<br>`production`: Live |
| level | `debug`, `info`, `warn`, `error` |
```

### 7.5 Cross-Reference Tables

Link to detailed documentation:

```markdown
| Module | Purpose | Details |
|--------|---------|---------|
| Auth | Authentication | [AUTH.md](./AUTH.md) |
| API | REST endpoints | [API.md](./API.md) |
| DB | Data models | [MODELS.md](./MODELS.md) |
```

---

## 8. Anti-Patterns

### 8.1 Content Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Paragraph cells** | Hard to scan | Use phrases, not sentences |
| **Empty cells** | Ambiguous meaning | Use `-` or `N/A` |
| **Inconsistent units** | Confusing | Always include units |
| **Mixed formats** | Inconsistent | Standardize per column |

### 8.2 Structure Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Too many columns** | Horizontal scroll | Split into multiple tables |
| **Too many rows** | Lost context | Group with subheadings |
| **Single column** | Pointless table | Use list instead |
| **Sparse table** | Many empty cells | Restructure or use prose |

### 8.3 Formatting Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Over-formatting** | Visual noise | Minimal emphasis |
| **No alignment** | Harder to read | Use consistent alignment |
| **Inconsistent headers** | Confusing | Use standard terminology |
| **Missing separator** | Invalid markdown | Always include `|---|` row |

---

## 9. Troubleshooting

### 9.1 Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Table not rendering | Missing separator row | Add `|---|---|` after headers |
| Misaligned columns | Inconsistent pipe count | Ensure same pipes per row |
| Broken formatting | Unescaped special chars | Escape `\|` and backticks |
| Wide table overflow | Too many/wide columns | Split or abbreviate |

### 9.2 Validation Checklist

- [ ] Header row present
- [ ] Separator row with `---` for each column
- [ ] Equal number of pipes in each row
- [ ] No blank cells (use `-` or `N/A`)
- [ ] Consistent alignment specifiers
- [ ] Special characters escaped
- [ ] Reasonable column widths

### 9.3 Editor Tips

| Editor | Tip |
|--------|-----|
| VS Code | Use "Markdown All in One" for table formatting |
| PyCharm | Use `Ctrl+Alt+L` to format tables |
| Vim | Use `:TableModeToggle` plugin |
| Online | Use [Tables Generator](https://www.tablesgenerator.com/markdown_tables) |

---

## Related

- `.knowledge/practices/documentation/DOCUMENTATION_STANDARDS.md` — Documentation standards (SSOT)
- `.knowledge/practices/documentation/DIAGRAM_STANDARDS.md` — Diagram creation standards
- `.knowledge/practices/documentation/CODE_BLOCK_STANDARDS.md` — Code and quote block standards
- `.knowledge/guidelines/DOCUMENTATION.md` — Documentation guidelines

---

*AI Collaboration Knowledge Base*
