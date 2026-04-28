from src.stats.throughput import ThroughputTracker

def test_throughput():
    t = ThroughputTracker()
    t.record("github")
    t.record("github")
    t.record("stripe")
    s = t.summary()
    assert s["github"] == 2 and s["stripe"] == 1
