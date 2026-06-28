from app.indicators.indicator_registry import IndicatorRegistry

from app.indicators.sma import SMA

from app.indicators.ema import EMA


def test_registry():

    registry = IndicatorRegistry()

    registry.register(SMA())

    registry.register(EMA())

    assert len(registry) == 2

    assert registry.get("SMA").name == "SMA"

    assert registry.get("EMA").name == "EMA"