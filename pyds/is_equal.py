from .is_a_tensor import *
from .is_a_pandas_series import *
from .is_a_pandas_dataframe import *
from numpy import shape


def isEqual(a, b):
    if type(a) != type(b):
        return False

    if isATensor(a) and isATensor(b):
        if isAPandasSeries(a) or isAPandasDataFrame(a):
            a = a.values

        if isAPandasSeries(b) or isAPandasDataFrame(b):
            b = b.values

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

    fntype = type(lambda x: x)

    if type(a) == fntype and type(b) == fntype:
        return a is b

    return a == b
