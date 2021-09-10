from .is_a_number import *
from .is_a_tensor import *
from .contains_only_numbers import *
from numpy import sqrt, sum, array, ndarray
from pandas import Series


def distance(a, b):
    if not isANumber(a):
        assert isATensor(a), "`a` must be a number, vector, matrix, or tensor!"
        assert containsOnlyNumbers(a), "`a` must contain only numbers!"

    if not isANumber(b):
        assert isATensor(b), "`b` must be a number, vector, matrix, or tensor!"
        assert containsOnlyNumbers(b), "`b` must contain only numbers!"

    a = array(a)
    b = array(b)
    return sqrt(sum((a - b) ** 2))
