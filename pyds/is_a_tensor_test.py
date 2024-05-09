from numpy.random import normal
from pandas import DataFrame, Series

from .is_a_tensor import is_a_tensor


def test():
    tensors = [
        [2, 3, 4],
        [[2, 3, 4]],
        [[[2, 3, 4]]],
        normal(size=100),
        normal(size=[100, 100]),
        normal(size=[100, 100, 100]),
        DataFrame(normal(size=[100, 100])),
        Series(normal(size=100)),
    ]

    for tensor in tensors:
        assert is_a_tensor(tensor)

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
        assert not is_a_tensor(item)
