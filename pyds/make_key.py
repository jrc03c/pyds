from numpy.random import random


def makeKey(n):
    alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
    out = ""

    for i in range(0, n):
        out += alpha[int(random() * len(alpha))]

    return out
