"""Tests for sage.core.events.bus module."""

import pytest

from sage.core.events.bus import EventBus, Subscription, get_event_bus, reset_event_bus
from sage.core.events.events import Event, EventType


class TestSubscription:
    """Test cases for Subscription class."""

    def test_subscription_creation(self) -> None:
        """Test that Subscription can be created."""
        async def handler(event: Event) -> None:
            pass
        
        sub = Subscription(
            subscription_id="test-sub",
            event_pattern="test.*",
            handler=handler,
        )
        assert sub.subscription_id == "test-sub"
        assert sub.event_pattern == "test.*"

    def test_subscription_matches_exact(self) -> None:
        """Test that subscription matches exact event type."""
        async def handler(event: Event) -> None:
            pass
        
        sub = Subscription(
            subscription_id="test-sub",
            event_pattern="test.created",
            handler=handler,
        )
        assert sub.matches("test.created")
        assert not sub.matches("test.updated")

    def test_subscription_matches_wildcard(self) -> None:
        """Test that subscription matches wildcard pattern."""
        async def handler(event: Event) -> None:
            pass
        
        sub = Subscription(
            subscription_id="test-sub",
            event_pattern="test.*",
            handler=handler,
        )
        assert sub.matches("test.created")
        assert sub.matches("test.updated")
        assert not sub.matches("other.created")


class TestEventBus:
    """Test cases for EventBus class."""

    def setup_method(self) -> None:
        """Reset event bus before each test."""
        reset_event_bus()

    def test_eventbus_creation(self) -> None:
        """Test that EventBus can be instantiated."""
        bus = EventBus()
        assert bus is not None

    def test_subscribe(self) -> None:
        """Test subscribing to events."""
        bus = EventBus()
        
        async def handler(event: Event) -> None:
            pass
        
        sub_id = bus.subscribe("test.*", handler)
        assert sub_id is not None
        assert bus.subscription_count > 0

    def test_unsubscribe(self) -> None:
        """Test unsubscribing from events."""
        bus = EventBus()
        
        async def handler(event: Event) -> None:
            pass
        
        sub_id = bus.subscribe("test.*", handler)
        initial_count = bus.subscription_count
        
        bus.unsubscribe(sub_id)
        assert bus.subscription_count < initial_count

    @pytest.mark.asyncio
    async def test_publish(self) -> None:
        """Test publishing events."""
        bus = EventBus()
        received_events: list[Event] = []
        
        async def handler(event: Event) -> None:
            received_events.append(event)
        
        bus.subscribe("test.created", handler)
        
        event = Event(event_type="test.created", data={"id": 1})
        await bus.publish(event)
        
        assert len(received_events) == 1
        assert received_events[0].event_type == "test.created"

    def test_clear(self) -> None:
        """Test clearing all subscriptions."""
        bus = EventBus()
        
        async def handler(event: Event) -> None:
            pass
        
        bus.subscribe("test.*", handler)
        bus.subscribe("other.*", handler)
        assert bus.subscription_count >= 2
        
        bus.clear()
        assert bus.subscription_count == 0

    def test_get_subscriptions(self) -> None:
        """Test getting subscriptions by pattern."""
        bus = EventBus()
        
        async def handler(event: Event) -> None:
            pass
        
        bus.subscribe("test.created", handler)
        bus.subscribe("test.updated", handler)
        
        subs = bus.get_subscriptions("test.created")
        assert len(subs) >= 1


class TestGetEventBus:
    """Test cases for get_event_bus function."""

    def setup_method(self) -> None:
        """Reset event bus before each test."""
        reset_event_bus()

    def test_get_event_bus_returns_singleton(self) -> None:
        """Test that get_event_bus returns same instance."""
        bus1 = get_event_bus()
        bus2 = get_event_bus()
        assert bus1 is bus2

    def test_reset_event_bus(self) -> None:
        """Test that reset creates new instance."""
        bus1 = get_event_bus()
        reset_event_bus()
        bus2 = get_event_bus()
        assert bus1 is not bus2
