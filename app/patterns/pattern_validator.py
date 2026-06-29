"""
===============================================================================
Pattern Validator
===============================================================================

Validation utilities for chart pattern detection.
"""

from __future__ import annotations

import pandas as pd


class PatternValidator:
    """
    Common validation helpers used by pattern detectors.
    """

    REQUIRED_COLUMNS = (
        "open",
        "high",
        "low",
        "close",
    )

    @classmethod
    def validate_dataframe(
        cls,
        data: pd.DataFrame,
    ) -> None:
        """
        Validate an OHLC DataFrame.
        """

        if data is None:
            raise ValueError("Data cannot be None.")

        if data.empty:
            raise ValueError("DataFrame is empty.")

        columns = {column.lower() for column in data.columns}

        missing = [
            column
            for column in cls.REQUIRED_COLUMNS
            if column not in columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {', '.join(missing)}"
            )

    @staticmethod
    def validate_minimum_bars(
        data: pd.DataFrame,
        minimum_bars: int,
    ) -> None:
        """
        Ensure sufficient history exists.
        """

        if len(data) < minimum_bars:
            raise ValueError(
                f"At least {minimum_bars} bars are required."
            )

    @staticmethod
    def validate_window(
        window: int,
    ) -> None:
        """
        Validate rolling window size.
        """

        if window < 2:
            raise ValueError(
                "Window size must be at least 2."
            )

    @staticmethod
    def validate_positive(
        value: int | float,
        name: str,
    ) -> None:
        """
        Validate a positive numeric parameter.
        """

        if value <= 0:
            raise ValueError(
                f"{name} must be greater than zero."
            )