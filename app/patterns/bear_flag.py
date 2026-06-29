"""
===============================================================================
Bear Flag Pattern
===============================================================================
"""

from __future__ import annotations

import pandas as pd

from app.patterns.base_pattern import BasePattern
from app.patterns.pattern_result import PatternResult


class BearFlag(BasePattern):
    """
    Bear Flag pattern detector.

    Logic:
    1. Strong downward impulse.
    2. Short upward retracement.
    3. Retracement remains below 50% of the impulse.
    """

    name = "Bear Flag"

    def detect(
        self,
        data: pd.DataFrame,
    ) -> PatternResult:

        if len(data) < 25:
            return PatternResult.not_found(self.name)

        close = data["close"].astype(float)

        impulse = close.iloc[-25] - close.iloc[-15]

        retracement = close.iloc[-1] - close.iloc[-15]

        if (
            impulse > 0
            and retracement > 0
            and retracement < impulse * 0.5
        ):

            confidence = min(
                1.0,
                impulse / close.iloc[-25],
            )

            return PatternResult(
                pattern=self.name,
                detected=True,
                confidence=confidence,
                metadata={
                    "impulse": float(impulse),
                    "retracement": float(retracement),
                },
            )

        return PatternResult.not_found(self.name)