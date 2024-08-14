from .flatten import flatten
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series


def combinations(arr, r):
    # if (isDataFrame(arr) || isSeries(arr)) {
    #     return combinations(arr.values, r)
    # }

    if is_a_pandas_dataframe(arr) or is_a_pandas_series(arr):
        return combinations(arr.values, r)

    if is_a_numpy_array(arr):
        return combinations(arr.tolist(), r)

    # assert(
    #     isArray(arr),
    #     "The `combinations` function only works on arrays, Series, and DataFrames!"
    # )

    assert isinstance(
        arr, list
    ), "The `combinations` function only works on pandas DataFrames, pandas Series, numpy arrays, and regular Python arrays!"

    # assert(isNumber(r), "`r` must be a whole number!")
    assert int(r) == r, "`r` must be an integer!"

    # arr = flatten(arr)
    arr = flatten(arr).tolist()

    # if (r > arr.length) {
    #     return [arr]
    # }

    if r > len(arr):
        return [arr]

    # if (r <= 0) {
    #     return [[]]
    # }

    if r <= 0:
        return [[]]

    # if (arr.length < 2) return arr
    if len(arr) < 2:
        return arr

    # const out = []
    out = []

    # arr.forEach((item, i) => {
    for i, v in enumerate(arr):
        #     const after = arr.slice(i + 1)
        after = arr[i + 1 :]

        #     if (after.length < r - 1) return
        if len(after) < r - 1:
            continue

        #     const children = combinations(after, r - 1)
        children = combinations(after, r - 1)

        #     children.forEach(child => {
        for child in children:
            if isinstance(child, list):
                out.append([v] + child)

            else:
                out.append([v, child])

    #     out.push([item].concat(child))
    #     })
    # })

    # return out
    return out
