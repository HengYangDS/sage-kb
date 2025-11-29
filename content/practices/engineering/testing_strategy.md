# Testing Strategy

> **Load Time**: On-demand (~120 tokens)  
> **Purpose**: Universal testing layers, organization, and best practices

---

## 1. Test Pyramid

```
        /\
       /  \        E2E Tests (Few)
      /────\       - End-to-end flows
     /      \      - Slow, high cost
    /────────\     Integration Tests (Some)
   /          \    - Component interactions
  /────────────\   - Medium speed
 /              \  Unit Tests (Many)
/────────────────\ - Single function/class
                   - Fast, low cost
```

### Recommended Ratios

| Test Type         | Ratio | Execution Time |
|-------------------|-------|----------------|
| Unit tests        | 70%   | < 10ms each    |
| Integration tests | 20%   | < 1s each      |
| E2E tests         | 10%   | < 30s each     |

---

## 2. Test Types

### Unit Tests

| Aspect       | Description                  |
|--------------|------------------------------|
| Scope        | Single function/method/class |
| Dependencies | All mocked                   |
| Speed        | Very fast (< 10ms)           |
| Goal         | Logic correctness            |

### Integration Tests

| Aspect       | Description                     |
|--------------|---------------------------------|
| Scope        | Multi-component interaction     |
| Dependencies | Partially real (e.g., database) |
| Speed        | Medium (< 1s)                   |
| Goal         | Interface contracts, data flow  |

### End-to-End Tests (E2E)

| Aspect       | Description                       |
|--------------|-----------------------------------|
| Scope        | Complete user flows               |
| Dependencies | All real                          |
| Speed        | Slow (seconds to tens of seconds) |
| Goal         | Business flow correctness         |

---

## 3. Test Naming

### Naming Convention

```python
def test_function_scenario_expected_result():
    pass


# Examples
def test_calculate_total_empty_cart_returns_zero():
    pass


def test_login_invalid_password_raises_auth_error():
    pass
```

### Test Class Organization

```python
class TestUserService:
    """User service tests"""

    class TestCreate:
        def test_valid_data_creates_user(self): ...

        def test_duplicate_email_raises_error(self): ...

    class TestDelete:
        def test_existing_user_deleted(self): ...

        def test_nonexistent_user_raises_not_found(self): ...
```

---

## 4. Test Structure (AAA)

### Arrange-Act-Assert

```python
def test_add_item_to_cart():
    # Arrange - Setup
    cart = Cart()
    item = Item(id=1, price=100)

    # Act - Execute
    cart.add(item)

    # Assert - Verify
    assert cart.total == 100
    assert len(cart.items) == 1
```

### Given-When-Then (BDD Style)

```python
def test_user_checkout():
    # Given - a user with items in cart
    user = create_user_with_cart_items()

    # When - user completes checkout
    order = checkout_service.process(user)

    # Then - order is created successfully
    assert order.status == "completed"
    assert user.cart.is_empty()
```

---

## 5. Test Data

### Fixtures

```python
@pytest.fixture
def sample_user():
    return User(id=1, name="Test User", email="test@example.com")


@pytest.fixture
def sample_order(sample_user):
    return Order(user=sample_user, items=[])


def test_order_belongs_to_user(sample_order, sample_user):
    assert sample_order.user == sample_user
```

### Factory Pattern

```python
class UserFactory:
    @staticmethod
    def create(**overrides):
        defaults = {
            "name"  : "Test User",
            "email" : "test@example.com",
            "active": True,
        }
        return User(**{**defaults, **overrides})


# Usage
def test_inactive_user_cannot_login():
    user = UserFactory.create(active=False)
    assert not auth_service.can_login(user)
```

---

## 6. Mocking

### When to Mock

| Mock                     | Don't Mock             |
|--------------------------|------------------------|
| External APIs            | Core business logic    |
| Database (in unit tests) | Simple data structures |
| Time/random              | Pure functions         |
| File system              | Tested components      |

### Mock Examples

```python
from unittest.mock import Mock, patch


def test_send_notification():
    # Mock external service
    email_service = Mock()
    email_service.send.return_value = True

    notifier = Notifier(email_service)
    result = notifier.notify("user@example.com", "Hello")

    assert result is True
    email_service.send.assert_called_once()


@patch("app.services.external_api.fetch")
def test_data_fetcher(mock_fetch):
    mock_fetch.return_value = {"data": "test"}
    result = fetch_and_process()
    assert result == "processed: test"
```

---

## 7. Coverage Guidelines

### Coverage Targets

| Code Type           | Target | Reason         |
|---------------------|--------|----------------|
| Core business logic | 95%+   | Critical paths |
| Utilities           | 90%+   | Widely used    |
| API endpoints       | 85%+   | User-facing    |
| Configuration       | 70%+   | Less critical  |

### What to Cover

| Priority | Examples                            |
|----------|-------------------------------------|
| High     | Happy path, error paths, edge cases |
| Medium   | Boundary values, null handling      |
| Low      | Logging, debug code                 |

---

## 8. Test Organization

### Directory Structure

```
tests/
├── conftest.py           # Shared fixtures
├── fixtures/             # Test data files
├── unit/                 # Unit tests
│   ├── test_models.py
│   └── test_utils.py
├── integration/          # Integration tests
│   ├── test_api.py
│   └── test_database.py
└── e2e/                  # End-to-end tests
    └── test_workflows.py
```

### File Naming

| Source File        | Test File               |
|--------------------|-------------------------|
| `models.py`        | `test_models.py`        |
| `services/user.py` | `services/test_user.py` |
| `utils/helpers.py` | `utils/test_helpers.py` |

---

## 9. Quick Checklist

| ✓ Do                       | ✗ Don't                   |
|----------------------------|---------------------------|
| Test one thing per test    | Test multiple behaviors   |
| Use descriptive names      | Use `test_1`, `test_2`    |
| Keep tests independent     | Share state between tests |
| Test edge cases            | Only test happy path      |
| Mock external dependencies | Mock everything           |
| Run tests frequently       | Run only before commit    |

---

## 10. CI Integration

### Pipeline Stages

```yaml
test:
  stages:
    - unit:
        command: pytest tests/unit -v
        timeout: 5m
    - integration:
        command: pytest tests/integration -v
        timeout: 15m
    - e2e:
        command: pytest tests/e2e -v
        timeout: 30m
        only: [ main, release/* ]
```

### Failure Actions

| Stage       | On Failure          |
|-------------|---------------------|
| Unit        | Block merge         |
| Integration | Block merge         |
| E2E         | Notify, investigate |

---

## Related

- `content/practices/engineering/code_review.md` — Code review checklist
- `content/guidelines/python.md` — Python testing specifics
- `content/guidelines/quality.md` — Quality standards

---

*Part of AI Collaboration Knowledge Base*
