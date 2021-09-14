from .is_a_matrix import *
from .is_a_vector import *
from .contains_only_numbers import *
from numpy.linalg import lstsq


def leastSquares(a, b):
    assert isAMatrix(a), "`a` must be a matrix!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"

    assert isAVector(b) or isAMatrix(b), "`b` must be a vector or matrix!"
    assert containsOnlyNumbers(b), "`b` must contain only numbers!"

    return lstsq(a, b, rcond=None)[0]
