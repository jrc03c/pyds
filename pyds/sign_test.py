from numpy import array
from numpy.random import random

from .is_equal import is_equal
from .round_standard import round_standard
from .sign import sign


def test():
    assert sign(234) == 1
    assert isinstance(sign(234), int)
    assert sign(-234) == -1
    assert isinstance(sign(-234), int)
    assert sign(0) == 0
    assert isinstance(sign(0), int)

    a = array([2, -3, 4, -5, 6, 0])
    b = array([1, -1, 1, -1, 1, 0])
    assert is_equal(sign(a), b)

    a = round_standard(random(size=[10, 10, 10]) * 2 - 1)
    b = sign(a)
    assert is_equal(a, b)


def test_errors():
    missing = random(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        lambda x: x * 2,
        [2, 3, "four"],
        [[[2, 3, None]]],
        missing,
    ]

    for item in wrongs:
        raised = False

        try:
            sign(item)

        except Exception:
            raised = True

        assert raised
