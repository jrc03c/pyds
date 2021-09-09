from .is_a_tensor import *


def flatten(x):
    if isATensor(x):
        out = []

        for item in x:
            out += flatten(item)

        return out

    else:
        return [x]
