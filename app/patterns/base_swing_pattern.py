"""
===============================================================================
Base Swing Pattern
===============================================================================

Base class for all swing-based chart pattern detectors.

Examples:
    - Double Top
    - Double Bottom
    - Head & Shoulders
    - Inverse Head & Shoulders
    - Triple Top
    - Triple Bottom
"""

from __future__ import annotations

from abc import abstractmethod

import pandas as pd

from app.patterns.base_pattern import BasePattern
from app.patterns.pattern_result import PatternResult
from app.patterns.pattern_validator import PatternValidator


class BaseSwingPattern(BasePattern):
    """
    Base class for swing-based chart patterns.
    """

    lookback: int = 150

    swing_window: int = 5

    tolerance: float = 0.02

    min_bars: int = 50

    def validate(
        self,
        data: pd.DataFrame,
    ) -> bool:
        """
        Validate data before pattern detection.
        """
        PatternValidator.validate_dataframe(data)
        PatternValidator.validate_minimum_bars(
            data,
            self.min_bars,
        )
        PatternValidator.validate_window(
            self.swing_window,
        )
        return True

    @abstractmethod
    def detect(
        self,
        data: pd.DataFrame,
    ) -> list[PatternResult]:
        """
        Detect swing pattern.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"lookback={self.lookback}, "
            f"swing_window={self.swing_window}, "
            f"tolerance={self.tolerance})"
        )