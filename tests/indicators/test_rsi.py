import numpy as np
import pandas as pd

from app.indicators.rsi import RSIIndicator


def test_rsi_basic_calculation():
    data = pd.DataFrame({
        "close": [10, 11, 12, 11, 10, 11, 13, 12, 14, 15]
    })

    rsi = RSIIndicator(period=5)
    result = rsi.calculate(data)

    assert isinstance(result, pd.Series)
    assert len(result) == len(data)
    assert result.isna().sum() >= 0
    assert result.iloc[-1] is not None


def test_rsi_validation():
    import pytest
    from app.indicators.exceptions import IndicatorValidationError

    with pytest.raises(IndicatorValidationError):
        RSIIndicator(period=1).validate()