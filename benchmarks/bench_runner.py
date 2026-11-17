"""Automated micro-benchmark runner."""
import time
from typing import Callable, Dict, Any

def benchmark_execution(fn: Callable, iterations: int = 100) -> Dict[str, Any]:
    start = time.perf_counter()
    for _ in range(iterations):
        fn()
    elapsed = time.perf_counter() - start
    return {
        "iterations": iterations,
        "total_seconds": round(elapsed, 4),
        "ops_per_second": round(iterations / (elapsed + 1e-8), 2)
    }
