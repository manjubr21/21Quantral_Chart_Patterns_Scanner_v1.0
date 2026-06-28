"""
===============================================================================
Indicator Cache
===============================================================================

Simple in-memory cache for indicator calculation results.
"""

from __future__ import annotations

from typing import Dict

from app.indicators.indicator_result import IndicatorResult


class IndicatorCache:
    """
    In-memory cache for indicator results.
    """

    def __init__(self) -> None:
        self._cache: Dict[str, IndicatorResult] = {}

    def has(self, key: str) -> bool:
        """
        Check whether a cache key exists.

        Args:
            key:
                Cache key.

        Returns:
            True if present.
        """
        return key in self._cache

    def get(self, key: str) -> IndicatorResult:
        """
        Retrieve a cached result.

        Args:
            key:
                Cache key.

        Raises:
            KeyError:
                If the key is not present.

        Returns:
            Cached IndicatorResult.
        """
        return self._cache[key]

    def set(
        self,
        key: str,
        result: IndicatorResult,
    ) -> None:
        """
        Store a calculation result.

        Args:
            key:
                Cache key.

            result:
                Indicator result.
        """
        self._cache[key] = result

    def clear(self) -> None:
        """
        Clear all cached results.
        """
        self._cache.clear()

    def __contains__(self, key: str) -> bool:
        return self.has(key)

    def __len__(self) -> int:
        return len(self._cache)