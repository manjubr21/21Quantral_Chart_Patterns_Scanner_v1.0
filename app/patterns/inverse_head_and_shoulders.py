"""
===============================================================================
Inverse Head And Shoulders Pattern
===============================================================================

Production implementation of the Inverse Head & Shoulders reversal pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class InverseHeadAndShoulders(BaseSwingPattern):
    """
    Inverse Head & Shoulders detector.
    """

    name = "INVERSE_HEAD_AND_SHOULDERS"

    description = (
        "Bullish reversal consisting of a left shoulder, "
        "head and right shoulder."
    )

    shoulder_tolerance: float = 0.03

    head_margin: float = 0.02

    def detect(
        self,
        data: pd.DataFrame,
    ) -> list[PatternResult]:

        if not self.validate(data):
            return []

        data = data.copy()
        data.columns = [c.lower() for c in data.columns]

        lows = SwingPoints.lows(
            data,
            self.swing_window,
        )

        results: list[PatternResult] = []

        if len(lows) < 3:
            return results

        for i in range(len(lows) - 2):

            left = lows[i]
            head = lows[i + 1]
            right = lows[i + 2]

            if right.index - left.index > self.lookback:
                continue

            # Head must be lowest
            if head.price >= left.price:
                continue

            if head.price >= right.price:
                continue

            # Head should clearly exceed shoulders
            if (
                head.price
                > min(left.price, right.price)
                * (1 - self.head_margin)
            ):
                continue

            # Shoulders approximately equal
            shoulder_difference = abs(
                left.price - right.price
            ) / left.price

            if shoulder_difference > self.shoulder_tolerance:
                continue

            neckline = (
                data["high"]
                .iloc[left.index:right.index + 1]
                .max()
            )

            breakout = (
                data["close"]
                .iloc[right.index:]
                > neckline
            )

            if not breakout.any():
                continue

            breakout_index = breakout.idxmax()

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=left.timestamp,
                    end_index=breakout_index,
                    confidence=92.0,
                    metadata={
                        "left_shoulder": left.price,
                        "head": head.price,
                        "right_shoulder": right.price,
                        "neckline": neckline,
                    },
                )
            )

        return results