from numpy import nan
from numpy.random import normal, random
from pandas import DataFrame, Series

from .is_binary import is_binary
from .round_standard import round_standard


def test():
    binaries = [
        0,
        1,
        [0, 1],
        round_standard(random(size=100)),
        Series(round_standard(random(size=100))),
        DataFrame(round_standard(random(size=[100, 100]))),
        round_standard(random(size=[100, 100, 100])),
    ]

    for b in binaries:
        assert is_binary(b)

    others = [
        234,
        "foo",
        True,
        False,
        None,
        normal(size=100),
        random(size=[100, 100]),
        {"hello": "world"},
        lambda x: x * 2,
        [0, 1, nan],
    ]

    for item in others:
        assert not is_binary(item)
