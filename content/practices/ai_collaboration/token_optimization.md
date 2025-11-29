# Token Optimization Principles

> **Load Priority**: On Demand  
> **Purpose**: Maximize knowledge density per token in AI collaboration

---

## Core Principles

| Principle | Description | Example |
|-----------|-------------|---------|
| **Shared Vocabulary** | Establish mutually understood terms | T1-T5, L1-L6 |
| **Information Layering** | Core → Details → Examples | quick_ref → defaults → full docs |
| **Structure First** | Tables > Paragraphs, Symbols > Text | ✓✗⚠️ replace yes/no/warning |
| **Precision Conservation** | Compression without accuracy loss | 信达雅 |
| **Reference over Repeat** | Link to detailed docs, don't duplicate | `See frameworks/autonomy/levels.md` |

---

## High-Density Patterns

### Effective Compression

| Pattern | Before | After | Savings |
|---------|--------|-------|---------|
| Pipe separation | Table with 5 rows | `T1:100ms\|T2:500ms\|T3:2s` | ~60% |
| Symbol lists | Checkbox lists | ✓ item1 · ✓ item2 · ✗ item3 | ~40% |
| Inline flow | Multi-step list | A → B → C → D | ~50% |
| Merged tables | 2 separate tables | Single 2-column comparison | ~30% |

### Anti-Patterns

- ❌ Self-invented abbreviations without shared semantics
- ❌ Over-nested abstractions
- ❌ Sacrificing accuracy for brevity
- ❌ Duplicating content across files (use references)
- ❌ ASCII art diagrams (use text descriptions or tables)

---

## Optimal Compression Point

| Compression | Tokens | Fidelity | Efficiency |
|-------------|--------|----------|------------|
| None | 100 | 100% | 1.0 |
| **Moderate** | 40 | 95% | **2.4** ⭐ |
| Excessive | 15 | 60% | 1.7* |

*Excessive compression may trigger clarification roundtrips

---

## Document Optimization Techniques

### Proven Transformations (30-50% reduction)

| Technique | Description | Example |
|-----------|-------------|---------|
| **Remove TOC links** | AI doesn't need click navigation | Delete `<p align="right">↑ TOC</p>` |
| **Remove ASCII art** | Convert to text or tables | Pyramid → "Unit → Integration → E2E" |
| **Merge checklists** | Combine phase-based lists | Before/During/After → Single table |
| **Inline principles** | Single-line summaries | List of 4 items → `A · B · C · D` |
| **Reference frameworks** | Link instead of repeat | `> See frameworks/autonomy/levels.md` |
| **Compress examples** | Good/Bad pairs only | Remove verbose explanations |

### Before/After Examples

```
# Before (verbose)
### When to Comment
- When implementing complex algorithms
- When making non-obvious decisions  
- When working around bugs
- When documenting public APIs

# After (compressed)
**When to Comment**: Complex algorithms · Non-obvious decisions · Workarounds · Public APIs
```

```
# Before (separate tables)
| Pre-Commit | ... |
| Pre-Merge | ... |
| Pre-Release | ... |

# After (merged)
| Stage | Requirements |
| Pre-Commit | Lint · Format · Tests |
| Pre-Merge | Review · Coverage · Docs |
| Pre-Release | E2E · Performance · Changelog |
```

---

## Task-Based Adaptation

| Scenario | Recommended Density | Rationale |
|----------|---------------------|-----------|
| Repetitive operations | High | Patterns established |
| Complex reasoning | Medium | Needs reasoning chain |
| First collaboration | Low | Build consensus first |
| Documentation files | High | Reference material |
| Code examples | Medium | Preserve clarity |

---

## Format Selection Guide

| Information Type | Best Format | Example |
|------------------|-------------|---------|
| Key-value pairs | `k:v` or `k=v` | `timeout=5s` |
| Boolean lists | ✓/✗ symbols | ✓ enabled · ✗ disabled |
| Sequences/Levels | Pipe: `a\|b\|c` | `T1:100ms\|T2:500ms` |
| Comparisons | Tables | Side-by-side columns |
| Procedures | Flow arrows | A → B → C |
| Checklists | Inline dots | ✓ A · ✓ B · ✓ C |

---

## Density Calibration

| Context Window | Action |
|----------------|--------|
| < 30% | Normal density OK |
| 30-60% | Prefer high-density |
| 60-80% | Compress non-critical |
| > 80% | Maximum compression |

---

## Optimization Results Summary

| Category | Files | Avg Reduction | Key Techniques |
|----------|-------|---------------|----------------|
| Frameworks | 6 | -30% | Remove TOC links, merge tables |
| Guidelines | 9 | -41% | Remove ASCII, compress examples |
| **Total** | **15** | **-37%** | Combined techniques |

---

## Related

- `content/core/quick_reference.md` — Symbol conventions
- `content/core/defaults.md` — Configuration defaults
- `content/frameworks/cognitive/expert_committee.md` — Decision framework

---

*信达雅: Elegance (雅) serves efficiency, but always with Faithfulness (信) and Clarity (达) as prerequisites*
