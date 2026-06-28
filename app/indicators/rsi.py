from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from app.indicators.base import BaseIndicator
from app.indicators.exceptions import IndicatorValidationError


@dataclass(frozen=True)
class RSIIndicator(BaseIndicator):
    period: int = 14

    def validate(self) -> None:
        if self.period < 2:
            raise IndicatorValidationError("RSI period must be >= 2")

    def calculate(self, data: pd.DataFrame, **kwargs) -> pd.Series:
        period = kwargs.get("period", self.period)

        close = data["close"].astype(float)
        delta = close.diff()

        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)

        avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
        avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()

        rs = avg_gain / avg_loss.replace(0, np.nan)
        return 100 - (100 / (1 + rs))

