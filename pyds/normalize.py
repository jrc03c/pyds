from numpy import array, mean, std

from .contains_only_numbers import contains_only_numbers
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_tensor import is_a_tensor


def normalize(x, axis=0):
    assert is_a_tensor(x), "The `normalize` function only works on tensors!"

    assert contains_only_numbers(
        x
    ), "The `normalize` function only works on tensors of numbers!"

    assert (
        (isinstance(axis, int) and axis >= 0) or axis is None
    ), "The `axis` argument passed into the `normalize` function must be `None` or a non-negative integer!"

    if is_a_pandas_dataframe(x):
        x = x.values

    if not is_a_numpy_array(x):
        x = array(x)

    if len(x.shape) == 1:
        return (x - mean(x)) / std(x)

    if len(x.shape) == 2 and axis is not None:
        if axis == 0:
            x = x.T

            for i in range(0, x.shape[0]):
                x[i] = (x[i] - mean(x[i])) / std(x[i])

            return x.T

        else:
            for i in range(0, x.shape[0]):
                x[i] = (x[i] - mean(x[i])) / std(x[i])

            return x

    return (x - mean(x)) / std(x)
