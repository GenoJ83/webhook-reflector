from src.workers.pool import WorkerPool

def test_worker_pool_execution():
    pool = WorkerPool()
    pool.submit(lambda x: x * 2, 5)
    pool.submit(lambda x, y: x + y, 3, 7)
    res = pool.run_all()
    assert res == [10, 10]
