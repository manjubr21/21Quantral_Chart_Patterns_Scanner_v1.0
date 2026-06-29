"""
===============================================================================
Descending Triangle Pattern
===============================================================================

Production implementation of the Descending Triangle continuation pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class DescendingTriangle(BaseSwingPattern):
    """
    Descending Triangle detector.
    """

    name = "DESCENDING_TRIANGLE"

    description = (
        "Bearish continuation pattern consisting of "
        "lower highs against horizontal support."
    )

    support_tolerance: float = 0.02

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

        for i in range(len(lows) - 1):

            support1 = lows[i]
            support2 = lows[i + 1]

            difference = abs(
                support1.price - support2.price
            ) / support1.price

            if difference > self.support_tolerance:
                continue

            pattern_highs = [
                high
                for high in highs
                if support1.index < high.index < support2.index
            ]

            if len(pattern_highs) < 2:
                continue

            lower_highs = all(
                pattern_highs[k].price <
                pattern_highs[k - 1].price
                for k in range(1, len(pattern_highs))
            )

            if not lower_highs:
                continue

            support = (
                support1.price + support2.price
            ) / 2

            breakdown = (
                data["close"]
                .iloc[support2.index:]
                < support
            )

            if not breakdown.any():
                continue

            breakdown_index = breakdown.idxmax()

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=support1.timestamp,
                    end_index=breakdown_index,
                    confidence=90.0,
                    metadata={
                        "support": support,
                        "lower_highs": len(pattern_highs),
                    },
                )
            )

        return results