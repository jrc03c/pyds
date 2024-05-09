from .is_a_tensor import is_a_tensor
from .set import set


def is_jagged(x):
    if not is_a_tensor(x):
        return False

    if len(x) == 0:
        return False

    children_are_arrays = [is_a_tensor(item) for item in x]

    if len(set(children_are_arrays)) > 1:
        return True

    if not children_are_arrays[0]:
        return False

    child_lengths = [len(item) for item in x]

    if len(set(child_lengths)) > 1:
        return True

    children_are_jagged = [is_jagged(item) for item in x]

    if True in children_are_jagged:
        return True

    return False
