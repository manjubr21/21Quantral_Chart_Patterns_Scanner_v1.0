"""
===============================================================================
Symmetrical Triangle Pattern
===============================================================================

Production implementation of the Symmetrical Triangle continuation pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class SymmetricalTriangle(BaseSwingPattern):
    """
    Symmetrical Triangle detector.
    """

    name = "SYMMETRICAL_TRIANGLE"

    description = (
        "Continuation pattern formed by converging "
        "higher lows and lower highs."
    )

    convergence_tolerance: float = 0.02

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

        pair_count = min(
            len(highs),
            len(lows),
        )

        for i in range(pair_count - 1):

            high1 = highs[i]
            high2 = highs[i + 1]

            low1 = lows[i]
            low2 = lows[i + 1]

            if high2.price >= high1.price:
                continue

            if low2.price <= low1.price:
                continue

            initial_range = high1.price - low1.price
            final_range = high2.price - low2.price

            if final_range >= initial_range:
                continue

            compression = (
                initial_range - final_range
            ) / initial_range

            if compression < self.convergence_tolerance:
                continue

            upper_line = high2.price
            lower_line = low2.price

            closes = data["close"].iloc[
                max(high2.index, low2.index):
            ]

            upside = closes > upper_line
            downside = closes < lower_line

            if upside.any():

                breakout = upside.idxmax()

                direction = "UP"

            elif downside.any():

                breakout = downside.idxmax()

                direction = "DOWN"

            else:
                continue

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=min(
                        high1.timestamp,
                        low1.timestamp,
                    ),
                    end_index=breakout,
                    confidence=88.0,
                    metadata={
                        "direction": direction,
                        "compression": round(
                            compression,
                            3,
                        ),
                        "upper_line": upper_line,
                        "lower_line": lower_line,
                    },
                )
            )

        return results