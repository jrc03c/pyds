from numpy.random import normal
from pandas import DataFrame, Series

from .is_a_pandas_series import is_a_pandas_series


def test():
    series = [Series(dtype="object"), Series(normal(size=100))]

    for s in series:
        assert is_a_pandas_series(s)

    others = [
        234,
        "foo",
        True,
        False,
        None,
        {"hello", "world"},
        lambda x: x * 2,
        [2, 3, 4, 5],
        DataFrame(normal(size=[100, 100])),
    ]

    for item in others:
        assert not is_a_pandas_series(item)
