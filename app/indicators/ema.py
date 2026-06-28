"""
===============================================================================
Project     : 21Quantral Chart Patterns Scanner
Module      : Exponential Moving Average (EMA)

Author      : Manjunatha Ramachandra
Co-Developer: OpenAI ChatGPT

Description:
    Exponential Moving Average Indicator.

===============================================================================
"""

from __future__ import annotations

import pandas as pd

from app.indicators.base_indicator import BaseIndicator


class EMA(BaseIndicator):
    """
    Exponential Moving Average Indicator.
    """

    @property
    def name(self) -> str:
        return "EMA"

    def calculate(
        self,
        history: pd.DataFrame,
        period: int,
    ) -> pd.Series:
        """
        Calculate Exponential Moving Average.

        Parameters
        ----------
        history : pandas.DataFrame
            OHLCV DataFrame containing a 'Close' column.

        period : int
            EMA period.

        Returns
        -------
        pandas.Series
            EMA values.
        """

        if period <= 0:
            raise ValueError("Period must be greater than zero.")

        if "Close" not in history.columns:
            raise KeyError("Column 'Close' not found.")

        return (
            history["Close"]
            .ewm(
                span=period,
                adjust=False,
            )
            .mean()
        )