from numpy import isnan, shape, zeros
from numpy.random import normal
from pandas import Series

from .r_score import r_score


def test():
    a = normal(size=[10, 10, 10, 10])
    last_r_score = 1
    assert r_score(a, a) == 1

    for scalar in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]:
        b = a + scalar * normal(size=shape(a))
        r = r_score(a, b)

        assert r <= last_r_score

        last_r_score = r

    c = Series(normal(size=1000))
    assert r_score(c, c) == 1

    # confirm that nan is returned when the true set only has one value
    true = zeros(1000)
    pred = normal(size=1000)
    assert isnan(r_score(true, pred))


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        [234, 567],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye", "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [missing, missing],
    ]

    for pair in wrongs:
        raised = False

        try:
            r_score(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
