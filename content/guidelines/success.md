# Success Principles Guidelines

> Philosophy mapping, success criteria, holistic excellence

---

## 9.1 Xin-Da-Ya (信达雅) Framework

> **Full Reference**: `content/core/principles.md`

| Principle | Meaning | Application |
|-----------|---------|-------------|
| **信 Xin** | Faithfulness | Accurate, reliable, trustworthy |
| **达 Da** | Clarity | Clear, comprehensible, accessible |
| **雅 Ya** | Elegance | Refined, balanced, harmonious |

**Hierarchy**: 信 (Foundation) → 达 (Build clarity) → 雅 (Refine elegance)

---

## 9.2 Xin (信) - Faithfulness

**Definition**: Code that does exactly what it claims, reliably.

**Checklist**: Behavior matches docs · Edge cases handled · No hidden side effects · Contracts honored

```python
# ✅ HIGH XIN: Clear contract
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# ❌ LOW XIN: Silent failure
def divide(a, b):
    try: return a / b
    except: return 0  # Wrong result silently
```

---

## 9.3 Da (达) - Clarity

**Definition**: Code that communicates intent clearly.

**Checklist**: Names reveal intent · Structure follows logic · Complexity minimized · Flow easy to follow

```python
# ✅ HIGH DA: Clear intent
def calculate_order_total(items: List[Item], discount_percent: float) -> Money:
    subtotal = sum(item.price for item in items)
    return subtotal * (1 - discount_percent / 100)

# ❌ LOW DA: Cryptic
def calc(i, d):
    return sum(x.p for x in i) * (1 - d/100)
```

---

## 9.4 Ya (雅) - Elegance

**Definition**: Code that achieves purpose with grace and balance.

**Checklist**: No unnecessary complexity · Proportional to problem · Consistent · Natural to use

```python
# ✅ HIGH YA: Elegant, proportional
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

# ❌ LOW YA: Over-engineered
class PalindromeChecker:
    def __init__(self, config, preprocessor, comparator): ...
    # 50 lines of unnecessary abstraction
```

---

## 9.5 Shu-Fa-Dao (术法道) Framework

| Level | Meaning | Focus |
|-------|---------|-------|
| **术 Shu** | Technique | Syntax, patterns, tools, best practices |
| **法 Fa** | Method | Why patterns exist, trade-offs, strategies |
| **道 Dao** | Way | Simplicity, clarity, sustainability, value |

**Progression**: Learn Shu → Understand Fa → Embody Dao

---

## 9.6 Success Criteria Matrix

### Project Success

| Dimension | Criteria | Measure |
|-----------|----------|---------|
| Functional | Does it work? | Tests pass, requirements met |
| Technical | Well-built? | Code quality metrics |
| Process | Efficient? | Time, resources used |
| Learning | Did we grow? | Skills gained, shared |

### Code Success

| Criterion | Question | Indicator |
|-----------|----------|-----------|
| Correct | Right thing? | Tests, validation |
| Clear | Understandable? | Review feedback |
| Maintainable | Can evolve? | Change cost |
| Performant | Fast enough? | Benchmarks |

---

## 9.7 Trade-offs

> "The best solution balances competing concerns for the context."

| Trade-off | Lean A When | Lean B When |
|-----------|-------------|-------------|
| Speed vs Quality | Prototype | Production |
| Simple vs Flexible | Clear requirements | Uncertain future |
| DRY vs Clarity | Pattern stable | Abstraction obscures |
| Performance vs Readability | Proven bottleneck | General code |

**Framework**: Identify trade-off → Understand context → Choose → Document → Revisit

---

## 9.8 Quick Reference

| Phase | Checklist |
|-------|-----------|
| **Before** | Success criteria · Trade-offs · Priorities |
| **During** | 信 Correct? · 达 Clear? · 雅 Elegant? |
| **After** | Criteria met? · Learnings? · Improvements? |

---

*Part of SAGE Knowledge Base*
