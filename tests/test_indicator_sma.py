import pandas as pd

from app.indicators.sma import SMA


def test_sma():

    df = pd.DataFrame(
        {
            "Close": [1, 2, 3, 4, 5]
        }
    )

    sma = SMA(3)

    result = sma.calculate(df)

    assert round(result.iloc[-1], 2) == 4.0