from .is_a_function import is_a_function
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def find(a, b):
    if is_a_function(a):
        fn = a
        x = b

    else:
        fn = b
        x = a

    assert is_a_function(
        fn
    ), "You must pass a function and a tensor into the `find` function!"

    assert is_a_tensor(
        x
    ), "You must pass a function and a tensor into the `find` function!"

    if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
        x = x.values

    if is_a_numpy_array(x):
        x = x.tolist()

    for item in x:
        try:
            if fn(item):
                return item

        except Exception:
            pass

    for item in x:
        try:
            result = find(fn, item)

            if result is not None:
                return result

        except Exception:
            pass

    return None
