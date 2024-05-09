from numpy.random import normal
from pandas import DataFrame, Series

from .is_a_matrix import is_a_matrix


def test():
    matrices = [
        [[2, 3, 4], [5, 6, 7]],
        normal(size=[100, 100]),
        DataFrame(normal(size=[100, 100])),
    ]

    for matrix in matrices:
        assert is_a_matrix(matrix)

    others = [
        [2, 3, 4],
        [[[2, 3, 4]]],
        normal(size=100),
        normal(size=[100, 100, 100]),
        Series(normal(size=100)),
        234,
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        lambda x: x * 2,
    ]

    for item in others:
        assert not is_a_matrix(item)
