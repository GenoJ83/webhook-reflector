from src.reflector import WebhookReflector

def test_reflector_ingest():
    reflector = WebhookReflector()
    e = reflector.ingest("slack", "app_mention", {}, {"text": "hello"}, b'{"text": "hello"}')
    assert e.verified is True
    assert len(reflector.journal.events) == 1
