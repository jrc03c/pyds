from numpy import abs, array

from .contains_only_numbers import containsOnlyNumbers
from .is_a_number import isANumber
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor


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
