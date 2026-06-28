from app.plugins import BasePlugin
from app.plugins import PluginRegistry


class DummyPlugin(BasePlugin):

    @property
    def name(self):

        return "Dummy"

    def execute(self):

        return 100


def test_registry():

    registry = PluginRegistry()

    registry.register(DummyPlugin())

    assert registry.exists("dummy")

    plugin = registry.get("Dummy")

    assert plugin.execute() == 100

    assert len(registry) == 1