import time
from typing import Any, Optional, Dict

class LruTtlCache:
    def __init__(self, capacity: int = 100, default_ttl_sec: float = 300.0):
        self.capacity = capacity
        self.default_ttl = default_ttl_sec
        self.cache: Dict[str, Any] = {}
        self.expiry: Dict[str, float] = {}

    def get(self, key: str) -> Optional[Any]:
        if key not in self.cache:
            return None
        if time.time() > self.expiry.get(key, 0):
            del self.cache[key]
            del self.expiry[key]
            return None
        return self.cache[key]

    def set(self, key: str, value: Any, ttl_sec: Optional[float] = None) -> None:
        if len(self.cache) >= self.capacity:
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
            self.expiry.pop(oldest_key, None)
        self.cache[key] = value
        self.expiry[key] = time.time() + (ttl_sec or self.default_ttl)
