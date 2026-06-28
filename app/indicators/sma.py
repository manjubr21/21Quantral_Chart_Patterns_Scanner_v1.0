"""
Simple Moving Average
"""

from __future__ import annotations

import pandas as pd

from app.indicators.base_indicator import BaseIndicator


class SMA(BaseIndicator):

    def __init__(
        self,
        period: int,
    ):
        self.period = period

    @property
    def name(self):

        return f"SMA({self.period})"

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:

        return data["Close"].rolling(
            window=self.period
        ).mean()
    