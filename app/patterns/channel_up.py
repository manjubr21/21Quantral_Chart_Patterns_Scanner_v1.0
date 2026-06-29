"""
===============================================================================
Channel Up Pattern
===============================================================================

Production implementation of the Channel Up pattern.
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_swing_pattern import BaseSwingPattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoints


class ChannelUp(BaseSwingPattern):
    """
    Ascending Price Channel detector.
    """

    name = "CHANNEL_UP"

    description = (
        "Bullish price channel formed by higher highs "
        "and higher lows moving in parallel."
    )

    max_width_change: float = 0.15

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

        if pair_count < 3:
            return results

        for i in range(pair_count - 2):

            high1 = highs[i]
            high2 = highs[i + 1]
            high3 = highs[i + 2]

            low1 = lows[i]
            low2 = lows[i + 1]
            low3 = lows[i + 2]

            if not (
                high1.price < high2.price < high3.price
            ):
                continue

            if not (
                low1.price < low2.price < low3.price
            ):
                continue

            width1 = high1.price - low1.price
            width2 = high2.price - low2.price
            width3 = high3.price - low3.price

            average_width = (
                width1 + width2 + width3
            ) / 3

            if average_width <= 0:
                continue

            if (
                abs(width1 - average_width) / average_width
                > self.max_width_change
            ):
                continue

            if (
                abs(width2 - average_width) / average_width
                > self.max_width_change
            ):
                continue

            if (
                abs(width3 - average_width) / average_width
                > self.max_width_change
            ):
                continue

            results.append(
                PatternResult(
                    pattern=self.name,
                    start_index=min(
                        high1.timestamp,
                        low1.timestamp,
                    ),
                    end_index=max(
                        high3.timestamp,
                        low3.timestamp,
                    ),
                    confidence=87.0,
                    metadata={
                        "upper_channel": high3.price,
                        "lower_channel": low3.price,
                        "channel_width": round(
                            average_width,
                            4,
                        ),
                    },
                )
            )

        return results