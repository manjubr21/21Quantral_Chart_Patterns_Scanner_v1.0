"""
===============================================================================
Indicator Exceptions
===============================================================================
"""


class IndicatorError(Exception):
    """Base indicator exception."""


class IndicatorRegistrationError(IndicatorError):
    """Raised when an indicator cannot be registered."""


class IndicatorCalculationError(IndicatorError):
    """Raised when an indicator calculation fails."""