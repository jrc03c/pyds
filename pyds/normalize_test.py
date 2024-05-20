from numpy import mean, std
from numpy.random import normal
from pandas import DataFrame as DF

from .chop import chop
from .normalize import normalize


def test():
    x = normal(size=100) * normal() * 1000 + normal() * 1000
    y = normalize(x)

    assert chop(mean(y)) == 0
    assert chop(std(y) - 1) == 0

    x = DF(normal(size=[100, 100]) * normal() * 100 + normal() * 100)
    y = DF(normalize(x))

    for col in y.columns:
        assert chop(mean(y[col])) == 0
        assert chop(std(y[col]) - 1) == 0

    x = DF(normal(size=[100, 100]) * normal() * 100 + normal() * 100)
    y = DF(normalize(x, axis=1))

    for i in range(0, y.shape[0]):
        row = y.iloc[i, :].values
        assert chop(mean(row)) == 0
        assert chop(std(row) - 1) == 0

    x = DF(normal(size=[100, 100]) * normal() * 100 + normal() * 100)
    y = normalize(x, axis=None)

    assert chop(mean(y)) == 0
    assert chop(std(y) - 1) == 0

    x = normal(size=[10, 10, 10, 10]) * 100 + 100
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
