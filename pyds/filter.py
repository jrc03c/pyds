from .is_a_tensor import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *
from .is_a_numpy_array import *
from .is_a_function import *
from .is_jagged import *

oldFilter = filter


def filter(a, b):
    if isAFunction(a):
        fn = a
        arr = b
    else:
        fn = b
        arr = a

    assert isAFunction(
        fn
    ), "You must pass a function and an array into the `filter` function!"

    assert isATensor(
        arr
    ), "You must pass a function and an array into the `filter` function!"

    if isAPandasSeries(arr) or isAPandasDataFrame(arr):
        arr = arr.values.tolist()

    if isANumpyArray(arr):
        arr = arr.tolist()

    out = list(oldFilter(fn, arr))

    if isJagged(out):
        return array(out, dtype=object)
    else:
        return array(out)
