from copy import deepcopy

from numpy import array, dot, zeros

from .contains_only_numbers import containsOnlyNumbers
from .distance import distance
from .is_a_matrix import isAMatrix
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_vector import isAVector
from .map import map


def getMagnitude(x):
    return distance(x, zeros(x.shape))


def project(v, u):
    assert isAVector(v), "The `project` function only works on vectors!"
    assert isAVector(u), "The `project` function only works on vectors!"

    assert containsOnlyNumbers(
        v
    ), "The `project` function only works on vectors of numbers!"

    assert containsOnlyNumbers(
        u
    ), "The `project` function only works on vectors of numbers!"

    if isAPandasSeries(v):
        v = v.values

    if not isANumpyArray(v):
        v = array(v)

    if isAPandasSeries(u):
        u = u.values

    if not isANumpyArray(u):
        u = array(u)

    return u * dot(u, v) / dot(u, u)


def orthonormalize(x):
    assert isAMatrix(x), "The `orthonormalize` function only works on matrices!"

    assert containsOnlyNumbers(
        x
    ), "The `orthonormalize` function only works on matrices of numbers!"

    if isAPandasDataFrame(x):
        x = x.values

    if not isANumpyArray(x):
        x = array(x)

    temp = x.T
    bases = []

    for row in temp:
        rowCopy = deepcopy(row)

        for basis in bases:
            rowCopy = rowCopy - project(rowCopy, basis)

        bases.append(rowCopy)

    ortho = map(bases, lambda basis: basis / getMagnitude(basis))
    return ortho.T
