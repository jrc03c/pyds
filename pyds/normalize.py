from numpy import array, mean, std

from .contains_only_numbers import contains_only_numbers
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_tensor import is_a_tensor


def normalize(x):
    assert is_a_tensor(x), "The `normalize` function only works on tensors!"

    assert contains_only_numbers(
        x
    ), "The `normalize` function only works on tensors of numbers!"

    if is_a_pandas_dataframe(x):
        x = x.values

    if not is_a_numpy_array(x):
        x = array(x)

    return (x - mean(x)) / std(x)
