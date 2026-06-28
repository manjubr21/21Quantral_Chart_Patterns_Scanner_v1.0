import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine
from app.indicators.indicator_request import IndicatorRequest
from app.indicators.indicator_type import IndicatorType


def test_engine_rsi_execution():
    data = pd.DataFrame({
        "close": [10, 11, 12, 11, 10, 11, 13, 12, 14, 15]
    })

    engine = IndicatorEngine()
    result = engine.calculate(
        IndicatorRequest(
            indicator=IndicatorType.RSI,
            period=5,
        ),
        data=data,
    )

    assert result is not None
    assert len(result) == len(data)


def test_engine_atr_execution():
    data = pd.DataFrame({
        "high": [10, 12, 13, 14, 15, 16, 17],
        "low": [9, 10, 11, 12, 13, 14, 15],
        "close": [9.5, 11, 12, 13, 14, 15, 16],
    })

    engine = IndicatorEngine()
    result = engine.calculate(
        IndicatorRequest(
            indicator=IndicatorType.ATR,
            period=3,
        ),
        data=data,
    )

    assert result is not None
    assert len(result) == len(data)