from .flatten import flatten
from .is_a_number import is_a_number
from .is_a_tensor import is_a_tensor


def is_binary(x):
    if is_a_tensor(x):
        temp = flatten(x)

        for v in temp:
            if v != 0 and v != 1:
                return False

        return True

    elif is_a_number(x):
        return x == 0 or x == 1

    return False
