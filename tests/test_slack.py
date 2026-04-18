import time
import hmac
import hashlib
from src.slack.verify import verify_slack_signature

def test_slack_verify():
    secret = "slack_sec"
    body = b"foo=bar"
    ts = str(int(time.time()))
    base = f"v0:{ts}:".encode() + body
    sig = "v0=" + hmac.new(secret.encode(), base, hashlib.sha256).hexdigest()
    assert verify_slack_signature(body, ts, sig, secret) is True
    assert verify_slack_signature(body, ts, "v0=bad", secret) is False
