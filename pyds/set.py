from numpy import array

from .flatten import flatten
from .is_a_tensor import is_a_tensor


def set(x):
    assert is_a_tensor(x), "`x` must be a tensor!"

    out = []

    for item in flatten(x):
        if item not in out:
            out.append(item)

    return array(out)
