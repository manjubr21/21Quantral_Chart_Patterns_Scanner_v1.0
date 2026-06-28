"""
===============================================================================
Indicator Cache
===============================================================================
"""

from __future__ import annotations


class IndicatorCache:
    """
    Stores already calculated indicators.
    """

    def __init__(self):

        self._cache: dict[str, object] = {}

    def has(self, key: str) -> bool:

        return key in self._cache

    def get(self, key: str):

        return self._cache[key]

    def set(self, key: str, value):

        self._cache[key] = value

    def clear(self):

        self._cache.clear()

    def size(self):

        return len(self._cache)