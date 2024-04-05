from numpy import shape

from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_string import isAString
from .is_iterable import isIterable


def isATensor(x):
    if isIterable(x):
        return not isAString(x) and not type(x) == dict

    if isAPandasSeries(x) or isAPandasDataFrame(x):
        return True

    try:
        return len(shape(x)) >= 1

    except:
        return False
