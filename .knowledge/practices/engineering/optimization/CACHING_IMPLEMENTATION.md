# Caching Implementation

> Code implementations for caching patterns

---

## Table of Contents

- [1. Caching Strategy Implementations](#1-caching-strategy-implementations)
- [2. Cache Invalidation](#2-cache-invalidation)
- [3. Advanced Patterns](#3-advanced-patterns)
- [4. Distributed Caching](#4-distributed-caching)

---

## 1. Caching Strategy Implementations

### 1.1 Cache-Aside (Lazy Loading)

```python
class CacheAsidePattern:
    """Cache-aside (lazy loading) pattern."""
    
    def __init__(self, cache, database):
        self.cache = cache
        self.db = database
    
    async def get(self, key: str):
        # 1. Check cache
        value = await self.cache.get(key)
        if value is not None:
            return value
        
        # 2. Cache miss - query database
        value = await self.db.get(key)
        if value is not None:
            # 3. Populate cache
            await self.cache.set(key, value, ttl=3600)
        
        return value
    
    async def update(self, key: str, value):
        # Update database
        await self.db.update(key, value)
        # Invalidate cache
        await self.cache.delete(key)
```

### 1.2 Read-Through

```python
class ReadThroughCache:
    """Read-through caching pattern."""
    
    def __init__(self, cache, loader):
        self.cache = cache
        self.loader = loader  # Database/API client
    
    async def get(self, key: str):
        # Cache handles loading automatically
        value = await self.cache.get(key)
        if value is None:
            value = await self.loader(key)
            if value is not None:
                await self.cache.set(key, value)
        return value
```

### 1.3 Write-Through

```python
class WriteThroughCache:
    """Write-through caching pattern."""
    
    def __init__(self, cache, database):
        self.cache = cache
        self.db = database
    
    async def write(self, key: str, value):
        # Write to both synchronously
        await self.db.write(key, value)
        await self.cache.set(key, value)
        # Both succeed or operation fails
```

### 1.4 Write-Behind (Write-Back)

```python
import asyncio
from collections import deque

class WriteBehindCache:
    """Write-behind (async) caching pattern."""
    
    def __init__(self, cache, database, flush_interval: int = 5):
        self.cache = cache
        self.db = database
        self.write_queue = deque()
        self.flush_interval = flush_interval
        self._start_flusher()
    
    def _start_flusher(self):
        asyncio.create_task(self._flush_loop())
    
    async def _flush_loop(self):
        while True:
            await asyncio.sleep(self.flush_interval)
            await self._flush()
    
    async def _flush(self):
        while self.write_queue:
            key, value = self.write_queue.popleft()
            await self.db.write(key, value)
    
    async def write(self, key: str, value):
        # Write to cache immediately
        await self.cache.set(key, value)
        # Queue for async database write
        self.write_queue.append((key, value))
```

---

## 2. Cache Invalidation

### 2.1 TTL-Based Invalidation

```python
# Simple TTL
await cache.set("user:123", user_data, ttl=3600)  # 1 hour

# Staggered TTL to prevent thundering herd
import random

base_ttl = 3600
jitter = random.randint(-300, 300)  # ±5 minutes
await cache.set("user:123", user_data, ttl=base_ttl + jitter)
```

### 2.2 Event-Driven Invalidation

```python
class EventDrivenCache:
    """Cache with event-driven invalidation."""
    
    def __init__(self, cache, event_bus):
        self.cache = cache
        event_bus.subscribe("user.updated", self._on_user_updated)
        event_bus.subscribe("user.deleted", self._on_user_deleted)
    
    async def _on_user_updated(self, event):
        user_id = event.data["user_id"]
        await self.cache.delete(f"user:{user_id}")
        # Also invalidate related caches
        await self.cache.delete(f"user_profile:{user_id}")
    
    async def _on_user_deleted(self, event):
        user_id = event.data["user_id"]
        # Delete all related cache entries
        pattern = f"*:{user_id}:*"
        await self.cache.delete_pattern(pattern)
```

### 2.3 Version-Based Invalidation

```python
class VersionedCache:
    """Cache with version-based invalidation."""
    
    def __init__(self, cache):
        self.cache = cache
    
    async def get(self, key: str, version: int):
        cached = await self.cache.get(key)
        if cached and cached.get("version") == version:
            return cached["data"]
        return None
    
    async def set(self, key: str, data, version: int):
        await self.cache.set(key, {
            "data": data,
            "version": version
        })
```

---

## 3. Advanced Patterns

### 3.1 Decorator Pattern

```python
from functools import wraps
from typing import Callable

def cached(ttl: int = 3600, key_prefix: str = ""):
    """Caching decorator."""
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = f"{key_prefix}:{func.__name__}:{hash((args, tuple(kwargs.items())))}"
            
            # Check cache
            cached_value = await cache.get(cache_key)
            if cached_value is not None:
                return cached_value
            
            # Execute function
            result = await func(*args, **kwargs)
            
            # Cache result
            await cache.set(cache_key, result, ttl=ttl)
            return result
        return wrapper
    return decorator

# Usage
@cached(ttl=3600, key_prefix="users")
async def get_user(user_id: str):
    return await db.get_user(user_id)
```

### 3.2 Cache-Stampede Prevention

```python
import asyncio
from typing import Dict, Any, Callable

class StampedeProtectedCache:
    """Cache with stampede prevention using locks."""
    
    def __init__(self, cache):
        self.cache = cache
        self.locks: Dict[str, asyncio.Lock] = {}
    
    async def get_or_set(
        self,
        key: str,
        loader: Callable,
        ttl: int = 3600
    ) -> Any:
        # Check cache first
        value = await self.cache.get(key)
        if value is not None:
            return value
        
        # Get or create lock for this key
        if key not in self.locks:
            self.locks[key] = asyncio.Lock()
        
        async with self.locks[key]:
            # Double-check after acquiring lock
            value = await self.cache.get(key)
            if value is not None:
                return value
            
            # Load and cache
            value = await loader()
            await self.cache.set(key, value, ttl=ttl)
            return value
```

### 3.3 Multi-Level Caching

```python
class MultiLevelCache:
    """L1 (local) + L2 (distributed) cache."""
    
    def __init__(self, l1_cache, l2_cache):
        self.l1 = l1_cache  # In-memory (fast, small)
        self.l2 = l2_cache  # Redis (slower, large)
    
    async def get(self, key: str):
        # Check L1 first
        value = self.l1.get(key)
        if value is not None:
            return value
        
        # Check L2
        value = await self.l2.get(key)
        if value is not None:
            # Populate L1
            self.l1.set(key, value, ttl=60)  # Short L1 TTL
            return value
        
        return None
    
    async def set(self, key: str, value, ttl: int = 3600):
        # Set in both levels
        self.l1.set(key, value, ttl=min(ttl, 60))
        await self.l2.set(key, value, ttl=ttl)
    
    async def delete(self, key: str):
        self.l1.delete(key)
        await self.l2.delete(key)
```

---

## 4. Distributed Caching

### 4.1 Redis Cache Implementation

```python
import redis.asyncio as redis
from typing import Optional, Callable

class RedisCache:
    """Redis-based distributed cache."""
    
    def __init__(self, url: str = "redis://localhost:6379"):
        self.redis = redis.from_url(url)
    
    async def get(self, key: str) -> Optional[str]:
        return await self.redis.get(key)
    
    async def set(
        self,
        key: str,
        value: str,
        ttl: int = 3600
    ) -> None:
        await self.redis.set(key, value, ex=ttl)
    
    async def delete(self, key: str) -> None:
        await self.redis.delete(key)
    
    async def get_or_set(
        self,
        key: str,
        loader: Callable,
        ttl: int = 3600
    ) -> str:
        """Atomic get-or-set with Lua script."""
        script = """
        local value = redis.call('GET', KEYS[1])
        if value then
            return value
        end
        return nil
        """
        value = await self.redis.eval(script, 1, key)
        if value is None:
            value = await loader()
            await self.set(key, value, ttl)
        return value
```

### 4.2 Redis Configuration

```python
# Redis eviction policy configuration
# In redis.conf or via CONFIG SET
# maxmemory-policy allkeys-lru
```

### 4.3 Cache Key Patterns

```python
# Good cache keys
"user:123"                    # Type:ID
"user:123:profile"            # Type:ID:Subtype
"api:v2:users:list:page:1"    # Versioned, descriptive

# Bad cache keys
"u123"                        # Unclear
user_data                     # No structure
"user_123_profile_data_v2"    # Inconsistent format
```

---

## Related

- `.knowledge/frameworks/performance/CACHING_PATTERNS.md` — Caching theory and strategies
- `.knowledge/frameworks/performance/OPTIMIZATION_STRATEGIES.md` — General optimization
- `.knowledge/practices/engineering/optimization/OPTIMIZATION_RECIPES.md` — Other optimization recipes

---

*AI Collaboration Knowledge Base*
