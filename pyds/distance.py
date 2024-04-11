from numpy import array, shape, sqrt, sum

from .contains_only_numbers import contains_only_numbers
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_equal import is_equal


def distance(a, b):
    if not is_a_number(a):
        assert is_a_tensor(a), "`a` must be a number, vector, matrix, or tensor!"
        assert contains_only_numbers(a), "`a` must contain only numbers!"

        if is_a_pandas_series(a) or is_a_pandas_dataframe(a):
            a = a.values

        if not is_a_numpy_array(a):
            a = array(a)

    if not is_a_number(b):
        assert is_a_tensor(b), "`b` must be a number, vector, matrix, or tensor!"
        assert contains_only_numbers(b), "`b` must contain only numbers!"

        if is_a_pandas_series(b) or is_a_pandas_dataframe(b):
            b = b.values

        if not is_a_numpy_array(b):
            b = array(b)

    if is_a_tensor(a) and is_a_tensor(b):
        assert is_equal(shape(a), shape(b)), "`a` and `b` must have the same shape!"

    return sqrt(sum((a - b) ** 2))
