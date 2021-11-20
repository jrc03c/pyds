from numpy import array
from .is_a_tensor import *
from .is_a_pandas_dataframe import *
from .is_a_pandas_series import *
from .is_a_numpy_array import *
from .flatten import *


def count(x, item=None):
    assert isATensor(x), "`x` must be a tensor!"

    if isAPandasDataFrame(x) or isAPandasSeries(x):
        x = x.values

    if isANumpyArray(x):
        x = x.tolist()

    out = {}

    for value in flatten(x):
        if value not in out:
            out[value] = 0

        out[value] += 1

    if item is not None:
        if item in out:
            return out[item]

        return 0

    return out

