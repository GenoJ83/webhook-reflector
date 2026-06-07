import time
from typing import Callable, Any

def retry_with_backoff(fn: Callable, max_retries: int = 3, initial_delay: float = 0.001, backoff_factor: float = 2.0) -> Any:
    delay = initial_delay
    last_err = None
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except Exception as e:
            last_err = e
            if attempt == max_retries:
                raise last_err
            time.sleep(delay)
            delay *= backoff_factor
