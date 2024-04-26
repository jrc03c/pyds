from .flatten import flatten
from .is_a_number import isANumber
from .is_a_tensor import is_a_tensor


def isBinary(x):
    if is_a_tensor(x):
        temp = flatten(x)

        for v in temp:
            if v != 0 and v != 1:
                return False

        return True

    elif isANumber(x):
        return x == 0 or x == 1

    return False
