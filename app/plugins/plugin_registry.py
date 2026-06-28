"""
===============================================================================
Plugin Registry
===============================================================================
"""

from __future__ import annotations

from typing import Dict

from app.plugins.base_plugin import BasePlugin


class PluginRegistry:
    """
    Stores registered plugins.
    """

    def __init__(self):

        self._plugins: Dict[str, BasePlugin] = {}

    def register(
        self,
        plugin: BasePlugin,
    ):

        key = plugin.name.lower()

        if key in self._plugins:
            raise ValueError(
                f"Plugin '{plugin.name}' already registered."
            )

        self._plugins[key] = plugin

    def unregister(
        self,
        name: str,
    ):

        self._plugins.pop(name.lower(), None)

    def get(
        self,
        name: str,
    ) -> BasePlugin:

        key = name.lower()

        if key not in self._plugins:
            raise LookupError(
                f"Plugin '{name}' not found."
            )

        return self._plugins[key]

    def exists(
        self,
        name: str,
    ) -> bool:

        return name.lower() in self._plugins

    def clear(self):

        self._plugins.clear()

    def names(self):

        return sorted(self._plugins.keys())

    def __len__(self):

        return len(self._plugins)