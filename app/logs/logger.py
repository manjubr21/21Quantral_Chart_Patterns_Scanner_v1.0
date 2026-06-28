"""
Central logs module.
"""

from __future__ import annotations

import logging

LOGGER_NAME = "21Quantral"


def get_logger() -> logging.Logger:
    """
    Return application logger.
    """

    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(console)

    return logger