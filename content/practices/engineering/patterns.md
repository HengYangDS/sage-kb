# Engineering Patterns Practice Guide

> **Load Time**: On-demand (~150 tokens)  
> **Purpose**: Common engineering patterns and their practical application

---

## Pattern Quick Reference

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| **Repository** | Abstract data access | Multiple data sources, swappable backends, mock testing |
| **Service Layer** | Encapsulate business logic | Logic spans entities, side effects, transaction mgmt |
| **Factory** | Encapsulate object creation | Complex creation, dynamic type selection |
| **Strategy** | Interchangeable algorithms | Multiple algorithms, runtime selection, avoid conditionals |
| **Observer** | Decoupled notifications | Event-driven, plugin architecture, async processing |
| **Circuit Breaker** | Prevent cascade failures | External services, graceful degradation, self-healing |

---

## Repository Pattern

**Purpose**: Abstract data access from business logic

```python
class Repository(ABC, Generic[T]):
    @abstractmethod
    def get(self, id: str) -> Optional[T]: ...
    @abstractmethod
    def save(self, entity: T) -> T: ...
    @abstractmethod
    def delete(self, id: str) -> bool: ...
    @abstractmethod
    def find_all(self) -> List[T]: ...

class UserRepository(Repository[User]):
    def __init__(self, session: Session):
        self._session = session
    def get(self, id: str) -> Optional[User]:
        return self._session.query(User).get(id)
```

---

## Service Layer Pattern

**Purpose**: Encapsulate business logic separate from presentation/data access

```python
class UserService:
    def __init__(self, repository: UserRepository, email: EmailService, events: EventBus):
        self._repo, self._email, self._events = repository, email, events
    
    def register(self, data: UserCreate) -> User:
        if self._repo.find_by_email(data.email):
            raise EmailAlreadyExistsError(data.email)
        user = self._repo.save(User(email=data.email, password_hash=hash(data.password)))
        self._email.send_welcome(user)
        self._events.publish(UserRegistered(user.id))
        return user
```

---

## Factory Pattern

**Purpose**: Encapsulate object creation logic

```python
class HandlerFactory:
    _handlers: Dict[str, Type[Handler]] = {}
    
    @classmethod
    def register(cls, msg_type: str):
        def decorator(handler_cls):
            cls._handlers[msg_type] = handler_cls
            return handler_cls
        return decorator
    
    @classmethod
    def create(cls, msg_type: str, **kwargs) -> Handler:
        return cls._handlers[msg_type](**kwargs)

@HandlerFactory.register("order.created")
class OrderCreatedHandler(Handler): ...
```

---

## Strategy Pattern

**Purpose**: Define interchangeable algorithms

```python
class PricingStrategy(Protocol):
    def calculate(self, base_price: float, quantity: int) -> float: ...

class RegularPricing:
    def calculate(self, base_price: float, quantity: int) -> float:
        return base_price * quantity

class BulkPricing:
    def __init__(self, threshold: int, discount: float):
        self.threshold, self.discount = threshold, discount
    def calculate(self, base_price: float, quantity: int) -> float:
        return base_price * quantity * (1 - self.discount if quantity >= self.threshold else 1)

class Order:
    def __init__(self, pricing: PricingStrategy):
        self._pricing = pricing
```

---

## Observer Pattern

**Purpose**: One-to-many dependency with decoupled notifications

```python
class EventBus:
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}
    
    def subscribe(self, event_type: str, handler: Callable) -> None:
        self._subscribers.setdefault(event_type, []).append(handler)
    
    def publish(self, event_type: str, data: Any) -> None:
        for handler in self._subscribers.get(event_type, []):
            handler(data)

# Usage: event_bus.subscribe("user.created", send_email)
```

---

## Circuit Breaker Pattern

**Purpose**: Prevent cascading failures by failing fast

```python
class CircuitState(Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing fast
    HALF_OPEN = "half_open"  # Testing recovery

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 30):
        self.threshold, self.timeout = failure_threshold, recovery_timeout
        self.failures, self.state = 0, CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            raise CircuitOpenError("Circuit is open")
        try:
            result = func(*args, **kwargs)
            self.failures, self.state = 0, CircuitState.CLOSED
            return result
        except Exception:
            self.failures += 1
            if self.failures >= self.threshold:
                self.state = CircuitState.OPEN
            raise
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| God Object | Does everything | Split responsibilities |
| Anemic Domain | Logic outside entities | Rich domain models |
| Service Locator | Hidden dependencies | Dependency injection |
| Singleton Overuse | Global state | Scoped instances |

---

## Related

- `content/guidelines/code_style.md` — Code style guidelines
- `content/guidelines/python.md` — Python-specific patterns
- `content/frameworks/design/design_axioms.md` — Design principles

---

*Part of AI Collaboration Knowledge Base*
