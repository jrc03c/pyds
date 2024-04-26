from numpy import shape

from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_string import isAString
from .is_iterable import isIterable


def is_a_tensor(x):
    if isIterable(x):
        return not isAString(x) and not isinstance(x, dict)

    if is_a_pandas_series(x) or is_a_pandas_dataframe(x):
        return True

    try:
        return len(shape(x)) >= 1

    except:
        return False
