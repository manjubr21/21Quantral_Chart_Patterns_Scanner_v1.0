"""
Manual Indicator Engine Test

This script is intended for manual verification of the
Indicator Engine. It is not a pytest unit test.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine
from app.indicators.indicator_registry import IndicatorRegistry
from app.indicators.indicator_type import IndicatorType

from app.indicators.sma import SMAIndicator
from app.indicators.ema import EMAIndicator


def main() -> None:
    history = pd.DataFrame(
        {
            "close": range(1, 101),
        }
    )

    registry = IndicatorRegistry()

    registry.register(
        IndicatorType.SMA,
        SMAIndicator,
    )

    registry.register(
        IndicatorType.EMA,
        EMAIndicator,
    )

    engine = IndicatorEngine(registry)

    print("\n===== SMA =====")

    sma = engine.calculate(
        IndicatorType.SMA,
        history,
        period=20,
    )

    print(sma.tail())

    print("\n===== EMA =====")

    ema = engine.calculate(
        IndicatorType.EMA,
        history,
        period=20,
    )

    print(ema.tail())


if __name__ == "__main__":
    main()