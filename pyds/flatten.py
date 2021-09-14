from .is_a_tensor import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *


def flatten(x):
    if isATensor(x):
        if isAPandasSeries(x) or isAPandasDataFrame(x):
            x = x.values

        out = []

        for item in x:
            out += flatten(item)

        return out

    else:
        return [x]
