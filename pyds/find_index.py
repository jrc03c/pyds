from .flatten import flatten
from .is_a_function import isAFunction
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor


def findIndex(a, b):
    if isAFunction(a):
        fn = a
        x = b

    else:
        fn = b
        x = a

    assert isAFunction(
        fn
    ), "You must pass a function and a tensor into the `findIndex` function!"

    assert isATensor(
        x
    ), "You must pass a function and a tensor into the `findIndex` function!"

    if isAPandasDataFrame(x) or isAPandasSeries(x):
        x = x.values

    if isANumpyArray(x):
        x = x.tolist()

    for i in range(0, len(x)):
        item = x[i]

        try:
            if fn(item):
                return i

        except:
            pass

    for i in range(0, len(x)):
        try:
            item = x[i]
            result = findIndex(fn, item)

            if result is not None:
                return [i] + flatten(result).tolist()

        except:
            pass

    return None
