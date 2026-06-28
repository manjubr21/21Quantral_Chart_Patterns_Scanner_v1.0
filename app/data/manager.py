"""
===============================================================================
Data Manager

Single entry point for all market data.

===============================================================================
"""

from __future__ import annotations

from app.data.registry import ProviderRegistry


class DataManager:

    def __init__(self, registry: ProviderRegistry):

        self._registry = registry

    def get_history(
        self,
        provider: str,
        symbol: str,
        timeframe: str,
        limit: int = 500,
    ):

        provider_instance = self._registry.get(provider)

        return provider_instance.get_history(
            symbol=symbol,
            timeframe=timeframe,
            limit=limit,
        )

    def get_symbols(self, provider: str):

        return self._registry.get(provider).get_symbols()
    