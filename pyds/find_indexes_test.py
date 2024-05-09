import pandas as pd

from .find_indexes import find_indexes
from .is_equal import is_equal


def test():
    x = [2, 3, 4, 5, 6, 7]
    y_true = [[3], [4], [5]]
    y_pred = find_indexes(lambda v: v > 4, x)
    assert is_equal(y_true, y_pred)

    x = [2, [3, 4, [5, 6, 7, [8, 9, 10]]]]
    y_true = [[1, 2, 3, 1], [1, 2, 3, 2]]
    y_pred = find_indexes(lambda v: v > 8, x)
    assert is_equal(y_true, y_pred)

    for i in range(0, len(y_true)):
        i_true = y_true[i]
        i_pred = y_pred[i]

        assert is_equal(
            x[i_true[0]][i_true[1]][i_true[2]][i_true[3]],
            x[i_pred[0]][i_pred[1]][i_pred[2]][i_pred[3]],
        )

    x = pd.DataFrame([[2, 3, 4], [5, 6, 7]])
    y_true = [[0, 0]]
    y_pred = find_indexes(lambda v: v < 3, x)
    assert is_equal(y_true, y_pred)
    assert is_equal(x.values[0][0], x.values[y_pred[0][0]][y_pred[0][1]])

    y_true = [[1, 2]]
    y_pred = find_indexes(x, lambda v: v > 6)
    assert is_equal(y_true, y_pred)
    assert is_equal(x.values[1][2], x.values[y_pred[0][0]][y_pred[0][1]])


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
            find_indexes(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
