import pandas as pd
from numpy.random import random

from .every import every


def test():
    x = [2, 3, 4, 5, 6]

    assert every(x, lambda v: v < 7)
    assert every(lambda v: v < 7, x)
    assert not (every(x, lambda v: v < 6))
    assert not (every(lambda v: v < 6, x))

    x = [[2, 3, 4], [5, 6]]

    assert every(x, lambda row: isinstance(row, list))
    assert not (every(x, lambda row: len(row) > 2))

    x = pd.DataFrame(random(size=[100, 100]))

    assert every(x, lambda row: len(row) == 100)
    assert not (every(x, lambda row: every(row, lambda v: v > 0.5)))


def test_errors():
    wrongs = [
        [[2, 3, 4], [2, 3, 4]],
        [lambda x: x, lambda x: x],
        [234, 234],
        ["foo", "bar"],
        [True, True],
        [False, False],
        [None, None],
        [{"hello": "world"}, {"hello": "world"}],
    ]

    for pair in wrongs:
        raised = False

        try:
            every(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
