from .is_a_number import *
from .is_a_tensor import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *
from .is_a_numpy_array import *
from .contains_only_numbers import *
from numpy import abs, array


def chop(x, threshold=1e-10):
    if isANumber(x):
        return 0 if abs(x) < threshold else x

    else:
        assert isATensor(x), "`x` must be a number or a tensor of numbers!"
        assert containsOnlyNumbers(x), "`x` must contain only numbers!"

        if isAPandasSeries(x) or isAPandasDataFrame(x):
            x = x.values.tolist()

        if isANumpyArray(x):
            x = x.tolist()

        return array(list(chop(val, threshold=threshold) for val in x))
