from numpy import nan

from .is_a_function import is_a_function
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_undefined import is_undefined


def replaceUndefined(x, newValue=nan, strings=[]):
    if is_a_tensor(x):
        if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
            x = x.values.tolist()

        if is_a_numpy_array(x):
            x = x.tolist()

        out = []

        for value in x:
            temp = replaceUndefined(value, newValue=newValue, strings=strings)
            out.append(temp)

        return out

    elif isinstance(x, dict):
        out = {}

        for key in x.keys():
            value = x[key]
            temp = replaceUndefined(value, newValue=newValue, strings=strings)
            out[key] = temp

        return out

    else:
        if is_undefined(x):
            return newValue

        if isinstance(x, str):
            if x in strings:
                return newValue

            return x

        if is_a_function(x):
            return x

        try:
            return replaceUndefined(x.__dict__, newValue=newValue, strings=strings)

        except:
            pass

        return x
