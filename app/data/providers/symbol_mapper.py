"""
===============================================================================
Project : 21Quantral Chart Patterns Scanner

Converts internal symbols to provider symbols.

===============================================================================
"""

from __future__ import annotations


class SymbolMapper:

    @staticmethod
    def yahoo(symbol: str) -> str:
        """
        RELIANCE -> RELIANCE.NS
        """

        symbol = symbol.upper()

        if symbol.endswith(".NS"):
            return symbol

        return f"{symbol}.NS"

    @staticmethod
    def shoonya(symbol: str) -> str:
        """
        Placeholder.

        Will later translate symbol into Shoonya token.
        """

        return symbol.upper()

    @staticmethod
    def mstock(symbol: str) -> str:

        return symbol.upper()