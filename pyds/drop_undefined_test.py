from math import nan as math_nan

from numpy import nan as numpy_nan
from numpy.random import normal
from pandas import DataFrame, Series

from .drop_undefined import drop_undefined
from .is_equal import is_equal


def test():
    df = DataFrame({"foo": [2, 3, 4], "bar": [5, 6, 7]})
    series = Series(["yes", "no", "maybe so"])
    norm = normal(size=[2, 3, 4, 5])
    identity = lambda x: x

    x = [
        234,
        math_nan,
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        numpy_nan,
        identity,
        [2, None, 3, 4, "NULL", "undefined", ""],
        df,
        series,
        norm,
    ]

    y_true = [
        234,
        "foo",
        True,
        False,
        {"hello": "world"},
        identity,
        [2, 3, 4],
        df.values.tolist(),
        series.values.tolist(),
        norm.tolist(),
    ]

    strings = [
        "NULL",
        "None",
        "none",
        "Nil",
        "nil",
        "",
        "undefined",
        "Undefined",
        "---",
    ]

    y_pred = drop_undefined(x, strings=strings)
    assert is_equal(y_true, y_pred)
