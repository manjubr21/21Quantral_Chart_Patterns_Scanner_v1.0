"""
===============================================================================
Indicator Cache Key
===============================================================================

Creates deterministic cache keys for indicator calculations.
"""

from __future__ import annotations

from app.indicators.indicator_request import IndicatorRequest


class IndicatorKey:
    """
    Utility class responsible for generating deterministic cache keys.
    """

    @staticmethod
    def build(request: IndicatorRequest) -> str:
        """
        Build a cache key from an IndicatorRequest.

        Example:
            SMA|period=20

            RSI|period=14

            ATR|period=14

        Args:
            request:
                Indicator request.

        Returns:
            Cache key.
        """

        if not request.parameters:
            return str(request.indicator)

        parameters = ",".join(
            f"{key}={value}"
            for key, value in sorted(request.parameters.items())
        )

        return f"{request.indicator}|{parameters}"