from typing import Callable, Any, List
import queue

class WorkerPool:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self.queue = queue.Queue()

    def submit(self, fn: Callable, *args, **kwargs) -> None:
        self.queue.put((fn, args, kwargs))

    def run_all(self) -> List[Any]:
        results = []
        while not self.queue.empty():
            fn, args, kwargs = self.queue.get()
            results.append(fn(*args, **kwargs))
        return results
