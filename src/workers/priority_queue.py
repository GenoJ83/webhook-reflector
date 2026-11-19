import heapq
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedTask:
    priority: int
    task: Any = field(compare=False)

class PriorityTaskQueue:
    def __init__(self):
        self._heap = []

    def push(self, task: Any, priority: int = 10) -> None:
        heapq.heappush(self._heap, PrioritizedTask(priority=priority, task=task))

    def pop(self) -> Any:
        if not self._heap:
            raise IndexError("Queue is empty")
        return heapq.heappop(self._heap).task

    def __len__(self) -> int:
        return len(self._heap)
