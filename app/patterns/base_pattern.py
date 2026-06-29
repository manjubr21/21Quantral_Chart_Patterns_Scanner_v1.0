"""
===============================================================================
Base Pattern
===============================================================================

Abstract base class for every chart pattern detector.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from app.patterns.pattern_result import PatternResult


class BasePattern(ABC):
    """
    Base class for all chart pattern detectors.
    """

    name: str = "BASE"

    description: str = ""

    min_bars: int = 20

    @abstractmethod
    def detect(
        self,
        data: pd.DataFrame,
    ) -> list[PatternResult]:
        """
        Detect pattern occurrences.

        Parameters
        ----------
        data
            OHLCV DataFrame.

        Returns
        -------
        list[PatternResult]
            Detected pattern results.
        """
        raise NotImplementedError

    def validate(
        self,
        data: pd.DataFrame,
    ) -> bool:
        """
        Basic validation before detection.
        """

        return (
            data is not None
            and not data.empty
            and len(data) >= self.min_bars
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"