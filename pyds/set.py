from .flatten import *
from .is_a_tensor import *


def set(x):
    assert isATensor(x), "`x` must be a tensor!"

    out = []

    for item in flatten(x):
        if item not in out:
            out.append(item)

    return array(out)
