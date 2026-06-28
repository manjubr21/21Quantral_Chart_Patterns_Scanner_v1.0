"""
===============================================================================
Indicator Result
===============================================================================

Immutable result object returned by the Indicator Engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

import pandas as pd

from app.indicators.indicator_request import IndicatorRequest


@dataclass(frozen=True, slots=True)
class IndicatorResult:
    """
    Represents the result of an indicator calculation.

    Attributes:
        request:
            Original indicator request.

        values:
            Calculated indicator values.

        created_at:
            UTC timestamp when the calculation completed.
    """

    request: IndicatorRequest

    values: pd.Series

    created_at: datetime

    @property
    def indicator(self) -> str:
        """
        Returns:
            Indicator name.
        """
        return str(self.request.indicator)

    @property
    def parameters(self) -> dict[str, object]:
        """
        Returns:
            Indicator parameters.
        """
        return self.request.parameters

    def tail(self, rows: int = 5) -> pd.Series:
        """
        Convenience wrapper around pandas.Series.tail().

        Args:
            rows:
                Number of rows.

        Returns:
            Tail of indicator values.
        """
        return self.values.tail(rows)

    def latest(self):
        """
        Returns:
            Latest calculated value.
        """
        return self.values.iloc[-1]

    def __len__(self) -> int:
        return len(self.values)

    def __repr__(self) -> str:
        return (
            "IndicatorResult("
            f"indicator={self.indicator}, "
            f"rows={len(self.values)}, "
            f"created_at={self.created_at.isoformat()})"
        )