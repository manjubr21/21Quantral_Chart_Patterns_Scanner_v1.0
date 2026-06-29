from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from app.indicators.base import BaseIndicator
from app.indicators.exceptions import IndicatorValidationError


@dataclass(frozen=True)
class SMAIndicator(BaseIndicator):
    """
    Simple Moving Average indicator.
    """

    name: str = "sma"
    period: int = 14

    def validate(self) -> None:
        if self.period < 1:
            raise IndicatorValidationError(
                "SMA period must be >= 1"
            )

    def calculate(
        self,
        data: pd.DataFrame,
        **kwargs,
    ) -> pd.Series:
        """
        Calculate the Simple Moving Average.
        """
        period = kwargs.get("period", self.period)

        close = data["close"].astype(float)

        return close.rolling(window=period).mean()


# Backward compatibility
SMA = SMAIndicator