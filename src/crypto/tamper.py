def tamper_signature(valid_sig: str) -> str:
    return valid_sig[:-4] + "0000"
