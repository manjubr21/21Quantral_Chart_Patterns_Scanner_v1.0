"""
Datetime helper functions.
"""

from datetime import datetime


def now() -> datetime:
    """
    Return current local datetime.
    """

    return datetime.now()