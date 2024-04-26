from math import nan as mathNan

from numpy import nan as numpyNan

from .is_a_function import is_a_function
from .is_a_number import isANumber
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_tensor import is_a_tensor


def isEqual(a, b):
    if a is numpyNan and b is numpyNan:
        return True

    if a is mathNan and b is mathNan:
        return True

    if a is numpyNan and b is mathNan:
        return True

    if a is mathNan and b is numpyNan:
        return True

    if isANumber(a) and isANumber(b):
        return float(a) == float(b)

    if type(a) != type(b):
        return False

    if is_a_tensor(a) and is_a_tensor(b):
        if is_a_pandas_series(a) or is_a_pandas_dataframe(a):
            a = a.values

        if is_a_pandas_series(b) or is_a_pandas_dataframe(b):
            b = b.values

        if is_a_numpy_array(a):
            a = a.tolist()

        if is_a_numpy_array(b):
            b = b.tolist()

        if len(a) != len(b):
            return False

        for i in range(0, len(a)):
            if not isEqual(a[i], b[i]):
                return False

        return True

    if isinstance(a, dict and type(b) == dict):
        aKeys = list(sorted(a.keys()))
        bKeys = list(sorted(b.keys()))

        if not isEqual(aKeys, bKeys):
            return False

        for i in range(0, len(aKeys)):
            aKey = aKeys[i]
            bKey = bKeys[i]
            aChild = a[aKey]
            bChild = b[bKey]

            if not isEqual(aChild, bChild):
                return False

        return True

    if is_a_function(a) and is_a_function(b):
        return a is b

    try:
        return isEqual(a.__dict__, b.__dict__)
    except:
        pass

    return a == b
