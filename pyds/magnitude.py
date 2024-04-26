from numpy.linalg import norm

from .contains_only_numbers import contains_only_numbers
from .is_a_tensor import is_a_tensor


def magnitude(a):
    assert is_a_tensor(a), "`a` must be a vector, matrix, or tensor!"
    assert contains_only_numbers(a), "`a` must contain only numbers!"
    return norm(a)
