"""
===============================================================================
Double Bottom Pattern
===============================================================================

Production implementation of the Double Bottom reversal pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult


class DoubleBottom(BaseSwingPattern):
    """
    Double Bottom detector.
    """

    name = "DOUBLE_BOTTOM"

    description = (
        "Bullish reversal consisting of two similar lows "
        "separated by a reaction high."
    )

    def detect(
        self,
        data: pd.DataFrame,
    ) -> list[PatternResult]:

        if not self.validate(data):
            return []

        data = data.copy()
        data.columns = [c.lower() for c in data.columns]

        lows = data["low"].values

        results: list[PatternResult] = []

        n = len(data)

        for i in range(
            self.swing_window,
            n - self.swing_window,
        ):

            left = lows[
                i - self.swing_window:i + self.swing_window + 1
            ]

            if lows[i] != left.min():
                continue

            for j in range(
                i + self.swing_window,
                min(i + self.lookback, n - self.swing_window),
            ):

                right = lows[
                    j - self.swing_window:
                    j + self.swing_window + 1
                ]

                if lows[j] != right.min():
                    continue

                diff = abs(
                    lows[i] - lows[j]
                ) / lows[i]

                if diff > self.tolerance:
                    continue

                neckline = (
                    data["high"]
                    .iloc[i:j + 1]
                    .max()
                )

                breakout = (
                    data["close"]
                    .iloc[j:]
                    > neckline
                )

                if not breakout.any():
                    continue

                breakout_index = breakout.idxmax()

                results.append(
                    PatternResult(
                        pattern=self.name,
                        start_index=data.index[i],
                        end_index=breakout_index,
                        confidence=90.0,
                        metadata={
                            "left_low": lows[i],
                            "right_low": lows[j],
                            "neckline": neckline,
                        },
                    )
                )

                break

        return results