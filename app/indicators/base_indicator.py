"""
===============================================================================
Base Indicator
===============================================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseIndicator(ABC):
    """
    Base class implemented by every indicator.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Indicator name.
        """

    @abstractmethod
    def calculate(self, history, **kwargs):
        """
        Calculate indicator.
        """