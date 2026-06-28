"""
Data related exceptions.
"""


class DataProviderError(Exception):
    """Raised when a provider fails."""


class InvalidSymbolError(Exception):
    """Invalid NSE symbol."""


class InvalidTimeFrameError(Exception):
    """Unsupported timeframe."""