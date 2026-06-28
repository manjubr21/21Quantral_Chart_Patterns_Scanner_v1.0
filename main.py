"""
===============================================================================

Project     : 21Quantral_Chart_Patterns_Scanner_v1.0
File        : main.py
Version     : 1.0.2

Author      : Manjunatha Ramachandra
Co-Developer: OpenAI ChatGPT

Description:
    Application entry point.

===============================================================================
"""

from __future__ import annotations

from app.core import Application
from app.core.logger import configure_logging


def main() -> None:
    """
    Start the application.
    """

    configure_logging()

    app = Application()
    app.run()


if __name__ == "__main__":
    main()