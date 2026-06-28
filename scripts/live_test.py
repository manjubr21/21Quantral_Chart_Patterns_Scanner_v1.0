"""
===============================================================================
Project : 21Quantral Chart Patterns Scanner

First Live Yahoo Finance Test

===============================================================================
"""

from pathlib import Path
import sys

# ----------------------------------------------------------------------
# Add project root to Python path
# ----------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ----------------------------------------------------------------------

from app.data.providers.yahoo_provider import YahooProvider


def main():

    provider = YahooProvider()

    candles = provider.get_history(
        symbol="RELIANCE",
        timeframe="1d",
        limit=10,
    )

    print("\n")
    print("=" * 80)
    print(f"Downloaded {len(candles)} candles")
    print("=" * 80)

    for candle in candles:
        print(candle)

    print("=" * 80)


if __name__ == "__main__":
    main()