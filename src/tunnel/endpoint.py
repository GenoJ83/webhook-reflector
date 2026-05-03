class TunnelEndpoint:
    def __init__(self, subdomain: str = "webhook-local"):
        self.subdomain = subdomain
        
    def get_public_url(self) -> str:
        return f"https://{self.subdomain}.localtunnel.me"
