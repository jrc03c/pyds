from numpy import mean

from .contains_only_numbers import containsOnlyNumbers
from .correl import correl
from .is_a_matrix import isAMatrix
from .is_a_pandas_dataframe import isAPandasDataFrame
from .range import range


def getAverageCorrelation(a, b):
    assert isAMatrix(a), "`a` must be a matrix!"
    assert isAMatrix(b), "`b` must be a matrix!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"
    assert containsOnlyNumbers(b), "`b` must contain only numbers!"

    if isAPandasDataFrame(a):
        a = a.values

    if isAPandasDataFrame(b):
        b = b.values

    temp = []

    for i in range(0, a.shape[1]):
        temp.append(correl(a[:, i], b[:, i]))

    return mean(temp)
