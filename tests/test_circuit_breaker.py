from src.workers.circuit_breaker import CircuitBreaker

def test_circuit_breaker_flow():
    cb = CircuitBreaker(failure_threshold=2)
    assert cb.can_execute() is True
    cb.record_failure()
    assert cb.can_execute() is True
    cb.record_failure()
    assert cb.state == "OPEN"
    assert cb.can_execute() is False
    cb.record_success()
    assert cb.state == "CLOSED"
