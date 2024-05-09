from numpy import nan

from .left_pad import left_pad


def test():
    assert left_pad(2, 9) == "2"
    assert left_pad(2, 12) == "02"
    assert left_pad(2, 123) == "002"
    assert left_pad(2, 1234) == "0002"


def test_errors():
    wrongs = [
        [234, 123],
        [-234, -234],
        [234.5, 1000],
        [234, 1000.5],
        ["foo", "bar"],
        [True, False],
        [None, None],
        [{"hello": "world"}, {"goodbye": "world"}],
        [lambda x: x * 2, lambda x: x * 3],
        [[1, 10, 100, 1000, nan], 1000],
    ]

    for pair in wrongs:
        raised = False

        try:
            left_pad(pair[0], pair[1])

        except Exception:
            raised = True

        assert raised
