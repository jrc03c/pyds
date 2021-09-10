from .is_a_matrix import *
from .range import *
from .correl import *
from .contains_only_numbers import *
from numpy import mean


def getAverageCorrelation(a, b):
    assert isAMatrix(a), "`a` must be a matrix!"
    assert isAMatrix(b), "`b` must be a matrix!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"
    assert containsOnlyNumbers(b), "`b` must contain only numbers!"

    temp = []

    for i in range(0, a.shape[1]):
        temp.append(correl(a[:, i], b[:, i]))

    return mean(temp)
