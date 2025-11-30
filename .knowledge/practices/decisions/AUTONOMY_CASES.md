# Autonomy Decision Cases

> Concrete examples for autonomy level decisions

---

## Table of Contents

- [1. Code Changes](#1-code-changes)
- [2. File Operations](#2-file-operations)
- [3. Documentation](#3-documentation)
- [4. Testing](#4-testing)
- [5. Infrastructure](#5-infrastructure)
- [6. Decision Matrix](#6-decision-matrix)
- [7. Concrete Scenario Examples](#7-concrete-scenario-examples)
- [8. Override Conditions](#8-override-conditions)

---

## 1. Code Changes

| Change Type       | Level | Rationale           |
|-------------------|-------|---------------------|
| Fix typo          | L5    | Trivial, low risk   |
| Add comment       | L4-L5 | No behavior change  |
| Refactor function | L3-L4 | Moderate complexity |
| Change API        | L2-L3 | Breaking potential  |
| Security fix      | L1-L2 | High impact         |

---

## 2. File Operations

| Operation       | Level | Rationale            |
|-----------------|-------|----------------------|
| Create new file | L4    | Additive, reversible |
| Modify config   | L2-L3 | System impact        |
| Delete file     | L1-L2 | Irreversible         |
| Rename/move     | L3    | Moderate impact      |
| Bulk changes    | L2    | Scale increases risk |

---

## 3. Documentation

| Action          | Level | Rationale         |
|-----------------|-------|-------------------|
| Fix typo        | L5    | Trivial           |
| Update examples | L4    | Low risk          |
| Restructure doc | L3    | Moderate change   |
| Change API docs | L2-L3 | Accuracy critical |
| Delete section  | L2    | Information loss  |

---

## 4. Testing

| Action           | Level | Rationale         |
|------------------|-------|-------------------|
| Add test         | L4-L5 | Additive          |
| Fix failing test | L3-L4 | Improve coverage  |
| Skip test        | L2    | Hiding issues     |
| Delete test      | L1-L2 | Reducing coverage |
| Change test data | L3    | Validity impact   |

---

## 5. Infrastructure

| Action               | Level | Rationale          |
|----------------------|-------|--------------------|
| Update dependency    | L2-L3 | Compatibility risk |
| Change CI config     | L2    | Build impact       |
| Modify deploy script | L1-L2 | Production risk    |
| Update dev config    | L3-L4 | Local only         |
| Database migration   | L1    | Data risk          |

---

## 6. Decision Matrix

| Risk Level | Reversible | Recommended Level |
|------------|------------|-------------------|
| Low        | Yes        | L4-L5             |
| Low        | No         | L3-L4             |
| Medium     | Yes        | L3-L4             |
| Medium     | No         | L2-L3             |
| High       | Yes        | L2-L3             |
| High       | No         | L1-L2             |

---

## 7. Concrete Scenario Examples

### 7.1 L3 vs L4 Boundary Cases

| Scenario | Context | Decision | Level | Rationale |
|----------|---------|----------|:-----:|-----------|
| Refactor utility function | Done 5 times before, good tests | Proceed, report after | L4 | Familiar pattern, safety net |
| Refactor utility function | First time in this codebase | Ask before proceeding | L3 | New context risk |
| Add database index | Read-only, dev environment | Proceed, report after | L4 | Low risk, reversible |
| Add database index | Production, write-heavy table | Ask before proceeding | L3 | Production risk |
| Update npm dependency | Patch version, good CI | Proceed, report after | L4 | Low risk, tested |
| Update npm dependency | Major version, breaking changes | Ask before proceeding | L3 | Breaking potential |

### 7.2 Knowledge Base Operations

| Operation | Context | Level | Rationale |
|-----------|---------|:-----:|-----------|
| Fix typo in .md file | Obvious error | L5 | Trivial, reversible |
| Add new practice doc | Following template | L4 | Additive, established pattern |
| Restructure INDEX.md | Single directory | L3-L4 | Moderate impact |
| Move files between dirs | Multiple files | L3 | Cross-reference impact |
| Delete framework doc | Active references | L1-L2 | High impact, irreversible |
| Update SSOT document | Referenced by many | L2-L3 | Cascading impact |

### 7.3 Real Decision Examples

**Example 1: Bug Fix (L4)**
```
Context: Login button not working on mobile
Action: Fix CSS media query in button.css
Factors: ✓ Clear fix, ✓ Good test coverage, ✓ Isolated change
Decision: L4 - Proceed, report completion
```

**Example 2: New Feature (L3)**
```
Context: Add dark mode support
Action: Implement theme switching
Factors: ✗ First implementation, ✓ Dev environment, ✗ Multiple files
Decision: L3 - Ask before major changes, proceed on routine parts
```

**Example 3: Security Patch (L2)**
```
Context: CVE reported in auth library
Action: Update library version
Factors: ✗ Security sensitive, ✗ Production impact, ✓ Patch available
Decision: L2 - Detailed review before proceeding
```

---

## 8. Override Conditions

### 8.1 Force Lower Level

| Condition          | Action          |
|--------------------|-----------------|
| Production system  | -1 to -2 levels |
| Security sensitive | L1-L2 max       |
| Irreversible       | -1 level        |
| Unfamiliar domain  | -1 level        |

### 8.2 Allow Higher Level

| Condition           | Action       |
|---------------------|--------------|
| Sandbox/dev         | +1 level     |
| Well-tested pattern | +1 level     |
| Explicit permission | As specified |

---

## Related

- `.knowledge/frameworks/autonomy/LEVELS.md` — Full autonomy framework
- `.knowledge/guidelines/AI_COLLABORATION.md` — Collaboration patterns

---

*Autonomy Decision Cases v1.1*
*Updated: 2025-12-01 - Added concrete scenario examples (§7)*

---

*AI Collaboration Knowledge Base*
