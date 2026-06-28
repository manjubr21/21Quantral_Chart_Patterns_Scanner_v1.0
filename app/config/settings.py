"""
===============================================================================
Project : 21Quantral_Chart_Patterns_Scanner_v1.0
File    : settings.py
Version : 1.0.0
===============================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from app.common.constants import PROJECT_ROOT


@dataclass(slots=True)
class Settings:
    """
    Global application settings.

    In Version 1.0 these values are defaults.

    In Version 1.1 they will automatically load from
    config/settings.yaml.
    """

    app_name: str = "21Quantral Chart Patterns Scanner"

    version: str = "1.0.0"

    database_name: str = "21quantral.db"

    log_file: str = "21quantral.log"

    data_provider: str = "Yahoo Finance"

    default_timeframe: str = "1d"

    max_workers: int = 8

    debug: bool = False

    project_root: Path = PROJECT_ROOT