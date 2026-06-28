"""
===============================================================================
Base Indicator

Every indicator in 21Quantral inherits from this class.
===============================================================================
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

import pandas as pd


class BaseIndicator(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Indicator name.
        """

    @abstractmethod
    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.Series:
        """
        Calculate indicator.
        """