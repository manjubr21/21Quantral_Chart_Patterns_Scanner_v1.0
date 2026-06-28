"""
===============================================================================
Indicator Registry
===============================================================================
"""

from __future__ import annotations

from app.indicators.base_indicator import BaseIndicator


class IndicatorRegistry:

    def __init__(self):

        self._indicators = {}

    def register(
        self,
        indicator: BaseIndicator,
    ):

        self._indicators[
            indicator.name.upper()
        ] = indicator

    def get(
        self,
        name: str,
    ) -> BaseIndicator:

        key = name.upper()

        if key not in self._indicators:

            raise LookupError(
                f"Indicator '{name}' not registered."
            )

        return self._indicators[key]

    def names(self):

        return sorted(self._indicators.keys())

    def clear(self):

        self._indicators.clear()

    def __len__(self):

        return len(self._indicators)