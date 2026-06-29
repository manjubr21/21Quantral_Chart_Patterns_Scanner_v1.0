"""
===============================================================================
Pattern Test Builder
===============================================================================

Utility for generating synthetic OHLCV data for pattern detector tests.

Every chart pattern test should use this builder instead of manually creating
DataFrames.

This guarantees consistent, reusable and realistic test data.
"""

from __future__ import annotations

import pandas as pd


class PatternBuilder:
    """
    Generates synthetic OHLCV datasets.
    """

    @staticmethod
    def from_close(close_prices: list[float]) -> pd.DataFrame:
        """
        Build OHLCV data from close prices.

        Parameters
        ----------
        close_prices:
            Close price series.

        Returns
        -------
        DataFrame
        """

        rows = []

        volume = 100000

        for close in close_prices:

            rows.append(
                {
                    "open": close,
                    "high": close * 1.01,
                    "low": close * 0.99,
                    "close": close,
                    "volume": volume,
                }
            )

            volume *= 0.99

        return pd.DataFrame(rows)

    @staticmethod
    def empty() -> pd.DataFrame:

        return pd.DataFrame(
            columns=[
                "open",
                "high",
                "low",
                "close",
                "volume",
            ]
        )