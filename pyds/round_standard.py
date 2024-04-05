from math import nan

from numpy import array
from pandas import DataFrame, Series

from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .sign import sign


def roundStandard(x):
    if isAPandasDataFrame(x):
        out = DataFrame(roundStandard(x.values))
        out.columns = x.columns
        out.index = x.index
        return out

    if isAPandasSeries(x):
        out = Series(roundStandard(x.values))
        out.index = x.index
        out.name = x.name
        return out

    if isANumpyArray(x):
        return array(roundStandard(x.tolist()))

    if isATensor(x):
        return [roundStandard(v) for v in x]

    try:
        xint = int(x)
        xabs = abs(x)
        xabsint = int(xabs)

        if xabs - xabsint < 0.5:
            return xint

        else:
            return xint + sign(x)

    except:
        return nan


def round(x):
    return roundStandard(x)
