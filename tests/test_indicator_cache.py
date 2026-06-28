from app.indicators.indicator_cache import IndicatorCache


def test_cache():

    cache = IndicatorCache()

    cache.set("ABC", 100)

    assert cache.has("ABC")

    assert cache.get("ABC") == 100

    assert cache.size() == 1

    cache.clear()

    assert cache.size() == 0