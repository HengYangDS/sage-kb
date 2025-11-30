# Code Block & Quote Standards (SSOT)

> Single source of truth for code blocks, quote blocks, and other embedded content standards

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Design Principles](#2-design-principles)
- [3. Code Blocks](#3-code-blocks)
- [4. Syntax Highlighting](#4-syntax-highlighting)
- [5. Code Content Guidelines](#5-code-content-guidelines)
- [6. Quote Blocks](#6-quote-blocks)
- [7. Callout Blocks](#7-callout-blocks)
- [8. Inline Code](#8-inline-code)
- [9. Advanced Techniques](#9-advanced-techniques)
- [10. Anti-Patterns](#10-anti-patterns)
- [11. Troubleshooting](#11-troubleshooting)

---

## 1. Overview

Code blocks and quote blocks are essential for technical documentation, providing clear separation between explanatory text and executable/referenced content.

| Element | Purpose | Token Impact |
|---------|---------|--------------|
| **Code Block** | Display code, commands, output | High (preserved formatting) |
| **Quote Block** | Highlight important information | Medium |
| **Callout** | Draw attention to warnings/notes | Medium |
| **Inline Code** | Reference code elements in text | Low |

### 1.1 Element Selection Guide

| Content Type | Recommended Element |
|--------------|---------------------|
| Executable code | Fenced code block with language |
| Terminal commands | Code block with `bash`/`shell` |
| Configuration files | Code block with `yaml`/`json`/`toml` |
| API responses | Code block with `json` |
| File paths | Inline code |
| Variable names | Inline code |
| Important notes | Quote block or callout |
| Warnings | Callout block |
| External quotes | Quote block with attribution |

---

## 2. Design Principles

Apply 信达雅 (Xin-Da-Ya) and 术法道 (Shu-Fa-Dao) philosophies to create effective code documentation.

**Priority**: 信 → 达 → 雅 (Faithfulness → Clarity → Elegance)

### 2.1 信 (Faithfulness) — Accurate Representation

| Checkpoint | Requirement |
|------------|-------------|
| **Correctness** | Code must be syntactically valid |
| **Completeness** | Include necessary context (imports, setup) |
| **Testability** | Examples should be runnable |
| **Currency** | Code matches current API/syntax |

**术 (Technique)**:
```python
# ✅ Complete, runnable example
from datetime import datetime

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Today is {datetime.now():%Y-%m-%d}"

print(greet("World"))  # Output: Hello, World! Today is 2025-11-30
```

**Anti-patterns**:
- ❌ Incomplete snippets missing imports
- ❌ Outdated syntax or deprecated APIs
- ❌ Untested code that doesn't compile/run

### 2.2 达 (Clarity) — Clear Communication

| Checkpoint | Requirement |
|------------|-------------|
| **Purpose** | Clear what code demonstrates |
| **Comments** | Explain non-obvious logic |
| **Structure** | Logical organization |
| **Highlighting** | Correct language for syntax colors |

**法 (Method)**:
- State what the code does before showing it
- Use comments for "why", not "what"
- Group related code logically
- Always specify language identifier

**Anti-patterns**:
- ❌ Code without context or explanation
- ❌ Over-commented obvious code
- ❌ Missing language identifier (no syntax highlighting)

### 2.3 雅 (Elegance) — Refined Simplicity

| Checkpoint | Requirement |
|------------|-------------|
| **Minimalism** | Show only what's necessary |
| **Readability** | Consistent formatting |
| **Focus** | One concept per example |
| **Length** | Appropriate size (not too long/short) |

**道 (Philosophy)**:
- The best example is the simplest one that works
- Remove everything that doesn't teach
- Elegance emerges from clarity

**Anti-patterns**:
- ❌ Kitchen-sink examples showing everything
- ❌ Overly clever or "golf" code
- ❌ Inconsistent indentation or style

### 2.4 Design Checklist

Before finalizing code blocks:

1. **信**: Does the code actually work?
2. **达**: Will readers understand what it does and why?
3. **雅**: Is this the minimal example that demonstrates the concept?

---

## 3. Code Blocks

### 3.1 Fenced Code Block Syntax

**Basic syntax**:
~~~markdown
```language
code here
```
~~~

**Example**:
~~~markdown
```python
def hello():
    return "Hello, World!"
```
~~~

**Result**:
```python
def hello():
    return "Hello, World!"
```

### 3.2 Code Block Types

| Type | Use Case | Language ID |
|------|----------|-------------|
| **Source Code** | Implementation examples | `python`, `javascript`, etc. |
| **Shell Commands** | Terminal instructions | `bash`, `shell`, `powershell` |
| **Configuration** | Config file examples | `yaml`, `json`, `toml`, `ini` |
| **Output** | Command/program output | `text`, `console` |
| **Data** | Data structures | `json`, `xml`, `csv` |
| **Diff** | Code changes | `diff` |
| **Plain** | Generic preformatted | (none) or `text` |

### 3.3 Language Identifier Rules

| Scenario | Identifier | Example |
|----------|------------|---------|
| Python code | `python` | ```` ```python ```` |
| JavaScript | `javascript` or `js` | ```` ```javascript ```` |
| TypeScript | `typescript` or `ts` | ```` ```typescript ```` |
| Shell script | `bash` or `shell` | ```` ```bash ```` |
| Windows commands | `powershell` or `cmd` | ```` ```powershell ```` |
| JSON data | `json` | ```` ```json ```` |
| YAML config | `yaml` | ```` ```yaml ```` |
| SQL queries | `sql` | ```` ```sql ```` |
| Markdown | `markdown` or `md` | ```` ```markdown ```` |
| Plain text | `text` or none | ```` ```text ```` |

### 3.4 Code Block Size Guidelines

| Metric | Recommended | Maximum |
|--------|-------------|---------|
| Lines | 5-25 | 50 |
| Width | 80 chars | 100 chars |
| Functions | 1-2 | 3 |
| Concepts | 1 | 2 |

---

## 4. Syntax Highlighting

### 4.1 Common Languages

| Category | Languages | Identifiers |
|----------|-----------|-------------|
| **Systems** | C, C++, Rust, Go | `c`, `cpp`, `rust`, `go` |
| **Scripting** | Python, Ruby, Perl | `python`, `ruby`, `perl` |
| **Web Frontend** | JavaScript, TypeScript, HTML, CSS | `js`, `ts`, `html`, `css` |
| **Web Backend** | PHP, Java, C# | `php`, `java`, `csharp` |
| **Data** | SQL, JSON, YAML, XML | `sql`, `json`, `yaml`, `xml` |
| **Shell** | Bash, PowerShell, Zsh | `bash`, `powershell`, `zsh` |
| **Config** | TOML, INI, Properties | `toml`, `ini`, `properties` |
| **Docs** | Markdown, reStructuredText | `markdown`, `rst` |

### 4.2 Special Highlighting

| Use Case | Identifier | Notes |
|----------|------------|-------|
| Diff/patch | `diff` | Shows additions/removals |
| Console output | `console` | Mixed commands and output |
| HTTP | `http` | Request/response format |
| GraphQL | `graphql` | Query language |
| Mermaid diagrams | `mermaid` | Diagram syntax |
| Regex | `regex` | Pattern highlighting |

### 4.3 Diff Example

```diff
- old_function()  # Removed
+ new_function()  # Added
  unchanged_line()
```

### 4.4 Console Output Example

```console
$ python --version
Python 3.11.0
$ pip install requests
Collecting requests...
Successfully installed requests-2.28.0
```

---

## 5. Code Content Guidelines

### 5.1 Example Structure

**Recommended pattern**:

```markdown
Brief description of what the code does.

\`\`\`python
# Code example
result = do_something()
print(result)  # Output: expected_value
\`\`\`

Explanation of key points if needed.
```

### 5.2 Comment Guidelines

| Comment Type | When to Use | Example |
|--------------|-------------|---------|
| **Purpose** | Start of example | `# Calculate user age from birthdate` |
| **Output** | After print/return | `# Output: 42` |
| **Warning** | Non-obvious gotchas | `# Note: This blocks the thread` |
| **Step** | Multi-step processes | `# Step 1: Initialize` |
| **TODO** | Incomplete examples | `# TODO: Add error handling` |

### 5.3 Input/Output Convention

Always show expected output for clarity:

```python
# Input
data = [1, 2, 3, 4, 5]

# Processing
result = sum(data)

# Output
print(result)  # Output: 15
```

### 5.4 Error Examples

Show error handling and expected errors:

```python
# ❌ This raises an error
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: division by zero
```

### 5.5 Multiple File Examples

For multi-file examples, use headers:

```markdown
**`config.yaml`**:
\`\`\`yaml
database:
  host: localhost
  port: 5432
\`\`\`

**`app.py`**:
\`\`\`python
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)
\`\`\`
```

---

## 6. Quote Blocks

### 6.1 Basic Syntax

```markdown
> This is a quote block.
> It can span multiple lines.
```

**Result**:
> This is a quote block.
> It can span multiple lines.

### 6.2 Quote Block Types

| Type | Purpose | Example |
|------|---------|---------|
| **Definition** | Define terms | > **Term**: Definition text |
| **Note** | Additional information | > **Note**: Important detail |
| **Citation** | External quotes | > "Quote" — Author |
| **Summary** | Key takeaways | > **Summary**: Main points |

### 6.3 Document Purpose Quote

Every document should have a purpose quote after the title:

```markdown
# Document Title

> Single-line purpose statement describing document intent
```

### 6.4 Nested Quotes

```markdown
> Level 1 quote
> > Level 2 nested quote
> > > Level 3 nested quote (use sparingly)
```

**Result**:
> Level 1 quote
> > Level 2 nested quote
> > > Level 3 nested quote (use sparingly)

### 6.5 Quote with Attribution

```markdown
> "The best code is no code at all."
>
> — Jeff Atwood
```

**Result**:
> "The best code is no code at all."
>
> — Jeff Atwood

---

## 7. Callout Blocks

### 7.1 Standard Callout Types

| Type | Purpose | Visual |
|------|---------|--------|
| **Note** | Additional information | ℹ️ Blue |
| **Tip** | Helpful suggestion | 💡 Green |
| **Warning** | Caution required | ⚠️ Yellow |
| **Danger** | Critical warning | 🚫 Red |
| **Important** | Must-know information | ❗ Purple |

### 7.2 Callout Syntax (GitHub/GitLab)

```markdown
> [!NOTE]
> This is a note callout.

> [!TIP]
> This is a tip callout.

> [!WARNING]
> This is a warning callout.

> [!CAUTION]
> This is a caution callout.

> [!IMPORTANT]
> This is an important callout.
```

### 7.3 Alternative Callout Format

For platforms without callout support, use bold headers:

```markdown
> **Note**: This is additional information.

> **⚠️ Warning**: This action cannot be undone.

> **💡 Tip**: Use keyboard shortcuts for efficiency.
```

### 7.4 Callout Best Practices

| Guideline | Recommendation |
|-----------|----------------|
| **Frequency** | Max 2-3 per document section |
| **Length** | 1-3 sentences |
| **Placement** | Before relevant content |
| **Type selection** | Match severity to content |

---

## 8. Inline Code

### 8.1 Basic Syntax

```markdown
Use `backticks` for inline code.
```

**Result**: Use `backticks` for inline code.

### 8.2 When to Use Inline Code

| Use Case | Example |
|----------|---------|
| Variable names | The `user_id` parameter |
| Function names | Call `getData()` to fetch |
| File names | Edit `config.yaml` |
| Command names | Run `npm install` |
| Code snippets | Returns `true` or `false` |
| Key names | Press `Ctrl+C` to copy |
| Values | Set to `null` |

### 8.3 When NOT to Use Inline Code

| Avoid | Use Instead |
|-------|-------------|
| Emphasis | **bold** or *italic* |
| Product names | Plain text (Python, not `Python`) |
| Concept names | Plain text (REST API, not `REST API`) |
| URLs | Markdown links |

### 8.4 Escaping Backticks

To include backticks in inline code, use double backticks:

```markdown
Use `` `code` `` for inline code.
```

**Result**: Use `` `code` `` for inline code.

### 8.5 Long Inline Code

For long code, consider a code block instead:

```markdown
❌ Avoid: `const result = await fetchUserData(userId, { includeMetadata: true, timeout: 5000 })`

✅ Prefer: Use a code block for complex expressions.
```

---

## 9. Advanced Techniques

### 9.1 Code with Line Numbers

Some platforms support line numbers:

```markdown
\`\`\`python {linenos=true}
def hello():
    return "world"
\`\`\`
```

### 9.2 Code with Highlighting

Highlight specific lines:

```markdown
\`\`\`python {hl_lines=[2]}
def hello():
    return "world"  # This line is highlighted
\`\`\`
```

### 9.3 Collapsible Code Blocks

For long examples:

```markdown
<details>
<summary>Click to expand full example</summary>

\`\`\`python
# Long code example here
\`\`\`

</details>
```

### 9.4 Side-by-Side Comparison

Show before/after:

```markdown
**Before:**
\`\`\`python
result = []
for item in data:
    result.append(item * 2)
\`\`\`

**After:**
\`\`\`python
result = [item * 2 for item in data]
\`\`\`
```

### 9.5 Multi-Language Examples

Same functionality in different languages:

~~~markdown
**Python:**
```python
items = [1, 2, 3]
```

**JavaScript:**
```javascript
const items = [1, 2, 3];
```

**TypeScript:**
```typescript
const items: number[] = [1, 2, 3];
```
~~~

### 9.6 Code with Placeholders

Use clear placeholder conventions:

```python
# Placeholders: <description> or {DESCRIPTION}
api_key = "<your-api-key>"  # Replace with actual key
endpoint = "{BASE_URL}/api/v1/users"
```

---

## 10. Anti-Patterns

### 10.1 Code Block Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **No language ID** | No syntax highlighting | Always specify language |
| **Too long** | Overwhelming, hard to follow | Break into smaller examples |
| **Incomplete** | Missing imports/context | Include all necessary code |
| **Untested** | May contain errors | Test all code examples |
| **Over-commented** | Distracting | Comment only non-obvious parts |

### 10.2 Quote Block Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Overuse** | Diminished impact | Reserve for important content |
| **Too long** | Lost emphasis | Keep to 1-3 sentences |
| **Nested too deep** | Hard to read | Max 2 levels |
| **No purpose** | Confusion | Always indicate why quoted |

### 10.3 Inline Code Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Overuse** | Visual noise | Use only for code elements |
| **Product names** | Incorrect styling | Plain text for names |
| **Long expressions** | Hard to read | Use code block |
| **Formatting abuse** | Confusing | Use proper emphasis |

---

## 11. Troubleshooting

### 11.1 Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| No syntax highlighting | Missing/wrong language ID | Add correct identifier |
| Code runs off screen | Lines too long | Wrap or shorten |
| Backticks showing | Unclosed fences | Check matching ``` |
| Quote not formatting | Missing `>` on each line | Add `>` to all lines |
| Nested code broken | Improper escaping | Use `~~~` for outer fence |

### 11.2 Escaping Code Fences

To show code fences in documentation:

````markdown
~~~markdown
```python
code here
```
~~~
````

Or use 4 backticks:

`````markdown
````markdown
```python
code here
```
````
`````

### 11.3 Validation Checklist

**Code Blocks**:
- [ ] Language identifier specified
- [ ] Code is syntactically valid
- [ ] Examples are complete and runnable
- [ ] Output comments match actual output
- [ ] Line length ≤ 100 characters

**Quote Blocks**:
- [ ] Every line starts with `>`
- [ ] Purpose is clear (note, warning, etc.)
- [ ] Content is concise
- [ ] Formatting inside quote is correct

**Inline Code**:
- [ ] Used only for code elements
- [ ] Not used for emphasis
- [ ] Backticks properly closed

### 11.4 Editor Tips

| Editor | Feature |
|--------|---------|
| VS Code | Preview panel shows rendered markdown |
| PyCharm | Markdown preview with syntax highlighting |
| GitHub | Preview tab in edit mode |
| Obsidian | Live preview mode |

---

## Related

- `.knowledge/practices/documentation/DOCUMENTATION_STANDARDS.md` — Documentation standards (SSOT)
- `.knowledge/practices/documentation/TABLE_STANDARDS.md` — Table creation standards
- `.knowledge/practices/documentation/DIAGRAM_STANDARDS.md` — Diagram creation standards
- `.knowledge/guidelines/DOCUMENTATION.md` — Documentation guidelines

---

*AI Collaboration Knowledge Base*
