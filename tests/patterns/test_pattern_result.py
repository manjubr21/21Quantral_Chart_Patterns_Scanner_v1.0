from app.patterns import PatternResult


def test_result():

    result = PatternResult(
        pattern_name="dummy",
        detected=True,
        confidence=0.90,
    )

    assert result.detected
    assert result.pattern_name == "dummy"


def test_bool():

    result = PatternResult(
        pattern_name="dummy",
        detected=True,
    )

    assert result


def test_dict():

    result = PatternResult(
        pattern_name="dummy",
        detected=True,
    )

    d = result.to_dict()

    assert d["pattern_name"] == "dummy"