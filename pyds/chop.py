from numpy import abs, array

from .contains_only_numbers import contains_only_numbers
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def chop(x, threshold=1e-10):
    if is_a_number(x):
        return 0 if abs(x) < threshold else x

    else:
        assert is_a_tensor(x), "`x` must be a number or a tensor of numbers!"
        assert contains_only_numbers(x), "`x` must contain only numbers!"

        if is_a_pandas_series(x) or is_a_pandas_dataframe(x):
            x = x.values.tolist()

        if is_a_numpy_array(x):
            x = x.tolist()

        return array(list(chop(val, threshold=threshold) for val in x))
