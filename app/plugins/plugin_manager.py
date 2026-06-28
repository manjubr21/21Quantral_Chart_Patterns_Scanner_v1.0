"""
===============================================================================
Plugin Manager
===============================================================================
"""

from __future__ import annotations

from app.plugins.plugin_registry import PluginRegistry


class PluginManager:
    """
    Executes plugins through the registry.
    """

    def __init__(
        self,
        registry: PluginRegistry,
    ):

        self.registry = registry

    def execute(
        self,
        plugin_name: str,
        *args,
        **kwargs,
    ):

        plugin = self.registry.get(plugin_name)

        return plugin.execute(
            *args,
            **kwargs,
        )