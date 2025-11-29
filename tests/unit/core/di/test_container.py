"""Tests for sage.core.di.container module."""

import pytest

from sage.core.di import Lifetime
from sage.core.di.container import DIContainer, DIScope


class TestDIContainer:
    """Test cases for DIContainer class."""

    def test_container_creation(self) -> None:
        """Test that DIContainer can be instantiated."""
        container = DIContainer()
        assert container is not None

    def test_register_singleton(self) -> None:
        """Test registering a singleton service."""
        container = DIContainer()

        class TestService:
            pass

        container.register(TestService, lifetime=Lifetime.SINGLETON)
        instance1 = container.resolve(TestService)
        instance2 = container.resolve(TestService)

        assert instance1 is instance2

    def test_register_transient(self) -> None:
        """Test registering a transient service."""
        container = DIContainer()

        class TestService:
            pass

        container.register(TestService, lifetime=Lifetime.TRANSIENT)
        instance1 = container.resolve(TestService)
        instance2 = container.resolve(TestService)

        assert instance1 is not instance2

    def test_resolve_unregistered_raises(self) -> None:
        """Test that resolving unregistered service raises error."""
        container = DIContainer()

        class UnregisteredService:
            pass

        with pytest.raises(Exception):  # Adjust exception type as needed
            container.resolve(UnregisteredService)


class TestDIScope:
    """Test cases for DIScope class."""

    def test_scope_creation(self) -> None:
        """Test that DIScope can be created from container."""
        container = DIContainer()
        scope = container.create_scope("test-scope")
        assert isinstance(scope, DIScope)

    def test_scoped_lifetime(self) -> None:
        """Test that scoped services are same within scope."""
        container = DIContainer()

        class ScopedService:
            pass

        container.register(ScopedService, lifetime=Lifetime.SCOPED)

        with container.create_scope("test-scope") as scope:
            instance1 = scope.resolve(ScopedService)
            instance2 = scope.resolve(ScopedService)
            assert instance1 is instance2
