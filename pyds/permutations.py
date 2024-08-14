from .flatten import flatten
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series


def permutations(arr, r=None):
    if r is None:
        r = len(arr)

    if is_a_pandas_dataframe(arr) or is_a_pandas_series(arr):
        return permutations(arr.values, r)

    if is_a_numpy_array(arr):
        return permutations(arr.tolist(), r)

    assert isinstance(
        arr, list
    ), "The `permutations` function only works on pandas DataFrames, pandas Series, numpy arrays, and regular Python arrays!"

    assert int(r) == r, "`r` must be an integer!"

    arr = flatten(arr).tolist()

    if r > len(arr):
        return permutations(arr)

    if r <= 0:
        return [[]]

    if len(arr) < 2:
        return arr

    out = []

    for i, v in enumerate(arr):
        before = arr[:i]
        after = arr[i + 1 :]
        others = before + after
        children = permutations(others, r - 1)

        for child in children:
            if isinstance(child, list):
                out.append([v] + child)

            else:
                out.append([v, child])

    return out
