from inspect import signature

from numpy import array

from .is_a_function import is_a_function
from .is_a_tensor import is_a_tensor
from .is_jagged import is_jagged


def apply(a, b):
    if is_a_function(a):
        fn = a
        x = b
    else:
        fn = b
        x = a

    assert is_a_function(fn), "`fn` must be a function!"
    assert is_a_tensor(x), "`x` must be a tensor!"

    def helper(fn, x):
        if is_a_tensor(x):
            return [helper(fn, item) for item in x]

        else:
            sig = signature(fn)

            if len(sig.parameters) > 0:
                return fn(x)

            else:
                return fn()

    out = helper(fn, x)

    if is_jagged(out):
        return array(out, dtype=object)
    else:
        return array(out)
