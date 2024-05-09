from numpy import arange

from .is_a_number import is_a_number
from .sign import sign


def range(a, b, step=1):
    assert is_a_number(a), "`a` must be a number!"
    assert is_a_number(b), "`b` must be a number!"
    assert is_a_number(step), "`step` must be a number!"
    assert step != 0, "`step` cannot be zero!"

    assert sign(step) == sign(
        b - a
    ), "The sign of `step` must be consistent with the direction from `a` to `b`!"

    return arange(a, b, step)
