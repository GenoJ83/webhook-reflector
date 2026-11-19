from src.plugins.manager import PluginHookManager

def test_plugin_hooks():
    mgr = PluginHookManager()
    mgr.register("transform", lambda text: text.strip())
    mgr.register("transform", lambda text: text.upper())
    res = mgr.trigger("transform", "  hello world  ")
    assert res == "HELLO WORLD"
