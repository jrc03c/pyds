from numpy.random import random

from .is_a_number import is_a_number


def make_key(n):
    assert is_a_number(n) and n >= 0 and int(n) == n, "`n` must be a whole number!"

    alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
    out = ""

    for i in range(0, n):
        out += alpha[int(random() * len(alpha))]

    return out
