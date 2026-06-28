"""
===============================================================================
Indicator Cache
===============================================================================
"""

from __future__ import annotations


class IndicatorCache:

    def __init__(self):

        self._cache: dict[str, object] = {}

    def has(self, key: str) -> bool:

        return key in self._cache

    def get(self, key: str):

        return self._cache[key]

    def set(self, key: str, value) -> None:

        self._cache[key] = value

    def clear(self) -> None:

        self._cache.clear()

    def size(self) -> int:

        return len(self._cache)

    def __len__(self):

        return len(self._cache)