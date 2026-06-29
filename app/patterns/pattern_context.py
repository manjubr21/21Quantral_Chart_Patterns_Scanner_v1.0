"""
===============================================================================
Pattern Context
===============================================================================

Shared context passed to every pattern detector.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine


@dataclass(slots=True)
class PatternContext:
    """
    Context shared across all pattern detectors.
    """

    data: pd.DataFrame

    indicator_engine: IndicatorEngine

    symbol: str = ""

    timeframe: str = ""

    metadata: dict = field(default_factory=dict)