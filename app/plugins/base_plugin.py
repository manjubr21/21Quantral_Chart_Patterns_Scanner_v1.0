"""
===============================================================================
Base Plugin
===============================================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BasePlugin(ABC):
    """
    Base class for every plugin in 21Quantral.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique plugin name.
        """

    @property
    def version(self) -> str:
        return "1.0.0"

    @property
    def author(self) -> str:
        return "21Quantral"

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute plugin.
        """