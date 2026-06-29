import pandas as pd

from app.patterns import BasePattern
from app.patterns import PatternEngine
from app.patterns import PatternResult


class DummyPattern(BasePattern):

    name = "dummy"

    description = "Dummy"

    def calculate(self, data: pd.DataFrame, **kwargs):

        return PatternResult(
            pattern_name=self.name,
            detected=True,
            confidence=0.95,
        )


def sample_data():

    return pd.DataFrame(
        {
            "Open": [1, 2, 3],
            "High": [2, 3, 4],
            "Low": [0, 1, 2],
            "Close": [2, 3, 4],
            "Volume": [100, 100, 100],
        }
    )


def test_engine():

    engine = PatternEngine()

    engine.register(DummyPattern())

    result = engine.calculate(
        "dummy",
        sample_data(),
    )

    assert result.detected


def test_calculate_all():

    engine = PatternEngine()

    engine.register(DummyPattern())

    results = engine.calculate_all(
        sample_data()
    )

    assert len(results) == 1
