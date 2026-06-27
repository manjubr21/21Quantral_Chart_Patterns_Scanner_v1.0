"""
===============================================================================
Project     : 21Quantral_Chart_Patterns_Scanner_v1.0
File        : app/core/__init__.py
Version     : 1.0.0

Author      : Manjunatha Ramachandra
Co-Developer: OpenAI ChatGPT

Description:
    Core package.

    This package contains the application's central framework,
    lifecycle management, startup sequence and future dependency
    injection components.

===============================================================================
"""

from __future__ import annotations

from .application import Application

__all__ = [
    "Application",
]