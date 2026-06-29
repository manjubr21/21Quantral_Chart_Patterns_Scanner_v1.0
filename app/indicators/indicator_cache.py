"""
===============================================================================
Indicator Cache
===============================================================================

Simple in-memory cache for indicator calculation results.
"""

from __future__ import annotations

from typing import Any


class IndicatorCache:
    """
    In-memory cache for indicator results.
    """

    def __init__(self) -> None:
        self._cache: dict[str, Any] = {}

    def has(self, key: str) -> bool:
        return key in self._cache

    def get(self, key: str) -> Any:
        return self._cache[key]

    def set(
        self,
        key: str,
        result: Any,
    ) -> None:
        self._cache[key] = result

    def clear(self) -> None:
        self._cache.clear()

    def size(self) -> int:
        return len(self._cache)

    def __contains__(self, key: str) -> bool:
        return self.has(key)

    def __len__(self) -> int:
        return len(self._cache)