"""
===============================================================================
Project : 21Quantral Chart Patterns Scanner
File    : interval_mapper.py

Maps internal timeframes to provider-specific intervals.

===============================================================================
"""

from __future__ import annotations


class IntervalMapper:
    """
    Converts generic timeframe names into provider-specific intervals.
    """

    _YAHOO = {
        "1m": "1m",
        "2m": "2m",
        "5m": "5m",
        "15m": "15m",
        "30m": "30m",
        "60m": "60m",
        "90m": "90m",
        "1h": "60m",
        "1d": "1d",
        "5d": "5d",
        "1wk": "1wk",
        "1mo": "1mo",
        "3mo": "3mo",
    }

    _SHOONYA = {
        "1m": "1",
        "5m": "5",
        "15m": "15",
        "30m": "30",
        "60m": "60",
        "1h": "60",
        "1d": "D",
        "1wk": "W",
        "1mo": "M",
    }

    _MSTOCK = {
        "1m": "1",
        "5m": "5",
        "15m": "15",
        "30m": "30",
        "60m": "60",
        "1h": "60",
        "1d": "1D",
        "1wk": "1W",
        "1mo": "1M",
    }

    @classmethod
    def yahoo(cls, timeframe: str) -> str:

        tf = timeframe.lower()

        if tf not in cls._YAHOO:
            raise ValueError(f"Unsupported Yahoo timeframe: {timeframe}")

        return cls._YAHOO[tf]

    @classmethod
    def shoonya(cls, timeframe: str) -> str:

        tf = timeframe.lower()

        if tf not in cls._SHOONYA:
            raise ValueError(f"Unsupported Shoonya timeframe: {timeframe}")

        return cls._SHOONYA[tf]

    @classmethod
    def mstock(cls, timeframe: str) -> str:

        tf = timeframe.lower()

        if tf not in cls._MSTOCK:
            raise ValueError(f"Unsupported mStock timeframe: {timeframe}")

        return cls._MSTOCK[tf]