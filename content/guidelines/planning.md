# Planning and Design Guidelines

> Architecture and design principles for sustainable systems

---

## 1.1 Execution Principles

**Think Before Acting**: Understand scope → Plan with milestones → Validate assumptions → Iterate on feedback

**Scope**: ✅ "Implement user auth with JWT" · ❌ "Make the app secure"

**Task Decomposition**: Break into 2-4 hour subtasks · Clear acceptance criteria · Identify dependencies · Track
progress

---

## 1.2 Architecture Patterns

**Layered Architecture**: Presentation (UI/API) → Business Logic (Domain) → Data Access (Repository) → Infrastructure

### SOLID Principles

| Principle | Description           | Example                   |
|-----------|-----------------------|---------------------------|
| **SRP**   | Single Responsibility | One class = one purpose   |
| **OCP**   | Open/Closed           | Extend, don't modify      |
| **LSP**   | Liskov Substitution   | Subtypes substitutable    |
| **ISP**   | Interface Segregation | Small, focused interfaces |
| **DIP**   | Dependency Inversion  | Depend on abstractions    |

---

## 1.3 Modularity Guidelines

```python
# ✅ Clear boundaries, DI
class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def create_user(self, data: UserCreate) -> User:
        return self._repository.save(data)


# ❌ Mixed concerns
class UserService:
    def create_user(self, data):
        conn = sqlite3.connect('db.sqlite')  # Direct DB, email, logging mixed
```

**Dependency Management**: Explicit (constructor) · Interface-based (protocols) · Minimal coupling · Testable (mockable)

---

## 1.4 Design Checklist

| ✓   | Item                              |
|-----|-----------------------------------|
| [ ] | Requirements clear and complete   |
| [ ] | Edge cases identified             |
| [ ] | Error handling strategy defined   |
| [ ] | Performance requirements known    |
| [ ] | Security considerations addressed |
| [ ] | Testing approach determined       |
| [ ] | Documentation plan in place       |

---

## 1.5 Anti-Patterns

| ❌ Anti-Pattern         | Problem                 | ✅ Solution              |
|------------------------|-------------------------|-------------------------|
| God Class              | Does everything         | Split by responsibility |
| Spaghetti Code         | No structure            | Apply SOLID             |
| Premature Optimization | Complexity without need | Profile first           |
| Copy-Paste             | Duplication             | Extract to shared       |
| Magic Numbers          | Unclear intent          | Named constants         |

---

*Part of SAGE Knowledge Base*
