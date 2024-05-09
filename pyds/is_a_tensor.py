from numpy import shape

from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_string import is_a_string
from .is_iterable import is_iterable


def is_a_tensor(x):
    if is_iterable(x):
        return not is_a_string(x) and not isinstance(x, dict)

    if is_a_pandas_series(x) or is_a_pandas_dataframe(x):
        return True

    try:
        return len(shape(x)) >= 1

    except Exception:
        return False
