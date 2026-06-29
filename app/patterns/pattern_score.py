"""
===============================================================================
Pattern Score
===============================================================================

Represents the confidence score of a detected chart pattern.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PatternScore:
    """
    Immutable pattern confidence score.
    """

    value: float

    max_score: float = 100.0

    def __post_init__(self) -> None:
        if self.max_score <= 0:
            raise ValueError("max_score must be greater than zero.")

        if not 0 <= self.value <= self.max_score:
            raise ValueError(
                f"Score must be between 0 and {self.max_score}."
            )

    @property
    def percentage(self) -> float:
        """
        Score as a percentage.
        """
        return (self.value / self.max_score) * 100.0

    @property
    def normalized(self) -> float:
        """
        Score normalized to [0, 1].
        """
        return self.value / self.max_score

    @property
    def passed(self) -> bool:
        """
        Default quality threshold.
        """
        return self.percentage >= 70.0

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.percentage:.1f}%"