from numpy import array, shape, sqrt, sum

from .contains_only_numbers import containsOnlyNumbers
from .is_a_number import isANumber
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .is_equal import isEqual


def distance(a, b):
    if not isANumber(a):
        assert isATensor(a), "`a` must be a number, vector, matrix, or tensor!"
        assert containsOnlyNumbers(a), "`a` must contain only numbers!"

        if isAPandasSeries(a) or isAPandasDataFrame(a):
            a = a.values

        if not isANumpyArray(a):
            a = array(a)

    if not isANumber(b):
        assert isATensor(b), "`b` must be a number, vector, matrix, or tensor!"
        assert containsOnlyNumbers(b), "`b` must contain only numbers!"

        if isAPandasSeries(b) or isAPandasDataFrame(b):
            b = b.values

        if not isANumpyArray(b):
            b = array(b)

    if isATensor(a) and isATensor(b):
        assert isEqual(shape(a), shape(b)), "`a` and `b` must have the same shape!"

    return sqrt(sum((a - b) ** 2))
