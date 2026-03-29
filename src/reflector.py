from typing import Dict, Any, Optional
from src.core.models import WebhookEvent
from src.crypto.hmac_verify import HmacVerifier
from src.journal.event_log import WebhookJournal
from src.replay.replayer import WebhookReplayer

class WebhookReflector:
    def __init__(self, secret: str = ""):
        self.secret = secret
        self.journal = WebhookJournal()
        self.replayer = WebhookReplayer()
        
    def ingest(self, provider: str, event_type: str, headers: Dict[str, str], payload: Dict[str, Any], raw_body: bytes) -> WebhookEvent:
        verified = False
        if provider.lower() == "github" and self.secret:
            sig = headers.get("X-Hub-Signature-256", "")
            verified = HmacVerifier.verify_github(raw_body, sig, self.secret)
        elif provider.lower() == "stripe" and self.secret:
            sig = headers.get("Stripe-Signature", "")
            verified = HmacVerifier.verify_stripe(raw_body, sig, self.secret)
        else:
            verified = True
            
        event = WebhookEvent(provider=provider, event_type=event_type, headers=headers, payload=payload, verified=verified)
        self.journal.record(event)
        return event
