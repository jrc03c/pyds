from .is_a_function import isAFunction
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor
from .is_undefined import isUndefined


def dropUndefined(x, strings=[]):
    if isATensor(x):
        if isAPandasDataFrame(x) or isAPandasSeries(x):
            x = x.values.tolist()

        if isANumpyArray(x):
            x = x.tolist()

        out = []

        for value in x:
            temp = dropUndefined(value, strings=strings)

            if not isUndefined(temp):
                out.append(temp)

        return out

    elif type(x) == dict:
        out = {}

        for key in x.keys():
            value = x[key]
            temp = dropUndefined(value, strings=strings)

            if not isUndefined(temp):
                out[key] = temp

        return out

    else:
        if isUndefined(x):
            return None

        if type(x) == str:
            if x in strings:
                return None

            return x

        if isAFunction(x):
            return x

        try:
            return dropUndefined(x.__dict__, strings=strings)

        except:
            pass

        return x
