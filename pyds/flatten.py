from .is_a_tensor import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *
from numpy import array


def flatten(x):
    def helper(x):
        if isAPandasSeries(x) or isAPandasDataFrame(x):
            x = x.values.tolist()

        if isANumpyArray(x):
            x = x.tolist()

        if isATensor(x):
            out = []

            for item in x:
                out += helper(item)

            return out

        return [x]

    return array(helper(x))
