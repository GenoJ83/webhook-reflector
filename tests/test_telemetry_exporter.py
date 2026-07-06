from src.metrics.telemetry_exporter import TelemetryCollector

def test_telemetry_collector():
    col = TelemetryCollector()
    col.increment("requests_total", 5)
    col.set_gauge("memory_usage_mb", 256.5)
    prom = col.to_prometheus()
    assert "requests_total 5" in prom
    assert "memory_usage_mb 256.5" in prom
