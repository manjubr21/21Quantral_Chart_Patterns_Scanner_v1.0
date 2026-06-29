import pandas as pd

from app.patterns.double_top import DoubleTop


def test_valid_double_top():

    data = pd.DataFrame(
        {
            "high": [
                10,
                12,
                15,
                18,
                20,
                18,
                16,
                18,
                20,
                18,
                15,
                13,
            ],
            "low": [
                9,
                11,
                14,
                17,
                19,
                17,
                15,
                17,
                19,
                17,
                14,
                12,
            ],
            "close": [
                9.5,
                11.5,
                14.5,
                17.5,
                19.8,
                17.8,
                15.8,
                17.9,
                19.9,
                17.8,
                14.8,
                12.8,
            ],
        }
    )

    detector = DoubleTop()

    result = detector.detect(data)

    assert result is not None


def test_empty_dataframe():

    detector = DoubleTop()

    data = pd.DataFrame()

    result = detector.detect(data)

    assert result is not None


def test_small_dataframe():

    detector = DoubleTop()

    data = pd.DataFrame(
        {
            "high": [10, 11],
            "low": [9, 10],
            "close": [9.5, 10.5],
        }
    )

    result = detector.detect(data)

    assert result is not None