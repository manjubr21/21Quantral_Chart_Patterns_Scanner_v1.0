"""
Quote model.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class Quote:
    """
    Latest market quote.
    """

    symbol: str
    exchange: str

    last_price: float

    open: float
    high: float
    low: float
    close: float

    volume: int

    timestamp: datetime