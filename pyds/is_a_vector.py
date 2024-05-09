from numpy import shape

from .is_a_pandas_series import is_a_pandas_series
from .is_iterable import is_iterable


def is_a_vector(x):
    if not is_iterable(x):
        return False

    if is_a_pandas_series(x):
        x = x.values

    try:
        return len(shape(x)) == 1

    except Exception:
        return False
