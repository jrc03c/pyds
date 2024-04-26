from math import isnan as mathIsNaN

from numpy import isnan as numpyIsNaN

from .is_a_tensor import is_a_tensor


def isANumber(x):
    if x is None:
        return False

    if is_a_tensor(x):
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

    if isinstance(x, bool):
        return False

    if isinstance(x, str):
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
