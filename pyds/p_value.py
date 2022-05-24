from .contains_only_numbers import containsOnlyNumbers
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_series import isAPandasSeries
from .is_a_vector import isAVector
from scipy.stats import ttest_ind


def pValue(a, b):
    assert isAVector(a), "`a` must be a vector!"
    assert isAVector(b), "`b` must be a vector!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"
    assert containsOnlyNumbers(b), "`b` must contain only numbers!"

    if isANumpyArray(a):
        a = a.tolist()

    if isANumpyArray(b):
        b = b.tolist()

    if isAPandasSeries(a):
        a = a.values

    if isAPandasSeries(b):
        b = b.values

    return ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]
