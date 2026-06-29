"""
Pattern Engine

Executes registered chart pattern detectors.

Author: 21Quantral
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from app.patterns.base_pattern import BasePattern
from app.patterns.pattern_registry import PatternRegistry
from app.patterns.pattern_result import PatternResult


class PatternEngine:
    """
    Executes registered chart pattern detectors.
    """

    def __init__(self, registry: PatternRegistry | None = None) -> None:
        """
        Initialize the pattern engine.

        Parameters
        ----------
        registry : PatternRegistry | None
            Optional registry instance.
        """
        self._registry = registry or PatternRegistry()

    @property
    def registry(self) -> PatternRegistry:
        """
        Return the pattern registry.
        """
        return self._registry

    def register(self, pattern: BasePattern) -> None:
        """
        Register a pattern detector.
        """
        self._registry.register(pattern)

    def calculate(
        self,
        pattern_name: str,
        data: pd.DataFrame,
        **kwargs: Any,
    ) -> PatternResult:
        """
        Execute a single pattern detector.

        Parameters
        ----------
        pattern_name : str
            Registered pattern name.

        data : pd.DataFrame
            OHLCV dataframe.

        kwargs
            Pattern-specific parameters.

        Returns
        -------
        PatternResult
        """
        pattern = self._registry.get(pattern_name)
        return pattern.calculate(data=data, **kwargs)

    def calculate_all(
        self,
        data: pd.DataFrame,
        **kwargs: Any,
    ) -> list[PatternResult]:
        """
        Execute all registered patterns.

        Parameters
        ----------
        data : pd.DataFrame
            OHLCV dataframe.

        kwargs
            Optional parameters passed to every detector.

        Returns
        -------
        list[PatternResult]
        """
        results: list[PatternResult] = []

        for pattern in self._registry:
            result = pattern.calculate(
                data=data,
                **kwargs,
            )
            results.append(result)

        return results

    def detected_patterns(
        self,
        data: pd.DataFrame,
        **kwargs: Any,
    ) -> list[PatternResult]:
        """
        Return only detected patterns.
        """
        return [
            result
            for result in self.calculate_all(data, **kwargs)
            if result.detected
        ]

    def clear(self) -> None:
        """
        Remove all registered patterns.
        """
        self._registry.clear()

    def __len__(self) -> int:
        return len(self._registry)

    def __repr__(self) -> str:
        return (
            f"PatternEngine("
            f"{len(self)} registered patterns)"
        )