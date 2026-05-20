# Webhook Verification Architecture

Always verify cryptographic signatures before processing webhook payloads to prevent spoofing.

- **GitHub**: `X-Hub-Signature-256: sha256=<hex>`
- **Stripe**: `Stripe-Signature: t=<timestamp>,v1=<hex>`
- **Slack**: `X-Slack-Signature: v0=<hex>`
