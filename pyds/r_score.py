from .contains_only_numbers import containsOnlyNumbers
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .is_binary import isBinary
from .sign import sign
from numpy import abs, array, mean, nan, sqrt, sum
import scipy


def mode(x):
    return scipy.stats.mode(x)[0]


def rScore(true, pred, baseline=None):
    if baseline is None:
        baseline = true

    assert isATensor(true), "`true` must be a vector, matrix, or tensor!"
    assert isATensor(pred), "`pred` must be a vector, matrix, or tensor!"
    assert isATensor(baseline), "`baseline` must be a vector, matrix, or tensor!"
    assert containsOnlyNumbers(true), "`true` must contain only numbers!"
    assert containsOnlyNumbers(pred), "`pred` must contain only numbers!"
    assert containsOnlyNumbers(baseline), "`baseline` must contain only numbers!"

    if isAPandasSeries(true) or isAPandasDataFrame(true):
        true = true.values

    if isAPandasSeries(pred) or isAPandasDataFrame(pred):
        pred = pred.values

    if isAPandasSeries(baseline) or isAPandasDataFrame(baseline):
        baseline = baseline.values

    if not isANumpyArray(true):
        true = array(true)

    if not isANumpyArray(pred):
        pred = array(pred)

    if not isANumpyArray(baseline):
        baseline = array(baseline)

    if isBinary(baseline):
        helper = mode

    else:
        helper = mean

    num = sum((true - pred) ** 2)
    den = sum((true - helper(baseline)) ** 2)

    if den == 0:
        return nan

    r2 = 1 - num / den
    return sign(r2) * sqrt(abs(r2))
