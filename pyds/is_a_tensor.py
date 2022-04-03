from .is_iterable import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *
from .is_a_string import *
from numpy import shape


def isATensor(x):
    if isIterable(x):
        return not isAString(x) and not type(x) == dict

    if isAPandasSeries(x) or isAPandasDataFrame(x):
        return True

    try:
        return len(shape(x)) >= 1

    except:
        return False
