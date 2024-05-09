from numpy import array

from .is_equal import is_equal
from .map import map


def test():
    y_pred = map(lambda x: x * 2, [2, 3, 4])
    y_true = array([4, 6, 8])

    assert is_equal(y_true, y_pred)

    y_pred = map([2, 3, 4], lambda x: x * 2)
    y_true = array([4, 6, 8])

    assert is_equal(y_true, y_pred)

    # make sure that an array of dtype=object is returned when the values
    # are of mixed types!
    def floatify(x):
        try:
            return float(x)

        except Exception:
            return x

    x = ["2.3", "4.5", "six point seven"]
    y_true = array([2.3, 4.5, "six point seven"], dtype=object)
    y_pred = map(floatify, x)

    assert is_equal(y_true, y_pred)


def test_errors():
    wrongs = [
        [lambda x: x, "foo"],
        ["foo", lambda x: x],
        [[2, 3, 4], "foo"],
        ["foo", [2, 3, 4]],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x, lambda x: x],
        [[2, 3, 4], [2, 3, 4]],
        [234, 234],
    ]

    for pair in wrongs:
        raised = False

        try:
            map(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
