# Code Review Checklist

> **Load Time**: On-demand (~130 tokens)  
> **Purpose**: Universal code review checkpoints and best practices

---

## 1. Review Principles

| Principle | Description |
|-----------|-------------|
| **Constructive** | Provide improvement suggestions, not just point out problems |
| **Specific** | Reference specific code lines, avoid vague criticism |
| **Prioritized** | Distinguish must-fix from suggestions |
| **Respectful** | Focus on code not person, maintain professionalism |

---

## 2. Correctness Checks

| Item | Focus Areas |
|------|-------------|
| Logic correct | Edge cases, null handling, loop termination |
| Type safe | Complete type annotations, static checks pass |
| Exception handling | Catch specific exceptions, provide fallbacks |
| Resource management | File close, connection release, memory leaks |
| Concurrency safe | Race conditions, deadlocks, data consistency |

---

## 3. Readability Checks

| Item | Standard |
|------|----------|
| Clear naming | Variable/function names are self-explanatory |
| Function length | ≤50 lines (single responsibility) |
| File length | ≤500 lines (consider splitting) |
| Nesting depth | ≤3 levels |
| Appropriate comments | Explain "why" not "what" |

---

## 4. Consistency Checks

| Item | Standard |
|------|----------|
| Code style | Follows project formatting tools |
| Naming conventions | Consistent snake_case / PascalCase |
| Import order | Standard lib → Third party → Local |
| Project patterns | Follows existing code patterns |
| Error handling | Unified error handling approach |

---

## 5. Performance Checks

| Item | Focus Areas |
|------|-------------|
| Timeout protection | I/O operations have timeout settings |
| Cache usage | Repeated computations are cached |
| Batch operations | Avoid N+1 query problems |
| Memory efficiency | Large datasets processed in batches |
| Algorithm complexity | Avoid unnecessary O(n²) |

---

## 6. Security Checks

| Item | Risk |
|------|------|
| Input validation | SQL/command injection |
| Sensitive info | Keys/passwords leaked in logs |
| Path handling | Directory traversal attacks |
| Dependency versions | Known security vulnerabilities |
| Permission checks | Unauthorized access |

---

## 7. Testing Checks

| Item | Standard |
|------|----------|
| Test coverage | New code has corresponding tests |
| Boundary tests | Null, extreme values, exceptional input |
| Test isolation | No external service dependencies |
| Test naming | `test_<function>_<scenario>` |
| Test readability | Test intent is clear |

---

## 8. Documentation Checks

| Item | Requirement |
|------|-------------|
| Function docs | Public functions have docstrings |
| Type annotations | Parameters and return values typed |
| README | New features documented |
| CHANGELOG | Change records updated |
| API docs | Interface changes synchronized |

---

## 9. AI-Generated Code Review

### Special Focus Areas

| Item | Common Issues |
|------|---------------|
| Hallucinated code | Calls to non-existent APIs or methods |
| Over-engineering | Unnecessary abstractions and complexity |
| Style deviation | Inconsistent with project existing style |
| Missing tests | Implementation only, no tests |
| Hardcoded values | Values that should come from config |
| Copyright issues | Copied code snippets |

---

## 10. Feedback Templates

### Must Fix (MUST)

```
🔴 MUST [file:line]
Issue: [specific problem description]
Suggestion: [fix approach]
```

### Should Improve (SHOULD)

```
🟡 SHOULD [file:line]
Issue: [problem description]
Suggestion: [improvement approach]
```

### Could Enhance (COULD)

```
🟢 COULD [file:line]
Suggestion: [enhancement idea]
```

---

## 11. Quick Checklists

### Pre-Commit Self-Check

- [ ] Code formatting passes
- [ ] Static type checking passes
- [ ] All tests pass
- [ ] No hardcoded sensitive info
- [ ] Documentation updated

### Reviewer Checklist

- [ ] Understand change purpose
- [ ] Verify logic correctness
- [ ] Check edge cases
- [ ] Confirm test coverage
- [ ] Check documentation completeness

---

## Related

- `content/guidelines/code_style.md` — Code style guidelines
- `content/practices/engineering/testing_strategy.md` — Testing strategy
- `content/practices/engineering/error_handling.md` — Error handling

---

*Part of AI Collaboration Knowledge Base*
