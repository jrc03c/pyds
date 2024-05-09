import json

from .is_a_function import is_a_function
from .is_a_number import is_a_number
from .is_a_numpy_array import is_a_numpy_array
from .is_a_pandas_dataframe import is_a_pandas_dataframe
from .is_a_pandas_series import is_a_pandas_series
from .is_a_string import is_a_string
from .is_a_tensor import is_a_tensor
from .is_undefined import is_undefined


def is_primitive(x):
    if is_a_number(x):
        return True

    if is_a_string(x):
        return True

    if isinstance(x, bool):
        return True

    if is_undefined(x):
        return True

    return False


def to_serializable_object(x, used=[]):
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
    if is_primitive(x):
        return x

    elif is_a_function(x):
        return str(x)

    elif is_a_tensor(x):
        if is_a_numpy_array(x):
            return to_serializable_object(x.tolist(), used=used)

        elif is_a_pandas_series(x):
            return {
                "name": x.name,
                "values": to_serializable_object(x.values.tolist(), used=used),
                "index": to_serializable_object(x.index.tolist(), used=used),
            }

        elif is_a_pandas_dataframe(x):
            return {
                "values": to_serializable_object(x.values.tolist(), used=used),
                "columns": to_serializable_object(x.columns.tolist(), used=used),
                "index": to_serializable_object(x.index.tolist(), used=used),
            }

        else:
            out = []

            for item in x:
                hex_id = hex(id(item))

                if hex_id not in used:
                    if not is_primitive(item):
                        used.append(hex_id)

                    out.append(to_serializable_object(item, used=used))

                else:
                    out.append("<cyclic reference to: " + hex_id + ">")

            return out

    else:
        try:
            out = {}

            for key in x.keys():
                value = x[key]
                hex_id = hex(id(value))

                if hex_id not in used:
                    if not is_primitive(value):
                        used.append(hex_id)

                    out[key] = to_serializable_object(value, used=used)

                else:
                    out[key] = "<cyclic reference to: " + hex_id + ">"

            return out

        except Exception:
            pass

        try:
            return to_serializable_object(x.__dict__, used=used)

        except Exception:
            pass

        return x


def save_json(path, data, indentation=2):
    assert is_a_string(path), "`path` must be a string!"

    if not is_a_string(data):
        try:
            data = to_serializable_object(data)

        except Exception:
            raise Exception(
                "The data passed into the `save_json` function could not be serialized!"
            )

    data = json.dumps(data, sort_keys=True, indent=indentation)

    with open(path, "w") as file:
        file.write(data)
