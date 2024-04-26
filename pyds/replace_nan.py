from numpy import nan

from .is_a_function import is_a_function
from .is_a_number import isANumber
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


# Note that this function's structure should be closely linked to dropNaN's!
def replaceNaN(x, newValue=nan):
    if is_a_tensor(x):
        if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
            x = x.values.tolist()

        if is_a_numpy_array(x):
            x = x.tolist()

        out = []

        for value in x:
            out.append(replaceNaN(value, newValue=newValue))

        return out

    elif isinstance(x, dict):
        out = {}

        for key in x.keys():
            value = x[key]
            out[key] = replaceNaN(value, newValue=newValue)

        return out

    else:
        if is_a_function(x):
            return newValue

        try:
            return replaceNaN(x.__dict__, newValue=newValue)

        except:
            pass

        if isANumber(x):
            return x

        return newValue
