from .is_a_matrix import *
from numpy.linalg import svd
from scipy.linalg import diagsvd


def truncatedSVD(x, rank=1):
    assert isAMatrix(x), "`x` must be a matrix!"
    u, s, v = svd(x)
    u = u[:, :rank]
    s = diagsvd(s[:rank], rank, rank)
    v = v[:rank, :]
    return u, s, v
