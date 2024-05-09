from numpy import array, ndarray
from numpy.random import normal, random
from pandas import DataFrame as DF

from .is_a_numpy_array import is_a_numpy_array


def test():
    arrays = [
        normal(size=100),
        random(size=[2, 3, 4, 5]),
        array([2, 3, 4, 5]),
        ndarray([2, 3, 4, 5]),
    ]

    for arr in arrays:
        assert is_a_numpy_array(arr)

    others = [
        234,
        True,
        False,
        "foo",
        lambda x: x * 2,
        {"hello": "world"},
        [2, 3, 4, 5],
        DF(normal(size=[100, 100])),
    ]

    for item in others:
        assert not is_a_numpy_array(item)
