"""
===============================================================================
Project     : 21Quantral_Chart_Patterns_Scanner_v1.0
File        : app/common/version.py
Version     : 1.0.0

Description:
    Centralized version information for the application.

===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Version:
    """
    Immutable application version information.
    """

    project: str = "21Quantral Chart Patterns Scanner"
    repository: str = "21Quantral_Chart_Patterns_Scanner_v1.0"

    major: int = 1
    minor: int = 0
    patch: int = 0

    stage: str = "Development"

    @property
    def semantic_version(self) -> str:
        """Return semantic version."""

        return f"{self.major}.{self.minor}.{self.patch}"

    @property
    def full_version(self) -> str:
        """Return formatted application version."""

        return (
            f"{self.project} "
            f"v{self.semantic_version} "
            f"({self.stage})"
        )


VERSION = Version()