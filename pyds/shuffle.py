import numpy

from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def shuffle(x):
    assert is_a_tensor(x), "`x` must be a tensor!"

    if is_a_pandas_series(x) or is_a_pandas_dataframe(x):
        x = x.values

    out = numpy.copy(x)
    numpy.random.shuffle(out)
    return out
