"""
===============================================================================
Pattern Detector
===============================================================================

Abstract base class for all production chart pattern detectors.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.patterns.pattern_context import PatternContext
from app.patterns.pattern_result import PatternResult


class PatternDetector(ABC):
    """
    Base interface implemented by every chart pattern detector.
    """

    name: str = "UNKNOWN"

    description: str = ""

    enabled: bool = True

    @abstractmethod
    def detect(
        self,
        context: PatternContext,
    ) -> list[PatternResult]:
        """
        Detect chart patterns.

        Parameters
        ----------
        context
            Detection context.

        Returns
        -------
        list[PatternResult]
            All detected patterns.
        """
        raise NotImplementedError

    def supports(
        self,
        context: PatternContext,
    ) -> bool:
        """
        Override if a detector requires specific data.
        """
        return self.enabled

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"