from .is_a_tensor import *
from .is_a_pandas_dataframe import *
from .sign import *
from .contains_only_numbers import *
from numpy import sum, mean, sqrt, abs


def rScore(true, pred):
    assert isATensor(true), "`true` must be a vector, matrix, or tensor!"
    assert isATensor(pred), "`pred` must be a vector, matrix, or tensor!"
    assert containsOnlyNumbers(true), "`true` must contain only numbers!"
    assert containsOnlyNumbers(pred), "`pred` must contain only numbers!"

    if isAPandasDataFrame(true):
        true = true.values

    if isAPandasDataFrame(pred):
        pred = pred.values

    num = sum((true - pred) ** 2)
    den = sum((true - mean(true)) ** 2)

    if den == 0:
        return 0

    r2 = 1 - num / den
    return sign(r2) * sqrt(abs(r2))
