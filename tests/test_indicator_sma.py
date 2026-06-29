import pandas as pd

from app.indicators.sma import SMA


def test_sma():
    df = pd.DataFrame(
        {
            "close": [1, 2, 3, 4, 5],
        }
    )

    sma = SMA()

    result = sma.calculate(
        df,
        period=3,
    )

    assert result.iloc[-1] == 4.0