"""
Base Pattern Framework

All chart pattern detectors must inherit from BasePattern.

Author: 21Quantral
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

import pandas as pd


class BasePattern(ABC):
    """
    Abstract base class for all chart pattern detectors.

    Every concrete pattern implementation must define:
        - name
        - calculate()
    """

    #: Unique pattern name
    name: str = ""

    #: Human-readable description
    description: str = ""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"

    @abstractmethod
    def calculate(
        self,
        data: pd.DataFrame,
        **kwargs: Any,
    ):
        """
        Detect a chart pattern.

        Parameters
        ----------
        data : pd.DataFrame
            OHLCV data.

        kwargs :
            Pattern-specific parameters.

        Returns
        -------
        PatternResult
            Detection result.
        """
        raise NotImplementedError