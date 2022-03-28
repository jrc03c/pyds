from .is_a_function import *
from .is_a_tensor import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *


def some(a, b):
    if isAFunction(a):
        x = b
        fn = a

    else:
        x = a
        fn = b

    assert isATensor(
        x
    ), "You must pass a function and a tensor into the `some` function!"

    assert isAFunction(
        fn
    ), "You must pass a function and a tensor into the `some` function!"

    if isAPandasDataFrame(x) or isAPandasSeries(x):
        x = x.values

    if isANumpyArray(x):
        x = x.tolist()

    for value in x:
        if fn(value):
            return True

    return False
