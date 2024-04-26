from numpy import array

from .contains_only_numbers import contains_only_numbers
from .correl import correl
from .is_a_matrix import is_a_matrix
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .range import range


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

    out = []

    for i in range(0, a.shape[1]):
        row = []

        for j in range(0, b.shape[1]):
            row.append(correl(a[:, i], b[:, j]))

        out.append(row)

    return array(out)
