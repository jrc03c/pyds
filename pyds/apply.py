from .is_a_function import isAFunction
from .is_a_tensor import isATensor
from .is_jagged import isJagged
from inspect import signature
from numpy import array


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
            sig = signature(fn)

            if len(sig.parameters) > 0:
                return fn(x)

            else:
                return fn()

    out = helper(fn, x)

    if isJagged(out):
        return array(out, dtype=object)
    else:
        return array(out)
