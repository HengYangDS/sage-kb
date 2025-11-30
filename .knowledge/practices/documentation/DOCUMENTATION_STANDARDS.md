# Documentation Standards (SSOT)

> Single source of truth for documentation writing standards

---

## Table of Contents

- [1. Format](#1-format)
- [2. Structure](#2-structure)
- [3. Token Efficiency](#3-token-efficiency)
- [4. Writing](#4-writing)
- [5. Organization](#5-organization)
- [6. Quality](#6-quality)
- [7. Diagrams](#7-diagrams)
- [8. Tables](#8-tables)
- [9. Code Blocks & Quotes](#9-code-blocks--quotes)

---

## 1. Format

### 1.1 Document Template

```markdown
# Title

> Single-line purpose

---

## Table of Contents (if >60 lines or >3 H2)

- [1. Section](#1-section)
- [2. Section](#2-section)

---

## 1. Section

### 1.1 Subsection

---

## Related

- `path/FILE.md` — Description

---

*AI Collaboration Knowledge Base*
```

**Note**: Frontmatter metadata (version, tokens, etc.) is NOT used. Document content speaks for itself.

### 1.2 Heading Rules

| Level | Format               | Numbering  | Use                 |
|-------|----------------------|------------|---------------------|
| H1    | `# Title`            | None       | Document title only |
| H2    | `## N. Section`      | 1., 2., 3. | Main sections       |
| H3    | `### N.N Subsection` | 1.1, 1.2   | Subsections         |
| H4    | `#### N.N.N Detail`  | 1.1.1      | Use sparingly       |

### 1.3 TOC Rules

| Condition                   | Action                                    |
|-----------------------------|-------------------------------------------|
| >60 lines OR >3 H2 headings | Add TOC                                   |
| Format                      | Vertical list with `- [Section](#anchor)` |
| Content                     | H2 sections only                          |
| Anchor                      | `#N-section-name` (lowercase, hyphens)    |

---

## 2. Structure

### 2.1 Section Order

1. Title + Purpose (header)
2. TOC (conditional)
3. Numbered content sections
4. Related (unnumbered)
5. Footer

### 2.2 Content Types

| Type      | Structure                              | Use For            |
|-----------|----------------------------------------|--------------------|
| Index     | Navigation table + descriptions        | Layer entry points |
| Guide     | Numbered steps + examples              | How-to content     |
| Reference | Tables + code blocks                   | API, config docs   |
| Framework | Concepts + patterns + examples         | Conceptual models  |
| Practice  | Patterns + anti-patterns + checklist   | Best practices     |
| Template  | Placeholders `[MARKER]` + instructions | Reusable documents |

### 2.3 Cross-References

| Element         | Format                          |
|-----------------|---------------------------------|
| Related section | Unnumbered, at document end     |
| Link format     | `path/FILE.md` — Description    |
| Link count      | 3-5 per document                |
| Priority        | Same layer first, then adjacent |

### 2.4 Path Format Standard

**Rule**: All paths in Related sections and cross-references MUST use **project-root-relative paths** (starting with `.`).

#### Path Format Examples

| ✅ Correct (Project-Root-Relative)                        | ❌ Incorrect (Relative/Mixed)           |
|----------------------------------------------------------|----------------------------------------|
| `.knowledge/contexts/policies/TIMEOUT_HIERARCHY.md`      | `TIMEOUT_HIERARCHY.md`                 |
| `.knowledge/frameworks/autonomy/LEVELS.md`               | `../frameworks/autonomy/LEVELS.md`     |
| `.knowledge/practices/ai_collaboration/GUIDELINES.md`    | `GUIDELINES.md`                        |
| `.knowledge/references/design/01-ARCHITECTURE.md`        | `../../docs/design/01-ARCHITECTURE.md` |

#### Rationale

| Benefit             | Explanation                                      |
|---------------------|--------------------------------------------------|
| **Unambiguous**     | Clear location regardless of current file        |
| **IDE-friendly**    | Easy navigation with Ctrl+Click                  |
| **Maintainable**    | No broken links when files move within directory |
| **Consistent**      | Same format across all documents                 |
| **Cross-directory** | Works for references outside current directory   |

#### Format Rules

1. **Start with `.`**: All paths begin with `.` (project root) or directory name under root
2. **Use forward slashes**: Always `/`, never `\` (cross-platform)
3. **Include extension**: Always include `.md` for markdown files
4. **No `../`**: Never use relative parent traversal
5. **Directories end without `/`**: `docs/api` not `docs/api/`

#### Special Cases

| Case                  | Format              | Example                                  |
|-----------------------|---------------------|------------------------------------------|
| Same directory file   | Full path from root | `.knowledge/contexts/policies/TIMEOUT.md`|
| Source code reference | Path from root      | `src/app/core/config.py`                 |
| Config file reference | Path from root      | `config/app.yaml`                        |
| External URL          | Full URL            | `https://example.com/docs`               |

---

## 3. Token Efficiency

> **深入优化技术**: 参见 `practices/ai_collaboration/TOKEN_OPTIMIZATION.md`

### 3.1 High-Impact Patterns

| Pattern              | Savings | Use For                |
|----------------------|---------|------------------------|
| Tables vs paragraphs | ~40%    | Structured comparisons |
| Lists vs paragraphs  | ~30%    | Enumerations, steps    |
| Vertical TOC         | ~50%    | Document navigation    |
| Cross-references     | ~70%    | Repeated content       |

### 3.2 Anti-Patterns

| Avoid             | Problem         | Fix                   |
|-------------------|-----------------|-----------------------|
| Long paragraphs   | High token cost | Convert to table/list |
| Repeated content  | Waste           | Add cross-reference   |
| Verbose headers   | Overhead        | Single-line format    |
| Deep nesting (>3) | Complexity      | Flatten structure     |
| "In order to"     | Verbose         | "To"                  |
| "It is important" | Filler          | "Note:"               |

### 3.3 Target Metrics

| Metric               | Target |
|----------------------|--------|
| Tokens per section   | <500   |
| Lines per file       | <300   |
| H2 headings per file | 5-15   |
| Nesting depth        | ≤3     |
| Related links        | 3-5    |

---

## 4. Writing

### 4.1 Style Rules

| Rule          | ❌ Avoid                  | ✓ Prefer                       |
|---------------|--------------------------|--------------------------------|
| Active voice  | "File is read by loader" | "Loader reads file"            |
| Present tense | "This will create"       | "This creates"                 |
| Specific      | "Configure system"       | "Set `MAX=100` in config.yaml" |
| Concise       | "In order to"            | "To"                           |

### 4.2 Code Examples

**Requirements**: Complete · Minimal · Commented · Runnable

```python
# ✓ Good: focused, shows input/output
def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet("World"))  # Output: Hello, World
```

### 4.3 File Naming

| Type     | Convention                | Example                        |
|----------|---------------------------|--------------------------------|
| Markdown | `UPPER_SNAKE_CASE.md`     | `DOCUMENTATION_STANDARDS.md`   |
| ADR      | `ADR_NNNN_TITLE.md`       | `ADR_0001_FASTMCP_CHOICE.md`   |
| Session  | `YYYYMMDD-TOPIC.md`       | `20251129-TIMEOUT.md`          |
| Handoff  | `YYYYMMDD-HANDOFF.md`     | `20251129-API-HANDOFF.md`      |
| Index    | `INDEX.md`                | `INDEX.md`                     |
| Special  | `UPPERCASE.md`            | `README.md`, `CHANGELOG.md`    |

**Rationale**: Uppercase naming provides clear visual distinction for documentation files and ensures consistent cross-platform compatibility.

#### 4.3.1 Naming Exceptions

| Directory | Convention      | Example           | Rationale                                    |
|-----------|-----------------|-------------------|----------------------------------------------|
| `.junie/` | `lowercase.md`  | `guidelines.md`   | AI client config directory follows tool convention |

**Note**: The `.junie/` directory is the JetBrains Junie AI client configuration directory. Its root `guidelines.md` file must use lowercase naming to comply with the Junie tool's expected file structure.

---

## 5. Organization

### 5.1 Layer Architecture

| Layer         | Purpose                 | Token Budget | Load Timing    |
|---------------|-------------------------|--------------|----------------|
| `core/`       | Foundational principles | ~500         | Always         |
| `guidelines/` | Standards, conventions  | ~1200        | By role/task   |
| `frameworks/` | Deep conceptual models  | ~2000        | On-demand      |
| `practices/`  | Actionable patterns     | ~1500        | Implementation |
| `scenarios/`  | Context presets         | ~500         | By trigger     |
| `templates/`  | Ready-to-use templates  | ~300         | Direct copy    |

### 5.2 Directory Conventions

| Directory     | Purpose                    | Git Policy |
|---------------|----------------------------|------------|
| `.context/`   | Project-specific knowledge | Tracked    |
| `.history/`   | Session history, handoffs  | Tracked    |
| `.archive/`   | Historical/deprecated      | Tracked    |
| `.backups/`   | Pre-change snapshots       | Tracked    |
| `.logs/`      | Runtime logs               | Ignored    |
| `.outputs/`   | Intermediate files         | Ignored    |
| `.knowledge/` | Generic reusable knowledge | Tracked    |
| `docs/`       | User-facing documentation  | Tracked    |

### 5.3 Content Placement

| Content Type         | Location                 |
|----------------------|--------------------------|
| Project conventions  | `.context/conventions/`  |
| Universal guidelines | `.knowledge/guidelines/` |
| ADR records          | `.context/decisions/`    |
| API documentation    | `docs/api/`              |
| Session handoffs     | `.history/handoffs/`     |
| Deprecated content   | `.archive/`              |

### 5.4 MECE Principle

| Aspect                  | Application               |
|-------------------------|---------------------------|
| Mutually Exclusive      | No overlapping content    |
| Collectively Exhaustive | Complete coverage         |
| Single location         | Each concept defined once |
| Cross-reference         | Link, don't duplicate     |

---

## 6. Quality

### 6.1 Quality Checklist

**Header**:

- [ ] H1 title (no emoji in production)
- [ ] Single-line blockquote purpose
- [ ] Horizontal rule after header

**Structure**:

- [ ] TOC if >60 lines or >3 H2
- [ ] TOC uses vertical list format
- [ ] H2 sections numbered
- [ ] H3 uses decimal notation

**Content**:

- [ ] Tables for comparisons
- [ ] Lists for enumerations
- [ ] No redundant info (cross-ref)
- [ ] Code blocks for examples

**Navigation**:

- [ ] Related section present
- [ ] 3-5 cross-references
- [ ] Relative path links
- [ ] `—` separator in descriptions

**Footer**:

- [ ] Horizontal rule before
- [ ] `*AI Collaboration Knowledge Base*`

### 6.2 Update Triggers

| Event         | Action               |
|---------------|----------------------|
| Code change   | Update affected docs |
| API change    | Update reference     |
| New feature   | Add guide            |
| User question | Improve clarity      |

### 6.3 Optimization Workflow

```
1. Review against checklist
       ↓
2. Identify deviations
       ↓
3. Batch apply fixes
       ↓
4. Verify consistency
```

---

## 7. Diagrams

> **Rule**: All diagrams MUST use Mermaid syntax.
>
> **Full Standards**: See `.knowledge/practices/documentation/DIAGRAM_STANDARDS.md`

### 7.1 Quick Reference

| Rule | Requirement |
|------|-------------|
| **Tool** | Must use Mermaid |
| **Design Philosophy** | 信达雅 (Xin-Da-Ya): Faithfulness → Clarity → Elegance |
| **Node Limit** | Max 15 nodes per diagram |
| **Nesting Limit** | Max 2 levels deep |

### 7.2 Diagram Types (21 Total)

| Priority | Types |
|----------|-------|
| ⭐ **Primary** | Flowchart, Sequence |
| **Common** | Class, State, ER, User Journey, Timeline, C4 |
| **Occasional** | Gantt, Pie, Quadrant, XY Chart, Block, Architecture |
| **Rare** | Mindmap, Git Graph, Requirement, Sankey, Kanban, Packet, Radar |

### 7.3 Selection Guide

| Scenario | Recommended Type |
|----------|------------------|
| Process/workflow | Flowchart |
| API interactions | Sequence diagram |
| Data models | Class diagram |
| State machines | State diagram |
| Database schemas | ER diagram |
| User experience | User Journey |
| Version history | Timeline |
| Software architecture | C4 diagram |

---

## 8. Tables

> **Full Standards**: See `.knowledge/practices/documentation/TABLE_STANDARDS.md`

### 8.1 Quick Reference

| Rule | Requirement |
|------|-------------|
| **Purpose** | Present structured, comparable data |
| **Design Philosophy** | 信达雅 (Xin-Da-Ya): Faithfulness → Clarity → Elegance |
| **Column Limit** | 3-5 recommended, 7 maximum |
| **Row Limit** | 5-15 recommended, 25 maximum |

### 8.2 When to Use Tables

| Scenario | Use Table? |
|----------|------------|
| Comparing multiple items | ✅ Yes |
| Key-value pairs (>3) | ✅ Yes |
| Sequential steps | ❌ Use numbered list |
| Hierarchical data | ❌ Use nested lists |

### 8.3 Alignment Rules

| Data Type | Alignment |
|-----------|-----------|
| Text | Left (`:---`) |
| Numbers | Right (`---:`) |
| Status/Icons | Center (`:---:`) |

---

## 9. Code Blocks & Quotes

> **Full Standards**: See `.knowledge/practices/documentation/CODE_BLOCK_STANDARDS.md`

### 9.1 Quick Reference

| Element | Purpose |
|---------|---------|
| **Code Block** | Display code, commands, output |
| **Quote Block** | Highlight important information |
| **Callout** | Draw attention to warnings/notes |
| **Inline Code** | Reference code elements in text |

### 9.2 Code Block Rules

| Rule | Requirement |
|------|-------------|
| **Language ID** | Always specify (e.g., `python`, `yaml`) |
| **Design Philosophy** | 信达雅 (Xin-Da-Ya): Faithfulness → Clarity → Elegance |
| **Line Limit** | 5-25 recommended, 50 maximum |
| **Width** | 80 chars recommended, 100 maximum |

### 9.3 Code Example Requirements

**Good examples are**: Complete · Minimal · Commented · Runnable

```python
# ✓ Good: focused, shows input/output
def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet("World"))  # Output: Hello, World
```

### 9.4 Quote Block Types

| Type | Syntax | Use Case |
|------|--------|----------|
| Note | `> **Note**:` | Additional information |
| Warning | `> **⚠️ Warning**:` | Caution required |
| Tip | `> **💡 Tip**:` | Helpful suggestion |

---

## Related

- `.knowledge/practices/documentation/DIAGRAM_STANDARDS.md` — Diagram creation standards (SSOT)
- `.knowledge/practices/documentation/TABLE_STANDARDS.md` — Table creation standards (SSOT)
- `.knowledge/practices/documentation/CODE_BLOCK_STANDARDS.md` — Code and quote block standards (SSOT)
- `.knowledge/practices/documentation/KNOWLEDGE_ORGANIZATION.md` — Layer architecture details
- `.knowledge/practices/documentation/OPTIMIZATION_WORKFLOW.md` — Full optimization process
- `.knowledge/templates/INDEX.md` — Document templates

---

*AI Collaboration Knowledge Base*
