"""
Data validation utilities.
"""

from __future__ import annotations

from app.data.models.candle import Candle


class DataValidator:

    @staticmethod
    def validate_history(
        candles: list[Candle],
    ) -> bool:

        if len(candles) == 0:
            return False

        previous = candles[0].timestamp

        for candle in candles[1:]:

            if candle.timestamp <= previous:
                return False

            if candle.high < candle.low:
                return False

            if candle.volume < 0:
                return False

            previous = candle.timestamp

        return True