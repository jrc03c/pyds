from numpy import dot
from numpy.random import normal
from pandas import DataFrame

from .least_squares import least_squares
from .r_score import r_score


def test():
    a = normal(size=[100, 75])
    b_true = normal(size=[75, 50])
    c = dot(a, b_true)
    b_pred = least_squares(a, c)

    assert r_score(b_true, b_pred) > 0.99

    d = DataFrame(normal(size=[100, 75]))
    e_true = DataFrame(normal(size=[75, 50]))
    f = d.dot(e_true)
    e_pred = DataFrame(least_squares(d, f))

    assert r_score(e_true, e_pred) > 0.99


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        [234, 567],
        ["foo", "bar"],
        [[["foo"]], [["bar"]]],
        [normal(size=100), normal(size=100)],
        [normal(size=[100, 100, 100]), normal(size=[100, 100, 100])],
        [{"hello": "world"}, {"goodbye": "world"}],
        [True, False],
        [None, None],
        [lambda x: x * 2, lambda x: x * 3],
        [missing, missing],
    ]

    for pair in wrongs:
        raised = False

        try:
            least_squares(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
