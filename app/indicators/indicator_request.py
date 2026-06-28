"""
===============================================================================
Indicator Request
===============================================================================

Immutable request object used by the Indicator Engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.indicators.indicator_type import IndicatorType


@dataclass(frozen=True, slots=True)
class IndicatorRequest:
    """
    Represents a request to calculate an indicator.

    Attributes:
        indicator:
            Indicator type.

        parameters:
            Indicator-specific parameters.
    """

    indicator: IndicatorType

    parameters: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        indicator: IndicatorType,
        **parameters: Any,
    ) -> "IndicatorRequest":
        """
        Convenience constructor.

        Example:
            request = IndicatorRequest.create(
                IndicatorType.SMA,
                period=20,
            )

        Args:
            indicator:
                Indicator type.

            **parameters:
                Indicator parameters.

        Returns:
            Immutable request object.
        """

        return cls(
            indicator=indicator,
            parameters=parameters,
        )

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a parameter.

        Args:
            key:
                Parameter name.

            default:
                Default value.

        Returns:
            Parameter value.
        """

        return self.parameters.get(key, default)

    def __repr__(self) -> str:
        """
        Developer-friendly representation.
        """

        return (
            f"IndicatorRequest("
            f"indicator={self.indicator}, "
            f"parameters={self.parameters})"
        )