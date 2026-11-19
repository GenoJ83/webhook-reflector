from src.plugins.filter_chain import FilterChain

def test_filter_chain():
    chain = FilterChain()
    chain.add_filter(lambda n: n * 2).add_filter(lambda n: n + 1)
    assert chain.execute(5) == 11
