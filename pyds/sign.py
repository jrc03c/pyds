from numpy import array

from .is_a_number import isANumber
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def sign(x):
    def helper(x):
        if is_a_tensor(x):
            if is_a_pandas_series(x) or is_a_pandas_dataframe(x):
                x = x.values.tolist()

            if is_a_numpy_array(x):
                x = x.tolist()

            return [helper(v) for v in x]

        else:
            assert isANumber(x), "`x` must be a number!"

            if x > 0:
                return 1
            if x < 0:
                return -1
            return 0

    if is_a_tensor(x):
        return array(helper(x))

    else:
        return helper(x)
