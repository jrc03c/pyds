from numpy import nan

from .is_a_function import is_a_function
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor
from .is_undefined import is_undefined


def replace_undefined(x, new_value=nan, strings=[]):
    if is_a_tensor(x):
        if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
            x = x.values.tolist()

        if is_a_numpy_array(x):
            x = x.tolist()

        out = []

        for value in x:
            temp = replace_undefined(value, new_value=new_value, strings=strings)
            out.append(temp)

        return out

    elif isinstance(x, dict):
        out = {}

        for key in x.keys():
            value = x[key]
            temp = replace_undefined(value, new_value=new_value, strings=strings)
            out[key] = temp

        return out

    else:
        if is_undefined(x):
            return new_value

        if isinstance(x, str):
            if x in strings:
                return new_value

            return x

        if is_a_function(x):
            return x

        try:
            return replace_undefined(x.__dict__, new_value=new_value, strings=strings)

        except Exception:
            pass

        return x
