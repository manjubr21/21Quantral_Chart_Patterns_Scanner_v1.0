from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Symbol:
    """
    Exchange symbol.
    """

    exchange: str

    symbol: str

    company_name: str

    instrument: str = "EQ"

    active: bool = True