"""
===============================================================================
Indicator Engine
===============================================================================
"""

from __future__ import annotations

import pandas as pd

from app.indicators.indicator_cache import IndicatorCache
from app.indicators.indicator_keys import IndicatorKey
from app.indicators.indicator_registry import IndicatorRegistry


class IndicatorEngine:

    def __init__(
        self,
        history: pd.DataFrame,
        registry: IndicatorRegistry,
    ):

        self.history = history
        self.registry = registry
        self.cache = IndicatorCache()

    def calculate(
            self,
            indicator,
            **kwargs,
    ):
        from app.indicators.indicator_request import IndicatorRequest

        request = IndicatorRequest(
            indicator=indicator,
            parameters=kwargs,
        )

        key = IndicatorKey.build(request)

        if self.cache.has(key):
            return self.cache.get(key)

        indicator_class = self.registry.get(indicator)

        indicator_object = indicator_class()

        result = indicator_object.calculate(
            self.history,
            **kwargs,
        )

        self.cache.set(key, result)

        return result