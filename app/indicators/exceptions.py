"""
===============================================================================
Indicator Exceptions
===============================================================================
"""


class IndicatorError(Exception):
    """Base indicator exception."""


class IndicatorNotFoundError(IndicatorError):
    """Raised when an indicator is unavailable."""


class InvalidPeriodError(IndicatorError):
    """Raised when an invalid indicator period is supplied."""