from numpy import transpose
from numpy.random import normal
from pandas import DataFrame

from .flatten import flatten
from .get_correlation_matrix import get_correlation_matrix


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
