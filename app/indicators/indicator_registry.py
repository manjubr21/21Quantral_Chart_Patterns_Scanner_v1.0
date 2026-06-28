"""
===============================================================================
Indicator Registry
===============================================================================
"""

from __future__ import annotations

from app.indicators.base_indicator import BaseIndicator


class IndicatorRegistry:

    def __init__(self):

        self._registry = {}

    def register(
        self,
        indicator: BaseIndicator,
    ):

        self._registry[indicator.name.lower()] = indicator

    def get(
        self,
        name: str,
    ) -> BaseIndicator:

        key = name.lower()

        if key not in self._registry:
            raise ValueError(f"Indicator '{name}' not registered.")

        return self._registry[key]

    def list(self):

        return sorted(self._registry.keys())
