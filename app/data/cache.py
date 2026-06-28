"""
Simple in-memory cache.

Version 1

Later this will become Redis compatible.
"""

from __future__ import annotations


class MemoryCache:

    def __init__(self):

        self._cache = {}

    def put(self, key, value):

        self._cache[key] = value

    def get(self, key):

        return self._cache.get(key)

    def exists(self, key):

        return key in self._cache

    def clear(self):

        self._cache.clear()