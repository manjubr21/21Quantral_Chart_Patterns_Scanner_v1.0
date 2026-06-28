from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine
from app.indicators.indicator_registry import IndicatorRegistry

from app.indicators.sma import SMA
from app.indicators.ema import EMA


history = pd.DataFrame(
    {
        "Close": range(1,101)
    }
)

registry = IndicatorRegistry()

registry.register(SMA())
registry.register(EMA())

engine = IndicatorEngine(
    history,
    registry,
)

print()

print("===== SMA =====")

print(
    engine.calculate(
        "SMA",
        period=20,
    ).tail()
)

print()

print("===== EMA =====")

print(
    engine.calculate(
        "EMA",
        period=20,
    ).tail()
)