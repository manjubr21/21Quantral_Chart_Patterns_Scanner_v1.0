"""
===============================================================================
Head And Shoulders Pattern
===============================================================================

Production implementation of the Head & Shoulders reversal pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class HeadAndShoulders(BaseSwingPattern):
    """
    Head & Shoulders detector.
    """

    name = "HEAD_AND_SHOULDERS"

    description = (
        "Bearish reversal consisting of a left shoulder, "
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

        highs = SwingPoints.highs(
            data,
            self.swing_window,
        )

        results: list[PatternResult] = []

        if len(highs) < 3:
            return results

        for i in range(len(highs) - 2):

            left = highs[i]
            head = highs[i + 1]
            right = highs[i + 2]

            if right.index - left.index > self.lookback:
                continue

            # Head must be highest
            if head.price <= left.price:
                continue

            if head.price <= right.price:
                continue

            # Head should clearly exceed shoulders
            if (
                head.price
                < max(left.price, right.price)
                * (1 + self.head_margin)
            ):
                continue

            # Shoulders approximately equal
            shoulder_difference = abs(
                left.price - right.price
            ) / left.price

            if shoulder_difference > self.shoulder_tolerance:
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

            breakdown_index = breakdown.idxmax()

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=left.timestamp,
                    end_index=breakdown_index,
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