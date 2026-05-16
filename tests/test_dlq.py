from src.retry.dlq import DeadLetterQueue
from src.core.models import WebhookEvent

def test_dlq():
    dlq = DeadLetterQueue()
    e = WebhookEvent("gh", "push", {}, {})
    dlq.push_failed(e)
    assert len(dlq.failed_events) == 1
    popped = dlq.pop_all()
    assert len(popped) == 1 and len(dlq.failed_events) == 0
