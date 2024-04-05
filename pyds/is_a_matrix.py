from numpy import shape

from .is_a_tensor import isATensor


def isAMatrix(x):
    return isATensor(x) and len(shape(x)) == 2
