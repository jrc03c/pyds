from .flatten import flatten
from .is_a_number import is_a_number
from .is_a_tensor import is_a_tensor


def contains_only_numbers(x):
    assert is_a_tensor(x), "`x` must be a vector, matrix, or tensor!"

    for item in flatten(x):
        if not is_a_number(item):
            return False

    return True
