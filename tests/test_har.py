import json
from src.export.har import export_har_entries
from src.core.models import WebhookEvent

def test_har_export():
    e = WebhookEvent("stripe", "payment_intent.succeeded", {}, {"amount": 500})
    out = json.loads(export_har_entries([e]))
    assert len(out) == 1
    assert out[0]["provider"] == "stripe"
