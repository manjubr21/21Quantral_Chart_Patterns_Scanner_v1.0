"""
===============================================================================
Indicator Engine
===============================================================================
"""

from __future__ import annotations

import pandas as pd

from app.indicators.cache import IndicatorCache
from app.indicators.keys import IndicatorKey

from app.indicators.sma import SMA
from app.indicators.ema import EMA


class IndicatorEngine:

    def __init__(
        self,
        history: pd.DataFrame,
    ):

        self.history = history

        self.cache = IndicatorCache()

    def sma(
        self,
        period: int,
    ):

        key = IndicatorKey.sma(period)

        if self.cache.has(key):
            return self.cache.get(key)

        value = SMA(period).calculate(self.history)

        self.cache.set(key, value)

        return value

    def ema(
        self,
        period: int,
    ):

        key = IndicatorKey.ema(period)

        if self.cache.has(key):
            return self.cache.get(key)

        value = EMA(period).calculate(self.history)

        self.cache.set(key, value)

        return value