"""
===============================================================================
Double Top Pattern
===============================================================================

Production implementation of the Double Top reversal pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class DoubleTop(BaseSwingPattern):
    """
    Double Top detector.
    """

    name = "DOUBLE_TOP"

    description = (
        "Bearish reversal consisting of two similar highs "
        "separated by a reaction low."
    )

    def detect(
        self,
        data: pd.DataFrame,
    ) -> list[PatternResult]:

        if not self.validate(data):
            return []

        data = data.copy()
        data.columns = [c.lower() for c in data.columns]

        swing_highs = SwingPoints.highs(
            data,
            self.swing_window,
        )

        results: list[PatternResult] = []

        for i in range(len(swing_highs) - 1):

            left = swing_highs[i]

            for j in range(i + 1, len(swing_highs)):

                right = swing_highs[j]

                if right.index - left.index > self.lookback:
                    break

                difference = abs(
                    left.price - right.price
                ) / left.price

                if difference > self.tolerance:
                    continue

                neckline = (
                    data["low"]
                    .iloc[left.index:right.index + 1]
                    .min()
                )

                breakdown = (
                    data["close"]
                    .iloc[right.index:]
                    < neckline
                )

                if not breakdown.any():
                    continue

                breakout_index = breakdown.idxmax()

                results.append(
                    PatternResult(
                        pattern=self.name,
                        start_index=left.timestamp,
                        end_index=breakout_index,
                        confidence=90.0,
                        metadata={
                            "left_peak": left.price,
                            "right_peak": right.price,
                            "neckline": neckline,
                        },
                    )
                )

                break

        return results