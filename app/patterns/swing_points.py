"""
===============================================================================
Swing Point Detection
===============================================================================

Reusable swing high / swing low detection utilities used by all swing-based
chart pattern detectors.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True, frozen=True)
class SwingPoint:
    """
    Represents a swing high or swing low.
    """

    index: int
    timestamp: object
    price: float
    is_high: bool


class SwingPoints:
    """
    Utility class for extracting swing highs and swing lows.
    """

    @staticmethod
    def highs(
        data: pd.DataFrame,
        window: int = 5,
    ) -> list[SwingPoint]:

        data = data.copy()
        data.columns = [c.lower() for c in data.columns]

        highs = data["high"].values

        swings: list[SwingPoint] = []

        for i in range(window, len(data) - window):

            section = highs[
                i - window:i + window + 1
            ]

            if highs[i] == section.max():

                swings.append(
                    SwingPoint(
                        index=i,
                        timestamp=data.index[i],
                        price=float(highs[i]),
                        is_high=True,
                    )
                )

        return swings

    @staticmethod
    def lows(
        data: pd.DataFrame,
        window: int = 5,
    ) -> list[SwingPoint]:

        data = data.copy()
        data.columns = [c.lower() for c in data.columns]

        lows = data["low"].values

        swings: list[SwingPoint] = []

        for i in range(window, len(data) - window):

            section = lows[
                i - window:i + window + 1
            ]

            if lows[i] == section.min():

                swings.append(
                    SwingPoint(
                        index=i,
                        timestamp=data.index[i],
                        price=float(lows[i]),
                        is_high=False,
                    )
                )

        return swings

    @staticmethod
    def all(
        data: pd.DataFrame,
        window: int = 5,
    ) -> list[SwingPoint]:

        swings = (
            SwingPoints.highs(data, window)
            + SwingPoints.lows(data, window)
        )

        swings.sort(key=lambda x: x.index)

        return swings