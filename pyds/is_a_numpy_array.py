from numpy import array, ndarray


def is_a_numpy_array(x):
    t = type(x)
    return t is array or t is ndarray
