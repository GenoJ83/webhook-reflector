from src.replay.replayer import WebhookReplayer
from src.core.models import WebhookEvent

def test_replayer():
    captured = []
    replayer = WebhookReplayer(lambda e: captured.append(e) or True)
    e = WebhookEvent("github", "ping", {}, {"zen": "Keep it logically awesome."})
    ok = replayer.replay(e)
    assert ok is True and len(captured) == 1
