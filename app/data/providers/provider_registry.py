"""
===============================================================================
Project : 21Quantral Chart Patterns Scanner
File    : provider_registry.py

Production Provider Registry

Author      : Manjunatha Ramachandra
Co-Developer: OpenAI ChatGPT
===============================================================================
"""

from __future__ import annotations

from typing import Dict

from app.data.providers.base_provider import BaseDataProvider


class ProviderRegistry:
    """
    Registry for all market data providers.

    Example
    -------
    >>> registry = ProviderRegistry()
    >>> registry.register(YahooProvider())
    >>> provider = registry.get("yahoo")
    """

    def __init__(self) -> None:
        self._providers: Dict[str, BaseDataProvider] = {}

    def register(self, provider: BaseDataProvider) -> None:
        """Register a provider instance."""
        name = provider.name.lower()

        if name in self._providers:
            raise ValueError(f"Provider '{name}' already registered.")

        self._providers[name] = provider

    def unregister(self, name: str) -> None:
        """Remove a provider."""
        self._providers.pop(name.lower(), None)

    def get(self, name: str) -> BaseDataProvider:
        """Return a registered provider."""
        key = name.lower()

        if key not in self._providers:
            available = ", ".join(self.list()) or "None"
            raise LookupError(
                f"Provider '{name}' not found. "
                f"Available providers: {available}"
            )

        return self._providers[key]

    def exists(self, name: str) -> bool:
        """Check whether a provider exists."""
        return name.lower() in self._providers

    def list(self) -> list[str]:
        """Return provider names."""
        return sorted(self._providers.keys())

    def clear(self) -> None:
        """Remove all providers."""
        self._providers.clear()

    def __len__(self) -> int:
        return len(self._providers)

    def __contains__(self, item: str) -> bool:
        return self.exists(item)