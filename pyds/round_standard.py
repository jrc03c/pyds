from math import nan

from numpy import array
from pandas import DataFrame, Series

from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .sign import sign


def round_standard(x):
    if is_a_pandas_dataframe(x):
        out = DataFrame(round_standard(x.values))
        out.columns = x.columns
        out.index = x.index
        return out

    if is_a_pandas_series(x):
        out = Series(round_standard(x.values))
        out.index = x.index
        out.name = x.name
        return out

    if is_a_numpy_array(x):
        return array(round_standard(x.tolist()))

    if is_a_tensor(x):
        return [round_standard(v) for v in x]

    try:
        xint = int(x)
        xabs = abs(x)
        xabsint = int(xabs)

        if xabs - xabsint < 0.5:
            return xint

        else:
            return xint + sign(x)

    except Exception:
        return nan


def round(x):
    return round_standard(x)
