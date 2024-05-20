from numpy import array, transpose
from numpy.random import normal
from pandas import DataFrame

from .correl import correl
from .flatten import flatten
from .get_correlation_matrix import get_correlation_matrix
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .r_score import r_score


def get_correlation_matrix_slow(a, b):
    if is_a_pandas_dataframe(a):
        a = a.values

    if is_a_pandas_dataframe(b):
        b = b.values

    out = []

    for i in range(0, a.shape[1]):
        row = []

        for j in range(0, b.shape[1]):
            row.append(correl(a[:, i], b[:, j]))

        out.append(row)

    return array(out)


def test():
    a = normal(size=[1000, 50])
    b = normal(size=[1000, 50])
    c = get_correlation_matrix(a, b)

    assert c.shape == (50, 50)
    assert min(flatten(c)) >= -1
    assert max(flatten(c)) <= 1

    d = normal(size=1000)
    x = [d]

    for i in range(0, 10):
        x.append(d + 0.0001 * normal(size=1000))

    x = transpose(x)
    c = get_correlation_matrix(x)

    assert min(flatten(c)) > 0.95
    assert max(flatten(c)) == 1

    e = DataFrame(normal(size=[100, 100]))
    f = DataFrame(normal(size=[100, 100]))

    try:
        get_correlation_matrix(e, f)
        failed = False

    except Exception:
        failed = True

    assert not (failed)

    g = DataFrame(normal(size=[100, 10]))
    g = g.apply(lambda col: col * normal() * 100 + normal() * 100)
    h = DataFrame(normal(size=[100, 10]))
    h = h.apply(lambda col: col * normal() * 100 + normal() * 100)

    c_true = get_correlation_matrix_slow(g, h)
    c_pred = get_correlation_matrix(g, h)
    assert r_score(c_true, c_pred) > 0.99


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        [[2, 3, 4], [5, 6, 7]],
        [[["a", "b", "c"]], [["1", "2", "3"]]],
        [234, 567],
        ["foo", "bar"],
        [normal(size=[10, 10, 10]), normal(size=[10, 10, 10])],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [missing, missing],
    ]

    for pair in wrongs:
        raised = False

        try:
            get_correlation_matrix(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
