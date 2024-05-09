import pandas as pd
from numpy.random import random

from .some import some


def test():
    x = [2, 3, 4, 5, 6]
    assert some(x, lambda v: v < 5)
    assert some(lambda v: v < 5, x)
    assert not (some(x, lambda v: v < 2))
    assert not (some(lambda v: v < 2, x))

    x = [[2, 3, 4], [5, 6], "foo", 234, True, False, None, {}, lambda x: x]
    assert some(x, lambda item: isinstance(item, list))
    assert not (some(x, lambda item: item == "hello"))

    x = pd.DataFrame(random(size=[100, 100]))
    assert some(x, lambda row: some(row, lambda v: v > 0.5))
    assert not (some(x, lambda row: len(row) < 100))


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
            some(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
