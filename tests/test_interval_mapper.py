from app.data.providers.interval_mapper import IntervalMapper


def test_yahoo():

    assert IntervalMapper.yahoo("1d") == "1d"

    assert IntervalMapper.yahoo("1wk") == "1wk"

    assert IntervalMapper.yahoo("1mo") == "1mo"

    assert IntervalMapper.yahoo("1h") == "60m"


def test_shoonya():

    assert IntervalMapper.shoonya("1d") == "D"

    assert IntervalMapper.shoonya("1wk") == "W"


def test_mstock():

    assert IntervalMapper.mstock("1d") == "1D"