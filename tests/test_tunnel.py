from src.tunnel.endpoint import TunnelEndpoint

def test_tunnel():
    t = TunnelEndpoint("my-app")
    assert t.get_public_url() == "https://my-app.localtunnel.me"
