import hmac
import hashlib
from src.crypto.hmac_verify import HmacVerifier

def test_github_verification():
    secret = "gh_secret_123"
    body = b'{"action": "opened"}'
    sig = "sha256=" + hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    assert HmacVerifier.verify_github(body, sig, secret) is True
    assert HmacVerifier.verify_github(body, "sha256=invalid", secret) is False
    
def test_stripe_verification():
    secret = "whsec_abc"
    body = b'{"id": "evt_1"}'
    t = "1700000000"
    sig = hmac.new(secret.encode(), f"{t}.".encode() + body, hashlib.sha256).hexdigest()
    hdr = f"t={t},v1={sig}"
    assert HmacVerifier.verify_stripe(body, hdr, secret) is True
    assert HmacVerifier.verify_stripe(body, f"t={t},v1=bad", secret) is False
