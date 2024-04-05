from numpy import array, mean, std

from .contains_only_numbers import containsOnlyNumbers
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_tensor import isATensor


def normalize(x):
    assert isATensor(x), "The `normalize` function only works on tensors!"
    assert containsOnlyNumbers(
        x
    ), "The `normalize` function only works on tensors of numbers!"

    if isAPandasDataFrame(x):
        x = x.values

    if not isANumpyArray(x):
        x = array(x)

    return (x - mean(x)) / std(x)
