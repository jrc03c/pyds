from numpy import shape

from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_series import is_a_pandas_series


def drop_nan_parallel(*args):
    if len(args) == 0:
        return None

    max_length = 0

    for arg in args:
        assert (
            len(shape(arg)) == 1
        ), "Only vectors can be passed into the `drop_nan_parallel` function!"

        if is_a_pandas_series(arg):
            arg = arg.values

        if is_a_numpy_array(arg):
            arg = arg.tolist()

        if len(arg) > max_length:
            max_length = len(arg)

    out = [[] for i in range(0, len(args))]

    for i in range(0, max_length):
        should_keep = True

        for arg in args:
            if not is_a_number(arg[i]):
                should_keep = False
                break

        if should_keep:
            for j, arg in enumerate(args):
                out[j].append(arg[i])

    return tuple(out)
