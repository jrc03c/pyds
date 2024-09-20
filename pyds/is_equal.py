from math import nan as math_nan

from numpy import nan as numpy_nan

from .is_a_function import is_a_function
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def is_equal(a, b):
    if a is numpy_nan and b is numpy_nan:
        return True

    if a is math_nan and b is math_nan:
        return True

    if a is numpy_nan and b is math_nan:
        return True

    if a is math_nan and b is numpy_nan:
        return True

    if is_a_number(a) and is_a_number(b):
        return float(a) == float(b)

    if type(a) is not type(b):
        return False

    if is_a_tensor(a) and is_a_tensor(b):
        if is_a_pandas_series(a) or is_a_pandas_dataframe(a):
            a = a.values

        if is_a_pandas_series(b) or is_a_pandas_dataframe(b):
            b = b.values

        if is_a_numpy_array(a):
            a = a.tolist()

        if is_a_numpy_array(b):
            b = b.tolist()

        try:
            if len(a) != len(b):
                return False

        except Exception:
            pass

        if isinstance(a, set) and isinstance(b, set):
            a = list(a)
            b = list(b)

        for i in range(0, len(a)):
            if not is_equal(a[i], b[i]):
                return False

        return True

    if isinstance(a, dict) and isinstance(b, dict):
        a_keys = list(sorted(a.keys()))
        b_keys = list(sorted(b.keys()))

        if not is_equal(a_keys, b_keys):
            return False

        for i in range(0, len(a_keys)):
            a_key = a_keys[i]
            b_key = b_keys[i]
            a_child = a[a_key]
            b_child = b[b_key]

            if not is_equal(a_child, b_child):
                return False

        return True

    if is_a_function(a) and is_a_function(b):
        return a is b

    try:
        return is_equal(a.__dict__, b.__dict__)
    except Exception:
        pass

    return a == b
