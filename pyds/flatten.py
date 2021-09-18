from .is_a_tensor import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *


def flatten(x):
    if isAPandasSeries(x) or isAPandasDataFrame(x):
        return flatten(x.values.tolist())

    if isANumpyArray(x):
        return flatten(x.tolist())

    if isATensor(x):
        out = []

        for item in x:
            out += flatten(item)

        return out

    return [x]
