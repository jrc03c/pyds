from numpy import nan

from .is_a_function import isAFunction
from .is_a_number import isANumber
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor


# Note that this function's structure should be closely linked to dropNaN's!
def replaceNaN(x, newValue=nan):
    if isATensor(x):
        if isAPandasDataFrame(x) or isAPandasSeries(x):
            x = x.values.tolist()

        if isANumpyArray(x):
            x = x.tolist()

        out = []

        for value in x:
            out.append(replaceNaN(value, newValue=newValue))

        return out

    elif type(x) == dict:
        out = {}

        for key in x.keys():
            value = x[key]
            out[key] = replaceNaN(value, newValue=newValue)

        return out

    else:
        if isAFunction(x):
            return newValue

        try:
            return replaceNaN(x.__dict__, newValue=newValue)

        except:
            pass

        if isANumber(x):
            return x

        return newValue
