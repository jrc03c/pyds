from .is_a_function import isAFunction
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor


def findAll(a, b):
    if isAFunction(a):
        fn = a
        x = b
    else:
        fn = b
        x = a

    assert isAFunction(
        fn
    ), "You must pass a function and a tensor into the `findAll` function!"

    assert isATensor(
        x
    ), "You must pass a function and a tensor into the `findAll` function!"

    if isAPandasDataFrame(x) or isAPandasSeries(x):
        x = x.values

    if isANumpyArray(x):
        x = x.tolist()

    out = []

    for item in x:
        try:
            if fn(item):
                out.append(item)

        except:
            pass

    for item in x:
        try:
            results = findAll(fn, item)

            if results is not None and len(results) > 0:
                for result in results:
                    out.append(result)

        except:
            pass

    if len(out) > 0:
        return out

    return None
