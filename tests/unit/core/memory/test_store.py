"""Tests for sage.core.memory.store module."""

import pytest
import tempfile
from pathlib import Path
from typing import Generator

from sage.core.memory.store import (
    MemoryStore,
    MemoryEntry,
    MemoryType,
    MemoryPriority,
)


class TestMemoryType:
    """Test cases for MemoryType enum."""

    def test_memory_types_exist(self) -> None:
        """Test that expected memory types exist."""
        assert MemoryType.CONVERSATION is not None
        assert MemoryType.DECISION is not None
        assert MemoryType.CONTEXT is not None
        assert MemoryType.SUMMARY is not None


class TestMemoryPriority:
    """Test cases for MemoryPriority enum."""

    def test_priority_ordering(self) -> None:
        """Test that priorities are ordered correctly."""
        assert MemoryPriority.LOW < MemoryPriority.NORMAL
        assert MemoryPriority.NORMAL < MemoryPriority.HIGH
        assert MemoryPriority.HIGH < MemoryPriority.CRITICAL


class TestMemoryEntry:
    """Test cases for MemoryEntry class."""

    def test_entry_to_dict(self) -> None:
        """Test converting entry to dictionary."""
        entry = MemoryEntry(
            id="test-id",
            type=MemoryType.CONVERSATION,
            content="Test content",
            priority=MemoryPriority.NORMAL,
        )
        data = entry.to_dict()
        assert data["id"] == "test-id"
        assert data["content"] == "Test content"

    def test_entry_from_dict(self) -> None:
        """Test creating entry from dictionary."""
        data = {
            "id": "test-id",
            "type": "conversation",
            "content": "Test content",
            "priority": 50,
            "tokens": 10,
            "session_id": None,
            "task_id": None,
            "tags": [],
            "metadata": {},
            "created_at": "2025-01-01T00:00:00",
            "updated_at": "2025-01-01T00:00:00",
            "is_summarized": False,
            "summary_of": [],
        }
        entry = MemoryEntry.from_dict(data)
        assert entry.id == "test-id"


class TestMemoryStore:
    """Test cases for MemoryStore class."""

    @pytest.fixture
    def temp_store(self) -> Generator[MemoryStore, None, None]:
        """Create a temporary memory store for testing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            store = MemoryStore(base_path=Path(tmpdir), auto_save=False)
            yield store

    def test_store_creation(self, temp_store: MemoryStore) -> None:
        """Test that MemoryStore can be instantiated."""
        assert temp_store is not None

    def test_add_entry(self, temp_store: MemoryStore) -> None:
        """Test adding an entry to the store."""
        entry = temp_store.add(
            type=MemoryType.CONVERSATION,
            content="Test content",
        )
        assert entry is not None
        assert entry.content == "Test content"

    def test_get_entry(self, temp_store: MemoryStore) -> None:
        """Test getting an entry by ID."""
        added = temp_store.add(
            type=MemoryType.CONVERSATION,
            content="Test content",
        )
        retrieved = temp_store.get(added.id)
        assert retrieved is not None
        assert retrieved.id == added.id

    def test_get_nonexistent_entry(self, temp_store: MemoryStore) -> None:
        """Test getting a nonexistent entry returns None."""
        result = temp_store.get("nonexistent-id")
        assert result is None

    def test_update_entry(self, temp_store: MemoryStore) -> None:
        """Test updating an entry."""
        entry = temp_store.add(
            type=MemoryType.CONVERSATION,
            content="Original content",
        )
        updated = temp_store.update(entry.id, content="Updated content")
        assert updated is not None
        assert updated.content == "Updated content"

    def test_delete_entry(self, temp_store: MemoryStore) -> None:
        """Test deleting an entry."""
        entry = temp_store.add(
            type=MemoryType.CONVERSATION,
            content="Test content",
        )
        result = temp_store.delete(entry.id)
        assert result is True
        assert temp_store.get(entry.id) is None

    def test_query_by_type(self, temp_store: MemoryStore) -> None:
        """Test querying entries by type."""
        temp_store.add(type=MemoryType.CONVERSATION, content="Conv 1")
        temp_store.add(type=MemoryType.DECISION, content="Decision 1")
        
        results = temp_store.query(type=MemoryType.CONVERSATION)
        assert len(results) >= 1

    def test_clear_store(self, temp_store: MemoryStore) -> None:
        """Test clearing the store."""
        temp_store.add(type=MemoryType.CONVERSATION, content="Test 1")
        temp_store.add(type=MemoryType.CONVERSATION, content="Test 2")
        
        temp_store.clear()
        results = temp_store.query()
        assert len(results) == 0

    def test_get_total_tokens(self, temp_store: MemoryStore) -> None:
        """Test getting total token count."""
        temp_store.add(type=MemoryType.CONVERSATION, content="Test", tokens=100)
        temp_store.add(type=MemoryType.CONVERSATION, content="Test", tokens=200)
        
        total = temp_store.get_total_tokens()
        assert total >= 300
