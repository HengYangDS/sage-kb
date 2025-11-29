# Autonomy Decision Cases

> **Load Time**: On-demand (~150 tokens)  
> **Purpose**: Concrete examples for autonomy level decisions  
> **Reference**: See `frameworks/autonomy/levels.md` for full theory

---

## 1. Code Changes

| Scenario                      | Level | Rationale                               |
|-------------------------------|-------|-----------------------------------------|
| Fix typo in variable name     | L6    | Trivial, no semantic change             |
| Add missing type hints        | L5    | Quality improvement, no behavior change |
| Format code with linter       | L6    | Automated, reversible                   |
| Add docstring                 | L5    | Documentation only                      |
| Remove unused imports         | L5    | Safe cleanup                            |
| Refactor to reduce complexity | L4    | Behavior preserved, tests verify        |
| Add error handling            | L4    | Robustness improvement                  |
| Extract method                | L4    | Standard refactoring                    |
| Update deprecated API         | L3    | May affect behavior                     |
| Change public API signature   | L1    | Breaking change                         |
| Modify business logic         | L2    | Core functionality                      |
| Add new dependency            | L2    | Project-wide impact                     |
| Change database schema        | L1    | Migration required                      |
| Modify auth flow              | L1    | Security critical                       |

---

## 2. Configuration & Infrastructure

| Scenario                  | Level | Rationale                 |
|---------------------------|-------|---------------------------|
| Update .gitignore         | L5    | Low risk, reversible      |
| Add editor config         | L6    | Tooling only              |
| Update linter rules       | L5    | Quality improvement       |
| Update CI pipeline        | L3    | May affect deployment     |
| Modify Docker config      | L3    | Environment impact        |
| Update minor dependencies | L4    | Usually safe              |
| Change production config  | L1    | Live system impact        |
| Modify secrets management | L1    | Security critical         |
| Update major dependencies | L2    | Breaking changes possible |

---

## 3. Documentation

| Scenario                  | Level | Rationale                 |
|---------------------------|-------|---------------------------|
| Fix typos                 | L6    | No semantic change        |
| Update code examples      | L5    | Accuracy improvement      |
| Add README sections       | L5    | Completeness              |
| Format markdown           | L6    | Style only                |
| Rewrite unclear docs      | L4    | May change meaning        |
| Add architecture diagrams | L4    | New content               |
| Update API documentation  | L3    | Must match implementation |
| Change license info       | L1    | Legal implications        |
| Update security docs      | L1    | Critical information      |

---

## 4. Testing

| Scenario                    | Level | Rationale                 |
|-----------------------------|-------|---------------------------|
| Add test for uncovered path | L5    | Improves coverage         |
| Fix flaky test              | L5    | Reliability improvement   |
| Improve test naming         | L6    | Clarity only              |
| Refactor test structure     | L4    | May affect coverage       |
| Add integration test        | L4    | New validation            |
| Update test fixtures        | L3    | May affect multiple tests |
| Remove existing test        | L1    | Reduces coverage          |
| Weaken test assertions      | L1    | May hide bugs             |
| Skip/disable test           | L2    | Technical debt            |

---

## 5. Security & Sensitive Operations

**Always L1** — Requires explicit approval:

Authentication · Authorization · Encryption · Input validation · Password policies · CORS · Rate limiting · Audit
logging

---

## 6. Architecture & Design

| Scenario                   | Level | Rationale             |
|----------------------------|-------|-----------------------|
| Add utility module         | L4    | Isolated addition     |
| Create helper function     | L4    | Reusability           |
| Implement design pattern   | L3    | Structural change     |
| Add internal service       | L3    | Component addition    |
| Change system architecture | L1    | Fundamental design    |
| Add external dependency    | L2    | Long-term maintenance |
| Create new public API      | L1    | Contract commitment   |
| Change data model          | L1    | Schema migration      |

---

## Decision Quick Reference

| Question           | If Yes                        | If No      |
|--------------------|-------------------------------|------------|
| Security-related?  | L1                            | Continue ↓ |
| Breaking change?   | L1-L2                         | Continue ↓ |
| Changes behavior?  | L2-L4 (tests verify → higher) | Continue ↓ |
| Easily reversible? | L5-L6                         | L3-L4      |

---

## Calibration Tips

**Start Conservative** · **Document Decisions** · **Review Periodically** · **Context Matters** · **When in Doubt →
Lower Level**

---

## Project Overrides Example

```yaml
# .junie/autonomy_overrides.yaml
overrides:
  - pattern: "tests/**"
    level: L5  # Trusted test patterns
  - pattern: "src/auth/**"
    level: L1  # Security-critical
```

---

## Related

- `frameworks/autonomy/levels.md` — Full 6-level spectrum
- `guidelines/ai_collaboration.md` — Collaboration patterns
- `templates/expert_committee.md` — Decision prompts
