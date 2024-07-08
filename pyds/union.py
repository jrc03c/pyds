from numpy import array

from .set import set


def union(a, b):
    a_set = set(a)
    b_set = set(b)
    return array(set(list(a_set) + list(b_set)))
