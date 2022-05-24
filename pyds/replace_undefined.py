from .is_a_function import isAFunction
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .is_undefined import isUndefined
from numpy import nan


def replaceUndefined(x, newValue=nan, strings=[]):
    if isATensor(x):
        if isAPandasDataFrame(x) or isAPandasSeries(x):
            x = x.values.tolist()

        if isANumpyArray(x):
            x = x.tolist()

        out = []

        for value in x:
            temp = replaceUndefined(value, newValue=newValue, strings=strings)
            out.append(temp)

        return out

    elif type(x) == dict:
        out = {}

        for key in x.keys():
            value = x[key]
            temp = replaceUndefined(value, newValue=newValue, strings=strings)
            out[key] = temp

        return out

    else:
        if isUndefined(x):
            return newValue

        if type(x) == str:
            if x in strings:
                return newValue

            return x

        if isAFunction(x):
            return x

        try:
            return replaceUndefined(x.__dict__, newValue=newValue, strings=strings)

        except:
            pass

        return x
