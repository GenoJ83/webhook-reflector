from src.workers.priority_queue import PriorityTaskQueue

def test_priority_queue():
    q = PriorityTaskQueue()
    q.push("low-priority", priority=100)
    q.push("critical", priority=1)
    q.push("medium", priority=50)
    assert len(q) == 3
    assert q.pop() == "critical"
    assert q.pop() == "medium"
    assert q.pop() == "low-priority"
