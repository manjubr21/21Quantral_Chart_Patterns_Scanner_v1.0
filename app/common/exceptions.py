"""
===============================================================================
Project     : 21Quantral_Chart_Patterns_Scanner_v1.0
File        : exceptions.py
Version     : 1.0.0

Description:
    Custom exceptions for the application.

===============================================================================
"""

from __future__ import annotations


class QuantralError(Exception):
    """Base exception for the application."""


class ConfigurationError(QuantralError):
    """Raised when configuration is invalid."""


class DataProviderError(QuantralError):
    """Raised when market data cannot be retrieved."""


class PatternDetectionError(QuantralError):
    """Raised when pattern detection fails."""


class ScannerError(QuantralError):
    """Raised when the scanner encounters an error."""
    