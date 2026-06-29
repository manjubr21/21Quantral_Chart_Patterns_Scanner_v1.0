from app.indicators.indicator_registry import IndicatorRegistry
from app.indicators.indicator_type import IndicatorType

from app.indicators.sma import SMAIndicator
from app.indicators.ema import EMAIndicator


def test_registry():
    registry = IndicatorRegistry()

    registry.register(
        IndicatorType.SMA,
        SMAIndicator,
    )

    registry.register(
        IndicatorType.EMA,
        EMAIndicator,
    )

    assert len(registry) == 2

    assert registry.get(IndicatorType.SMA) is SMAIndicator

    assert registry.get(IndicatorType.EMA) is EMAIndicator