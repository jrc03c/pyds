from numpy.random import normal, random, seed
from pandas import DataFrame, Series

from pyds import chop, is_equal


def test():
    seed(12345)
    a = Series(random(size=100) + 100)
    seed(12345)
    b = random(size=100) + 100

    seed(23456)
    c = DataFrame(random(size=[100, 100]) + 100)
    seed(23456)
    d = random(size=[100, 100]) + 100

    rights = [
        [0, 0],
        [1, 1],
        [-1, -1],
        [1e-20, 0],
        [-(1e-20), 0],
        [a, b],
        [c, d],
    ]

    for pair in rights:
        assert is_equal(chop(pair[0]), pair[1]), "Failed to chop values! (%s, %s)" % (
            pair[0],
            pair[1],
        )


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        "foo",
        True,
        False,
        None,
        {"hello": "world"},
        ["hello", "world"],
        lambda x: x * 2,
        missing,
    ]

    for item in wrongs:
        raised = False

        try:
            chop(item)
        except Exception:
            raised = True

        assert raised
