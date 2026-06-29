"""
===============================================================================
Volatility Contraction Pattern (VCP)
===============================================================================

Stage-2 Volatility Contraction Pattern based on
Mark Minervini methodology.

Current implementation:

✓ Swing detection
✓ Contraction calculation
✓ Higher low validation

Next milestones:

- Volume contraction
- Pivot resistance
- Breakout confirmation
- Relative Strength
- Trend Template
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from app.patterns.base_pattern import BasePattern
from app.patterns.pattern_result import PatternResult
from app.patterns.swing_points import SwingPoint, SwingPointDetector


@dataclass(slots=True)
class Contraction:

    high: float

    low: float

    percent: float

    start_index: int

    end_index: int


class VCP(BasePattern):

    name = "VCP"

    def detect(
        self,
        data: pd.DataFrame,
    ) -> PatternResult:

        detector = SwingPointDetector()

        swings = detector.detect(data)

        contractions = self._find_contractions(swings)

        valid = self._is_valid_sequence(contractions)

        return PatternResult(
            pattern=self.name,
            detected=valid,
            score=float(len(contractions)),
            metadata={
                "contractions": len(contractions),
            },
        )

    def _find_contractions(
        self,
        swings: list[SwingPoint],
    ) -> list[Contraction]:

        contractions: list[Contraction] = []

        highs = [s for s in swings if s.is_high]
        lows = [s for s in swings if not s.is_high]

        pairs = min(len(highs), len(lows))

        for i in range(pairs):

            high = highs[i]
            low = lows[i]

            decline = (high.price - low.price) / high.price * 100

            contractions.append(
                Contraction(
                    high=high.price,
                    low=low.price,
                    percent=decline,
                    start_index=high.index,
                    end_index=low.index,
                )
            )

        return contractions

    def _is_valid_sequence(
        self,
        contractions: list[Contraction],
    ) -> bool:

        if len(contractions) < 2:
            return False

        values = [c.percent for c in contractions]

        return all(
            values[i] > values[i + 1]
            for i in range(len(values) - 1)
        )