from numpy import isnan
from .is_a_tensor import *


def isANumber(x):
    if isATensor(x):
        return False

    try:
        if isnan(x):
            return False
    except:
        pass

    if type(x) is bool:
        return False

    if type(x) is str:
        return False

    try:
        float(x)
        return True
    except:
        return False
