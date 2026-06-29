"""
===============================================================================
Rectangle Pattern
===============================================================================

Production implementation of the Rectangle consolidation pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class Rectangle(BaseSwingPattern):
    """
    Rectangle consolidation detector.

    Detects horizontal trading ranges where both highs
    and lows remain nearly constant.
    """

    name = "RECTANGLE"

    description = (
        "Horizontal consolidation bounded by nearly "
        "equal resistance and support."
    )

    tolerance: float = 0.02

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

        if len(highs) < 3 or len(lows) < 3:
            return []

        results: list[PatternResult] = []

        pair_count = min(
            len(highs),
            len(lows),
        )

        for i in range(pair_count - 2):

            high_points = [
                highs[i],
                highs[i + 1],
                highs[i + 2],
            ]

            low_points = [
                lows[i],
                lows[i + 1],
                lows[i + 2],
            ]

            high_prices = [
                p.price
                for p in high_points
            ]

            low_prices = [
                p.price
                for p in low_points
            ]

            resistance = sum(high_prices) / 3
            support = sum(low_prices) / 3

            if support <= 0:
                continue

            if (
                max(high_prices) - min(high_prices)
            ) / resistance > self.tolerance:
                continue

            if (
                max(low_prices) - min(low_prices)
            ) / support > self.tolerance:
                continue

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=min(
                        high_points[0].timestamp,
                        low_points[0].timestamp,
                    ),
                    end_index=max(
                        high_points[-1].timestamp,
                        low_points[-1].timestamp,
                    ),
                    confidence=90.0,
                    metadata={
                        "resistance": round(
                            resistance,
                            4,
                        ),
                        "support": round(
                            support,
                            4,
                        ),
                        "range": round(
                            resistance - support,
                            4,
                        ),
                    },
                )
            )

        return results