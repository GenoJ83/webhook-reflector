class WebhookError(Exception):
    """Base exception."""

class InvalidSignatureError(WebhookError):
    """Raised when webhook signature verification fails."""

class ReplayError(WebhookError):
    """Raised when replaying an event fails."""
