from numpy.random import normal
from pandas import DataFrame, Series

from .distance import distance
from .magnitude import magnitude


def test():
    assert magnitude([3, 4]) == 5

    tensors = [
        normal(size=100),
        normal(size=[100, 100]),
        normal(size=[100, 100, 100]),
        Series(normal(size=100)),
        DataFrame(normal(size=[100, 100])),
    ]

    for tensor in tensors:
        assert abs(magnitude(tensor) - distance(tensor, 0)) < 0.0001


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        234,
        "foo",
        True,
        False,
        None,
        ["hello", "world"],
        {"hello": "world"},
        lambda x: x * 2,
        missing,
    ]

    for item in wrongs:
        raised = False

        try:
            magnitude(item)

        except Exception:
            raised = True

        assert raised
