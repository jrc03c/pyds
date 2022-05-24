from .contains_only_numbers import containsOnlyNumbers
from .is_a_tensor import isATensor
from numpy.linalg import norm


def magnitude(a):
    assert isATensor(a), "`a` must be a vector, matrix, or tensor!"
    assert containsOnlyNumbers(a), "`a` must contain only numbers!"
    return norm(a)
