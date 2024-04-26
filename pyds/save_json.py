import json

from .is_a_function import is_a_function
from .is_a_number import isANumber
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_string import isAString
from .is_a_tensor import is_a_tensor
from .is_undefined import is_undefined


def isPrimitive(x):
    if isANumber(x):
        return True

    if isAString(x):
        return True

    if isinstance(x, bool):
        return True

    if is_undefined(x):
        return True

    return False


def toSerializableObject(x, used=[]):
    # cases to handle:
    # primitives:
    #   - numbers
    #   - strings
    #   - booleans
    #   - undefined / None / nan
    # functions
    # arrays
    #   - plain lists
    #   - numpy arrays
    #   - pandas series and dataframes
    # dictionaries
    # class instances
    # circular references
    if isPrimitive(x):
        return x

    elif is_a_function(x):
        return str(x)

    elif is_a_tensor(x):
        if is_a_numpy_array(x):
            return toSerializableObject(x.tolist(), used=used)

        elif is_a_pandas_series(x):
            return {
                "name": x.name,
                "values": toSerializableObject(x.values.tolist(), used=used),
                "index": toSerializableObject(x.index.tolist(), used=used),
            }

        elif is_a_pandas_dataframe(x):
            return {
                "values": toSerializableObject(x.values.tolist(), used=used),
                "columns": toSerializableObject(x.columns.tolist(), used=used),
                "index": toSerializableObject(x.index.tolist(), used=used),
            }

        else:
            out = []

            for item in x:
                hexId = hex(id(item))

                if not hexId in used:
                    if not isPrimitive(item):
                        used.append(hexId)

                    out.append(toSerializableObject(item, used=used))

                else:
                    out.append("<cyclic reference to: " + hexId + ">")

            return out

    else:
        try:
            out = {}

            for key in x.keys():
                value = x[key]
                hexId = hex(id(value))

                if not hexId in used:
                    if not isPrimitive(value):
                        used.append(hexId)

                    out[key] = toSerializableObject(value, used=used)

                else:
                    out[key] = "<cyclic reference to: " + hexId + ">"

            return out

        except:
            pass

        try:
            return toSerializableObject(x.__dict__, used=used)

        except:
            pass

        return x


def saveJSON(path, data, indentation=2):
    assert isAString(path), "`path` must be a string!"

    if not isAString(data):
        try:
            data = toSerializableObject(data)

        except:
            raise Exception(
                "The data passed into the `saveJSON` function could not be serialized!"
            )

    data = json.dumps(data, sort_keys=True, indent=indentation)

    with open(path, "w") as file:
        file.write(data)
