from .is_a_tensor import *
from math import isnan as mathIsNaN
from numpy import isnan as numpyIsNaN


def isUndefined(x):
    if x is None:
        return True

    if isATensor(x):
        return False

    try:
        if mathIsNaN(x):
            return True

    except:
        try:
            if numpyIsNaN(x):
                return True

        except:
            pass

    return False
