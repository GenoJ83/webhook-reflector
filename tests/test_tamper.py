from src.crypto.tamper import tamper_signature

def test_tamper():
    sig = "sha256=1234567890abcdef"
    tampered = tamper_signature(sig)
    assert tampered != sig and tampered.endswith("0000")
