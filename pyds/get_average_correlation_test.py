from numpy.random import normal, random
from pandas import DataFrame

from .get_average_correlation import get_average_correlation


def test():
    a = normal(size=[1000, 50])
    b = 0.00001 + a
    assert get_average_correlation(a, b) > 0.95

    a = random(size=[1000, 50])
    b = random(size=[1000, 50])
    assert abs(get_average_correlation(a, b)) < 0.05

    a = DataFrame(a)
    b = DataFrame(b)
    assert abs(get_average_correlation(a, b)) < 0.05


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        [[2, 3, 4], [5, 6, 7]],
        [normal(size=[3, 3, 3]), normal(size=[3, 3, 3])],
        [234, 567],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [[["a", "b", "c"]], [["1", "2", "3"]]],
        [missing, missing],
    ]

    for pair in wrongs:
        raised = False

        try:
            get_average_correlation(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
