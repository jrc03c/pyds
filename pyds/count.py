from .flatten import flatten
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def count(x, item=None):
    assert is_a_tensor(x), "`x` must be a tensor!"

    if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
        x = x.values

    if is_a_numpy_array(x):
        x = x.tolist()

    out = {}

    for value in flatten(x):
        if value not in out:
            out[value] = 0

        out[value] += 1

    if item is not None:
        if item in out:
            return out[item]

        return 0

    return out
