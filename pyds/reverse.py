from numpy import array

from .is_a_number import isANumber
from .is_a_string import isAString
from .is_a_tensor import is_a_tensor


def reverse(x):
    if isANumber(x):
        return float(reverse(str(x)))

    if isAString(x):
        out = ""

        for i in range(0, len(x)):
            out += x[-i - 1]

        return out

    if is_a_tensor(x):
        out = []

        for i in range(0, len(x)):
            out.append(x[-i - 1])

        return array(out)

    raise AssertionError(
        "You must pass a number, string, or array to the `reverse` function!"
    )
