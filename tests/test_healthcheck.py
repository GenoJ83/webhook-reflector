from src.metrics.healthcheck import ComponentHealthCheck

def test_healthcheck():
    hc = ComponentHealthCheck()
    assert hc.get_aggregate_status() == "HEALTHY"
    hc.register_check("database", True)
    hc.register_check("cache", False)
    assert hc.get_aggregate_status() == "DEGRADED"
    hc.register_check("database", False)
    assert hc.get_aggregate_status() == "UNHEALTHY"
