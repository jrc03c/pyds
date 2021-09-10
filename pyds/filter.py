from .is_iterable import *

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
    ), "You must pass a function and an iterable into the `filter` function!"

    assert isIterable(
        arr
    ), "You must pass a function and an iterable into the `filter` function!"

    return list(oldFilter(fn, arr))
