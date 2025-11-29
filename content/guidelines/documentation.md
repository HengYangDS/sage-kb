# Documentation Guidelines

> Clear, maintainable, useful documentation

---

## 4.1 Documentation Philosophy

**Core Principles**: Accuracy · Clarity · Completeness · Accessibility

**信达雅 Applied**: 信 (accurate, no misleading) · 达 (clear structure) · 雅 (well-formatted, consistent)

---

## 4.2 Documentation Types

### README.md Structure

```
# Project Name → Brief description
## Features → Key features list
## Quick Start → Install + basic usage
## Installation → Detailed steps
## Usage → Common patterns + examples
## Configuration → Options + env vars
## Contributing → How to contribute
## License → License info
```

### API Documentation (Google Style)

```python
def fetch_user(user_id: str, include_profile: bool = False) -> User:
    """Fetch a user by unique identifier.
    
    Args:
        user_id: Unique identifier (UUID format).
        include_profile: If True, includes profile data.
        
    Returns:
        User object with requested data.
        
    Raises:
        UserNotFoundError: If no user matches ID.
    """
```

---

## 4.3 Code Comments

### When to Comment

| Scenario | Example |
|----------|---------|
| Complex algorithm | `# Using Dijkstra's for shortest path` |
| Non-obvious decision | `# JSON preferred for browser compat` |
| Workaround | `# HACK: API bug requires retry` |
| Public API | Full docstring |

### When NOT to Comment

```python
# ❌ Obvious
counter = 0  # Initialize counter

# ✅ Self-documenting
user_count = 0
```

---

## 4.4 Changelog Format

```markdown
## [Unreleased]
### Added / Changed / Deprecated / Removed / Fixed / Security

## [2.0.0] - 2024-01-15
### Added
- Major new feature
### Changed
- Breaking change (migration guide: ...)
```

---

## 4.5 Architecture Decision Record (ADR)

```markdown
# ADR-001: [Title]
## Status: Accepted/Rejected/Superseded
## Context: [Problem/need]
## Decision: [What we chose]
## Consequences: [Positive] · [Negative] · [Risks]
```

---

## 4.6 Documentation Maintenance

**Keep Current**: Update with code changes · Review in code review · Test examples · Remove outdated

**Debt Signs**: Outdated examples · Missing docs · Inconsistent terminology · Broken links

---

## 4.7 Quick Reference

### Markdown Best Practices

| Element | Usage |
|---------|-------|
| `# H1` | Document title only |
| `## H2` | Major sections |
| `### H3` | Subsections |
| `` `code` `` | Inline code, filenames |
| `**bold**` | Important terms |

### Checklist

✓ README complete · ✓ API docstrings · ✓ Complex code commented · ✓ Changelog maintained · ✓ Examples tested

---

*Part of SAGE Knowledge Base*
