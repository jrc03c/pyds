from .is_a_matrix import *
from .is_a_vector import *
from numpy.linalg import lstsq


def leastSquares(a, b):
    assert isAMatrix(a), "`a` must be a matrix!"
    assert isAVector(b) or isAMatrix(b), "`b` must be a vector or matrix!"
    return lstsq(a, b, rcond=None)[0]
