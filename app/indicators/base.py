"""
===============================================================================
Base Indicator
===============================================================================

Abstract base class for all technical indicators.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseIndicator(ABC):
    """
    Abstract base class for all indicators.

    Every indicator implementation must inherit from this class and implement
    both parameter validation and the calculation routine.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Return the unique indicator name.

        Returns:
            Indicator name.
        """
        raise NotImplementedError

    @abstractmethod
    def validate(self) -> None:
        """
        Validate indicator parameters.

        Raises:
            IndicatorValidationError:
                If any parameter is invalid.
        """
        raise NotImplementedError

    @abstractmethod
    def calculate(self, data: pd.DataFrame) -> pd.Series:
        """
        Calculate the indicator.

        Args:
            data:
                OHLCV DataFrame.

        Returns:
            pandas.Series containing the calculated values.
        """
        raise NotImplementedError

    def __call__(self, data: pd.DataFrame) -> pd.Series:
        """
        Allow an indicator instance to be called like a function.

        Args:
            data:
                OHLCV DataFrame.

        Returns:
            Calculated indicator values.
        """
        self.validate()
        return self.calculate(data)

    def __repr__(self) -> str:
        """
        Developer-friendly representation.

        Returns:
            String representation.
        """
        return f"{self.__class__.__name__}()"