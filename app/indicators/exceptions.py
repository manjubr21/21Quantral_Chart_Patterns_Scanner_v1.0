"""
===============================================================================
Indicator Exceptions
===============================================================================

Custom exception hierarchy for the indicator framework.
"""

from __future__ import annotations


class IndicatorError(Exception):
    """
    Base exception for all indicator-related errors.
    """


class IndicatorValidationError(IndicatorError):
    """
    Raised when indicator parameters are invalid.
    """


class IndicatorCalculationError(IndicatorError):
    """
    Raised when an indicator calculation fails.
    """


class IndicatorRegistrationError(IndicatorError):
    """
    Raised when an indicator cannot be registered.
    """


class IndicatorNotFoundError(IndicatorError):
    """
    Raised when an indicator is not found in the registry.
    """


class IndicatorCacheError(IndicatorError):
    """
    Raised for cache-related failures.
    """