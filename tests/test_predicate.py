from src.filter.predicate import filter_events
from src.core.models import WebhookEvent

def test_filter():
    e1 = WebhookEvent("gh", "push", {}, {"ref": "refs/heads/main"})
    e2 = WebhookEvent("gh", "push", {}, {"ref": "refs/heads/dev"})
    filtered = filter_events([e1, e2], "ref", "refs/heads/main")
    assert len(filtered) == 1 and filtered[0] == e1
