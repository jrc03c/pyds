from copy import deepcopy

from numpy import array, dot, zeros

from .contains_only_numbers import contains_only_numbers
from .distance import distance
from .is_a_matrix import is_a_matrix
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_vector import is_a_vector
from .magnitude import magnitude
from .map import map


def project(v, u):
    assert is_a_vector(v), "The `project` function only works on vectors!"
    assert is_a_vector(u), "The `project` function only works on vectors!"

    assert contains_only_numbers(
        v
    ), "The `project` function only works on vectors of numbers!"

    assert contains_only_numbers(
        u
    ), "The `project` function only works on vectors of numbers!"

    if is_a_pandas_series(v):
        v = v.values

    if not is_a_numpy_array(v):
        v = array(v)

    if is_a_pandas_series(u):
        u = u.values

    if not is_a_numpy_array(u):
        u = array(u)

    return u * dot(u, v) / dot(u, u)


def orthonormalize(x):
    assert is_a_matrix(x), "The `orthonormalize` function only works on matrices!"

    assert contains_only_numbers(
        x
    ), "The `orthonormalize` function only works on matrices of numbers!"

    if is_a_pandas_dataframe(x):
        x = x.values

    if not is_a_numpy_array(x):
        x = array(x)

    temp = x.T
    bases = []

    for row in temp:
        row_copy = deepcopy(row)

        for basis in bases:
            row_copy = row_copy - project(row_copy, basis)

        bases.append(row_copy)

    ortho = map(bases, lambda basis: basis / magnitude(basis))
    return ortho.T
