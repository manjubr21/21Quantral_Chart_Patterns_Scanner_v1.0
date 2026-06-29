"""
===============================================================================
Base Breakout Pattern
===============================================================================

Base class for breakout-based chart pattern detectors.

Examples:
    - Ascending Triangle
    - Descending Triangle
    - Symmetrical Triangle
    - Bull Flag
    - Bear Flag
    - Rectangle
    - Channel
    - Cup & Handle Breakout
"""

from __future__ import annotations

from abc import abstractmethod

import pandas as pd

from app.patterns.base_pattern import BasePattern
from app.patterns.pattern_result import PatternResult
from app.patterns.pattern_validator import PatternValidator


class BaseBreakoutPattern(BasePattern):
    """
    Base class for all breakout pattern detectors.
    """

    lookback: int = 200

    breakout_buffer: float = 0.005

    volume_confirmation: bool = True

    min_bars: int = 40

    def validate(
        self,
        data: pd.DataFrame,
    ) -> bool:
        """
        Validate input data.
        """
        PatternValidator.validate_dataframe(data)
        PatternValidator.validate_minimum_bars(
            data,
            self.min_bars,
        )
        return True

    @abstractmethod
    def detect(
        self,
        data: pd.DataFrame,
    ) -> list[PatternResult]:
        """
        Detect breakout patterns.
        """
        raise NotImplementedError

    def breakout_confirmed(
        self,
        resistance: float,
        close: float,
    ) -> bool:
        """
        Bullish breakout confirmation.
        """
        return close > resistance * (1.0 + self.breakout_buffer)

    def breakdown_confirmed(
        self,
        support: float,
        close: float,
    ) -> bool:
        """
        Bearish breakdown confirmation.
        """
        return close < support * (1.0 - self.breakout_buffer)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"lookback={self.lookback}, "
            f"buffer={self.breakout_buffer}, "
            f"volume_confirmation={self.volume_confirmation})"
        )