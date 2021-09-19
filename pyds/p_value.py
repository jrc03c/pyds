from .is_a_vector import *
from .is_a_numpy_array import *
from .is_a_pandas_series import *
from scipy.stats import ttest_ind


def pValue(a, b):
    assert isAVector(a), "`a` must be a vector!"
    assert isAVector(b), "`b` must be a vector!"

    if isANumpyArray(a):
        a = a.tolist()

    if isANumpyArray(b):
        b = b.tolist()

    if isAPandasSeries(a):
        a = a.values

    if isAPandasSeries(b):
        b = b.values

    return ttest_ind(a, b, equal_var=False, nan_policy="omit")[1]
