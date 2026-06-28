from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class Candle:
    """
    Immutable OHLCV candle.
    """

    timestamp: datetime

    open: float

    high: float

    low: float

    close: float

    volume: int

    @property
    def body(self) -> float:
        return abs(self.close - self.open)

    @property
    def range(self) -> float:
        return self.high - self.low

    @property
    def bullish(self) -> bool:
        return self.close > self.open

    @property
    def bearish(self) -> bool:
        return self.close < self.open