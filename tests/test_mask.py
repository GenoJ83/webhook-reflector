from src.sanitizer.mask import mask_sensitive_fields

def test_mask():
    p = {"user": "alice", "api_token": "secret123", "id": 1}
    masked = mask_sensitive_fields(p)
    assert masked["user"] == "alice"
    assert masked["api_token"] == "********"
