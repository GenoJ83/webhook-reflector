from src.generator.synth import generate_sample_github_push

def test_synth():
    p = generate_sample_github_push()
    assert p["ref"] == "refs/heads/main"
    assert p["repository"]["name"] == "test-repo"
