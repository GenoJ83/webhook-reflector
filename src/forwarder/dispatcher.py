from typing import Dict, Any
from src.core.models import WebhookEvent

class WebhookDispatcher:
    def __init__(self, target_url: str = "http://localhost:3000/webhook"):
        self.target_url = target_url
        
    def forward(self, event: WebhookEvent) -> Dict[str, Any]:
        return {
            "status": "FORWARDED",
            "destination": self.target_url,
            "event_id": event.id
        }
