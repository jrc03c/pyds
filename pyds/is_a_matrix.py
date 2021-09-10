from .is_a_tensor import *
from numpy import shape


def isAMatrix(x):
    return isATensor(x) and len(shape(x)) == 2
