import pandas as pd

from .find import find
from .is_equal import is_equal


def test():
    x = [2, 3, 4, 5, 6, 7]
    y_true = 5
    y_pred = find(lambda v: v > 4, x)
    assert is_equal(y_true, y_pred)

    x = [2, [3, 4, [5, 6, 7, [8, 9, 10]]]]
    y_true = 9
    y_pred = find(lambda v: v > 8, x)
    assert is_equal(y_true, y_pred)

    x = pd.DataFrame([[2, 3, 4], [5, 6, 7]])
    y_true = 2
    y_pred = find(lambda v: v < 3, x)
    assert is_equal(y_true, y_pred)

    y_true = 7
    y_pred = find(x, lambda v: v > 6)
    assert is_equal(y_true, y_pred)


def test_errors():
    wrongs = [
        [[2, 3, 4], [2, 3, 4]],
        [lambda x: x, lambda x: x],
        [234, 234],
        ["foo", "foo"],
        [True, True],
        [False, False],
        [None, None],
        [{}, {}],
    ]

    for pair in wrongs:
        raised = False

        try:
            find(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
