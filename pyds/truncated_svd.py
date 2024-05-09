from numpy.linalg import svd
from scipy.linalg import diagsvd

from .is_a_matrix import is_a_matrix
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe


def truncated_svd(x, rank=1):
    assert is_a_matrix(x), "`x` must be a matrix!"

    assert (
        is_a_number(rank) and rank > 0 and int(rank) == rank
    ), "`rank` must be a whole number!"

    if is_a_pandas_dataframe(x):
        x = x.values.tolist()

    if is_a_numpy_array(x):
        x = x.tolist()

    u, s, v = svd(x)
    u = u[:, :rank]
    s = diagsvd(s[:rank], rank, rank)
    v = v[:rank, :]
    return u, s, v
