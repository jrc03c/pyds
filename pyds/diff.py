from .set import set


def diff(a, b):
    a_set = set(a)
    b_set = set(b)
    return list(filter(lambda a_val: a_val not in b_set, a_set))


def diff_both(a, b):
    return diff(a, b) + diff(b, a)
