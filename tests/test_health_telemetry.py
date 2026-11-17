from src.telemetry.health import get_system_diagnostics

def test_system_diagnostics():
    diag = get_system_diagnostics()
    assert diag["status"] == "HEALTHY"
    assert "pid" in diag
    assert "python_version" in diag
