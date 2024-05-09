from numpy.random import normal
from pandas import DataFrame, Series

from .is_iterable import is_iterable


def test():
    iterables = [
        [2, 3, 4],
        [[2, 3, 4]],
        [[[2, 3, 4]]],
        normal(size=100),
        normal(size=[100, 100]),
        normal(size=[100, 100, 100]),
        Series(normal(size=100)),
        DataFrame(normal(size=[100, 100])),
        "foo",
        {"hello": "world"},
    ]

    for i in iterables:
        assert is_iterable(i)

    others = [
        234,
        True,
        False,
        None,
        lambda x: x * 2,
    ]

    for item in others:
        assert not is_iterable(item)
