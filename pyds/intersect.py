from numpy import array

from .set import set


def intersect(a, b):
    a_set = set(a)
    b_set = set(b)
    all = set(list(a_set) + list(b_set))
    return array(list(filter(lambda v: v in a_set and v in b_set, all)))
