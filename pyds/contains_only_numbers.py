from .flatten import flatten
from .is_a_number import isANumber
from .is_a_tensor import isATensor


def containsOnlyNumbers(x):
    assert isATensor(x), "`x` must be a vector, matrix, or tensor!"

    for item in flatten(x):
        if not isANumber(item):
            return False

    return True
