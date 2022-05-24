from .is_a_function import isAFunction
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .is_jagged import isJagged
from numpy import array

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
    ), "You must pass a function and a tensor into the `filter` function!"

    assert isATensor(
        arr
    ), "You must pass a function and a tensor into the `filter` function!"

    if isAPandasSeries(arr) or isAPandasDataFrame(arr):
        arr = arr.values.tolist()

    if isANumpyArray(arr):
        arr = arr.tolist()

    out = list(oldFilter(fn, arr))
    types = set(list(map(lambda v: type(v), out)))

    if isJagged(out) or len(types) > 1:
        return array(out, dtype=object)
    else:
        return array(out)
