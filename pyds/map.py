from .is_a_function import isAFunction
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .is_jagged import isJagged
from .set import set
from numpy import array

oldMap = map


def map(a, b):
    if isAFunction(a):
        fn = a
        arr = b
    else:
        fn = b
        arr = a

    assert isAFunction(
        fn
    ), "You must pass a function and a tensor into the `map` function!"

    assert isATensor(
        arr
    ), "You must pass a function and a tensor into the `map` function!"

    if isAPandasSeries(arr) or isAPandasDataFrame(arr):
        arr = arr.values.tolist()

    if isANumpyArray(arr):
        arr = arr.tolist()

    out = list(oldMap(fn, arr))

    types = set(list(oldMap(lambda v: type(v), out)))

    if isJagged(out) or len(types) > 1:
        return array(out, dtype=object)
    else:
        return array(out)
