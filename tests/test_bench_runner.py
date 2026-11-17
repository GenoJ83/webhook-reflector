from benchmarks.bench_runner import benchmark_execution

def test_benchmark_runner():
    res = benchmark_execution(lambda: sum(range(50)), iterations=25)
    assert res["iterations"] == 25
    assert res["total_seconds"] >= 0.0
    assert res["ops_per_second"] > 0
