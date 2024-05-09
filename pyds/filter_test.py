from numpy import array

from .filter import filter
from .is_equal import is_equal


def test():
    assert is_equal(filter([1, 2, 3, 4, 5], lambda x: x > 2), array([3, 4, 5]))

    assert is_equal(
        filter([[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]], lambda x: len(x) < 4),
        array([[1, 2, 3]]),
    )

    # make sure that an array of dtype=object is returned when the values
    # are of mixed types!
    def floatify(x):
        try:
            return float(x)

        except Exception:
            return x

    x = [234, "foo", True, False, None, {}, lambda x: x, []]
    y_true = array([234, True, False], dtype=object)
    y_pred = filter(lambda v: isinstance(v, bool) or isinstance(v, int), x)

    assert is_equal(y_true, y_pred)


def test_errors():
    wrongs = [
        [234, 567],
        ["foo", "bar"],
        [True, False],
        [[2, 3, 4], [2, 3, 4]],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
    ]

    for pair in wrongs:
        raised = False

        try:
            filter(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
