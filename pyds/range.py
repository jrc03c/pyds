from .is_a_number import isANumber
from .sign import sign
from numpy import arange


def range(a, b, step=1):
    assert isANumber(a), "`a` must be a number!"
    assert isANumber(b), "`b` must be a number!"
    assert isANumber(step), "`step` must be a number!"
    assert step != 0, "`step` cannot be zero!"

    assert sign(step) == sign(
        b - a
    ), "The sign of `step` must be consistent with the direction from `a` to `b`!"

    return arange(a, b, step)
