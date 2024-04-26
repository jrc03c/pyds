from math import isnan as mathIsNaN

from numpy import isnan as numpyIsNaN

from .is_a_tensor import is_a_tensor


def is_undefined(x):
    if x is None:
        return True

    if is_a_tensor(x):
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
