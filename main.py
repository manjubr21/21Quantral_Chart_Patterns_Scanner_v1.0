"""
===============================================================================
Project     : 21Quantral_Chart_Patterns_Scanner_v1.0
File        : main.py
Version     : 1.0.1

Description:
    Application entry point.

===============================================================================
"""

from app.core import Application


def main() -> None:
    """Start the application."""

    app = Application()
    app.run()


if __name__ == "__main__":
    main()