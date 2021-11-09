from numpy import shape, reshape, array
from .flatten import *
from .is_a_tensor import *
from .map import *
from .is_a_function import *


def apply(a, b):
    if isAFunction(a):
        fn = a
        x = b
    else:
        fn = b
        x = a

    assert isAFunction(fn), "`fn` must be a function!"
    assert isATensor(x), "`x` must be a tensor!"

    def helper(fn, x):
        if isATensor(x):
            return [helper(fn, item) for item in x]

        else:
            return fn(x)

    return array(helper(fn, x), dtype=object)
