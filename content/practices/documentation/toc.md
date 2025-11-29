# Table of Contents (TOC) Specification

> **Load Time**: On-demand (~120 tokens)  
> **Purpose**: Standards for adding and formatting TOC in documentation  
> **Config**: `config/documentation.yaml`

---

## 1. When to Add TOC

### Thresholds

| Condition            | Threshold    | Requirement  |
|----------------------|--------------|--------------|
| **Line Count**       | > 100 lines  | TOC required |
| **Heading Count**    | > 5 headings | TOC required |
| **Either condition** | Met          | Add TOC      |

### Decision Matrix

| Document Length | Headings | TOC Required |
|-----------------|----------|--------------|
| < 100 lines     | ≤ 5      | ❌ No         |
| < 100 lines     | > 5      | ✓ Yes        |
| > 100 lines     | Any      | ✓ Yes        |
| Any             | > 5      | ✓ Yes        |

### Rationale

- **100 lines**: ~3-5 minute read time, navigation aids improve UX
- **5 headings**: Multiple sections benefit from quick navigation
- **Rule of thumb**: If you need to scroll more than 2 screens, add TOC

---

## 2. TOC Placement

### Standard Position

```markdown
# Document Title

> **Metadata**: ...

---

## Table of Contents

[TOC content here]

---

## First Section
```

### Rules

1. **After metadata** — Place TOC after document header/metadata block
2. **Before content** — TOC precedes all main content sections
3. **Separated** — Use horizontal rules (`---`) before and after TOC
4. **H2 heading** — Use `## Table of Contents` or `## Contents`

---

## 3. TOC Styles

### Style: Inline Links (Recommended)

> **Config**: `documentation.toc.style: "inline_links"`

```markdown
## Table of Contents

[Section One](#section-one) · [Section Two](#section-two) · [Section Three](#section-three)
```

**Pros**: Compact, horizontal layout, saves vertical space  
**Use for**: Documents with 5-10 sections, single-level navigation

### Style: Bullet List

> **Config**: `documentation.toc.style: "bullet_list"`

```markdown
## Table of Contents

- [Section One](#section-one)
    - [Subsection A](#subsection-a)
    - [Subsection B](#subsection-b)
- [Section Two](#section-two)
- [Section Three](#section-three)
```

**Pros**: Hierarchical, shows document structure  
**Use for**: Documents with nested sections, complex navigation needs

---

## 4. Anchor Format

### Standard Anchor Rules

| Heading                    | Anchor                 |
|----------------------------|------------------------|
| `## Section Name`          | `#section-name`        |
| `## Multi Word Title`      | `#multi-word-title`    |
| `## 1. Numbered Section`   | `#1-numbered-section`  |
| `## Section (with parens)` | `#section-with-parens` |
| `## CamelCase`             | `#camelcase`           |

### Conversion Rules

1. **Lowercase** — Convert all characters to lowercase
2. **Spaces → Hyphens** — Replace spaces with `-`
3. **Remove special chars** — Strip `()`, `:`, etc. (keep alphanumeric and `-`)
4. **Keep numbers** — Preserve numbered sections

### Manual Anchors (Optional)

For precise control, use HTML anchors:

```markdown
<a id="custom-anchor"></a>

## Section Title

[Link to section](#custom-anchor)
```

---

## 5. Examples

### Example: Inline Links TOC

```markdown
# API Reference Guide

> **Purpose**: Complete API documentation

---

## Table of Contents

[Authentication](#authentication) · [Endpoints](#endpoints) · [Error Handling](#error-handling) · [Rate Limits](#rate-limits) · [Examples](#examples)

---

## Authentication

...
```

### Example: Bullet List TOC

```markdown
# Architecture Design Document

> **Purpose**: System architecture overview

---

## Table of Contents

- [Overview](#overview)
- [Components](#components)
    - [Core Layer](#core-layer)
    - [Service Layer](#service-layer)
    - [Plugin Layer](#plugin-layer)
- [Data Flow](#data-flow)
- [Deployment](#deployment)

---

## Overview

...
```

---

## 6. Maintenance

### Update Triggers

| Change           | Action                   |
|------------------|--------------------------|
| Add section      | Update TOC               |
| Remove section   | Update TOC               |
| Rename heading   | Update TOC link + anchor |
| Reorder sections | Update TOC order         |

### Verification

- ✓ All TOC links resolve to valid anchors
- ✓ Section order matches document flow
- ✓ No orphan anchors (linked but heading removed)
- ✓ Consistent style throughout document

---

## 7. Configuration Reference

```yaml
# config/documentation.yaml
documentation:
  toc:
    line_threshold: 100          # Lines threshold
    heading_threshold: 5         # Headings threshold
    style: "inline_links"        # inline_links | bullet_list
```

### Environment Override

```bash
SAGE_DOCUMENTATION__TOC__LINE_THRESHOLD=150
SAGE_DOCUMENTATION__TOC__STYLE=bullet_list
```

---

## Quick Reference

| Aspect        | Standard                                  |
|---------------|-------------------------------------------|
| **When**      | > 100 lines OR > 5 headings               |
| **Where**     | After metadata, before content            |
| **Style**     | `inline_links` (default) or `bullet_list` |
| **Heading**   | `## Table of Contents`                    |
| **Separator** | `·` for inline, `-` for bullets           |
| **Anchors**   | lowercase, hyphen-separated               |

---

## Related

- `config/documentation.yaml` — TOC configuration
- `content/practices/documentation/standards.md` — Documentation standards
- `content/guidelines/documentation.md` — Documentation guidelines

---

*Part of SAGE Knowledge Base Documentation Practices*
