from numpy.random import normal

from pyds import distance


def test():
    assert distance([3, 4], [0, 0]) == 5
    assert distance([1, 2, 3], [4, 5, 6]) == 27**0.5
    assert distance(3, 5) == 2


def test_errors():
    missing = normal(size=[100, 100])
    missing[0][0] = None

    wrongs = [
        [[2, 3, 4], [2, 3, 4, 5]],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [missing, missing],
    ]

    for pair in wrongs:
        raised = False

        try:
            distance(pair[0], pair[1])
        except Exception:
            raised = True

        assert raised
