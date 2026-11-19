import pytest
from src.workers.retry import retry_with_backoff

def test_retry_success_after_failure():
    attempts = [0]
    def flaky():
        attempts[0] += 1
        if attempts[0] < 3:
            raise ValueError("temporary error")
        return "success"
    res = retry_with_backoff(flaky, max_retries=3)
    assert res == "success"
    assert attempts[0] == 3

def test_retry_exhaustion():
    def always_fail():
        raise RuntimeError("fatal error")
    with pytest.raises(RuntimeError):
        retry_with_backoff(always_fail, max_retries=2)
