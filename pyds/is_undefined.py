from math import isnan as math_is_nan

from numpy import isnan as numpy_is_nan

from .is_a_tensor import is_a_tensor


def is_undefined(x):
    if x is None:
        return True

    if is_a_tensor(x):
        return False

    try:
        if math_is_nan(x):
            return True

    except Exception:
        try:
            if numpy_is_nan(x):
                return True

        except Exception:
            pass

    return False
