import pandas as pd

from app.indicators.indicator_engine import IndicatorEngine


def test_cache():

    df = pd.DataFrame(

        {

            "Close": [1,2,3,4,5,6,7,8,9,10]

        }

    )

    engine = IndicatorEngine(df)

    sma1 = engine.sma(5)

    sma2 = engine.sma(5)

    assert sma1.equals(sma2)

    assert engine.cache.size() == 1