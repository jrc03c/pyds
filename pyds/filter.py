from .is_a_tensor import *

oldFilter = filter
fnType = type(lambda x: x)


def filter(a, b):
    if type(a) == fnType:
        fn = a
        arr = b
    else:
        fn = b
        arr = a

    assert (
        type(fn) == fnType
    ), "You must pass a function and an array into the `filter` function!"

    assert isATensor(
        arr
    ), "You must pass a function and an array into the `filter` function!"

    return list(oldFilter(fn, arr))
