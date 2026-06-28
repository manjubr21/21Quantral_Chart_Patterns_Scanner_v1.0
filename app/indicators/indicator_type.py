"""
===============================================================================
Indicator Types
===============================================================================

Enumeration of all supported technical indicators.
"""

from __future__ import annotations

from enum import StrEnum


class IndicatorType(StrEnum):
    """
    Enumeration of supported technical indicators.
    """

    SMA = "SMA"
    EMA = "EMA"
    RSI = "RSI"
    ATR = "ATR"

    def __str__(self) -> str:
        """
        Return the indicator name.

        Returns:
            Indicator name.
        """
        return self.value