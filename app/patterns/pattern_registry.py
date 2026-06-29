"""
Pattern Registry

Central registry for all chart pattern detectors.

Author: 21Quantral
"""

from __future__ import annotations

from typing import Dict

from app.patterns.base_pattern import BasePattern


class PatternRegistry:
    """
    Registry for all chart pattern detectors.

    Example
    -------
    >>> registry = PatternRegistry()
    >>> registry.register(DoubleBottomPattern())
    >>> registry.get("double_bottom")
    """

    def __init__(self) -> None:
        self._patterns: Dict[str, BasePattern] = {}

    def register(self, pattern: BasePattern) -> None:
        """
        Register a pattern detector.

        Parameters
        ----------
        pattern : BasePattern
            Pattern instance.
        """
        if not pattern.name:
            raise ValueError("Pattern must define a name.")

        key = pattern.name.lower()

        if key in self._patterns:
            raise ValueError(
                f"Pattern '{pattern.name}' is already registered."
            )

        self._patterns[key] = pattern

    def unregister(self, name: str) -> None:
        """
        Remove a registered pattern.

        Parameters
        ----------
        name : str
            Pattern name.
        """
        self._patterns.pop(name.lower(), None)

    def get(self, name: str) -> BasePattern:
        """
        Retrieve a registered pattern.

        Parameters
        ----------
        name : str
            Pattern name.

        Returns
        -------
        BasePattern
        """
        key = name.lower()

        if key not in self._patterns:
            raise KeyError(f"Pattern '{name}' is not registered.")

        return self._patterns[key]

    def exists(self, name: str) -> bool:
        """
        Check whether a pattern is registered.
        """
        return name.lower() in self._patterns

    def clear(self) -> None:
        """
        Remove all registered patterns.
        """
        self._patterns.clear()

    def names(self) -> list[str]:
        """
        Return sorted pattern names.
        """
        return sorted(self._patterns.keys())

    def patterns(self) -> Dict[str, BasePattern]:
        """
        Return a shallow copy of registered patterns.
        """
        return self._patterns.copy()

    def __len__(self) -> int:
        return len(self._patterns)

    def __contains__(self, name: str) -> bool:
        return self.exists(name)

    def __iter__(self):
        return iter(self._patterns.values())

    def __repr__(self) -> str:
        return (
            f"PatternRegistry("
            f"{len(self._patterns)} registered patterns)"
        )