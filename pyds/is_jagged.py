from .is_a_tensor import is_a_tensor
from .set import set


def is_jagged(x):
    if not is_a_tensor(x):
        return False

    if len(x) == 0:
        return False

    childrenAreArrays = [is_a_tensor(item) for item in x]

    if len(set(childrenAreArrays)) > 1:
        return True

    if childrenAreArrays[0] == False:
        return False

    childLengths = [len(item) for item in x]

    if len(set(childLengths)) > 1:
        return True

    childrenAreJagged = [is_jagged(item) for item in x]

    if True in childrenAreJagged:
        return True

    return False
