from .flatten import flatten
from .is_a_function import is_a_function
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def find_indexes(a, b):
    if is_a_function(a):
        fn = a
        x = b

    else:
        fn = b
        x = a

    assert is_a_function(
        fn
    ), "You must pass a function and a tensor into the `find_indexes` function!"

    assert is_a_tensor(
        x
    ), "You must pass a function and a tensor into the `find_indexes` function!"

    if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
        x = x.values

    if is_a_numpy_array(x):
        x = x.tolist()

    out = []

    for i in range(0, len(x)):
        item = x[i]

        try:
            if fn(item):
                out.append([i])

        except:
            pass

    for i in range(0, len(x)):
        try:
            item = x[i]
            results = find_indexes(fn, item)

            if results is not None and len(results) > 0:
                for result in results:
                    out.append([i] + flatten(result).tolist())

        except:
            pass

    if len(out) > 0:
        return out

    return None
