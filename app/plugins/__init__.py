"""
===============================================================================
21Quantral Plugin System
===============================================================================

Every extensible component in the application is implemented as a plugin.

Examples
--------
Indicators
Patterns
Scanners
Data Providers
Ranking Engines

===============================================================================
"""

from .base_plugin import BasePlugin
from .plugin_registry import PluginRegistry
from .plugin_manager import PluginManager

__all__ = [
    "BasePlugin",
    "PluginRegistry",
    "PluginManager",
]