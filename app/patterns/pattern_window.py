"""
===============================================================================
Pattern Window
===============================================================================

Sliding window abstraction for chart pattern detection.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True, frozen=True)
class PatternWindow:
    """
    Represents a contiguous window of OHLCV data.
    """

    data: pd.DataFrame

    start: int

    end: int

    @property
    def frame(self) -> pd.DataFrame:
        """
        Windowed DataFrame.
        """
        return self.data.iloc[self.start:self.end]

    @property
    def length(self) -> int:
        """
        Number of bars in the window.
        """
        return self.end - self.start

    @property
    def first_index(self):
        return self.frame.index[0]

    @property
    def last_index(self):
        return self.frame.index[-1]

    @property
    def close(self) -> pd.Series:
        return self.frame["close"]

    @property
    def high(self) -> pd.Series:
        return self.frame["high"]

    @property
    def low(self) -> pd.Series:
        return self.frame["low"]

    @property
    def open(self) -> pd.Series:
        return self.frame["open"]

    @property
    def volume(self) -> pd.Series | None:
        if "volume" not in self.frame.columns:
            return None
        return self.frame["volume"]

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        return iter(self.frame.itertuples())