from .is_a_function import *
from .is_a_number import *
from .is_a_numpy_array import *
from .is_a_pandas_dataframe import *
from .is_a_pandas_series import *
from .is_a_tensor import *
from numpy import shape


def dropNaN(x):
    if isATensor(x):
        if isAPandasDataFrame(x) or isAPandasSeries(x):
            x = x.values.tolist()

        if isANumpyArray(x):
            x = x.tolist()

        out = []

        for value in x:
            temp = dropNaN(value)

            if temp is not None:
                out.append(temp)

        return out

    elif type(x) == dict:
        out = {}

        for key in x.keys():
            value = x[key]
            temp = dropNaN(value)

            if temp is not None:
                out[key] = temp

        return out

    else:
        if isAFunction(x):
            return None

        try:
            return dropNaN(x.__dict__)

        except:
            pass

        if isANumber(x):
            return x

        return None

