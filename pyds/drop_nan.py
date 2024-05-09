from .is_a_function import is_a_function
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def drop_nan(x):
    if is_a_tensor(x):
        if is_a_pandas_dataframe(x) or is_a_pandas_series(x):
            x = x.values.tolist()

        if is_a_numpy_array(x):
            x = x.tolist()

        out = []

        for value in x:
            temp = drop_nan(value)

            if temp is not None:
                out.append(temp)

        return out

    elif isinstance(x, dict):
        out = {}

        for key in x.keys():
            value = x[key]
            temp = drop_nan(value)

            if temp is not None:
                out[key] = temp

        return out

    else:
        if is_a_function(x):
            return None

        try:
            return drop_nan(x.__dict__)

        except Exception:
            pass

        if is_a_number(x):
            return x

        return None
