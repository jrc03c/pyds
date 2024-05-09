from numpy import shape
from numpy.random import normal
from pandas import DataFrame, Series

from .flatten import flatten


def test():
    tensors = [
        [2, 3, 4],
        [[2, 3, 4]],
        [[[2, 3, 4]]],
        normal(size=100),
        normal(size=[100, 100]),
        normal(size=[100, 100, 100]),
        Series(normal(size=100)),
        DataFrame(normal(size=[100, 100])),
    ]

    for tensor in tensors:
        assert len(shape(flatten(tensor))) == 1

    others = [
        234,
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        lambda x: x * 2,
    ]

    for item in others:
        pred = flatten(item)
        assert len(pred) == 1
        assert pred[0] == item
