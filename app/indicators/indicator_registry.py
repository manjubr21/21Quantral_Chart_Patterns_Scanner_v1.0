"""
===============================================================================
Indicator Registry
===============================================================================

Central registry for all supported indicators.
"""

from __future__ import annotations

from typing import Dict, Type

from app.indicators.base import BaseIndicator
from app.indicators.exceptions import IndicatorNotFoundError
from app.indicators.indicator_type import IndicatorType


class IndicatorRegistry:
    """
    Registry mapping IndicatorType to indicator implementation classes.
    """

    def __init__(self) -> None:
        self._registry: Dict[
            IndicatorType,
            Type[BaseIndicator],
        ] = {}

    def register(
        self,
        indicator_type: IndicatorType,
        indicator_class: Type[BaseIndicator],
    ) -> None:
        """
        Register an indicator implementation.

        Args:
            indicator_type:
                Indicator enum.

            indicator_class:
                Indicator implementation.
        """
        self._registry[indicator_type] = indicator_class

    def unregister(
        self,
        indicator_type: IndicatorType,
    ) -> None:
        """
        Remove an indicator.
        """
        self._registry.pop(indicator_type, None)

    def contains(
        self,
        indicator_type: IndicatorType,
    ) -> bool:
        """
        Returns:
            True if indicator exists.
        """
        return indicator_type in self._registry

    def get(
        self,
        indicator_type: IndicatorType,
    ) -> Type[BaseIndicator]:
        """
        Retrieve an indicator class.

        Args:
            indicator_type:
                Requested indicator.

        Raises:
            IndicatorNotFoundError

        Returns:
            Indicator implementation class.
        """
        try:
            return self._registry[indicator_type]
        except KeyError as exc:
            raise IndicatorNotFoundError(
                f"{indicator_type} is not registered."
            ) from exc

    def registered(self) -> tuple[IndicatorType, ...]:
        """
        Returns:
            Registered indicator types.
        """
        return tuple(sorted(self._registry.keys(), key=str))

    def clear(self) -> None:
        """
        Remove every registration.
        """
        self._registry.clear()

    def __len__(self) -> int:
        return len(self._registry)