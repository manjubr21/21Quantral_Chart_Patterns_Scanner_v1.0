import pandas as pd

from app.indicators.ema import EMA


def test_ema():

    df = pd.DataFrame(
        {
            "Close": [1, 2, 3, 4, 5]
        }
    )

    ema = EMA(3)

    result = ema.calculate(df)

    assert len(result) == 5