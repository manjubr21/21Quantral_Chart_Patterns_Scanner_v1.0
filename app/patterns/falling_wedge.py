"""
===============================================================================
Falling Wedge Pattern
===============================================================================

Production implementation of the Falling Wedge pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class FallingWedge(BaseSwingPattern):
    """
    Falling Wedge detector.
    """

    name = "FALLING_WEDGE"

    description = (
        "Bullish reversal/continuation pattern consisting of "
        "falling highs and falling lows with narrowing range."
    )

    def detect(
        self,
        data: pd.DataFrame,
    ) -> list[PatternResult]:

        if not self.validate(data):
            return []

        data = data.copy()
        data.columns = [c.lower() for c in data.columns]

        highs = SwingPoints.highs(
            data,
            self.swing_window,
        )

        lows = SwingPoints.lows(
            data,
            self.swing_window,
        )

        results: list[PatternResult] = []

        pair_count = min(
            len(highs),
            len(lows),
        )

        if pair_count < 2:
            return results

        for i in range(pair_count - 1):

            high1 = highs[i]
            high2 = highs[i + 1]

            low1 = lows[i]
            low2 = lows[i + 1]

            if high2.price >= high1.price:
                continue

            if low2.price >= low1.price:
                continue

            width1 = high1.price - low1.price
            width2 = high2.price - low2.price

            if width2 >= width1:
                continue

            resistance = high2.price

            breakout = (
                data["close"]
                .iloc[max(high2.index, low2.index):]
                > resistance
            )

            if not breakout.any():
                continue

            breakout_index = breakout.idxmax()

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=min(
                        high1.timestamp,
                        low1.timestamp,
                    ),
                    end_index=breakout_index,
                    confidence=89.0,
                    metadata={
                        "upper_resistance": resistance,
                        "lower_low": low2.price,
                        "compression": round(
                            (width1 - width2) / width1,
                            3,
                        ),
                    },
                )
            )

        return results