from math import nan as math_nan

from numpy import nan as numpy_nan

from .is_undefined import is_undefined


def test():
    undefineds = [None, math_nan, numpy_nan]

    for value in undefineds:
        assert is_undefined(value)

    defineds = [234, "foo", True, False, {}, lambda x: x]

    for value in defineds:
        assert not (is_undefined(value))
