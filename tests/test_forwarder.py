from src.forwarder.dispatcher import WebhookDispatcher
from src.core.models import WebhookEvent

def test_dispatcher():
    disp = WebhookDispatcher("http://localhost:8000/webhook")
    e = WebhookEvent("github", "push", {}, {})
    res = disp.forward(e)
    assert res["status"] == "FORWARDED"
    assert res["destination"] == "http://localhost:8000/webhook"
