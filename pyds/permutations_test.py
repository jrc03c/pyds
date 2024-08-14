import json

from numpy import inf, nan
from numpy.random import normal
from pandas import DataFrame, Series

from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_equal import is_equal
from .permutations import permutations
from .set import set
from .sort import sort


def trio_sort(a, b):
    if a[0] == b[0]:
        if a[1] == b[1]:
            return a[2] - b[2]

        else:
            return a[1] - b[1]

    else:
        return a[0] - b[0]


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


def get_permutations_count(arr, r):
    n = len(arr)
    return factorial(n) / factorial(n - r)


def test():
    a = [2, 3, 4]

    b_true = sort(
        set(
            stringify_values(
                [
                    [2, 3, 4],
                    [2, 4, 3],
                    [3, 2, 4],
                    [3, 4, 2],
                    [4, 2, 3],
                    [4, 3, 2],
                ]
            )
        )
    )

    b_pred = sort(set(stringify_values(permutations(a))))
    assert is_equal(b_true, b_pred)

    c = ["a", "b", "c", "d"]

    d_true = sort(
        set(
            stringify_values(
                [
                    ["a", "b", "c", "d"],
                    ["a", "b", "d", "c"],
                    ["a", "c", "b", "d"],
                    ["a", "c", "d", "b"],
                    ["a", "d", "b", "c"],
                    ["a", "d", "c", "b"],
                    ["b", "a", "c", "d"],
                    ["b", "a", "d", "c"],
                    ["b", "c", "a", "d"],
                    ["b", "c", "d", "a"],
                    ["b", "d", "a", "c"],
                    ["b", "d", "c", "a"],
                    ["c", "a", "b", "d"],
                    ["c", "a", "d", "b"],
                    ["c", "b", "a", "d"],
                    ["c", "b", "d", "a"],
                    ["c", "d", "a", "b"],
                    ["c", "d", "b", "a"],
                    ["d", "a", "b", "c"],
                    ["d", "a", "c", "b"],
                    ["d", "b", "a", "c"],
                    ["d", "b", "c", "a"],
                    ["d", "c", "a", "b"],
                    ["d", "c", "b", "a"],
                ]
            )
        )
    )

    d_pred = sort(set(stringify_values(permutations(c))))
    assert is_equal(d_true, d_pred)

    for i in range(2, 10):
        e = list(range(0, i))
        assert len(permutations(e)) == factorial(i)

    for i in range(1, 8):
        e = list(range(0, 8))
        assert len(permutations(e, i)) == get_permutations_count(e, i)

    f = [2, [3, 4, [5]]]

    g_true = sort(
        trio_sort,
        [
            [2, 3, 4],
            [2, 3, 5],
            [2, 4, 3],
            [2, 4, 5],
            [2, 5, 3],
            [2, 5, 4],
            [3, 2, 4],
            [3, 2, 5],
            [3, 4, 2],
            [3, 4, 5],
            [3, 5, 2],
            [3, 5, 4],
            [4, 2, 3],
            [4, 2, 5],
            [4, 3, 2],
            [4, 3, 5],
            [4, 5, 2],
            [4, 5, 3],
            [5, 2, 3],
            [5, 2, 4],
            [5, 3, 2],
            [5, 3, 4],
            [5, 4, 2],
            [5, 4, 3],
        ],
    )

    g_pred = sort(trio_sort, permutations(f, 3))
    assert is_equal(g_true, g_pred)

    h = Series({"hello": [1, 2, 3, 4, 5]})
    assert is_equal(permutations(h, 2), permutations(h.values, 2))
    assert is_equal(permutations(h, 2), permutations(h.values.tolist(), 2))

    i = DataFrame({"foo": [1, 2, 3, 4, 5], "bar": [6, 7, 8, 9, 10]})
    assert is_equal(permutations(i, 2), permutations(i.values, 2))
    assert is_equal(permutations(i, 2), permutations(i.values.tolist(), 2))

    j = normal(size=[2, 2, 2])
    assert is_equal(permutations(j, 3), permutations(j.tolist(), 3))


def test_errors():
    wrongs = [
        0,
        1,
        2.3,
        -2.3,
        inf,
        -inf,
        nan,
        "foo",
        True,
        False,
        None,
        lambda x: x,
        permutations,
        {"hello": "world"},
    ]

    for v1 in wrongs:
        for v2 in wrongs:
            failed = False

            try:
                permutations(v1, v2)

            except Exception:
                failed = True

            assert failed
