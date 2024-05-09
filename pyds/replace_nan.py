from numpy import nan

from .is_a_function import is_a_function
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


# Note that this function's structure should be closely linked to drop_nan's!
def replace_nan(x, new_value=nan):
    if is_a_tensor(x):
        if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
            x = x.values.tolist()

        if is_a_numpy_array(x):
            x = x.tolist()

        out = []

        for value in x:
            out.append(replace_nan(value, new_value=new_value))

        return out

    elif isinstance(x, dict):
        out = {}

        for key in x.keys():
            value = x[key]
            out[key] = replace_nan(value, new_value=new_value)

        return out

    else:
        if is_a_function(x):
            return new_value

        try:
            return replace_nan(x.__dict__, new_value=new_value)

        except Exception:
            pass

        if is_a_number(x):
            return x

        return new_value
