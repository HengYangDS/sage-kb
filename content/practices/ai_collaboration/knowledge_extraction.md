# Knowledge Extraction Patterns

> **Load Priority**: On-demand
> **Purpose**: Methods for extracting reusable knowledge from experience

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Goal** | Transform experience into transferable knowledge |
| **Scope** | Patterns, principles, frameworks (not implementations) |
| **Output** | Documented, reusable, project-independent content |

---

## When to Extract

| Trigger | Action | Example |
|---------|--------|---------|
| **Repeated pattern** (3+ times) | Formalize as practice | Error handling approach |
| **Successful experiment** | Document as case study | Optimization technique |
| **Hard-won insight** | Capture as principle | Performance tradeoff |
| **Reusable solution** | Template-ize | Document structure |
| **Cross-project applicability** | Abstract to framework | Decision protocol |

---

## Extraction Process

### Five-Step Method

```
Identify → Abstract → Validate → Document → Reference
```

| Step | Action | Output |
|------|--------|--------|
| **1. Identify** | Recognize reusable pattern | Pattern candidate |
| **2. Abstract** | Remove project-specific details | Generic principle |
| **3. Validate** | Test in different contexts | Confirmed universality |
| **4. Document** | Use standard format | Knowledge artifact |
| **5. Reference** | Link from relevant contexts | Integrated knowledge |

### Abstraction Techniques

| From | To | Method |
|------|-----|--------|
| Specific config value | Range/principle | `100ms` → `50-200ms for cache` |
| Named implementation | Pattern name | `SAGE protocol` → `4-stage workflow` |
| Project terminology | Generic terms | `T1-T5` → `timeout hierarchy levels` |
| Code example | Pseudocode/concept | Implementation → Design pattern |

---

## Quality Checklist

### Must-Have Criteria

- ✓ **Project-independent?** — No references to specific project names/configs
- ✓ **Transferable?** — Applicable to other domains/technologies
- ✓ **Long-term validity?** — Won't change with version updates
- ✓ **Self-contained?** — Understandable without external context

### Quality Levels

| Level | Criteria | Action |
|-------|----------|--------|
| **Gold** | All 4 criteria met | Ready for content/ |
| **Silver** | 3 criteria met | Minor abstraction needed |
| **Bronze** | 2 criteria met | Significant rework needed |
| **Reject** | <2 criteria met | Keep in project docs |

---

## Knowledge Categories

| Category | Location | Content Type |
|----------|----------|--------------|
| **Principles** | `core/` | Foundational philosophies |
| **Frameworks** | `frameworks/` | Structured approaches |
| **Guidelines** | `guidelines/` | How-to guidance |
| **Practices** | `practices/` | Proven methods |
| **Templates** | `templates/` | Reusable structures |
| **Scenarios** | `scenarios/` | Context-specific bundles |

---

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Over-specificity** | Contains project details | Abstract further |
| **Under-abstraction** | Too tied to technology | Generalize concepts |
| **Premature extraction** | Pattern not proven | Wait for 3+ occurrences |
| **Missing validation** | Not tested elsewhere | Validate in new context |
| **Orphan knowledge** | No references to it | Add links from relevant docs |

---

## Examples

### Good Extraction

| Original (Project-Specific) | Extracted (Universal) |
|-----------------------------|----------------------|
| "SAGE uses T1=100ms for cache" | "Cache lookups: 50-200ms typical" |
| "Our expert committee has 24 members" | "Expert committee: 4-6 groups × 4-6 experts" |
| "sage.yaml configures loading" | "Centralized config with modular overrides" |

### Bad Extraction

| Attempt | Problem |
|---------|---------|
| "Use T1-T5 timeout levels" | Preserves project terminology |
| "Follow SAGE protocol" | References specific implementation |
| "See config/timeout.yaml" | Links to project file |

---

## Integration with 信达雅

| Principle | Application to Extraction |
|-----------|--------------------------|
| **信 (Faithfulness)** | Preserve original insight accurately |
| **达 (Clarity)** | Make transferable and understandable |
| **雅 (Elegance)** | Abstract to essential pattern |

---

## Related

- `token_optimization.md` — Compression without losing fidelity
- `information_density.md` — Balance abstraction level
- `../documentation/standards.md` — Document formatting
