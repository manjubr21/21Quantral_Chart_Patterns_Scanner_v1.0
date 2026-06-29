"""
===============================================================================
Ascending Triangle Pattern
===============================================================================

Production implementation of the Ascending Triangle continuation pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class AscendingTriangle(BaseSwingPattern):
    """
    Ascending Triangle detector.
    """

    name = "ASCENDING_TRIANGLE"

    description = (
        "Bullish continuation pattern consisting of "
        "higher lows against horizontal resistance."
    )

    resistance_tolerance: float = 0.02

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

        if len(highs) < 2 or len(lows) < 2:
            return results

        for i in range(len(highs) - 1):

            resistance1 = highs[i]
            resistance2 = highs[i + 1]

            difference = abs(
                resistance1.price - resistance2.price
            ) / resistance1.price

            if difference > self.resistance_tolerance:
                continue

            pattern_lows = [
                low
                for low in lows
                if resistance1.index < low.index < resistance2.index
            ]

            if len(pattern_lows) < 2:
                continue

            higher_lows = all(
                pattern_lows[k].price >
                pattern_lows[k - 1].price
                for k in range(1, len(pattern_lows))
            )

            if not higher_lows:
                continue

            resistance = (
                resistance1.price + resistance2.price
            ) / 2

            breakout = (
                data["close"]
                .iloc[resistance2.index:]
                > resistance
            )

            if not breakout.any():
                continue

            breakout_index = breakout.idxmax()

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=resistance1.timestamp,
                    end_index=breakout_index,
                    confidence=90.0,
                    metadata={
                        "resistance": resistance,
                        "higher_lows": len(pattern_lows),
                    },
                )
            )

        return results