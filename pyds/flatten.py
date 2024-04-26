from numpy import array

from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def flatten(x):
    def helper(x):
        if is_a_pandas_series(x) or is_a_pandas_dataframe(x):
            x = x.values.tolist()

        if is_a_numpy_array(x):
            x = x.tolist()

        if is_a_tensor(x):
            out = []

            for item in x:
                out += helper(item)

            return out

        return [x]

    return array(helper(x))
