from app.patterns import BasePattern
from app.patterns import PatternRegistry
from app.patterns import PatternResult

import pandas as pd


class DummyPattern(BasePattern):

    name = "dummy"

    description = "Dummy Pattern"

    def calculate(self, data: pd.DataFrame, **kwargs):
        return PatternResult(
            pattern_name=self.name,
            detected=True,
            confidence=1.0,
        )


def test_register():

    registry = PatternRegistry()

    registry.register(DummyPattern())

    assert registry.exists("dummy")


def test_get():

    registry = PatternRegistry()

    registry.register(DummyPattern())

    pattern = registry.get("dummy")

    assert pattern.name == "dummy"


def test_unregister():

    registry = PatternRegistry()

    registry.register(DummyPattern())

    registry.unregister("dummy")

    assert not registry.exists("dummy")