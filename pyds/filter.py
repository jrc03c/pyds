from .is_a_tensor import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *
from .is_a_numpy_array import *

oldFilter = filter
fnType = type(lambda x: x)


def filter(a, b):
    if type(a) == fnType:
        fn = a
        arr = b
    else:
        fn = b
        arr = a

    assert (
        type(fn) == fnType
    ), "You must pass a function and an array into the `filter` function!"

    assert isATensor(
        arr
    ), "You must pass a function and an array into the `filter` function!"

    if isAPandasSeries(arr) or isAPandasDataFrame(arr):
        arr = arr.values.tolist()

    if isANumpyArray(arr):
        arr = arr.tolist()

    return array(list(oldFilter(fn, arr)))
