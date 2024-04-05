from math import nan as mathNan

from numpy import nan as numpyNan

from .is_a_function import isAFunction
from .is_a_number import isANumber
from .is_a_numpy_array import isANumpyArray
from .is_a_pandas_dataframe import isAPandasDataFrame
from .is_a_pandas_series import isAPandasSeries
from .is_a_tensor import isATensor


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

    if isATensor(a) and isATensor(b):
        if isAPandasSeries(a) or isAPandasDataFrame(a):
            a = a.values

        if isAPandasSeries(b) or isAPandasDataFrame(b):
            b = b.values

        if isANumpyArray(a):
            a = a.tolist()

        if isANumpyArray(b):
            b = b.tolist()

        if len(a) != len(b):
            return False

        for i in range(0, len(a)):
            if not isEqual(a[i], b[i]):
                return False

        return True

    if type(a) == dict and type(b) == dict:
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

    if isAFunction(a) and isAFunction(b):
        return a is b

    try:
        return isEqual(a.__dict__, b.__dict__)
    except:
        pass

    return a == b
