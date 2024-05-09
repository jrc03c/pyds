from numpy import dot, eye
from numpy.random import normal, random
from pandas import DataFrame

from .orthonormalize import orthonormalize
from .r_score import r_score


def test():
    x = orthonormalize(random(size=[10000, 10]))
    r = r_score(eye(10), dot(x.T, x))
    assert r > 0.95

    x = DataFrame(x)
    r = r_score(eye(10), dot(x.T, x))
    assert r > 0.95


def test_errors():
    wrongs = [
        normal(size=1000),
        normal(size=[10, 10, 10]),
        234,
        "foo",
        True,
        False,
        None,
        {},
        lambda x: x,
        [[2, "3"], [4, 5]],
    ]

    for item in wrongs:
        raised = False

        try:
            orthonormalize(item)

        except Exception:
            raised = True

        assert raised
