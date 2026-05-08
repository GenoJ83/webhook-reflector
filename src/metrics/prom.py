from typing import Dict, Any

def to_prometheus(stats: Dict[str, int]) -> str:
    lines = [
        "# HELP webhook_received_total Count of received webhooks by provider",
        "# TYPE webhook_received_total counter"
    ]
    for prov, count in stats.items():
        lines.append(f'webhook_received_total{{provider="{prov}"}} {count}')
    return "\n".join(lines)
