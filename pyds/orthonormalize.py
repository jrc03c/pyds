"""
let {
  assert,
  isArray,
  shape,
  transpose,
  copy,
  chop,
  distance,
  identity,
  dot,
  add,
  scale,
  pow,
} = require("js-math-tools")

let containsOnlyNumbers = require("./contains-only-numbers.js")
let getMagnitude = require("./get-magnitude.js")
let divide = (a, b) => scale(a, pow(b, -1))
let subtract = (a, b) => add(a, scale(b, -1))

function project(v, u) {
  assert(isArray(v), "`project` only works on vectors!")
  assert(isArray(u), "`project` only works on vectors!")
  assert(containsOnlyNumbers(v), "`project` only works on vectors of numbers!")
  assert(containsOnlyNumbers(u), "`project` only works on vectors of numbers!")
  assert(shape(v).length === 1, "`project` only works on vectors!")
  assert(shape(u).length === 1, "`project` only works on vectors!")
  return scale(dot(u, v) / dot(u, u), u)
}

function gramSchmidtOrthonormalize(x) {
  assert(isArray(x), "`gramSchmidtOrthonormalize` only works on matrices!")

  assert(
    containsOnlyNumbers(x),
    "`gramSchmidtOrthonormalize` only works on matrices of numbers!"
  )

  assert(
    shape(x).length === 2,
    "`gramSchmidtOrthonormalize` only works on matrices!"
  )

  // note: this produces a matrix where the *columns* are orthogonal to each other!
  let temp = transpose(x)
  let bases = []

  temp.forEach((v, i) => {
    let vCopy = copy(v)
    bases.forEach(basis => (vCopy = subtract(vCopy, project(vCopy, basis))))
    bases.push(vCopy)
  })

  let out = bases.map(basis => divide(basis, getMagnitude(basis)))
  let outTranspose = transpose(out)

  // assert(
  //   chop(distance(identity(out.length), dot(out, outTranspose))) === 0,
  //   "The matrix produced by the `gramSchmidtOrthonormalize` function must be orthogonal!"
  // )

  return outTranspose
}

module.exports = gramSchmidtOrthonormalize
"""

from copy import deepcopy
from numpy import array, zeros, dot
from .contains_only_numbers import *
from .is_a_matrix import *
from .chop import *
from .distance import *
from .is_a_numpy_array import *
from .is_a_pandas_dataframe import *
from .is_a_pandas_series import *
from .map import *
from .is_a_vector import *


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

