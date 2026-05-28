# webhook-reflector

Local webhook tunnel endpoint, cryptographic signature verifier (GitHub, Stripe, Slack), payload replay engine, and event router.

[![CI](https://github.com/GenoJ83/webhook-reflector/actions/workflows/ci.yml/badge.svg)](https://github.com/GenoJ83/webhook-reflector/actions)

## Features
- **Cryptographic Verification**: Native support for GitHub (`X-Hub-Signature-256`), Stripe (`v1`), and Slack (`v0`)
- **Local Forwarding**: Pipes public webhooks to local ports (`localhost:3000`, `localhost:8000`)
- **Event Journal & Replay**: Inspect, filter, and replay webhook payloads on demand
- **Dead Letter Queue (DLQ)**: Retains failed deliveries with automated retry mechanisms

## Quick Start
```python
from src.reflector import WebhookReflector

reflector = WebhookReflector(secret="whsec_test")
event = reflector.ingest(
    provider="github",
    event_type="push",
    headers={"X-Hub-Signature-256": "sha256=..."},
    payload={"ref": "refs/heads/main"},
    raw_body=b'{"ref": "refs/heads/main"}'
)
print(f"Event {event.id} received, verified={event.verified}")
```
