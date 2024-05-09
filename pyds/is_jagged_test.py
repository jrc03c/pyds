from numpy.random import normal

from .is_jagged import is_jagged


def test():
    jag = normal(size=[2, 3, 4, 5]).tolist()
    jag[1][2][3] = jag[1][2][3][:2]

    pairs = [
        [jag, True],
        [[[[2, 3, 4]], [[5, 6, 7]], [[8, 9, 0]]], False],
        [[[2], [3, 4], [5, 6, 7]], True],
        [True, False],
        [False, False],
        [None, False],
        ["foo", False],
        [234, False],
        [{}, False],
        [[], False],
        [lambda x: x, False],
    ]

    for pair in pairs:
        if pair[1] is True:
            assert is_jagged(pair[0])
        else:
            assert not (is_jagged(pair[1]))


def test_errors():
    pass
