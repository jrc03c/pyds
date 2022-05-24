from .flatten import flatten
from .is_a_number import isANumber
from .is_a_tensor import isATensor
from .set import set
from .sort import sort


def isBinary(x):
    if isATensor(x):
        temp = sort(set(flatten(x)))

        if len(temp) == 1:
            return temp[0] == 0 or temp[0] == 1

        if len(temp) == 2:
            return temp[0] == 0 and temp[1] == 1

        return False

    elif isANumber(x):
        return x == 0 or x == 1

    return False
