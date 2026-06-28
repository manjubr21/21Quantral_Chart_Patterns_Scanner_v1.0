from app.indicators.indicator_keys import IndicatorKey


def test_key_generation():

    key = IndicatorKey.build(
        "SMA",
        period=20,
    )

    assert key == "SMA:period=20"