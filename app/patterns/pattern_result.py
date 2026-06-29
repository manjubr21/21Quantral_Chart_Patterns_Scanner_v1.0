"""
Pattern Result

Standard result object returned by every chart pattern detector.

Author: 21Quantral
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class PatternResult:
    """
    Standard output returned by every pattern detector.

    Attributes
    ----------
    pattern_name : str
        Name of the detected pattern.

    detected : bool
        True if the pattern was found.

    confidence : float
        Confidence score between 0.0 and 1.0.

    index : int | None
        Candle index where the pattern completes.

    metadata : dict[str, Any]
        Additional pattern-specific information.
    """

    pattern_name: str
    detected: bool
    confidence: float = 0.0
    index: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate confidence score."""
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError(
                "confidence must be between 0.0 and 1.0"
            )

    @property
    def found(self) -> bool:
        """
        Alias for detected.

        Returns
        -------
        bool
            Detection status.
        """
        return self.detected

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the result to a dictionary.

        Returns
        -------
        dict[str, Any]
        """
        return {
            "pattern_name": self.pattern_name,
            "detected": self.detected,
            "confidence": self.confidence,
            "index": self.index,
            "metadata": self.metadata,
        }

    def __bool__(self) -> bool:
        """
        Allow:

            if result:

        instead of

            if result.detected:
        """
        return self.detected

    def __repr__(self) -> str:
        return (
            f"PatternResult("
            f"pattern_name='{self.pattern_name}', "
            f"detected={self.detected}, "
            f"confidence={self.confidence:.2f}, "
            f"index={self.index})"
        )