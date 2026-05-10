from src.metrics.prom import to_prometheus

def test_metrics():
    m = to_prometheus({"github": 10, "stripe": 5})
    assert 'provider="github"} 10' in m
    assert 'provider="stripe"} 5' in m
