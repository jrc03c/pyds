from .is_a_tensor import *
from numpy.linalg import lstsq

def leastSquares(a, b):
  assert isATensor(a), "`a` must be a vector, matrix, or tensor!"
  assert isATensor(b), "`b` must be a vector, matrix, or tensor!"
  return lstsq(a, b, rcond=None)[0]
