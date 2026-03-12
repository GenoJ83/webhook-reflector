import hmac
import hashlib

class HmacVerifier:
    @staticmethod
    def verify_github(raw_body: bytes, signature_header: str, secret: str) -> bool:
        if not signature_header.startswith("sha256="):
            return False
        actual_sig = signature_header.split("sha256=", 1)[1]
        computed = hmac.new(secret.encode("utf-8"), raw_body, hashlib.sha256).hexdigest()
        return hmac.compare_digest(computed, actual_sig)
        
    @staticmethod
    def verify_stripe(raw_body: bytes, signature_header: str, secret: str, timestamp_tolerance: int = 300) -> bool:
        # Header format: t=1492774577,v1=5257a869e7ecebeda32affa62cdca3fa51cad7e77a0e56ff536d0ce8e108d8bd
        items = dict(item.split("=", 1) for item in signature_header.split(",") if "=" in item)
        t_str = items.get("t")
        v1 = items.get("v1")
        if not t_str or not v1:
            return False
        signed_payload = f"{t_str}.".encode("utf-8") + raw_body
        computed = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
        return hmac.compare_digest(computed, v1)
