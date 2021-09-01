from .is_a_tensor import *
from numpy.linalg import norm

def magnitude(a):
	assert isATensor(a), "`a` must be a vector, matrix, or tensor!"
	return norm(a)
