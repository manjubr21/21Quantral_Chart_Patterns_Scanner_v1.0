import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine
from app.indicators.indicator_registry import IndicatorRegistry
from app.indicators.indicator_type import IndicatorType

from app.indicators.sma import SMA
from app.indicators.ema import EMA


def test_indicator_engine():
    history = pd.DataFrame(
        {
            "close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }
    )

    registry = IndicatorRegistry()

    registry.register(IndicatorType.SMA, SMA)
    registry.register(IndicatorType.EMA, EMA)

    engine = IndicatorEngine(
        history=history,
        registry=registry,
    )

    sma1 = engine.calculate(
        IndicatorType.SMA,
        period=5,
    )

    sma2 = engine.calculate(
        IndicatorType.SMA,
        period=5,
    )

    assert sma1.equals(sma2)

    assert len(engine.cache) == 1