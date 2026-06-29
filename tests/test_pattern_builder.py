from tests.utils.pattern_builder import PatternBuilder


def test_builder():

    df = PatternBuilder.from_close(
        [
            100,
            101,
            102,
            103,
        ]
    )

    assert len(df) == 4

    assert "open" in df.columns
    assert "high" in df.columns
    assert "low" in df.columns
    assert "close" in df.columns
    assert "volume" in df.columns


def test_empty():

    df = PatternBuilder.empty()

    assert len(df) == 0