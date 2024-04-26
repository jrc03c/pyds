from numpy import array, max

from .flatten import flatten
from .is_a_number import isANumber
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def leftPad(x, biggest=None):
    def helper(x, biggest=None):
        if is_a_tensor(x):
            if biggest is None:
                biggest = max(flatten(x))

            if is_a_pandas_series(x) or is_a_pandas_dataframe(x):
                x = x.values.tolist()

            if is_a_numpy_array(x):
                x = x.tolist()

            return [helper(v, biggest) for v in x]

        else:
            if biggest is None:
                biggest = x

            assert isANumber(x), "`x` must be a whole number!"
            assert int(x) == x, "`x` must be a whole number!"
            assert x >= 0, "`x` must be a whole number!"

            assert isANumber(x), "`biggest` must be a whole number! (%s)" % biggest
            assert int(biggest) == biggest, "`biggest` must be a whole number!"
            assert biggest >= 0, "`biggest` must be a whole number! (%s)" % biggest

            assert x <= biggest, "`x` must be less than or equal to `biggest`!"

            numberOfZeros = len(str(biggest)) - len(str(x))
            return "0" * numberOfZeros + str(x)

    return array(helper(x, biggest))
