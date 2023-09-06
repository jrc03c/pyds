from numpy import inf, nan

from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_string import isAString
from .is_iterable import isIterable


def parseFloat(x):
    if isAPandasDataFrame(x):
        return x.apply(lambda col: parseFloat(col))

    if isAPandasSeries(x):
        return x.apply(lambda v: parseFloat(v))

    if isIterable(x):
        if isAString(x):
            if x == "inf":
                return inf

            if x == "-inf":
                return -inf

            return parseFloat(x)

        return [parseFloat(v) for v in x]

    try:
        return float(x)

    except:
        return nan
