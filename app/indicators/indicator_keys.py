"""
===============================================================================
Indicator Cache Keys
===============================================================================
"""

from __future__ import annotations


class IndicatorKey:

    @staticmethod
    def build(name: str, **kwargs) -> str:

        parameters = ",".join(
            f"{k}={v}"
            for k, v in sorted(kwargs.items())
        )

        return f"{name.upper()}:{parameters}"