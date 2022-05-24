from .is_a_number import isANumber
from numpy.random import random


def makeKey(n):
    assert isANumber(n) and n >= 0 and int(n) == n, "`n` must be a whole number!"

    alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
    out = ""

    for i in range(0, n):
        out += alpha[int(random() * len(alpha))]

    return out
