import json
from typing import List
from src.core.models import WebhookEvent

def export_har_entries(events: List[WebhookEvent]) -> str:
    entries = [
        {
            "startedDateTime": e.received_at,
            "provider": e.provider,
            "event": e.event_type,
            "payload": e.payload
        }
        for e in events
    ]
    return json.dumps(entries, indent=2)
