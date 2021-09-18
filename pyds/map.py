from .is_a_tensor import *

oldMap = map
fnType = type(lambda x: x)


def map(a, b):
    if type(a) == fnType:
        fn = a
        arr = b
    else:
        fn = b
        arr = a

    assert (
        type(fn) == fnType
    ), "You must pass a function and an array into the `map` function!"

    assert isATensor(
        arr
    ), "You must pass a function and an array into the `map` function!"

    return list(oldMap(fn, arr))
