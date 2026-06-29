import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine
from app.indicators.indicator_registry import IndicatorRegistry
from app.indicators.indicator_type import IndicatorType

from app.indicators.rsi import RSIIndicator
from app.indicators.atr import ATRIndicator


def test_engine_rsi_execution():
    data = pd.DataFrame(
        {
            "close": [10, 11, 12, 11, 10, 11, 13, 12, 14, 15]
        }
    )

    registry = IndicatorRegistry()
    registry.register(IndicatorType.RSI, RSIIndicator)

    engine = IndicatorEngine(
        history=data,
        registry=registry,
    )

    result = engine.calculate(
        IndicatorType.RSI,
        period=5,
    )

    assert result is not None
    assert len(result) == len(data)


def test_engine_atr_execution():
    data = pd.DataFrame(
        {
            "high": [10, 12, 13, 14, 15, 16, 17],
            "low": [9, 10, 11, 12, 13, 14, 15],
            "close": [9.5, 11, 12, 13, 14, 15, 16],
        }
    )

    registry = IndicatorRegistry()
    registry.register(IndicatorType.ATR, ATRIndicator)

    engine = IndicatorEngine(
        history=data,
        registry=registry,
    )

    result = engine.calculate(
        IndicatorType.ATR,
        period=3,
    )

    assert result is not None
    assert len(result) == len(data)