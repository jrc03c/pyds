from math import isnan as math_is_nan

from numpy import isnan as numpy_is_nan

from .is_a_tensor import is_a_tensor


def is_a_number(x):
    if x is None:
        return False

    if is_a_tensor(x):
        return False

    try:
        if math_is_nan(x):
            return False

    except Exception:
        pass

    try:
        if numpy_is_nan(x):
            return False

    except Exception:
        pass

    if isinstance(x, bool):
        return False

    if isinstance(x, str):
        return False

    try:
        float(x)
        return True

    except Exception:
        pass

    try:
        int(x)
        return True

    except Exception:
        pass

    return False
