from numpy.random import normal
from pandas import DataFrame, Series

from .is_a_pandas_dataframe import is_a_pandas_dataframe


def test():
    dfs = [
        DataFrame(normal(size=[100, 100])),
        DataFrame(),
    ]

    for df in dfs:
        assert is_a_pandas_dataframe(df)

    others = [
        Series(normal(size=100)),
        [[2, 3, 4], [5, 6, 7]],
        234,
        True,
        False,
        None,
        lambda x: x * 2,
        {"hello", "world"},
        "foo",
    ]

    for item in others:
        assert not is_a_pandas_dataframe(item)
