from numpy import clip, dot, mean, std

from .contains_only_numbers import contains_only_numbers
from .is_a_matrix import is_a_matrix
from .is_a_pandas_dataframe import is_a_pandas_dataframe


def standardize(x):
    x = x.T

    for i in range(0, x.shape[0]):
        x[i] = (x[i] - mean(x[i])) / std(x[i])

    return x.T


def get_correlation_matrix(a, b=None):
    if b is None:
        b = a

    assert is_a_matrix(a), "`a` must be a matrix!"
    assert is_a_matrix(b), "`b` must be a matrix!"
    assert contains_only_numbers(a), "`a` must contain only numbers!"
    assert contains_only_numbers(b), "`b` must contain only numbers!"

    if is_a_pandas_dataframe(a):
        a = a.values

    if is_a_pandas_dataframe(b):
        b = b.values

    return clip(dot(standardize(a).T, standardize(b)) / a.shape[0], -1, 1)
