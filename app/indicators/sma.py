"""
===============================================================================
Project     : 21Quantral Chart Patterns Scanner
Module      : Simple Moving Average (SMA)

Author      : Manjunatha Ramachandra
Co-Developer: OpenAI ChatGPT

Description:
    Simple Moving Average Indicator.

===============================================================================
"""

from __future__ import annotations

import pandas as pd

from app.indicators.base_indicator import BaseIndicator


class SMA(BaseIndicator):
    """
    Simple Moving Average Indicator.
    """

    @property
    def name(self) -> str:
        return "SMA"

    def calculate(
        self,
        history: pd.DataFrame,
        period: int,
    ) -> pd.Series:
        """
        Calculate Simple Moving Average.

        Parameters
        ----------
        history : pandas.DataFrame
            OHLCV DataFrame containing a 'Close' column.

        period : int
            SMA period.

        Returns
        -------
        pandas.Series
            SMA values.
        """

        if period <= 0:
            raise ValueError("Period must be greater than zero.")

        if "Close" not in history.columns:
            raise KeyError("Column 'Close' not found.")

        return (
            history["Close"]
            .rolling(window=period, min_periods=period)
            .mean()
        )