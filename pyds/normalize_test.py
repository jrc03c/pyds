from numpy import mean, std
from numpy.random import normal
from pandas import DataFrame as DF

from .chop import chop
from .normalize import normalize


def test():
    x = normal(size=[10, 10, 10, 10])
    y = normalize(x)

    assert chop(mean(y)) == 0
    assert chop(std(y) - 1) == 0

    x = DF(normal(size=[100, 100]))
    y = normalize(x)

    assert chop(mean(y)) == 0
    assert chop(std(y) - 1) == 0


def test_errors():
    wrongs = [[2, "3", 4], 234, "foo", True, False, None, lambda x: x, {}]

    for item in wrongs:
        raised = False

        try:
            normalize(item)

        except Exception:
            raised = True

        assert raised
