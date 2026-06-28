import pandas as pd

from app.indicators.atr import ATRIndicator


def test_atr_basic_calculation():
    data = pd.DataFrame({
        "high": [10, 12, 13, 14, 15, 16, 17],
        "low": [9, 10, 11, 12, 13, 14, 15],
        "close": [9.5, 11, 12, 13, 14, 15, 16],
    })

    atr = ATRIndicator(period=3)
    result = atr.calculate(data)

    assert isinstance(result, pd.Series)
    assert len(result) == len(data)


def test_atr_validation():
    import pytest
    from app.indicators.exceptions import IndicatorValidationError

    with pytest.raises(IndicatorValidationError):
        ATRIndicator(period=0).validate()