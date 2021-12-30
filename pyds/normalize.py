from numpy import mean, std, array
from .is_a_tensor import *
from .contains_only_numbers import *
from .is_a_pandas_dataframe import *
from .is_a_numpy_array import *


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

