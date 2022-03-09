from .is_iterable import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from numpy import array


def isAVector(x):
    if not isIterable(x):
        return False

    if isAPandasSeries(x):
        x = x.values

    if not isANumpyArray(x):
        x = array(x, dtype=object)

    return len(x.shape) == 1
