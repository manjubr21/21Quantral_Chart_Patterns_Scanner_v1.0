"""
Yahoo Finance Provider
"""

from __future__ import annotations

import yfinance as yf

from app.data.models.candle import Candle
from app.data.models.symbol import Symbol
from app.data.providers.base_provider import BaseDataProvider


class YahooProvider(BaseDataProvider):

    @property
    def name(self) -> str:
        return "Yahoo"

    def get_symbols(self) -> list[Symbol]:
        """
        Placeholder.

        NSE symbol master will be added later.
        """
        return []

    def search(self, text: str):
        return []

    def get_history(
        self,
        symbol: str,
        timeframe: str,
        limit: int,
    ) -> list[Candle]:

        ticker = yf.Ticker(symbol + ".NS")

        df = ticker.history(
            period="max",
            interval=timeframe,
        )

        if limit:
            df = df.tail(limit)

        candles: list[Candle] = []

        for ts, row in df.iterrows():

            candles.append(
                Candle(
                    timestamp=ts.to_pydatetime(),
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    volume=int(row["Volume"]),
                )
            )

        return candles