from src.reporter.log import EventReporter
from src.core.models import WebhookEvent

def test_event_log_formatting():
    e = WebhookEvent("github", "issue_comment", {}, {}, verified=True)
    txt = EventReporter.format_log([e])
    assert "PROVIDER" in txt
    assert "issue_comment" in txt
    assert "VERIFIED" in txt
