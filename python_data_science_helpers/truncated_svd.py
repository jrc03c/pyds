from .is_a_tensor import *
from .is_a_vector import *
from numpy.linalg import svd
from scipy.linalg import diagsvd

def truncatedSVD(x, rank=1):
	assert isATensor(x) and not isAVector(x), "`x` must be a matrix or tensor!"
	u, s, v = svd(x)
	u = u[:, :rank]
	s = diagsvd(s[:rank], rank, rank)
	v = v[:rank, :]
	return u, s, v
