import json

from .combinations import combinations
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_equal import is_equal
from .set import set
from .sort import sort


def factorial(n):
    if n < 2:
        return 1

    return n * factorial(n - 1)


def stringify_values(arr):
    if is_a_pandas_dataframe(arr) or is_a_pandas_series(arr):
        return stringify_values(arr.values)

    if is_a_numpy_array(arr):
        return stringify_values(arr.tolist())

    if isinstance(arr, list):
        return [stringify_values(v) for v in arr]

    return json.dumps(arr)


def get_combinations_count(arr, r):
    n = len(arr)
    return factorial(n) / (factorial(r) * factorial(n - r))


def test():
    a_true = sort(
        set(
            stringify_values(
                [
                    [0, 1, 2],
                    [0, 1, 3],
                    [0, 1, 4],
                    [0, 2, 3],
                    [0, 2, 4],
                    [0, 3, 4],
                    [1, 2, 3],
                    [1, 2, 4],
                    [1, 3, 4],
                    [2, 3, 4],
                ]
            )
        )
    )

    a_pred = sort(set(stringify_values(combinations(list(range(0, 5)), 3))))
    assert is_equal(a_true, a_pred)

    x = list(range(0, 10))
    r = 3
    assert len(combinations(x, r)) == get_combinations_count(x, r)

    assert is_equal(combinations(list(range(0, 10)), -1), [[]])
    assert is_equal(combinations(list(range(0, 10)), 100), [list(range(0, 10))])


def test_errors():
    wrongs = [
        [[1, 2, 3, 4, 5], 3.5],
        [[1, 2, 3, 4, 5], "3"],
        ["foo", 3],
        [234, 3],
        [True, 3],
        [False, 3],
        [None, 3],
        [{}, 3],
        [lambda x: x, 3],
    ]

    for pair in wrongs:
        failed = False

        try:
            combinations(pair[0], pair[1])

        except Exception:
            failed = True

        assert failed
