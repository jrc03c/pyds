from .contains_only_numbers import containsOnlyNumbers
from .is_a_matrix import isAMatrix
from .is_a_vector import isAVector
from numpy.linalg import lstsq


def leastSquares(a, b):
    assert isAMatrix(a), "`a` must be a matrix!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"

    assert isAVector(b) or isAMatrix(b), "`b` must be a vector or matrix!"
    assert containsOnlyNumbers(b), "`b` must contain only numbers!"

    return lstsq(a, b, rcond=None)[0]
