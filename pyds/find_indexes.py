from .flatten import *
from .is_a_function import *
from .is_a_tensor import *
from .is_a_pandas_dataframe import *
from .is_a_pandas_series import *
from .is_a_numpy_array import *


def findIndexes(a, b):
    if isAFunction(a):
        fn = a
        x = b

    else:
        fn = b
        x = a

    assert isAFunction(
        fn
    ), "You must pass a function and a tensor into the `findIndexes` function!"

    assert isATensor(
        x
    ), "You must pass a function and a tensor into the `findIndexes` function!"

    if isAPandasDataFrame(x) or isAPandasSeries(x):
        x = x.values

    if isANumpyArray(x):
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
            results = findIndexes(fn, item)

            if results is not None and len(results) > 0:
                for result in results:
                    out.append([i] + flatten(result).tolist())

        except:
            pass

    if len(out) > 0:
        return out

    return None
