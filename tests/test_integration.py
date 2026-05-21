from src.reflector import WebhookReflector
from src.reporter.log import EventReporter
from src.export.har import export_har_entries

def test_full_reflector_lifecycle():
    reflector = WebhookReflector()
    e = reflector.ingest("github", "workflow_run", {"X-Hub-Signature-256": "sha256=dummy"}, {"status": "completed"}, b'{"status": "completed"}')
    assert len(reflector.journal.events) == 1
    table = EventReporter.format_log(reflector.journal.events)
    assert "workflow_run" in table
    har = export_har_entries(reflector.journal.events)
    assert "workflow_run" in har
