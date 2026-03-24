from src.journal.event_log import WebhookJournal
from src.core.models import WebhookEvent

def test_journal_recording():
    j = WebhookJournal(capacity=2)
    e1 = WebhookEvent("github", "push", {}, {})
    e2 = WebhookEvent("stripe", "charge", {}, {})
    e3 = WebhookEvent("slack", "event", {}, {})
    j.record(e1)
    j.record(e2)
    j.record(e3)
    assert len(j.events) == 2
    assert j.get_by_id(e1.id) is None
    assert len(j.filter_by_provider("stripe")) == 1
