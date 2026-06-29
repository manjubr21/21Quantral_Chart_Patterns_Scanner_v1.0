from app.indicators.indicator_keys import IndicatorKey
from app.indicators.indicator_request import IndicatorRequest
from app.indicators.indicator_type import IndicatorType


def test_key_generation():

    request = IndicatorRequest(
        indicator=IndicatorType.SMA,
        parameters={
            "period": 20,
        },
    )

    key = IndicatorKey.build(request)

    assert key == "SMA|period=20"