from .is_a_matrix import isAMatrix
from .is_a_number import isANumber
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from numpy.linalg import svd
from scipy.linalg import diagsvd


def truncatedSVD(x, rank=1):
    assert isAMatrix(x), "`x` must be a matrix!"

    assert (
        isANumber(rank) and rank > 0 and int(rank) == rank
    ), "`rank` must be a whole number!"

    if isAPandasDataFrame(x):
        x = x.values.tolist()

    if isANumpyArray(x):
        x = x.tolist()

    u, s, v = svd(x)
    u = u[:, :rank]
    s = diagsvd(s[:rank], rank, rank)
    v = v[:rank, :]
    return u, s, v
