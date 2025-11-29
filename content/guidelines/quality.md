# Quality Assurance Guidelines

> Quality metrics, review processes, continuous improvement

---

## 8.1 Quality Dimensions

| Dimension | Metrics | Target |
|-----------|---------|--------|
| **Correctness** | Test coverage, bug rate | >80% coverage, <1 bug/KLOC |
| **Maintainability** | Complexity, duplication | <10 cyclomatic, <3% duplication |
| **Performance** | Response time, throughput | <200ms P95, >1000 RPS |
| **Security** | Vulnerabilities, audit score | 0 critical, >90% score |
| **Reliability** | Uptime, MTTR | >99.9%, <15min MTTR |

---

## 8.2 Code Review Standards

### Review Checklist

| Category | Items |
|----------|-------|
| **Correctness** | Logic correct · Edge cases · Error handling |
| **Quality** | Style guidelines · No duplication · Clear names |
| **Testing** | New functionality · Edge cases · All pass |
| **Security** | No secrets · Input validation · No injection |
| **Docs** | APIs documented · Complex logic explained |

### Feedback Prefixes

| Prefix | Meaning | Example |
|--------|---------|---------|
| `[REQUIRED]` | Must fix | Security vulnerability |
| `[SUGGESTION]` | Should fix | Better approach |
| `[NIT]` | Nice to have | Style preference |
| `[QUESTION]` | Clarification | Seeking understanding |

---

## 8.3 Testing Strategy

### Coverage Goals

| Type | Target | Focus |
|------|--------|-------|
| Unit | >80% | Business logic |
| Integration | >60% | Component interactions |
| E2E | Critical paths | User journeys |

### Test Quality

```python
# ✅ Clear, focused, AAA pattern
def test_user_creation_with_valid_data():
    service = UserService(mock_repo)  # Arrange
    result = service.create({"name": "Alice"})  # Act
    assert result.name == "Alice"  # Assert

# ❌ Multiple concerns, unclear
def test_user():
    # Tests creation, update, delete all in one
```

---

## 8.4 Quality Gates

| Stage | Requirements |
|-------|--------------|
| **Pre-Commit** | Lint · Format · Type check · Unit tests |
| **Pre-Merge** | All tests · Review approved · Coverage maintained · No vulns · Docs updated |
| **Pre-Release** | E2E pass · Performance OK · Security scan · Changelog · Version bump |

---

## 8.5 Continuous Improvement

**Retrospective**: What went well? · What to improve? · What to try differently?

### Quality Debt

| Category | Priority |
|----------|----------|
| Security (unpatched) | High |
| Technical (missing tests) | Medium |
| Performance (slow query) | Medium |
| Documentation (outdated) | Low |

**Track**: Defect escape rate · MTTR · Review turnaround · Coverage trend · Debt ratio

---

## 8.6 Quality Culture

**Principles**: Everyone's responsibility · Prevention > Detection · Continuous improvement · Measure what matters

### Anti-Patterns

| ❌ Anti-Pattern | ✅ Better |
|----------------|-----------|
| "Ship and fix" | Build quality in |
| "Not my code" | Collective ownership |
| "Tests slow us down" | Tests enable speed |
| "Good enough" | Maintain standards |

---

## 8.7 Quick Reference

| Frequency | Habits |
|-----------|--------|
| **Daily** | Tests before commit · Self-review before PR · Update docs · Address feedback |
| **Weekly** | Coverage reports · Dependency updates · Technical debt · Share learnings |

---

*Part of SAGE Knowledge Base*
