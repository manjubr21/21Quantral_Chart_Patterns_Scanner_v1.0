from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from app.indicators.base import BaseIndicator
from app.indicators.exceptions import IndicatorValidationError


@dataclass(frozen=True)
class ATRIndicator(BaseIndicator):
    period: int = 14

    def validate(self) -> None:
        if self.period < 2:
            raise IndicatorValidationError("ATR period must be >= 2")

    def calculate(self, data: pd.DataFrame, **kwargs) -> pd.Series:
        period = kwargs.get("period", self.period)

        high = data["high"].astype(float)
        low = data["low"].astype(float)
        close = data["close"].astype(float)

        prev_close = close.shift(1)

        tr = pd.concat([
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ], axis=1).max(axis=1)

        return tr.ewm(alpha=1 / period, adjust=False).mean()