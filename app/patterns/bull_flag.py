"""
===============================================================================
Bull Flag Pattern
===============================================================================
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_pattern import BasePattern
from app.patterns.pattern_result import PatternResult


class BullFlag(BasePattern):
    """
    Bull Flag pattern detector.

    Logic:
    1. Strong upward impulse.
    2. Short pullback.
    3. Pullback remains above 50% of impulse.
    """

    name = "Bull Flag"

    def detect(
        self,
        data: pd.DataFrame,
    ) -> PatternResult:

        if len(data) < 25:
            return PatternResult.not_found(self.name)

        close = data["close"].astype(float)

        impulse = close.iloc[-15] - close.iloc[-25]

        pullback = close.iloc[-1] - close.iloc[-15]

        if (
            impulse > 0
            and pullback < 0
            and abs(pullback) < impulse * 0.5
        ):
            confidence = min(
                1.0,
                abs(impulse) / close.iloc[-25],
            )

            return PatternResult(
                pattern=self.name,
                detected=True,
                confidence=confidence,
                metadata={
                    "impulse": float(impulse),
                    "pullback": float(pullback),
                },
            )

        return PatternResult.not_found(self.name)