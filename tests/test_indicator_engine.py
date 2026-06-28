import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine
from app.indicators.indicator_registry import IndicatorRegistry

from app.indicators.sma import SMA
from app.indicators.ema import EMA


def test_indicator_engine():

    history = pd.DataFrame(
        {
            "Close": [1,2,3,4,5,6,7,8,9,10]
        }
    )

    registry = IndicatorRegistry()

    registry.register(SMA())
    registry.register(EMA())

    engine = IndicatorEngine(
        history=history,
        registry=registry,
    )

    sma1 = engine.calculate(
        "SMA",
        period=5,
    )

    sma2 = engine.calculate(
        "SMA",
        period=5,
    )

    assert sma1.equals(sma2)

    assert engine.cache.size() == 1