"""
===============================================================================
Pattern Utilities
===============================================================================

Shared utility functions used by chart pattern detectors.
"""

from __future__ import annotations

import pandas as pd


class PatternUtils:
    """
    Collection of reusable helper methods for pattern detection.
    """

    @staticmethod
    def normalize_columns(
        data: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Return a copy with lowercase column names.
        """
        df = data.copy()
        df.columns = [column.lower() for column in df.columns]
        return df

    @staticmethod
    def highest_high(
        data: pd.DataFrame,
        start: int,
        end: int,
    ) -> float:
        """
        Highest high within a window.
        """
        return float(data["high"].iloc[start:end].max())

    @staticmethod
    def lowest_low(
        data: pd.DataFrame,
        start: int,
        end: int,
    ) -> float:
        """
        Lowest low within a window.
        """
        return float(data["low"].iloc[start:end].min())

    @staticmethod
    def price_change(
        start_price: float,
        end_price: float,
    ) -> float:
        """
        Percentage price change.
        """
        if start_price == 0:
            return 0.0

        return ((end_price - start_price) / start_price) * 100.0

    @staticmethod
    def is_higher_high(
        previous: float,
        current: float,
    ) -> bool:
        return current > previous

    @staticmethod
    def is_lower_low(
        previous: float,
        current: float,
    ) -> bool:
        return current < previous

    @staticmethod
    def rolling_high(
        data: pd.DataFrame,
        window: int,
    ) -> pd.Series:
        return data["high"].rolling(window).max()

    @staticmethod
    def rolling_low(
        data: pd.DataFrame,
        window: int,
    ) -> pd.Series:
        return data["low"].rolling(window).min()

    @staticmethod
    def rolling_mean(
        series: pd.Series,
        window: int,
    ) -> pd.Series:
        return series.rolling(window).mean()