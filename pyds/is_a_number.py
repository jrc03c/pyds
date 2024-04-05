from math import isnan as mathIsNaN

from numpy import isnan as numpyIsNaN

from .is_a_tensor import isATensor


def isANumber(x):
    if x is None:
        return False

    if isATensor(x):
        return False

    try:
        if mathIsNaN(x):
            return False

    except:
        pass

    try:
        if numpyIsNaN(x):
            return False

    except:
        pass

    if type(x) == bool:
        return False

    if type(x) == str:
        return False

    try:
        float(x)
        return True

    except:
        pass

    try:
        int(x)
        return True

    except:
        pass

    return False
