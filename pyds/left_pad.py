from .is_a_number import *


def leftPad(n, max):
    assert type(n) is int, "`n` must be a whole number!"
    assert n >= 0, "`n` must be a whole number!"

    assert type(max) is int, "`max` must be a whole number!"
    assert max >= 0, "`max` must be a whole number!"

    assert n <= max, "`n` must be less than or equal to `max`!"

    numberOfZeros = len(str(max)) - len(str(n))
    return "0" * numberOfZeros + str(n)
