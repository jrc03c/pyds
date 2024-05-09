from numpy import array
from numpy.random import normal
from pandas import DataFrame, Series

from .is_equal import is_equal
from .range import range
from .set import set
from .sort import sort


def test():
    x = [2, 3, 2, 3, 3, 3, 4, 5, 6, 3]
    y_true = [2, 3, 4, 5, 6]
    y_pred = sort(set(x))
    assert is_equal(y_true, y_pred)

    a = range(0, 100)
    b = set(a)
    assert is_equal(a, b)

    x = [[2, 3], [3, 4, 5], [[2], [3, 4, 5]]]
    y_true = [2, 3, 4, 5]
    y_pred = sort(set(x))
    assert is_equal(y_true, y_pred)

    x = [["foo", "foo"], ["foo", "bar", "foo"], ["foo", ["bar", ["baz"]]]]
    y_true = ["bar", "baz", "foo"]
    y_pred = sort(set(x))
    assert is_equal(y_true, y_pred)

    x = array(
        [["foo", "foo"], ["foo", "bar", "foo"], ["foo", ["bar", ["baz"]]]],
        dtype=object,
    )

    y_true = ["bar", "baz", "foo"]
    y_pred = sort(set(x))
    assert is_equal(y_true, y_pred)

    x = Series([["foo", "foo"], ["foo", "bar", "foo"], ["foo", ["bar", ["baz"]]]])
    y_true = ["bar", "baz", "foo"]
    y_pred = sort(set(x))
    assert is_equal(y_true, y_pred)

    x = DataFrame({"foo": ["a", "b", "c"], "bar": ["f", "e", "d"]})
    y_true = ["a", "b", "c", "d", "e", "f"]
    y_pred = sort(set(x))
    assert is_equal(y_true, y_pred)

    try:
        set(DataFrame(normal(size=[100, 100])))
        failed = False

    except Exception:
        failed = True

    assert not failed

    try:
        set(Series(normal(size=1000)))
        failed = False

    except Exception:
        failed = True

    assert not failed


def test_errors():
    wrongs = [
        234,
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        lambda x: x * 2,
    ]

    for item in wrongs:
        raised = False

        try:
            set(item)

        except Exception:
            raised = True

        assert raised
