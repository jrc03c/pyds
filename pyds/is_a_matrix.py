from numpy import shape

from .is_a_tensor import is_a_tensor


def is_a_matrix(x):
    return is_a_tensor(x) and len(shape(x)) == 2
