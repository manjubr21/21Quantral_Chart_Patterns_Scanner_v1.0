"""
===============================================================================
Project     : 21Quantral_Chart_Patterns_Scanner_v1.0
File        : enums.py
Version     : 1.0.0

Description:
    Shared enumerations used throughout the application.

===============================================================================
"""

from __future__ import annotations

from enum import StrEnum


class TimeFrame(StrEnum):
    """Supported chart timeframes."""

    M15 = "15m"
    M30 = "30m"
    H1 = "1h"
    H2 = "2h"
    H4 = "4h"
    D1 = "1d"
    W1 = "1wk"
    MN1 = "1mo"


class DataProvider(StrEnum):
    """Market data providers."""

    YAHOO = "Yahoo Finance"
    MSTOCK = "mStock"
    SHOONYA = "Shoonya"


class PatternStatus(StrEnum):
    """Pattern detection status."""

    FORMING = "Forming"
    CONFIRMED = "Confirmed"
    FAILED = "Failed"