from math import nan as math_nan

from numpy import nan as numpy_nan
from numpy import round
from numpy.random import normal, random
from pandas import DataFrame, Series

from pyds import count, filter, flatten, is_equal


def test():
    x = [2, 4, 2, 4, 3, 3, 3, 3, 3]
    y_true = {2: 2, 3: 5, 4: 2}

    assert count(x, 2) == y_true[2]
    assert count(x, 3) == y_true[3]
    assert count(x, 4) == y_true[4]
    assert is_equal(count(x), y_true)

    x = round(random(size=[2, 3, 4, 5]))

    y_true = {
        0: len(filter(lambda v: v == 0, flatten(x))),
        1: len(filter(lambda v: v == 1, flatten(x))),
    }

    assert is_equal(count(x), y_true)

    x = Series(round(random(size=1000) * 100))
    assert is_equal(count(x), count(x.values))
    assert is_equal(count(x), count(x.values.tolist()))

    x = DataFrame(round(normal(size=[100, 5])))
    assert is_equal(count(x), count(x.values))
    assert is_equal(count(x), count(x.values.tolist()))


def test_errors():
    wrongs = [
        0,
        1,
        -1,
        234,
        234.567,
        -234.567,
        "foo",
        True,
        False,
        {"hello": "world"},
        lambda x: x * 2,
        test_errors,
        DataFrame,
        None,
        math_nan,
        numpy_nan,
    ]

    for v1 in wrongs:
        for v2 in wrongs:
            raised = False

            try:
                count(v1, v2)
            except Exception:
                raised = True

            assert raised
