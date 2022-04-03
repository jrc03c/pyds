from .find import *
from .is_a_function import *
from .is_a_number import *
from .is_a_numpy_array import *
from .is_a_pandas_dataframe import *
from .is_a_pandas_series import *
from .is_a_string import *
from .is_a_tensor import *
from .is_undefined import *
import json
import inspect


def isPrimitive(x):
    if isANumber(x):
        return True

    if isAString(x):
        return True

    if type(x) == bool:
        return True

    if isUndefined(x):
        return True

    return False


def toSerializableObject(x, used=[]):
    if not isPrimitive(x) or len(used) == 0:
        used.append(x)

    if isAFunction(x):
        return str(x)

    if isATensor(x):
        if isANumpyArray(x):
            return toSerializableObject(x.tolist(), used=used)

        if not isAPandasSeries(x) and not isAPandasDataFrame(x):
            out = []

            for item in x:
                if find(lambda other: other is item, used) is None:
                    if not isPrimitive(item):
                        used.append(item)

                    out.append(toSerializableObject(item, used=used))

                else:
                    out.append("<cyclic reference to: " + hex(id(item)) + ">")

            return out

    if isAPandasSeries(x):
        return {
            "values": toSerializableObject(x.values.tolist(), used=used),
            "index": toSerializableObject(x.index.tolist(), used=used),
        }

    if isAPandasDataFrame(x):
        return {
            "values": toSerializableObject(x.values.tolist(), used=used),
            "columns": toSerializableObject(x.columns.tolist(), used=used),
            "index": toSerializableObject(x.index.tolist(), used=used),
        }

    try:
        out = {}

        for key in x.keys():
            value = x[key]

            if find(lambda other: other is value, used) is None:
                if not isPrimitive(value):
                    used.append(value)

                out[key] = toSerializableObject(value, used=used)

            else:
                out[key] = "<cyclic reference to: " + hex(id(value)) + ">"

        return out

    except:
        pass

    try:
        return toSerializableObject(x.__dict__, used=used)

    except:
        return x


def saveJSON(path, data, indentation=2):
    assert isAString(path), "`path` must be a string!"

    if not isAString(data):
        try:
            data = toSerializableObject(data)
            data = json.dumps(data, sort_keys=True, indent=indentation)

        except:
            raise Exception(
                "The data passed into the `saveJSON` function could not be serialized!"
            )

    with open(path, "w") as file:
        file.write(data)
