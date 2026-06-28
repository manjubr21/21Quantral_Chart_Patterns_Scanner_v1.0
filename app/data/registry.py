"""
===============================================================================
Project : 21Quantral Chart Patterns Scanner
File    : registry.py

Provider Registry

Registers every available data provider and returns provider instances.

===============================================================================
"""

from __future__ import annotations

from typing import Dict

from app.data.providers.base_provider import BaseDataProvider


class ProviderRegistry:
    """
    Registry of all available data providers.
    """

    def __init__(self) -> None:
        self._providers: Dict[str, BaseDataProvider] = {}

    def register(self, provider: BaseDataProvider) -> None:
        """
        Register a provider.
        """

        self._providers[provider.name.lower()] = provider

    def get(self, name: str) -> BaseDataProvider:
        """
        Retrieve a provider by name.
        """

        provider = self._providers.get(name.lower())

        if provider is None:
            raise ValueError(f"Unknown provider: {name}")

        return provider

    def list(self) -> list[str]:
        """
        Returns registered provider names.
        """

        return sorted(self._providers.keys())