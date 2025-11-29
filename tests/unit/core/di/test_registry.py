"""Tests for sage.core.di.registry module."""

from sage.core.di.registry import TypeRegistry, get_registry


class TestTypeRegistry:
    """Test cases for TypeRegistry class."""

    def setup_method(self) -> None:
        """Reset registry before each test."""
        TypeRegistry.reset_instance()

    def test_registry_creation(self) -> None:
        """Test that TypeRegistry can be instantiated."""
        registry = TypeRegistry()
        assert registry is not None

    def test_singleton_instance(self) -> None:
        """Test that get_instance returns singleton."""
        instance1 = TypeRegistry.get_instance()
        instance2 = TypeRegistry.get_instance()
        assert instance1 is instance2

    def test_register_type(self) -> None:
        """Test registering a type in the registry."""
        registry = TypeRegistry()

        class TestService:
            pass

        registry.register("test_service", TestService)
        assert registry.is_registered("test_service")

    def test_register_factory(self) -> None:
        """Test registering a factory function."""
        registry = TypeRegistry()

        def create_service() -> dict:
            return {"name": "test"}

        registry.register_factory("service_factory", create_service)
        assert registry.is_registered("service_factory")

    def test_resolve_type(self) -> None:
        """Test resolving a registered type."""
        registry = TypeRegistry()

        class TestService:
            pass

        registry.register_type("test_service", TestService)
        resolved = registry.resolve("test_service")
        assert isinstance(resolved, TestService)

    def test_is_registered_false(self) -> None:
        """Test that unregistered name returns False."""
        registry = TypeRegistry()
        assert not registry.is_registered("unregistered_service")

    def test_get_all_types(self) -> None:
        """Test getting all registered types."""
        registry = TypeRegistry()

        class Service1:
            pass

        class Service2:
            pass

        registry.register_type("service1", Service1)
        registry.register_type("service2", Service2)

        all_types = registry.get_all_types()
        assert "service1" in all_types
        assert "service2" in all_types

    def test_clear_registry(self) -> None:
        """Test clearing the registry."""
        registry = TypeRegistry()

        class TestService:
            pass

        registry.register_type("test_service", TestService)
        assert registry.is_registered("test_service")

        registry.clear()
        assert not registry.is_registered("test_service")


class TestGetRegistry:
    """Test cases for get_registry function."""

    def setup_method(self) -> None:
        """Reset registry before each test."""
        TypeRegistry.reset_instance()

    def test_get_registry_returns_instance(self) -> None:
        """Test that get_registry returns a TypeRegistry instance."""
        registry = get_registry()
        assert isinstance(registry, TypeRegistry)
