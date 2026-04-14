import hmac
import hashlib
import time

def verify_slack_signature(raw_body: bytes, timestamp_header: str, signature_header: str, secret: str) -> bool:
    # Format: v0=a2114d57b48eac39b9ad0eab69602b5137648505c349e11b82e5b8912423788a
    try:
        ts = int(timestamp_header)
        if abs(time.time() - ts) > 300: return False
    except ValueError:
        return False
    sig_basestring = f"v0:{timestamp_header}:".encode("utf-8") + raw_body
    computed = "v0=" + hmac.new(secret.encode("utf-8"), sig_basestring, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed, signature_header)
