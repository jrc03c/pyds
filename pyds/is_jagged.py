from .is_a_tensor import *
from .set import *


def isJagged(x):
    if not isATensor(x):
        return False

    childrenAreArrays = [isATensor(item) for item in x]

    if len(set(childrenAreArrays)) > 1:
        return True

    if childrenAreArrays[0] == False:
        return False

    childLengths = [len(item) for item in x]

    if len(set(childLengths)) > 1:
        return True

    childrenAreJagged = [isJagged(item) for item in x]

    if True in childrenAreJagged:
        return True

    return False

