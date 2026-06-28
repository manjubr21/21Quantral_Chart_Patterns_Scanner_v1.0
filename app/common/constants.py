"""
===============================================================================
Project     : 21Quantral_Chart_Patterns_Scanner_v1.0
File        : constants.py
Version     : 1.0.0

Author      : Manjunatha Ramachandra
Co-Developer: OpenAI ChatGPT

Description:
    Application-wide constants.

===============================================================================
"""

from __future__ import annotations

from pathlib import Path

# =============================================================================
# Application
# =============================================================================

APP_NAME: str = "21Quantral Chart Patterns Scanner"
APP_SHORT_NAME: str = "21Quantral"

# =============================================================================
# Project
# =============================================================================

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

# =============================================================================
# Directories
# =============================================================================

APP_DIR: Path = PROJECT_ROOT / "app"
CONFIG_DIR: Path = PROJECT_ROOT / "config"
DATA_DIR: Path = PROJECT_ROOT / "data"
DOCS_DIR: Path = PROJECT_ROOT / "docs"
EXPORTS_DIR: Path = PROJECT_ROOT / "exports"
LOGS_DIR: Path = PROJECT_ROOT / "logs"
REPORTS_DIR: Path = PROJECT_ROOT / "reports"
SCRIPTS_DIR: Path = PROJECT_ROOT / "scripts"
TESTS_DIR: Path = PROJECT_ROOT / "tests"

# =============================================================================
# Database
# =============================================================================

DATABASE_NAME: str = "21quantral.db"

# =============================================================================
# Logging
# =============================================================================

LOG_FILE: str = "21quantral.log"

# =============================================================================
# Timeframes
# =============================================================================

SUPPORTED_TIMEFRAMES: tuple[str, ...] = (
    "15m",
    "30m",
    "1h",
    "2h",
    "4h",
    "1d",
    "1wk",
    "1mo",
)