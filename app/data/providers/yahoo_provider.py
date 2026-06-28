"""
===============================================================================
Project     : 21Quantral Chart Patterns Scanner
Module      : Yahoo Finance Provider

Author      : Manjunatha Ramachandra
Co-Developer: OpenAI ChatGPT
===============================================================================
"""

from __future__ import annotations

import logging

import yfinance as yf

from app.data.models.candle import Candle
from app.data.providers.base_provider import BaseDataProvider
from app.data.providers.interval_mapper import IntervalMapper
from app.data.providers.symbol_mapper import SymbolMapper

logger = logging.getLogger(__name__)


class YahooProvider(BaseDataProvider):
    """
    Yahoo Finance implementation.
    """

    @property
    def name(self) -> str:
        return "Yahoo"

    def get_symbols(self):
        """
        Placeholder.

        NSE symbol master will be added later.
        """
        return []

    def search(self, text: str):
        """
        Placeholder.
        """
        return []

    def get_history(
        self,
        symbol: str,
        timeframe: str,
        limit: int = 500,
    ) -> list[Candle]:

        yahoo_symbol = SymbolMapper.yahoo(symbol)

        interval = IntervalMapper.yahoo(timeframe)

        logger.info(
            "Downloading %s (%s)",
            yahoo_symbol,
            interval,
        )

        ticker = yf.Ticker(yahoo_symbol)

        df = ticker.history(
            period="max",
            interval=interval,
            auto_adjust=False,
            actions=False,
        )

        if df.empty:
            raise ValueError(
                f"No data returned for {symbol}"
            )

        if limit > 0:
            df = df.tail(limit)

        candles: list[Candle] = []

        for ts, row in df.iterrows():

            candles.append(
                Candle(
                    timestamp=ts.to_pydatetime(),
                    open=float(row.Open),
                    high=float(row.High),
                    low=float(row.Low),
                    close=float(row.Close),
                    volume=int(row.Volume),
                )
            )

        logger.info(
            "%s candles downloaded.",
            len(candles),
        )

        return candles