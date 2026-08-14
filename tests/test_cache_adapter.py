from src.plugins.cache_adapter import LruTtlCache

def test_lru_cache():
    cache = LruTtlCache(capacity=2)
    cache.set("a", 1)
    cache.set("b", 2)
    assert cache.get("a") == 1
    cache.set("c", 3)
    assert len(cache.cache) == 2
