from numpy.linalg import lstsq

from .contains_only_numbers import contains_only_numbers
from .is_a_matrix import is_a_matrix
from .is_a_vector import isAVector


def leastSquares(a, b):
    assert is_a_matrix(a), "`a` must be a matrix!"
    assert contains_only_numbers(a), "`a` must contain only numbers!"

    assert isAVector(b) or is_a_matrix(b), "`b` must be a vector or matrix!"
    assert contains_only_numbers(b), "`b` must contain only numbers!"

    return lstsq(a, b, rcond=None)[0]
