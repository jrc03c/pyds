from .is_a_function import is_a_function
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def some(a, b):
    if is_a_function(a):
        x = b
        fn = a

    else:
        x = a
        fn = b

    assert is_a_tensor(
        x
    ), "You must pass a function and a tensor into the `some` function!"

    assert is_a_function(
        fn
    ), "You must pass a function and a tensor into the `some` function!"

    if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
        x = x.values

    if is_a_numpy_array(x):
        x = x.tolist()

    for value in x:
        if fn(value):
            return True

    return False
