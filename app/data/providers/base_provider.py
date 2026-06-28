"""
Abstract interface implemented by every
data provider.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from typing import Iterable

from app.data.models.candle import Candle
from app.data.models.symbol import Symbol


class BaseDataProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Provider name.
        """

    @abstractmethod
    def get_symbols(self) -> list[Symbol]:
        """
        Returns all tradable symbols.
        """

    @abstractmethod
    def get_history(
        self,
        symbol: str,
        timeframe: str,
        limit: int,
    ) -> list[Candle]:
        """
        Returns OHLCV candles.
        """

    @abstractmethod
    def search(
        self,
        text: str,
    ) -> Iterable[Symbol]:
        """
        Symbol search.
        """