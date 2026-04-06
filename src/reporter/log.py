from typing import List
from src.core.models import WebhookEvent

class EventReporter:
    @staticmethod
    def format_log(events: List[WebhookEvent]) -> str:
        h1 = "PROVIDER"
        h2 = "EVENT TYPE"
        h3 = "VERIFIED"
        h4 = "ID"
        lines = [f"{h1:<12} | {h2:<18} | {h3:<10} | {h4}"]
        lines.append("-" * 65)
        for e in events:
            ver = "VERIFIED" if e.verified else "UNVERIFIED"
            lines.append(f"{e.provider:<12} | {e.event_type:<18} | {ver:<10} | {e.id}")
        return "\n".join(lines)
