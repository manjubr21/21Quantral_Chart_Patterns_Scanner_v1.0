"""
History model.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.data.models.candle import Candle


@dataclass(slots=True, frozen=True)
class History:
    """
    Historical candle collection.
    """

    symbol: str
    timeframe: str
    candles: list[Candle]

    @property
    def count(self) -> int:
        return len(self.candles)