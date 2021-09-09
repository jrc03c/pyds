from .flatten import *
from .is_a_number import *
from .is_a_tensor import *


def containsOnlyNumbers(x):
    assert isATensor(x), "`x` must be a vector, matrix, or tensor!"

    for item in flatten(x):
        if not isANumber(item):
            return False

    return True
