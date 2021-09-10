from .correl import *
from .is_a_matrix import *
from .is_a_pandas_dataframe import *
from .range import *
from .contains_only_numbers import *
from numpy import array


def getCorrelationMatrix(a, b=None):
    try:
        if b == None:
            b = a
    except:
        pass

    assert isAMatrix(a), "`a` must be a matrix!"
    assert isAMatrix(b), "`b` must be a matrix!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"
    assert containsOnlyNumbers(b), "`b` must contain only numbers!"

    if isAPandasDataFrame(a):
        a = a.values

    if isAPandasDataFrame(b):
        b = b.values

    out = []

    for i in range(0, a.shape[1]):
        row = []

        for j in range(0, b.shape[1]):
            row.append(correl(a[:, i], b[:, j]))

        out.append(row)

    return array(out)
